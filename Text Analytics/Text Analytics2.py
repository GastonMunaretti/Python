# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:20:45 2020

@author: gmunaretti
"""

# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
# sample text for performing tokenization
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America"






# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token






#Finding frequency distinct in the text
# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist



# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
fdist1



