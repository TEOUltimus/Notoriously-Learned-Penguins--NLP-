import nltk
from nltk.corpus import brown
import string

# Paragraphs separated by 3 \n
# First line is the title
def preprocess(wikipedia_text):
	brown_text = brown.sents()
	brown_tagged = brown.tagged_sents()
	unigram_tagger = nltk.UnigramTagger(brown_tagged)
	bigram_tagger = nltk.BigramTagger(brown_tagged,backoff=unigram_tagger)
	paragraph_text = wikipedia_text.split('\n')
	paragraph_tagged = [tp for p in paragraph_text for tp in bigram_tagger.tag(nltk.word_tokenize(p).translate(None,'.'))]
	print paragraph_tagged

	return