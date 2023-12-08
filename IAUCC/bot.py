import LUIS
import extraction
import recVoice
import voicetotext
import playwave
import time

LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/2a9f0849-04e1-4c3c-9659-490d07d52ed8/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="

#QUESTION 1
#playwave.playwave('botvoice/bonjour.wav')
print("Bonjour, Je suis Léa du bureau de la transition énérgétique et je vous appelle pour vérifier si vous êtes éligible au programme de la pompe à chaleur à 1Euro. En avez vous entendu parler ?")

recVoice.RecVoice('rep1')
start_time = time.time()
q = voicetotext.VoiceToText('rep1.wav')
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
print(q)
#QUESTION 2
playwave.playwave('botvoice/exigence.wav')
print("Suite à l'explosion du coût énérgétique, l'Etat à renouvelé pour 2023 les aides pour les propriétaires de maison individuelles afin d'éviter de perdre totalement le contrôle sur les factures de chauffage. Avez-vous 2 petites minutes à m'accorder afin de verifier si vous répondez aux exigences du programme ?")

q = recVoice.RecVoice('rep1')
print(q)
rep = voicetotext.VoiceToText('rep1.wav')
print(rep)

topIntent, score =LUIS.PredictLUIS(LUISurl,rep)
#print(topIntent)
#print(score)
rep3 = ""
rep4 = ""
rep5 = ""
rep6 = ""
if(topIntent=="OuiVerifier"):
    playwave.playwave('botvoice/propriétaire.wav')
    print("Parfait")
    print("Etes-vous propriétaire ou locataire?")
    q = recVoice.RecVoice('rep1')
    rep3 = voicetotext.VoiceToText('rep1.wav')
    LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/df85c175-869f-4db2-aadb-b55157e21491/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
    print(rep3)
    topIntent, score =LUIS.PredictLUIS(LUISurl,rep3)
    #print(topIntent)
    #print(score)
    if(topIntent=='Proprietaire'):
        playwave.playwave('botvoice/maison.wav')
        print('C\'est bien une maison individuelle ?')
        LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/fc42763d-f0a9-4ce9-b64d-eee8ef3c9bce/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
        #rep4 = input()
        q = recVoice.RecVoice('rep1')
        rep4 = voicetotext.VoiceToText('rep1.wav')
        print(rep4)
        topIntent, score =LUIS.PredictLUIS(LUISurl,rep4)
       # print(topIntent)
        #print(score)
        if(topIntent=='OuiIndividuelle'):
            playwave.playwave('botvoice/chauffage.wav')
            print("Quelle est votre mode de chauffage actueil?")
            LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/16fb03fa-aa4a-4037-8d45-95e04a79fc8a/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
            #rep5 = input()
            q = recVoice.RecVoice('rep1')
            rep5 = voicetotext.VoiceToText('rep1.wav')
            print(rep5)
            topIntent, score =LUIS.PredictLUIS(LUISurl,rep5)
            #print(topIntent)
            #print(score)
            if(topIntent=='OuiElectrique'):
                print("Au revoir")
            elif(topIntent=='NonElectrique'):
                playwave.playwave('botvoice/droit.wav')
                print("Parfait, vous semblez bien éligible aux dispositifs 2023. Plusieurs dispositifs peuvent d'ailleurs s'ajouter à la pompe à chaleur à 1 £. Donc concrètement, vous pourrez faire diminuer votre facture de chauffage jusqu'à 75% sans payer autre chose qu'1£ symbolique. Moi à mon niveau je ne suis pas habilité à vous donner plus de renseignements mais souhaitez-vous que je demande à un agent habilité de vous contacter pour vous expliquer exactement à quoi vous avez le droit")
                LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/57622c6e-a17c-474c-ba32-e9739203e859/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
                #rep6 = input()
                q = recVoice.RecVoice('rep1')
                rep6 = voicetotext.VoiceToText('rep1.wav')
                print(rep6)
                topIntent, score =LUIS.PredictLUIS(LUISurl,rep6)
                #print(topIntent)
                #print(score)
                if(topIntent=="OuiExpliquer"):
                    playwave.playwave('botvoice/noter.wav')
                    print("Parfait, je vais vous donner un numéro de dossier afin d'être sûr que la personne qui vous contacte fait bien partie de ce programme et qu'elle ne fait pas partie des nombreuses sociétés qui tentent de vous vendre à des prix exorbitants")
                    print("DM018RENOV. Vous avez bien noté ?")
                    LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/a44abb60-cd4d-410d-a6b7-13a8500fdb44/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
                    #rep6 = input()
                    q = recVoice.RecVoice('rep1')
                    rep6 = voicetotext.VoiceToText('rep1.wav')
                    print(rep6)
                    topIntent, score =LUIS.PredictLUIS(LUISurl,rep6)
                    #print(topIntent)
                    note =False
                    if(topIntent=="Repeter"):
                        
                        while(note==False):
                            playwave.playwave('botvoice/noterrepeter.wav')
                            print('je répète DM018RENOV')
                            LUISurl = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/a44abb60-cd4d-410d-a6b7-13a8500fdb44/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
                            #rep6 = input()
                            q = recVoice.RecVoice('rep1')
                            rep6 = voicetotext.VoiceToText('rep1.wav')
                            print(rep6)
                            topIntent, score =LUIS.PredictLUIS(LUISurl,rep6)
                            #print(topIntent)
                            if(topIntent=="Noter"):
                                note=True
                            
                    if(topIntent=="Noter" or note==True):
                        playwave.playwave('botvoice/portable.wav')
                        print('Parfait, Puis-je avoir un portable pour qu\'ils puissent vous contacter plus facilement?')
                        #rep7 = input()
                        q = recVoice.RecVoice('rep1')
                        rep7 = voicetotext.VoiceToText('rep1.wav')
                        print(rep7)
                        numero = extraction.PhoneNumber(rep7)
                        print(numero[0])
                        playwave.playwave('botvoice/mail.wav')
                        print('Et votre mail?')
                        q = recVoice.RecVoice('rep1')
                        rep7 = voicetotext.VoiceToText('rep1.wav')
                        #rep7 = input()
                        email = extraction.Email(rep7)
                        print(email[0])
                        playwave.playwave('botvoice/valider.wav')
                        print('Parfait, si quelqu\'un vous appelle et n\'est pas en mesure de vous donner ce code de sécurité, vous pouvez raccrocher directement, c\'est qu\'il ne fait pas partie du programme.')
                        print('Je vous souhaite entre temps une excellente journée.')
                        
                    #print(topIntent)
                    #print(score)
                if(topIntent=="NonExpliquer"):
                    print("Au revoir")
        elif(topIntent=='NonIndividuelle'):
            print("Au revoir")
    elif(topIntent=='Locataire'):
        print("Au revoir")
    
elif(topIntent=="NonVerifier"):
    print("Au revoir")