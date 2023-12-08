import pyaudio
import wave
import audioop
import time
import threading
def RecVoice(file):
    # Set the VAD threshold and chunk size
    THRESHOLD = 3000
    CHUNK_SIZE = 1024

    # Set the format for the audio stream and the output file
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = file+".wav"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK_SIZE)

    # Initialize variables for recording
    frames = []
    silence_counter = 2
    silence_threshold = 50
    is_recording = False

    # Start recording
    print("Recording started")
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE)

        # Calculate the volume (RMS) of the audio data
        volume = audioop.rms(data, 2)
        #print("volume")
        #print(volume)
        #print("THRESHOLD")
        #print(THRESHOLD)
        # Determine if the audio data is above the threshold
        if volume > THRESHOLD:
            # If audio data is above threshold, reset silence counter
            silence_counter = 0

            # If not already recording, start recording
            if not is_recording:
                is_recording = True
                print("Recording...")
            
            # Add audio data to the recorded frames
            frames.append(data)
        else:
            # If audio data is below threshold, increment silence counter
            if(is_recording):
                frames.append(data)
            silence_counter += 1
            #print(silence_counter)
            # If recording and silence counter exceeds threshold, stop recording
            if is_recording and silence_counter > silence_threshold:
                is_recording = False
                break

    # Stop the audio stream
    stream.stop_stream()
    stream.close()

    # Close PyAudio
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b''.join(frames))

    print("Recording stopped")
    
    return True


#RecVoice("rep1")
def record_audio():
    # Set the VAD threshold and chunk size
    THRESHOLD = 3000
    CHUNK_SIZE = 1024
    file="rep"
    # Set the format for the audio stream and the output file
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = file+".wav"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK_SIZE)

    # Initialize variables for recording
    frames = []
    silence_counter = 2
    silence_threshold = 50
    is_recording = False

    # Start recording
    print("Recording started")
    while True:
        # Read audio data from the stream
        data = stream.read(CHUNK_SIZE)

        # Calculate the volume (RMS) of the audio data
        volume = audioop.rms(data, 2)
        #print("volume")
        #print(volume)
        #print("THRESHOLD")
        #print(THRESHOLD)
        # Determine if the audio data is above the threshold
        if volume > THRESHOLD:
            # If audio data is above threshold, reset silence counter
            silence_counter = 0

            # If not already recording, start recording
            if not is_recording:
                is_recording = True
                print("Recording...")
            
            # Add audio data to the recorded frames
            frames.append(data)
        else:
            # If audio data is below threshold, increment silence counter
            if(is_recording):
                frames.append(data)
            silence_counter += 1
            #print(silence_counter)
            # If recording and silence counter exceeds threshold, stop recording
            if is_recording and silence_counter > silence_threshold:
                is_recording = False
                break

    # Stop the audio stream
    stream.stop_stream()
    stream.close()

    # Close PyAudio
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b''.join(frames))

    print("Recording stopped")
    
    #return True

def play_audio():
    chunk = 1024  # number of samples per frame
    wf = wave.open("botvoice/bonjour.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()

# create two threads for recording and playing audio
record_thread = threading.Thread(target=record_audio)
play_thread = threading.Thread(target=play_audio)

# start the threads
record_thread.start()
play_thread.start()

# wait for the threads to finish
record_thread.join()
play_thread.join()

print("Done")