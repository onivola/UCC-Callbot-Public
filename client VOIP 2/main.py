from pyVoIP.VoIP import VoIPPhone, InvalidStateError

def answer(call): # This will be your callback function for when you receive a phone call.
    try:
      call.answer()
      call.hangup()
    except InvalidStateError:
      pass
  
if __name__ == "__main__":
    phone=VoIPPhone('192.168.88.96', 5060, 'phone2  ', 'poseidon', callCallback=answer)
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()