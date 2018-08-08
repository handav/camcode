print 'hello world'

harry_potter = open('harryPotter.txt', 'r')
#print harry_potter.read()
hp = harry_potter.read()
hp = hp.decode('utf-8')
print hp

import nltk
# words = nltk.wordpunct_tokenize(hp)
# print words

# for word in words:
#     if word[0].isupper():
#         print word

sentences = nltk.sent_tokenize(hp)
for s in sentences:
    words = nltk.wordpunct_tokenize(s)
    for w in words:
        if w[0].isupper():
            print w


