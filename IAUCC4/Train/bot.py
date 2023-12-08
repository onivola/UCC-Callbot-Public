import random
import json
import numpy as np

import voicetotext
import playwave
import extraction
import pyttsx3 as tts
import sys
import time
from Neuronal import Neuronal


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

neuronq6 = Neuronal("intentQ6.json", "modeleQ6")
neuronq6.load_model()
ints = neuronq6.predict_class("non")
res = neuronq6.get_response(ints)


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
    playwave.playwave('botvoice/'+wav+'.wav') #play wav file
    text = voicetotext.recognize_from_microphone() #rec micro and transcript to text
    print(text)
    ints = neurone.predict_class(text) #neuronal intent
    res = neurone.get_response(ints) #neuronal intent predict
    print(res)
    return res
def ReponseRapide(neurone,wav):
    text =voicetotext.playwavetime('myvoice/'+wav+'.wav') #play wav file
    print(text)
    ints = neurone.predict_class(text) #neuronal intent
    res = neurone.get_response(ints) #neuronal intent predict
    print(res)
    return res

def ReponseNoNeurone(wav):
    text =voicetotext.playwavetime('myvoice/'+wav+'.wav') #play wav file
    print(text)
    return text




def Reponse1():
    resultat = ReponseRapide(neuronq1,"exigence")
    if(resultat=="OuiVerifier"):
        return "propriétaire"
    else:
        return "propriétaire2"
def Reponse2(reponse1):
    resultat = ReponseRapide(neuronq2,reponse1)
    if(resultat=="Proprietaire"):
        return "Proprietaire"
    elif(resultat=="Locataire"):
        playwave.playwave('myvoice/paseligible.wav')
        return "Locataire"
    else:
        playwave.playwave('myvoice/noninteresser.wav')
        return "Non"



ReponseNoNeurone("bonjour")  
reponse1 = Reponse1()
reponse2 = Reponse2(reponse1)
if(reponse2=="Proprietaire"):
    resultat = ReponseRapide(neuronq5,"maison")
    if(resultat=="Ouiindividuel"):
        resultat = ReponseRapide(neuronq3,"chauffage")
        if(resultat=="NonElectrique"):
            resultat = ReponseRapide(neuronq6,"droit")
            if(resultat=="OuiExpliquer"):
                resultat = ReponseRapide(neuronq4,"noter")
                note = False
                if(resultat=="Repeter"):
                    while(note==False):
                        resultat = ReponseRapide(neuronq4,"noterrepeter")
                        if(resultat=="Noter"):
                            note=True
                if(resultat=="Noter" or note==True):
                    resultat = ReponseNoNeurone("portable")
                    resultat = ReponseNoNeurone("valider")
        else:
            playwave.playwave('myvoice/paseligible.wav')
    else:
        playwave.playwave('myvoice/paseligible.wav')
