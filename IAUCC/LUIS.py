import requests
from bs4 import BeautifulSoup
import json

def test():
    print('test')
def PredictLUIS(url,query):
    #"https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/2a9f0849-04e1-4c3c-9659-490d07d52ed8/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query="
    url = url+query
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    #print(text)
    json_data = json.loads(text)
    return json_data['prediction']['topIntent'],json_data['prediction']['intents'][json_data['prediction']['topIntent']]['score']
    #print(json_data)
    #print(json_data['prediction']['topIntent']) #topIntent
    #print(json_data['prediction']['intents'][json_data['prediction']['topIntent']]['score']) #score
    #print("Execution time:", execution_time, "seconds")

#{'query': 'non', 'prediction': 
#{'topIntent': 'NonVerifier', 'intents': {'NonVerifier': {'score': 0.94052225}, 'OuiVerifier': {'score': 0.04115706}, 'None': {'score': 0.017315136}}, 'entities': {}}}