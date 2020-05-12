#       Alex Petralia
#       CSCI 141
#       12/02/2013
#       Project #3 - Ngrams!

import random

###############################Global Variables###########################################

sentence = 'She was'
txt = open('alice.txt')
file = txt.read()
split = file.split()
wordcount = len(split)
ngrams = {}
NumberOfWords = 100

##############################Definitions########################################

def ngram(words):
    TheSentence = sentence.split()
    for x in range(NumberOfWords):
        ngram = []
        for i in range(wordcount):
            if i >= wordcount - 2:
                pass
            else:
                s = [split[i], split[i + 1]]
                z = [TheSentence[x], TheSentence[x + 1]]
                zgram = ' '.join(z)
                gram = ' '.join(s)
                if zgram == gram:
                    ngram.append(split[i + 2])
                else:
                    pass
        g = random.randint(0, len(ngram) - 1)
        TheSentence.append(ngram[g])
    TheSentence = ' '.join(TheSentence)
    print(TheSentence)

##############################Execution#########################################

ngram(sentence)
