# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:48:29 2022

@author: mori
"""

from gensim import corpora
from gensim import models
import re

texts=[]

for i in range(5):
    with open('data'+str(i)+".txt") as f:
        tmp_doc=[]
        for line in f:
            s=re.split("\s+",line.strip().lower())
            tmp_doc += s
        texts.append(tmp_doc)
        
dictionary = corpora.Dictionary(texts)
corpus = list(map(dictionary.doc2bow, texts))
test_model = models.TfidfModel(corpus)
corpus_tfidf = test_model[corpus]


doc_tfidf = []
for doc in corpus_tfidf:
    tmp = []
    for word in doc:
        tmp.append([dictionary[word[0]],word[1]])
    doc_tfidf.append(tmp)

for i in range(5):
    print("ddata"+str(i)+".txt")
    sorted_result=sorted(doc_tfidf[i],key=lambda x:x[1],reverse=True)
    print(sorted_result[:5])

