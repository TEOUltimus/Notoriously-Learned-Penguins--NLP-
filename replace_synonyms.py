import os, os.path, string, sys
from nltk.corpus import wordnet
from nltk.tokenize.punkt import PunktWordTokenizer

# Given a filename, opens the file and returns its text
def read_file(filename):
	with open(filename) as f:
		text = ""
		for line in f:
			text += line
		return text

# translates name of input file into output file
def output_name(fname):
	return os.path.splitext(fname)[0] + "_edited.txt"

# Takes two command-line arguments: a question (query_file), and 
# a document (doc_file)
# Replaces all synonyms of words in the query that are found in the document
# with the original wording of the query.
# Outputs the result of this to [query_file]_edited.txt
def main():
	query_file = sys.argv[1]
	doc_file = sys.argv[2]
	new_file = output_name(doc_file)

	query = read_file(query_file).translate(None, string.punctuation)
	query_words = PunktWordTokenizer().tokenize(query)

	lookup = {}

	# Construct dictionary from words to synonyms in query
	for word in query_words:
		word = str.lower(word)
		if word in lookup:
			break
		synonyms = [lemma.name for lemma in sum([ss.lemmas for ss in wordnet.synsets(word)],[])]
		lookup[word] = synonyms

	output = ""
	with open(doc_file) as f:
		# traverse the document looking to replace synonyms of words in the query
		for line in f:
			text = line.translate(None, string.punctuation)
			text_words = PunktWordTokenizer().tokenize(text)
			for (i, word) in enumerate(text_words):
				for key in lookup:
					if str.lower(word) in lookup[key]:
						text_words[i] = key
						break
			output += " ".join(text_words) + "\n"

	if os.path.exists(new_file):
		os.remove(new_file)
	with open(new_file, 'w') as f:
		f.write(output)
	print 'done'

if __name__ == "__main__":
	main()
