import os, re, sys
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktWordTokenizer
from stat_parser import Parser

# Set up verbs, will later do pos tagging to include maybe_verbs as well
verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'could',
	'do', 'did', 'does', 'doing', 'have', 'has', 'having',
	'must', 'shall', 'should', 'would']
maybe_verbs = ['can', 'had', 'may', 'might', 'will']
punctuation = ['.', ',', '?', '!']
parser = Parser()
# Parse tree of a good question should match this
goodQ = re.compile('\\(SBARQ')

# Given a sentence, return a question if possible (and '' otherwise) 
def to_question(sent):
	verb = ''
	sentence = sent.split('.')[0]
	for i in xrange(0, len(sentence)):
		if sentence[i] in verbs:
			# for the first auxilliary ver found, move it to the fron of the sentence
			verb = sentence[i]
			sentence.remove(verb)
			sentence.insert(0, verb)

			# replace final punctuation if any is present
			if sentence[-1] in punctuation:
				sentence[-1] = '?'
			else:
				sentence.append('?')

			# attempt to verify prospective question is grammatical
			sent =  ' '.join(sentence)
			ptree = parser.parse(sent)
			ptreenode = ptree.node
			#print ptree
			if goodQ.match(ptree):
				return sent
			else:
				return ''
	return ''

def main():
	textfile = sys.argv[1]
	lines = None
	text = []
	with open(textfile) as f:
		lines = f.readlines()

	# remove newlines and tokenize sentences
	for i in xrange(0, len(lines)):
		lines[i] = lines[i].split('\n')[0].lower()
		text += PunktSentenceTokenizer().tokenize(lines[i])
	#text =i ' '.join(lines)
	
	#lines = PunktSentenceTokenizer().tokeniize(text)

	# list of questions to return
	questions = []
	for i in xrange(0, len(text)):
		out = text[i].split(', ')
		for line in out:
			questions.append(to_question(PunktWordTokenizer().tokenize(line)))
	print outs

if __name__=='__main__':
	main()
