import random
import json
import numpy as np

import voicetotext
import playwave
import pyttsx3 as tts
import sys
import time
from Neuronal import Neuronal
import threading

# Create a new instance of the neuronal class
neuronq1 = Neuronal("intentQ1.json", "modeleQ1")
neuronq1.load_model()
ints = neuronq1.predict_class("non")
res = neuronq1.get_response(ints)

neuronq2 = Neuronal("intentQ2.json", "modeleQ2")
neuronq2.load_model()
ints = neuronq2.predict_class("non")
res = neuronq2.get_response(ints)

neuronq5 = Neuronal("intentQ5.json", "modeleQ5")
neuronq5.load_model()
ints = neuronq5.predict_class("non")
res = neuronq5.get_response(ints)

neuronq3 = Neuronal("intentQ3.json", "modeleQ3")
neuronq3.load_model()
ints = neuronq3.predict_class("non")
res = neuronq3.get_response(ints)


neuronq4 = Neuronal("intentQ4.json", "modeleQ4")
neuronq4.load_model()
ints = neuronq4.predict_class("non")
res = neuronq4.get_response(ints)

def Rep1():
    playwave.playwave('botvoice/bonjour.wav') #play wav file
    text = voicetotext.recognize_from_microphone() #rec micro and transcript to text
    print(text)
    return text
def Reponse(neurone,wav):
    #playwave.playwave('botvoice/'+wav+'.wav') #play wav file
    #text = voicetotext.recognize_from_microphone() #rec micro and transcript to text
    text = voicetotext.PlayRecwave('botvoice/'+wav+'.wav') #play and rec at the same time
    print("---")
    print(text)
    ints = neurone.predict_class(text) #neuronal intent
    res = neurone.get_response(ints) #neuronal intent predict
    print(res)
    return res

#voicetotext.PlayRecwave('botvoice/exigence.wav')

#resultat = Rep1()
resultat = Reponse(neuronq1,"exigence")
if(resultat=="OuiVerifier"):
    resultat = Reponse(neuronq2,"propriétaire")
    if(resultat=="Proprietaire"):
        resultat = Reponse(neuronq5,"maison")
        if(resultat=="Ouiindividuel"):
            resultat = Reponse(neuronq3,"chauffage")
            if(resultat=="NonElectrique"):
                resultat = Reponse(neuronq4,"droit")