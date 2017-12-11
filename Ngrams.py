""" ------------------------------------------------------------------------
File: NGrams.py
Author: Fouad El Hamdouni and Jennifer Arnold
Date: December 2017

This file contains an implementation of N-Grams, specifically bigrams where it takes in a two textfiles found
in the Paper Santitized folder of this project. The bigrams are returned as a dictionary and the Counter
package accumulates the frequency and retuns a list of tuples, using the birgram as the key and the
frequency as its value.

NOTES:
  * this DOES NOT make use of the NLP Python library
  * print statements are Python 3 style,
  * Must be run in Python 3.4
----------------------------------------------------------------------------
"""
"Imports"

from collections import Counter
import numpy as np


#------------------------------------------------------------------------
# The section that follows is where you can add in two files to be read and words split.
# Files must be found in the Paper sanitized folder, if you would like to add in a new text file
# you must "sanitize it" by using the Working Text Files class and drag the file to the sanitized folder.

path = "Papers_sanitized/FederalistNo_10_san.txt"
file = open(path, 'r', errors='replace')
text1 = file.read()
text1 = text1.split()

path = "Papers_sanitized/FederalistNo_10_san_A.txt"
file = open(path, 'r', errors='replace')
text2 = file.read()
text2 = text2.split()


#-------------------------------------------------------------------------
# The section that follows contains all the main and helper methods.

def find_ngrams(text):
    """Given a text, the method parses through the text and finds all the bigrams."""
    bigram = []
    for i in range(len(text)-1):
        bigram.append((text[i], text[i+1]))
    return bigram


def CountertoDict(text1, text2):
    """Given two texts, the method converts the Counter for each text and returns all the bigrams from both texts"""
    dict1 = dict(Counter(find_ngrams(text1)))
    dict2 = dict(Counter(find_ngrams(text2)))
    dict3 = merge_two_dicts(dict1, dict2)
    return list(dict3.keys())


def merge_two_dicts(x, y):
    """This is a helper function to merge two dictionnaries together"""
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


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
            freq = dictionary.get(bigram)
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

# Dictionary frequency for the first text
nGramsText1 = find_ngrams(text1)
dictFreqText1 = dict(Counter(nGramsText1))


# Dictionary frequency for the second text
nGramsText2 = find_ngrams(text2)
dictFreqText2 = dict(Counter(nGramsText2))

nGramsDict = CountertoDict(text1, text2)

# print("======= TESTING ========")
# print(makeIndividualFreqSet(dictFreqText1, nGramsDict))

setFreqText1 = makeIndividualFreqSet(dictFreqText1, nGramsDict)
setFreqText2 = makeIndividualFreqSet(dictFreqText2, nGramsDict)

sentence_m = np.array(setFreqText1)
sentence_h = np.array(setFreqText2)


first = cosine_similarity(sentence_h, sentence_m)
print(first)



