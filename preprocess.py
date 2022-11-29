from datetime import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string 

def remove_stopwords(s):

    stop_words = list(stopwords.words('english'))
    word_list = s.split()

    #word_list = [x for x in word_list if len(x)>2]
    word_list = [x for x in word_list if x not in stop_words or len(x)>2]

    return ' '.join(word_list)

def clean_text(df):

    #df = df.apply(lambda x: str(x))
    df = df.str.lower() 
    df = df.apply(lambda x: re.sub(r'http\S+', '', str(x)))
    df = df.apply(lambda x: re.sub(r'http', '', str(x)))
    df = df.apply(lambda x: re.sub(r'www', '', str(x)))
    df = df.apply(lambda x: re.sub(r'<\S+', '', str(x)))
    df = df.apply(lambda x: re.sub(r'[`]', '\'', str(x)))
    df = df.apply(lambda x: re.sub(r'won\'t', 'will not', str(x)))
    df = df.apply(lambda x: re.sub(r'wouldn\'t', 'would not', str(x)))
    df = df.apply(lambda x: re.sub(r'shouldn\'t', 'should not', str(x)))
    df = df.apply(lambda x: re.sub(r'can\'t', 'can not', str(x)))
    df = df.apply(lambda x: re.sub(r'couldn\'t', 'could not', str(x)))
    df = df.apply(lambda x: re.sub(r'doesn\'t', 'does not', str(x)))
    df = df.apply(lambda x: re.sub(r'\'m', ' am', str(x)))
    df = df.apply(lambda x: re.sub(r'\'re', ' are', str(x)))
    df = df.apply(lambda x: re.sub(r'\'s', ' is', str(x)))
    df = df.apply(lambda x: re.sub(r'\'t', ' not', str(x)))
    df = df.apply(lambda x: re.sub(r'\'ll', ' will', str(x)))
    df = df.apply(lambda x: re.sub(r'\'d', ' would', str(x)))
    df = df.apply(lambda x: re.sub(r'\'ve', ' have', str(x)))
    df = df.apply(lambda x: re.sub(r'[!|@|#|$|%|^|?|<|>|\'|"]', '', str(x)))
    df = df.apply(lambda x: re.sub(r'[0-9]', '', str(x)))
    df = df.apply(lambda x: re.sub(r'[-|.|,|:|;|/|~|(|)|[|]|{|}]', ' ', str(x)))
    df = df.apply(lambda x: re.sub(r' +', ' ', str(x)))
    df = df.apply(remove_stopwords)
    #df = df.apply(lambda x: re.sub(r' i ', ' ', str(x)))
    #df = df.apply(lambda x: re.sub(r' a ', ' ', str(x)))

    return df