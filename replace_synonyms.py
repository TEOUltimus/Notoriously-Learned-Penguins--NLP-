from nltk.corpus import wordnet
import sys
import os
import os.path

def read_file(filename):
    f = open(filename)
    text = ""
    for line in f:
        text += line
    return text

query_file = sys.argv[1]
doc_file = sys.argv[2]
new_file = os.path.splitext(doc_file)[0] + "_edited.txt"

query = read_file(query_file)
text = read_file(doc_file)

query_words = str.split(query)
text_words = str.split(text)

for word in query_words:
    synonyms = [lemma.name for lemma in sum([ss.lemmas for ss in wordnet.synsets(str.lower(word))],[])]
    for (i, w) in enumerate(text_words):
        if str.lower(w) in synonyms:
            text_words[i] = word

text = " ".join(text_words)

if os.path.exists(new_file):
    os.remove(new_file)
f = open(new_file, 'w')
f.write(text)
f.close()
