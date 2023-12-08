import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)

while True:
    with mic as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Vous avez dit: " + text)
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit")
    except sr.RequestError as e:
        print("La requête à l'API de reconnaissance vocale a échoué; {0}".format(e))
