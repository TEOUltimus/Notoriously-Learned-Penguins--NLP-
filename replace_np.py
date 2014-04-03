from stat_parser import Parser

def count_np(t):
    count = 0
    try:
        t.node
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        if t.node == 'NP':
            count += 1
        else:
            if len(t.leaves()) == 1:
                return 0
        for child in t:
            count += count_np(child)
        return count

def replace_ith_np(t,curr_np,i):
    s = ''
    np_num = curr_np
    try:
        t.node
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        if t.node == 'NP':
            if curr_np == i:
                return 'what '
            else:
                return 'N P ' + ' '.join(t.leaves()) + ' '
        else:
            if len(t.leaves()) == 1:
                return t.leaves()[0] + ' '
        for child in t:
            next_phrase = replace_ith_np(child,np_num,i)
            if next_phrase == 'what ':
                np_num += 1
            elif 'N P ' in next_phrase:
                np_num += 1
                next_phrase = next_phrase[4:]
            s += next_phrase
        return s
      

def replace_np(sentence, parser):
    if sentence == "":
        return []
    sentence_parse = parser.parse(sentence)
    wh_sentences = []
    for i in range(0,count_np(sentence_parse)):
        wh_sentences.append(replace_ith_np(sentence_parse,0,i))
    return wh_sentences
