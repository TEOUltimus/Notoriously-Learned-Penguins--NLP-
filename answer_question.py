import ds2, re

# q is the question
# sections is a list of sections from the article
def answer_sections(q,sections):
	highest = 0.0
	highestsect = 0
	# Score each section and take the highest one
	for i in range(0,len(sections)):
		if ds2.compare(sections[i],q) > highest and len(sections[i].split(' ')) > 4:
			highest = ds2.compare(sections[i],q)
			highestsect = i
	return sections[highestsect]

# q is the question
# sentence is a sentence from the article
def answer_clause(q,sentence):
	# split the sections into 'clauses' by splitting on commas (excluding dates/numbers) and periods
	sections = re.split('(?<!\d)[,]|[.]',sentence.split('\n')[-1])
	highest = 0.0
	highestsect = 0
	# score each clause and pick the highest one
	for i in range(0,len(sections)):
		if ds2.compare(sections[i],q) > highest and len(sections[i].split(' ')) > 4:
			highest = ds2.compare(sections[i],q)
			highestsect = i
	return sections[highestsect]

# q is a question as a string
# text is the text of the wikipedia article that the question is asking about
def answer(q,text):
	# Break the text into both sentences and sections
	sents = text.split('.')
	sects = text.split('\n\n\n')
	# Try to score by sentence and by section; pick the answer that scores the highest
	a1 = answer_clause(q,answer_sections(q,sects))
	a2 = answer_clause(q,answer_sections(q,sents))
	if ds2.compare(q,a1) > ds2.compare(q,a2):
		return a1
	return a2