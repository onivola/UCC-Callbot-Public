import wave
import pyaudio
import time

def playwave(file):
    # open the wave file
    wf = wave.open(file, 'rb')

    # initialize the pyaudio module
    p = pyaudio.PyAudio()

    # open a stream to play the audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    # read data from the wave file and play it through the stream
    chunk = 1024
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # close the stream and terminate pyaudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    return True
    
