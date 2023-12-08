import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model
class Neuronal:
    def __init__(self, intents, model_name="assistant_model"):
        self.intents = intents
        self.model_name = model_name

        if intents.endswith(".json"):
            self.load_json_intents(intents)

        self.lemmatizer = WordNetLemmatizer()
    
    def load_json_intents(self,intents):
         self.intents = json.loads(open(intents).read())
    
    
    def train_model(self):
        self.words = []
        self.classes = []
        documents = []
        ignore_letters = ['?','!','.','.',',']

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                word_list = nltk.word_tokenize(pattern)
                self.words.extend(word_list)
                documents.append((word_list, intent['tag']))
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])
                    
        #print(documents)

        self.words = [self.lemmatizer.lemmatize(word) for word in self.words if word not in ignore_letters]
        self.words = sorted(set(self.words))

        #print(words)

        self.classes = sorted(set(self.classes))
        
        training = []
        output_empty = [0]*len(self.classes)

        for document in documents:
            bag = []
            word_patterns = document[0]
            word_patterns = [self.lemmatizer.lemmatize(word.lower()) for word in word_patterns]
            for word in self.words:
                bag.append(1) if word in word_patterns else bag.append(0)

            output_row = list(output_empty)
            output_row[self.classes.index(document[1])] =1
            training.append([bag,output_row])
            
        random.shuffle(training)
        training = np.array(training)

        train_x = list(training[:,0])
        train_y = list(training[:,1])

        #print(train_x)
        #print(train_y)

        self.model = Sequential()
        self.model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(64,activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(len(train_y[0]),activation='softmax'))
        #opt = tf.keras.optimizers.experimental.SGD(learning_rate=0.1)
        opt = tf.keras.optimizers.SGD(learning_rate=0.01)

        self.model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

        self.hist = self.model.fit(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose=1)
        print('Done')

    def save_model(self, model_name=None):
        if model_name is None:
            self.model.save(f"modele/{self.model_name}.h5", self.hist)
            pickle.dump(self.words, open(f'modele/{self.model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(f'modele/{self.model_name}_classes.pkl', 'wb'))
        else:
            self.model.save(f"modele/{model_name}.h5", self.hist)
            pickle.dump(self.words, open(f'modele/{model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(f'modele/{model_name}_classes.pkl', 'wb'))

    def load_model(self, model_name=None):
        if model_name is None:
            self.words = pickle.load(open(f'modele/{self.model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(open(f'modele/{self.model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'modele/{self.model_name}.h5')
        else:
            self.words = pickle.load(open(f'modele/{model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(open(f'modele/{model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'modele/{model_name}.h5')
            
            
    def clean_up_sentence(self,sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bag_of_words(self,sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for s in sentence_words:
            for i, word in enumerate(self.words):
                if word == s:
                    bag[i] = 1
        return np.array(bag)

    def predict_class(self,sentence):
        p = self.bag_of_words(sentence)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})
        print(return_list)
        return return_list
        
    def get_response(self,intents_list):
        try:
            tag = intents_list[0]['intent']
            list_of_intents = self.intents['intents']
            for i in list_of_intents:
                if i['tag']  == tag:
                    result = random.choice(i['responses'])
                    break
            return result
        except IndexError:
            result = "I don't understand!"
            return result 