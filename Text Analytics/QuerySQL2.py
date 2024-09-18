# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:26:01 2020

@author: gmunaretti
"""

import pyodbc
import nltk
import pandas as pd

# Generar conexion con la base de datos
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=ezesql;'
                          'Database=OPERACIONES;'
                          'Trusted_Connection=yes;')

# Definir un cursor
cur = conn.cursor()


# Definir consulta SQL
querystring = "SELECT  A.[diagnostico] FROM [OPERACIONES].[RrHh].[MedicinaLab_Cab] as A WHERE A.fecha > '2018-01-01'"


# Ejecutar consulta
cur.execute(querystring)

# Generar lista con los datos de la consulta
tabla =  cur.fetchall()


df=pd.DataFrame(tabla)
str1 = ""  
# recorrer lista pàra verificar
for r in tabla:
    print( r)
    str1 += r
    
# Cerrar la conexion    
conn.close()


# Moda
df.mode()

print(tabla)

str2=[row[0] for row in tabla]

cadena = " ".join(str2)

print(cadena)

cadena = cadena.lower()



cadena = cadena.replace('[^ \w \s]','')
cadena = cadena.replace('[^\w\s]','')



print(cadena)



"""########################################################################"""


# El tokenizer de Word divide el párrafo de texto en palabras.

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(cadena)
print(tokenized_word)


#Distribución de frecuencias

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)


fdist.most_common(5)


# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


from nltk.corpus import stopwords
stop_words=set(stopwords.words("spanish"))
print(stop_words)



filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent)






#Distribución de frecuencias

from nltk.probability import FreqDist
fdist = FreqDist(filtered_sent)
print(fdist)


fdist.most_common(3)


# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()





"""##################################################################"""

stop_words2 = [".",",","izq","tx","de","en","y","con","la","el","por","a","se","que","dolor","izquierdo","izquierda","derecho","derecha","me","no","refiere","gec","2018","del","cx","2019","cuadro","hta","sme","+",":"]

filtered_sent2=[]
for w in tokenized_word:
    if w not in stop_words2:
        filtered_sent2.append(w)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent2)




#Distribución de frecuencias

from nltk.probability import FreqDist
fdist = FreqDist(filtered_sent2)
print(fdist)


fdist.most_common(3)


"""#########################################################################"""

from nltk.stem import SnowballStemmer
sb = SnowballStemmer('spanish')


for words in filtered_sent2:
    print(words+ ":" +sb.stem(words))



from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer




from es_lemmatizer import lemmatize
import spacy
nlp = spacy.load("es")
nlp.add_pipe(lemmatize, after="tagger")




import textacy
text = 'Los gatos y los perros juegan juntos en el patio de su casa'
doc = textacy.Doc(text, lang='es')
print(doc.to_bag_of_words(normalize='lemma', as_strings=True))


"""#########################################################################"""



""" Pruebas de Clase """





# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()



cadCorpus = ' '.join(filtered_sent2)
from wordcloud import WordCloud
wordcloud = WordCloud().generate(cadCorpus)
import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

from Class.TextMinigA import TextMining as pf

pf.ver("")


from Class.TextMinigA import TextMining

ty = TextMining()

TextMining().ver()

ty.ver()


"""#########################################################################"""


from Class.TextMinigA import TextMining

tm = TextMining()

cad1 = tm.remove_non_ascii(tokenized_word)
cad2 = tm.to_lowercase(cad1)
cad3 = tm.remove_punctuation(cad2)
cad4 = tm.replace_numbers(cad3)
cad5 = tm.remove_stopwords(cad4)
cad6 = tm.stem_words(cad5)
cad7 = tm.lemmatize_verbs(cad6)

print(cad7)



from nltk.probability import FreqDist
fdist = FreqDist(cad7)
print(fdist)


fdist.most_common(3)



# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


cadCorpus = ' '.join(cad7)
from wordcloud import WordCloud
wordcloud = WordCloud().generate(cadCorpus)
import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")













