import speech_recognition as sr
import os
import azure.cognitiveservices.speech as speechsdk
# initialisation du recognizer

def VocalReconnaissance():
    
    # Créer un objet recognizer
    r = sr.Recognizer()

    # Utiliser le microphone pour capturer l'audio
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        try:
            audio = r.listen(source)
        except Exception as e:
            print("Une erreur s'est produite lors de la capture de l'audio : {0}".format(e))

    # Transcrire l'audio en texte
    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Vous avez dit: " + text)
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris ce que vous avez dit.")
    except sr.RequestError as e:
        print("Impossible d'obtenir les résultats de Google Speech Recognition ; {0}".format(e))
        

def VoiceToText(wave):
    r = sr.Recognizer()

    audio_file = sr.AudioFile(wave)

    with audio_file as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='fr-FR')
        return text
        
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
        return ""
    except sr.RequestError as e:
        print("Impossible de demander des résultats au service de reconnaissance vocale de Google ; {0}".format(e))
        return ""

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='c1c5c582e3f447e2bcca4d253f0476c6', region='francecentral')
    speech_config.speech_recognition_language="fr-FR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""
def VoiceToTextAzure(wave):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='c1c5c582e3f447e2bcca4d253f0476c6', region='francecentral')
    speech_config.speech_recognition_language="fr-FR"

    audio_config = speechsdk.audio.AudioConfig(filename =wave)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Reconnaissance vocal")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""