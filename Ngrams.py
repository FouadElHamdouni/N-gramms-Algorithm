
"-------------------------------------------------------------------------"
"Imports"
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
text = file.read()
text = text.split()


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


# ------------------------------ Methods ---------------------------------
#-------------------------------------------------------------------------

def find_ngrams(text):
    """Given a text, the method parses through the text and finds all the bigrams."""
    bigram = []
    for i in range(len(text)-1):
        bigram.append((text[i], text[i+1]))
    return bigram

def makeIndividualFreqSet(counterForTextFile, allList):
    """ Method takes in dictionary for a textfile and a list of all the bigrams, returning an frequency list for one particular textfile.
    """
    dictionary = counterForTextFile
    allBigrams = allList

    # New empty list
    freqList = []

    for bigram in allBigrams:
        # find bigram in counter
        if (bigram in dictionary):
            freq = dictionary.get[bigram]
            freqList.append(freq)
        else:
            freq = 0
            freqList.append(freq)
    return freqList


def cosine_similarity(a, b):
    """ Method compares two freqencies arrays that represent the frequencies of two seperate textfiles and returns how dissimilar they are.
    The more similarly related a file is, the closer it is to 1.0."""
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a*norm_b)

#-------------------------------------------------------------------------

# Example
listOfNum = [1, 1, 1, 1, 0, 0, 0, 0, 0]
sentence_m = np.array(listOfNum)
sentence_h = np.array([0, 3, 1, 1, 1, 2, 0, 0, 0])
sentence_w = np.array([0, 0, 4, 1, 0, 0, 1, 4, 1])

first = cosine_similarity(sentence_h, sentence_w)
print(first)

# Each bigram is going to be a tuple
print(dict(Counter(find_ngrams(text))))



