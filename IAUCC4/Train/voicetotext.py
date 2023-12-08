import speech_recognition as sr
import os
import azure.cognitiveservices.speech as speechsdk
# initialisation du recognizer
import threading
import wave
import pyaudio
import queue
import time
# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription='c1c5c582e3f447e2bcca4d253f0476c6', region='francecentral')
speech_config.speech_recognition_language="fr-FR"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

vtglobale=False
def recognize_from_microphone2(result_queue):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='c1c5c582e3f447e2bcca4d253f0476c6', region='francecentral')
    speech_config.speech_recognition_language="fr-FR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        result_queue.put(speech_recognition_result.text)
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    result_queue.put("")
    return ""

def playwavetime(file):
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
    # Obtenir la durée totale du fichier audio en secondes
    total_duration = wf.getnframes() / wf.getframerate()
    print(total_duration)
    total_duration = total_duration+stream.get_time()
    chunk = 1024
    data = wf.readframes(chunk)
    
    result_queue = queue.Queue()
    my_queue = False
    def voicetotext2():
        print("Speak into your microphone----------------------------------------------.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
            result_queue.put(speech_recognition_result.text)
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        result_queue.put("")
        return ""
    def Play(data):
        rec = False
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
            current_time = stream.get_time()

            # Obtenir le temps restant en secondes
            remaining_time = total_duration - current_time
            # Afficher le temps restant au format hh:mm:ss
            #print("Temps restant:"+str(remaining_time))
            if(remaining_time<0.6 and rec==False):
                thread = threading.Thread(target=voicetotext2)
                thread.start()
                rec=True
                
        thread.join()
        return True
    
    
    
    # Create two threads to run the functions
    
    thread2 = threading.Thread(target=Play,args=(data,))

    # Start the threads
    #thread.start()
    thread2.start()

    # Wait for the threads to finish
    #thread.join()
    
    thread2.join()
    # close the stream and terminate pyaudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    result = result_queue.get()
    print(result)
    return result

#playwavetime('botvoice/bonjour.wav')
def PlayRecwave(file):
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
    globale = False
    def Play(data):
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
            if(globale==True):
                return
        return True
        
    result_queue = queue.Queue()
    # Create two threads to run the functions
    thread = threading.Thread(target=recognize_from_microphone2,args=(result_queue,))
    thread2 = threading.Thread(target=Play,args=(data,))

    # Start the threads
    thread.start()
    thread2.start()

    # Wait for the threads to finish
    thread.join()
    result = result_queue.get()
    print("--------")
    print(result)
    globale=True
    thread2.join()
    # close the stream and terminate pyaudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    return result


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