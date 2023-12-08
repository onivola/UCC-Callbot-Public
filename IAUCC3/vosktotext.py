import vosk
import wave
import speech_recognition as sr
import pyaudio

modelvsk = vosk.Model(r"E:\Travaille\IAUCC\IAUCC3\vosk-model-small-fr-0.22")
def vosktotext(file):
    
    audio_file = wave.open(file+".wav", "rb")
    
    sample_rate = audio_file.getframerate()
    print(sample_rate)
    audio_data = audio_file.readframes(audio_file.getnframes())
    recognizer = vosk.KaldiRecognizer(modelvsk, sample_rate)
    recognizer.AcceptWaveform(audio_data)
    result = eval(recognizer.FinalResult())
    transcription = result["text"]
    return transcription
