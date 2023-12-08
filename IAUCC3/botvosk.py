import random
import json
import pickle
import numpy as np
import speech_recognition as sr
import recVoice
import voicetotext
import playwave
import vosktotext

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
    print(return_list)
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
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)
ints = predict_class("Bonjour")
res = get_response(ints,intents)

r = sr.Recognizer()

# ouverture du flux audio à partir du microphone
with sr.Microphone() as source:
    # ajustement automatique du niveau du bruit de fond
    r.adjust_for_ambient_noise(source)
    print("En écoute...")

    # écoute de l'audio en temps réel
    while True:
        try:
            audio = r.listen(source, phrase_time_limit=1)
            start_time = time.time()
            text = r.recognize_google(audio, language='fr-FR')
            print(text)
            ints = predict_class(text)
            res = get_response(ints,intents)
            end_time = time.time()
            execution_time = end_time - start_time
            print("Execution time:", execution_time, "seconds")
            speaker.say(f"{res}")
            speaker.runAndWait()
        except sr.UnknownValueError:
            print("Je n'ai pas compris ce que vous avez dit.")
            speaker.say(f"Je n'ai pas compris ce que vous avez dit.")
            speaker.runAndWait()
        except sr.RequestError as e:
            print(f"Erreur lors de la demande au service de reconnaissance vocale : {e}")

