import os, re, sys
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktWordTokenizer

verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'can', 'could',
	'do', 'did', 'does', 'doing', 'have', 'had', 'has', 'having',
	'may', 'might', 'must', 'shall', 'should', 'will', 'would']

def to_question(sentence):
	verb = ''
	for i in xrange(0, len(sentence)):
		if sentence[i] in verbs:
			verb = sentence[i]
			sentence.remove(verb)
			sentence.insert(0, verb)
			sentence[-1] = '?'
			return ' '.join(sentence)
	return ''

def main():
	textfile = sys.argv[1]
	lines = None
	text = ''
	with open(textfile) as f:
		lines = f.readlines()
	for i in xrange(0, len(lines)):
		lines[i] = lines[i].split('\n')[0]
	text = ' '.join(lines)
	lines = PunktSentenceTokenizer().tokenize(text)
	for i in xrange(0, len(lines)):
		lines[i] = to_question(PunktWordTokenizer().tokenize(lines[i]))
	print lines

if __name__=='__main__':
	main()
