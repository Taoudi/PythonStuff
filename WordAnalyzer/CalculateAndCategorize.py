import re
import operator
import nltk

fh = open("movie", "r")
script = fh.read()
script = script.lower()
tokens = nltk.word_tokenize(script)
tagged = nltk.pos_tag(tokens)
data = {}
splitted = re.findall(r"[\w']+", script)

i = 0
while i < len(tagged):
    word = tagged[i]
    if word in data:
        data[word] += 1
    else:
        data[word] = 1
    i += 1

another_fh = open("words", "w")
for key in sorted(data, key=operator.itemgetter(1), reverse=True):
    another_fh.write(str(data[key]) + " - " + str(key[0]) + " - " + str(key[1]) + "\n")
    i += 1

another_fh.close()

