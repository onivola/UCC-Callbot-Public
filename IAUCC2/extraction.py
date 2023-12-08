#fonction extraction des informations 'email' 'adresse' et numero de telephone
import re

#texte = "Je suis situé au 15 rue des Lilas, 75020 Paris je suis un mec brillant avec chatGPT mais on realite lksdfjalk;sghfdaskdnvjkash . Mon adresse e-mail est contact@example.com. Je suis également joignable au 06 01 02 03 04. Mon autre adresse est 123 avenue des Champs-Élysées, 75008 Paris. Bonjour, vous pouvez me contacter à l'adresse e-mail john@example.com ou par téléphone au 06 01 02 03 04. Mon deuxième numéro de téléphone est le 01-23-45-67-89. Mon adresse e-mail de secours est john.doe@gmail.com."
# Extraire les adresses e-mail

def Email(texte):
	Emails=[]
	emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texte)
	#print("Adresses e-mail trouvées :")
	for email in emails:
	    #print(email)
	    Emails.append(email)
	return Emails


# Extraire les numéros de téléphone
def PhoneNumber(texte):
	Numb=[]
	telephones = re.findall(r'\b0[1-9](?:[\s.-]*\d{2}){4}\b', texte)
	#print("Numéros de téléphone trouvés :")
	for telephone in telephones:
	    Numb.append(telephone)
	    #print(telephone)
	return Numb

# Extraire les adresses en France

def Adress(texte):
	Adress=[]
	adresses = re.findall(r'\b[0-9]{1,4}\s(?:[a-zA-Z\u00C0-\u017F]+\s)+[a-zA-Z\u00C0-\u017F]+,\s[0-9]{5}\s[a-zA-Z\u00C0-\u017F]+\b', texte)
	#print("Adresses en France trouvées :")
	for adresse in adresses:
	    #print(adresse)
	    Adress.append(adresse)
	return Adress


text = "mon numéro est 034 60 556 78"
num = PhoneNumber(text)
print(num)