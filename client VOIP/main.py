

import datetime
import re
import socket
import time
from Asterisk.Manager import Manager
"""with wave.open('bonjour.wav', 'rb') as audio_file:
    audio_data = audio_file.readframes(audio_file.getnframes())
# Connect to the Asterisk Manager Interface
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.88.96', 5038))


# Send login request
'''login = "Action: Login\r\nUsername: phone2\r\nSecret: poseidon\r\n\r\n"
sock.send(login.encode())
response = sock.recv(1024)'''
s.send(b"Action: Login\r\n")
s.send(b"Username: bot\r\n")
s.send(b"Secret: 123456\r\n")
s.send(b"\r\n")

s.send(b"Action: Originate\r\n")
s.send(b"Channel: SIP/phone1/1234\r\n")
s.send(b"CallerID: phone1 <1234>\r\n")
s.send(b"Application: Playback\r\n")
s.send(b"Data: WAV|\r\n")
s.send(b"\r\n")

# Stream audio data over socket connection
s.send(audio_data)"""
'''
# Send call request
call = "Action: Originate\r\nChannel: SIP/1001/5551234\r\nContext: default\r\nExten: 5551234\r\nPriority: 1\r\nCallerID: 1234\r\nTimeout: 30000\r\n\r\n"
sock.send(call.encode())
response = sock.recv(1024)

# Close socket connection
sock.close()'''
