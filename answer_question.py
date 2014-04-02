import ds2, re

def answer_sections(q,sections):
	highest = 0.0
	highestsect = 0
	for i in range(0,len(sections)):
		if ds2.compare(sections[i],q) > highest and len(sections[i].split(' ')) > 4:
			highest = ds2.compare(sections[i],q)
			highestsect = i
	return sections[highestsect]

def answer_clause(q,sentence):
	sections = re.split('(?<!\d)[,]|[.]',sentence.split('\n')[-1])
	highest = 0.0
	highestsect = 0
	for i in range(0,len(sections)):
		if ds2.compare(sections[i],q) > highest and len(sections[i].split(' ')) > 4:
			highest = ds2.compare(sections[i],q)
			highestsect = i
	return sections[highestsect]

def answer(q,text):
	sents = text.split('.')
	sects = text.split('\n\n\n')
	a1 = answer_clause(q,answer_sections(q,sects))
	a2 = answer_clause(q,answer_sections(q,sents))
	if ds2.compare(q,a1) > ds2.compare(q,a2):
		return a1
	return a2