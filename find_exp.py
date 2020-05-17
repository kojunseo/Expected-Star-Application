import numpy as np
from konlpy.tag import Okt
import pandas as pd

whole = pd.read_csv("for_app.csv")
whole.전처리=whole.전처리.astype(str)
train_text = list(whole["전처리"])
train_sent = list(whole["별점"])

from sklearn.feature_extraction.text import CountVectorizer
CV = CountVectorizer(lowercase=True, max_df=1.0)
term_docs_train_s = CV.fit_transform(train_text)
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB(alpha = 0.25, fit_prior=False)
nb.fit(term_docs_train_s, train_sent)



okt = Okt()

def clean_text(text):
    text = okt.pos(text, norm=True, stem=True)
    tmp = []
    for i in text:
        if i[1] == "Adjective" or i[1] == "Noun" or i[1] == "Verb" or i[1] == "Adjective" or i[1] == "Suffix" or i[1] == "KoreanParticle":
            tmp.append(i[0])

    return " ".join(tmp)


import pandas as pd



def get_expected(review):
    a = [review]
    a_test = CV.transform(a)
    return nb.predict(a_test)[0]

get_expected("너무 착하고 좋으신 교수")