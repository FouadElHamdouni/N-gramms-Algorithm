#-------------------------------------------------------------------------

import nltk
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import numpy as np
import numpy.linalg
#-------------------------------------------------------------------------


path = "Papers_sanitized/FederalistNo_2_san.txt"
file = open(path, 'r', errors='replace')
text1 = file.read()
text1 = text1.split()

path = "Papers_sanitized/FederalistNo_10_san.txt"
file = open(path, 'r', errors='replace')
text2 = file.read()
text2 = text2.split()


def find_ngrams(text):
    bigram = []
    for i in range(len(text)-1):
        bigram.append((text[i], text[i+1]))
    return bigram

# print(dict(Counter(find_ngrams(text))))



def CountertoDict(text1, text2):
    dict1 = dict(Counter(find_ngrams(text1)))
    print("dict1 is:" + str(dict1))
    dict2 = dict(Counter(find_ngrams(text2)))
    dict3 = merge_two_dicts(dict1, dict2)
    return dict3.keys()


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

print(CountertoDict(text1, text2))



#-------------------------------------------------------------------------
# print(text)
# token = nltk.word_tokenize(text)
# bigrams = ngrams(token, 2)
# trigrams = ngrams(token, 3)
# fourgrams = ngrams(token, 4)
# fivegrams = ngrams(token, 5)
#
# print(Counter(bigrams))
#-------------------------------------------------------------------------

#
# def makeIndividualFreqSet(c, a):
#     c = counter
#     allBigrams = a
#     for each bigram in allBigrams:


# def cosine_similarity(a, b):
#     dot_product = np.dot(a, b)
#     norm_a = np.linalg.norm(a)
#     norm_b = np.linalg.norm(b)
#     return dot_product / (norm_a*norm_b)
#
# # Example
# listOfNum = [1, 1, 1, 1, 0, 0, 0, 0, 0]
# sentence_m = np.array(listOfNum)
# sentence_h = np.array([0, 3, 1, 1, 1, 2, 0, 0, 0])
# sentence_w = np.array([0, 0, 4, 1, 0, 0, 1, 4, 1])
#
# first = cosine_similarity(sentence_h, sentence_w)
# print(first)



