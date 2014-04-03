import os, os.path, re, sys, replace_synonyms, vector_score

def main():
	edge = re.compile('\n\n+')

	print 'replacing synonyms'
	replace_synonyms.main()
	
	synText = replace_synonyms.output_name(sys.argv[2])
	sections = None
	with open(synText) as f:
		sections = re.split(edge, ''.join(f.readlines()))
	os.system('rm ' + synText)
	print sections

if __name__ == '__main__':
	main()
