import sys, os, os.path
from nltk.corpus import wordnet

# Given a filename, opens the file and returns it's text
def read_file(filename):
    f = open(filename)
    text = ""
    for line in f:
        text += line
    return text

# Takes two command-line arguments: a question (query_file), and a document (doc_file)
# Replaces all synonyms of words in the query that are found in the document with the
#	original wording of the query.
# Outputs the result of this to [query_file]_edited.txt
def main():
	query_file = sys.argv[1]
	doc_file = sys.argv[2]
	new_file = os.path.splitext(doc_file)[0] + "_edited.txt"

	query = read_file(query_file)
	text = read_file(doc_file)

	query_words = str.split(query)
	text_words = str.split(text)

	lookup = {}

	# Construct dictionary from words to synonyms in query
	for word in query_words:
		word = str.lower(word)
		if word in lookup:
			break
		synonyms = [lemma.name for lemma in sum([ss.lemmas for ss in wordnet.synsets(word)],[])]
		lookup[word] = synonyms

	# traverse the document looking to replace synonyms of words in the query
	for (i, word) in enumerate(text_words):
		for key in lookup:
			if str.lower(word) in lookup[key]:
       				text_words[i] = key
				break

	text = " ".join(text_words)

	if os.path.exists(new_file):
		os.remove(new_file)
	f = open(new_file, 'w')
	f.write(text)
	f.close()

if __name__ == "__main__":
    main()
