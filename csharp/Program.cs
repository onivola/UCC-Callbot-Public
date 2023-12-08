using System;
using System.Threading;
using Ozeki.Media;
using Ozeki.VoIP;
using Ozeki.Common;

class Program
{

    static void Main(string[] args)
    {
        // Create a new SoftPhone object
        
        // Create a new phone line object

            ISoftPhone softphone = SoftPhoneFactory.CreateSoftPhone(5000, 10000);
            Console.WriteLine(123);
        
        /*// Register the phone line with the Asterisk server

        phoneLine.Register();

        // Create a new phone call object
        var call = phoneLine.CreateCall("destination_phone_number");

        // Attach event handlers to the phone call object
        call.CallStateChanged += (sender, e) => Console.WriteLine($"Call state changed to {e.State}");
        call.DTMFReceived += (sender, e) => Console.WriteLine($"DTMF received: {e.DTMFSignal}");
        call.AudioSender = new MicrophoneAudioSender();
        call.AudioReceiver = new SpeakerAudioReceiver();

        // Make the call
        call.Start();

        Console.WriteLine("Press any key to end the call.");
        Console.ReadKey();

        // End the call
        call.HangUp();*/
    }

}
