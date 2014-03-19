import os, re, sys
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktWordTokenizer
from stat_parser import Parser

# Set up verbs, will later do pos tagging to include maybe_verbs as well
verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'could',
    'do', 'did', 'does', 'doing', 'have', 'has', 'having',
    'must', 'shall', 'should', 'would']
maybe_verbs = ['can', 'had', 'may', 'might', 'will']
punctuation = ['.', ',', '?', '!']
parser = Parser()
# Parse tree of a good question should match this
goodQ = re.compile('\\(SBARQ')

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

            # This may cause problems with checking grammaticality
            # replace final punctuation if any is present
            #if sentence[-1] in punctuation:
            #    sentence[-1] = '?'
            #else:
            #    sentence.append('?')

            # Not working correctly at the moment
            # attempt to verify prospective question is grammatical
            #sent =  ' '.join(sentence)
            #ptree = parser.parse(sent)
            #ptreenode = ptree.node
            #if goodQ.match(ptreenode):
            #    return sent
            #else:
            #    return ''
            return ' '.join(sentence) + '?'
    return ''

def main():
    textfile = sys.argv[1]
    lines = None
    text = []
    with open(textfile) as f:
        lines = f.readlines()

    # remove newlines and tokenize sentences
    for i in xrange(0, len(lines)):
        lines[i] = lines[i].split('\n')[0].lower()
        text += PunktSentenceTokenizer().tokenize(lines[i])
    #text =i ' '.join(lines)
    
    #lines = PunktSentenceTokenizer().tokeniize(text)

    # list of questions to return
    questions = []
    for i in xrange(0, len(text)):
        out = text[i].split('. ')
        for line in out:
            question = to_question(line)
            if question != '':
                questions.append(question)
            #sentences = line.split('. ')
            #for sent in sentences:
            #    questions.append(to_question(sent))
            #questions.append(to_question(PunktWordTokenizer().tokenize(line)))
    #print outs
    for q in questions:
        print q

if __name__=='__main__':
    main()
