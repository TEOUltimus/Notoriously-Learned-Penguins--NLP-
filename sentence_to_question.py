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

# Given a sentence, return a question if possible (and '' otherwise) 
def to_question(sent):
	verb = ''
	sentence = (sent.split('.')[0]).split(' ')
	for i in xrange(0, len(sentence)):
		if sentence[i] in verbs:
			# for the first auxilliary ver found, move it to the
			# front  of the sentence
			verb = sentence[i]
			sentence.remove(verb)
			sentence.insert(0, verb)

			sent = ' '.join(sentence) + "?"
			tree = parser.parse(sent)
			print tree.node
			print  sent
			if tree.node == "SBARQ" or tree.node == "SQ":
				print "GOOD!"
				return sent
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
	
	# list of questions to return
	questions = []
	for i in xrange(0, len(text)):
		out = text[i].split('. ')
		for line in out:
			phrases = line.split(', ')
			for phrase in phrases:
				question = to_question(phrase)
			if question != '':
				questions.append(question)
	#for q in questions:
	#	print q

if __name__=='__main__':
	main()
