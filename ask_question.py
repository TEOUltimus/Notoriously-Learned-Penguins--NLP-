import os, re, sys
import replace_np
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktWordTokenizer
from stat_parser import Parser

# Set up verbs, will later do pos tagging to include maybe_verbs as well
verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'could',
	'do', 'did', 'does', 'doing', 'have', 'has', 'having',
	'must', 'shall', 'should', 'would']
maybe_verbs = ['can', 'had', 'may', 'might', 'will']
punctuation = ['.', ',', '?', '!']
parser = Parser()

# Given a sentence, returns the same sentence if it is a valid question,
# and '' otherwise 
def check_question(sent):
	 tree = parser.parse(sent)
	 print tree
	 print  sent
	 if tree.node == "SBARQ" or tree.node == "SQ":
		  print "GOOD!"
		  return sent
	 return ''

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
				sent = ' '.join(sentence) + '?'			 

				#question = check_question(sent)
				#if question != '':
				#	return question

				return sent

	 return ''

def main():
	textfile = sys.argv[1]
	numqs = int(sys.argv[2])
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
			print line
			sep = re.compile(r', |; |\(|\) ')
			phrases = sep.split(line)
			for phrase in phrases:
				question = to_question(phrase)
				if question != '':
					questions.append(question)
			#wh_questions = replace_np.replace_np(line, parser)
			#for q in wh_questions:
			#	questions.append(q)
	i = 0
	for q in questions:
		print q
		i += 1
		if i >= numqs:
			break

if __name__=='__main__':
	main()
