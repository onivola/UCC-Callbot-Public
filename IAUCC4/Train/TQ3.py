from Neuronal import Neuronal

# Create a new instance of the Voiture class
neuron = Neuronal("intentQ3.json", "modeleQ3")

neuron.train_model()

neuron.save_model()
neuron.load_model()

ints = neuron.predict_class("Electrique")
res = neuron.get_response(ints)
#print(ints)
print(ints[0])
print(res)