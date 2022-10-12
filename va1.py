import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            try:
                command = listener.recognize_google(voice)
                if 'cat' in command:
                    command = command.replace('cat', '')
                print(command)
            except:
                print("sorry, could not recognise")
    except:
        pass
    return command


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB #Import Naive Bayes

class IntentClassifier:
    def __init__(self):
        self.data = pd.read_csv('data.csv') #Read the CSV file
    
        
        self.train() #It will train whenever an instance is made

    def train(self):
        X_train, y_train= self.data['utterance'], self.data['intent']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts) #Calculates tf-idf for the text
        self.clf = MultinomialNB().fit(X_train_tfidf, y_train)
    
    def predict(self, text):
        return self.clf.predict(self.count_vect.transform([text]))[0]

def module (command):
    intent_classifier = IntentClassifier()
    x = intent_classifier.predict(command)
    return x 

isTrue = True
df2 = pd.read_csv('Book2.csv')
df2= df2.set_index('Lodin_ID')
tf = True
while tf == True:
    talk('Please enter your account details')   
    id1 = int(input('ENTER LOGN ID : '))
    password = input('ENTER Password : ')
    try:
        passw = df2.loc[id1,'Password'] 
        if passw== password:
            tf = False
        else:
            talk('invalid Password')
            print('invalid Password')
    except KeyError:
        talk("Invalid Login ID")
        print ("Invalid Login ID")
order = df2.loc[id1, 'order']
ordp =  df2.loc[id1, 'Order_price']
add = df2.loc[id1, 'shipping_adress']

def edit(x,y,z):
    df2.loc[x, y ] = z
talk('how may i help you')
def run_cat():
    command = take_command()
    x = module (command)

    if x == 'change_order':
       talk('What is your new order?')
       up =take_command()
       edit(id1 , 'order',up)
    elif x == 'change_shipping_address':
        talk('What is your new Shipping address?')
        up1 =take_command()
        edit(id1 , 'shipping_adress',up1)
    elif x == 'contact_customer_service':
        talk('you can see your customer service Contact informationon the screen ')
        print('9420189209')
        print('mail : shanbndseh@mitwpu.in')
    elif x == 'check_cancellation_fee':
        talk('Cancelation fee is 200 rupees')
    elif x== 'set_up_shipping_address':
        talk('what is your adress')
        up3 = take_command()
        edit(id1, 'shipping_adress',up3)
    elif x == 'check_invoice':
        talk('Here is your invoice')
        print(df2.loc[id1,['order','Order_price','shipping_adress']])

    else:
        talk('Please say the command again.')

while isTrue:
    run_cat()