from stat_parser import Parser

# counts the nps in the list l
def count_np(l):
    count = 0
    for elem in l:
    	if 'N P ' in elem:
    		count += 1
    return count

# Replaces the ith np of the list l
def replace_ith_np(l,i):
	k = 0
	s = ''
	for elem in l:
		if 'N P ' in elem:
			if k == i:
				s += 'what '
			else:
				s += elem[4:] + ' '
			k += 1
		else:
			s += elem + ' '
	return s

# Takes a parse tree of sentence s and returns a 1-dimensional list
# of words with the top level NPs marked with 'N P ' as a prefix
def tree_to_list(t):
	l = []
	try:
		t.node
	except AttributeError:
		print t,
	# Now we know that t.node is defined
	if t.node == 'NP':
		l.append('N P ' + ' '.join(t.leaves()))
		return l
	else:
 		if len(t.leaves()) == 1:
 			l.append(t.leaves()[0])
 			return l
	for child in t:
		next = tree_to_list(child)
		if not (next is None):
			for elem in next:
				l.append(elem)
	return l

# Takes a sentence and a parser and returns a list of questions
# by replacing each top level NP with a wh-word
def replace_np(sentence, parser):
    if sentence == "":
        return []
    sentence_parse = parser.parse(sentence)
    sentence_l = tree_to_list(sentence_parse)
    wh_sentences = []
    for i in range(0,count_np(sentence_l)):
        wh_sentences.append(replace_ith_np(sentence_l,i))
    return wh_sentences

# Test on the first sentence of the first data set
def test():
	s = open('data\\set1\\a1.txt').readlines()[3]
	p = Parser()
	print(replace_np(s,p))