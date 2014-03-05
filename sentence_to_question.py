import os, re, sys

def to_question(sentence):
	pass

def main():
	textfile = sys.argv[1]
	text = ''
	with open(textfile) as f:
		for line in f:		
			text += line
	print text

if __name__=='__main__':
	main()
