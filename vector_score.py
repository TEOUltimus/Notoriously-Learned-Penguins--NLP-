import collections, math, numpy, sys

# dimension of next new vocab word in vector
index = -1

# new vocab word has been added
def incr():
	global index
	index += 1
	return index

# set lst[i] to val
# propagate 0s to prevent indexOutOfBounds
def setList(lst, i, val):
	if i >= len(lst):
		lst = lst + ([0] * (i + 1 - len(lst)))
	lst[i] = val
	return lst

# prevent indexOutOfBounds by returning 0
def getList(lst, i):
	if i >= len(lst):
		return 0
	else:
		return lst[i]

# contains mapping from each vocab word to its vector dimension
lookup = collections.defaultdict(incr)

# given to strings, return their cosine similarity
# it is left to the caller to ensure that cases match and that
# no unwanted symbols are present
def score(str1, str2):
	# construct string vectors by counting word occurences
	v1 = []
	v2 = []
	for w in str1.split(' '):
		i = lookup[w]
		v1 = setList(v1, i, getList(v1, i) + 1)
	for w in str2.split(' '):
                i = lookup[w]
                v2 = setList(v2, i, getList(v2, i) + 1)

	# match lengths
	l = len(v2) - 1
	v1 = setList(v1, l, getList(v1, l))
	l = len(v1) - 1
	v2 = setList(v2, l, getList(v2, l))

	# calculate dot products
	dot = numpy.dot(v1, v2)
	magsq1 = numpy.dot(v1, v1)
	magsq2 = numpy.dot(v2, v2)

	# return cosine similarity
	return dot / (math.sqrt(magsq1) * math.sqrt(magsq2))

if __name__ == '__main__':
	s1 = sys.argv[1].translate(None, '\'')
	s2 = sys.argv[2].translate(None, '\'')
	print score(s1, s2)
