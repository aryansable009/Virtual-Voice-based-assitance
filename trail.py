import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

class IntentClassifier:
    def __init__(self):
        self.data = pd.read_csv('data.csv') #Read the CSV file
        #You might need to change 'data.csv' in the line above to intent_classification/data.csv
        #if you run it from the root directory of the project.
        
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

#Test it out now!
intent_classifier = IntentClassifier()

#Prints greeting
w= intent_classifier.predict("I have problems with canceling an order")

#prints weather
print(type(intent_classifier.predict("i want to cancel my order")))
if w == 'cancel_order':
    print('1')
else:
    print(0)