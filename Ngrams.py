import nltk
nltk.download('punkt')
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

file = open("/Users/jenniferarnold/PycharmProjects/N-gramms-Algorithm/Papers/FederalistNo.84Hamilton.txt", 'r', errors='replace')
text = file.read()
text = text.split()

# # print(text)
# token = nltk.word_tokenize(text)
# bigrams = ngrams(token, 2)
# trigrams = ngrams(token, 3)
# fourgrams = ngrams(token, 4)
# fivegrams = ngrams(token, 5)
#
# print(Counter(bigrams))



def find_ngrams(text):
    bigram = []
    for i in range(len(text)-1):
        bigram.append((text[i], text[i+1]))
    return bigram



print(Counter(find_ngrams(text)))
