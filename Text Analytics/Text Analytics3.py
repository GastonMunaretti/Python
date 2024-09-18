# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:30:21 2020

@author: gmunaretti
"""

import Stemmer

print(Stemmer.algorithms())
stemmer = Stemmer.Stemmer('spanish')
print(stemmer.stemWord('trabajar'))














from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
 
print(stemmer.stem('trabajando'))




from nltk.corpus import wordnet
 
synonyms = []
 
for syn in wordnet.synsets('Computadora'):
 
    for lemma in syn.lemmas():
 
        synonyms.append(lemma.name())
 
print(synonyms)