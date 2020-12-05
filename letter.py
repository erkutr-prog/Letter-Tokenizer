#Letter tokenizer for a text
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

#Text
sentences  = []
sentences = str(input("Enter the sentences"))

tokens = Tokenizer()
tokens.fit_on_texts(sentences)
wordİndex = tokens.word_index
print(wordİndex)


