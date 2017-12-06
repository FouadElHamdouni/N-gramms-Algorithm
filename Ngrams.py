import nltk
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

text = set(open("1970ALB.txt", 'r'))

token = nltk.word_tokenize(text)
bigrams = ngrams(token, 2)
trigrams = ngrams(token, 3)
fourgrams = ngrams(token, 4)
fivegrams = ngrams(token, 5)

print(Counter(bigrams))


# listgram = ["all", "is", "good", "between", "us"]
#
# def find_ngrams(listofGrams):
#     bigram = []
#     for i in range(len(listofGrams)-1):
#         bigram.append((listofGrams[i], listofGrams[i+1]))
#     return bigram
#
#
#
# print(find_ngrams(listgram))
