import os, re, sys

def to_question(sentence):
	pass

def main():
	textfile = sys.argv[1]
	lines = None
	text = ''
	with open(textfile) as f:
		lines = f.readlines()
	for i in xrange(0, len(lines)):
		lines[i] = lines[i].split('\n')[0]
	text = ' '.join(lines)
	print text

if __name__=='__main__':
	main()
