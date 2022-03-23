import pandas as pd
import json
import time
import numpy as np
from datetime import datetime
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download ()
stop_words= set(stopwords.words('english'))

## Cleaning the dataframe

def clean_df(df):
    
    df['created_at'] = pd.to_datetime(df['created_at'])

    pub_metz = pd.Series(df["public_metrics"])
    pm_df = pd.DataFrame(columns=['retweet_count', 'reply_count', 'like_count', 'quote_count'])

    k = []
    for d in pub_metz:
        k.append(d)
    
    pub_metz_clean = pd.DataFrame(k)
                                        
    df= pd.concat([df,pub_metz_clean], axis=1)                                
    df= df.drop(columns= ["public_metrics","entities","id"])
                                
    text_df= df["text"]
    #df= df.drop(columns= "text")
                                
    return df

                                  
##  Preprocessing text in text column
                                  
def preprocess_text(df):
    texts= df["text"]
    lemma_words= []
    for text in texts:
    # convert text to lower case
        text= text.lower()
    
    # remove urls if any
        text= re.sub(r'(http\s|ftp\s|https\s|www)(://|\.)[A-Za-z0-9-_\.]*(\.)[a-z]', " " , text, flags= re.MULTILINE)
    
    # remove punctuation
        text= text.translate(str.maketrans("", "", string.punctuation))
    
    # remove @, #
        text= re.sub(r'\@\w+|\#'," ", text)
    
    # remove stopwords
        text_tokens= word_tokenize(text)
        filtered_words= [word for word in text_tokens if word not in stop_words]
    
    # lemmatizing
        lemmatizer= WordNetLemmatizer()
        lemma_word= [lemmatizer.lemmatize(word, pos='a') for word in filtered_words]
        for word in lemma_word:
            lemma_words.append(word)
    return lemma_words
                                  
                                  
    
## Converting preprocessed text to vectors
                                  
def get_feature_vector(lemma_words):
    print(lemma_words)
    vector= TfidfVectorizer(sublinear_tf= True)
    X = vector.fit_transform(lemma_words)
    print(X.shape)
    return X
                                  
                                  