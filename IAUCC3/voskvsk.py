import vosk
import sys
import os
import wave
import json
import pyaudio
import random
import json
import pickle
import numpy as np

import recVoice
import voicetotext
import playwave

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer =WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbotmodel.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    p = bag_of_words(sentence)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    #print(return_list)
    return return_list
    
def get_response(intents_list, intents_json):
    try:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag']  == tag:
                result = random.choice(i['responses'])
                break
        return result
    except IndexError:
        result = "I don't understand!"
        return result 
"""
message = "hi"
ints = predict_class(message)
res = get_response(ints,intents)
print("Go! Bot is running!")
while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints,intents)
    print(res)
"""
import speech_recognition
import pyttsx3 as tts
import sys
import time

speaker = tts.init()
speaker.setProperty('rate',150)
ints = predict_class("Bonjour")
res = get_response(ints,intents)
    
# Chemin vers le modèle de reconnaissance vocale
model_path = r"E:\Travaille\IAUCC\IAUCC3\vosk-model-small-fr-0.22"

# Chargement du modèle de reconnaissance vocale
modelvosk = vosk.Model(model_path)

# Initialisation du recognizer
recognizer = vosk.KaldiRecognizer(modelvosk, 16000)

# Configuration du microphone et du flux audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Boucle de capture et de transcription de la parole
def callloop():
    while True:
        data = stream.read(4000 , exception_on_overflow=False)
        
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            print("-boucle-")
            start_time = time.time()
            result = recognizer.Result()
            result_dict = json.loads(result)
            print("result="+result)
            text = result_dict['text']
            print("text="+text)
            if(text!=""):
                text = ""
                print("null")
                ints = predict_class(text)
                print("text="+text)
                res = get_response(ints,intents)
                end_time = time.time()
                execution_time = end_time - start_time
                print("Execution time:", execution_time, "seconds")
                speaker.say(f"{res}")
                speaker.runAndWait()
                #break
                #callloop()
            
callloop()