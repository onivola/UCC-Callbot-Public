using System;
using Ozeki.VoIP;

namespace _01_SIP_Registration
{
    /// <summary>
    /// Basic softphone logic.
    /// </summary>
    /// <remarks>
    /// This class is used to introduce how to declare, define and initialize a softphone,
    /// how to handle some of it's events, and use some of it's functions.
    /// The Program.cs uses this class to create a softphone,
    /// uses the functions and events declared here as public.
    /// </remarks>
    class Softphone
    {
        ISoftPhone _softphone;   // softphone object
        IPhoneLine _phoneLine;   // phoneline object

        /// <summary>
        /// Occurs when the registration state of the phone line has changed.
        /// </summary>
        public event EventHandler<RegistrationStateChangedArgs> PhoneLineStateChanged;

        /// <summary>
        /// Default constructor, initalizes our softphone with deafult parameters.
        /// </summary>
        public Softphone()
        {
            //you can specify the User-Agent of the softphone
            string userAgent = "My-SoftPhone-example";

            _softphone = SoftPhoneFactory.CreateSoftPhone(5000, 10000, userAgent);
        }

        /// <summary>
        /// Registers the SIP account to the PBX. 
        /// </summary>
        public void Register(bool registrationRequired, string displayName, string userName, string authenticationId, string registerPassword, string domainHost, int domainPort)
        {
            try
            {
                // To register to a PBX, we need to create a SIP account
                var account = new SIPAccount(registrationRequired, displayName, userName, authenticationId, registerPassword, domainHost, domainPort);
                Console.WriteLine("\nCreating SIP account {0}", account);

                // With the SIP account and the NAT configuration, we can create a phoneline.
                _phoneLine = _softphone.CreatePhoneLine(account);
                Console.WriteLine("Phoneline created.");
                // The phoneline has states, we need to handle the event, when it is being changed.
                _phoneLine.RegistrationStateChanged += phoneLine_PhoneLineStateChanged;

                // If our phoneline is created, we can register that.
                _softphone.RegisterPhoneLine(_phoneLine);

            }
            catch (Exception ex)
            {
                Console.WriteLine("Error during SIP registration: " + ex.ToString());
            }
        }

        public void Unregister()
        {
            if(_softphone != null && _phoneLine != null)
                _softphone.UnregisterPhoneLine(_phoneLine);
        }

        /// <summary>
        /// This will be called when the registration state of the phone line has changed.
        /// </summary>
        private void phoneLine_PhoneLineStateChanged(object sender, RegistrationStateChangedArgs e)
        {
            var handler = PhoneLineStateChanged;
            if (handler != null)
                handler(this, e);
        }
    }
}
