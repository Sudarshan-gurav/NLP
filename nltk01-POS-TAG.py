import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

example = '''Technical Sergeant Taylor and Guinn from the U.S. Department of Defense.U.S. and Indian government officials pressed on with talks on Thursday to resolve their differences over trade and investment,
Indian government sources said, even though U.S.'''

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(example)
sent


'''OUTPUT
[('Technical', 'JJ'),
 ('Sergeant', 'NNP'),
 ('Taylor', 'NNP'),
 ('and', 'CC'),
 ('Guinn', 'NNP'),
 ('from', 'IN'),
 ('the', 'DT'),
 ('U.S.', 'NNP'),
 ('Department', 'NNP'),
 ('of', 'IN'),
 ('Defense.U.S', 'NNP')
 etc...............
 )]
 
 '''
