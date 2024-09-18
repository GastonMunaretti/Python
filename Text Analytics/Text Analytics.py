# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:58:54 2020

@author: gmunaretti
"""

#Loading NLTK
import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)



from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)


from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

fdist.most_common(2)




# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()
