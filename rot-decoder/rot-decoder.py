#!/usr/bin/python

import string
import subprocess 

#create list with alphabets
def gen():
    global letters 
    global out_index_letters
    letters = string.ascii_lowercase
    out_index_letters = string.ascii_lowercase
    letters = list(letters)
    out_index_letters = list(out_index_letters)
    #add blank space so list indexing can start from 1 instead of 0 
    # letters.insert(0, '')
    # out_index_letters.insert(0,'')
   
gen()
def rot(text, n):
#take input text iterate through it and find index 
# move the 13 steps forward from current letter and add to a list
    try:
        dec_word = []
        for x in text:
            if x in letters:
                index = letters.index(x)
                mov = index + n
                list_added = letters * 2
                dec_word += list_added[mov]
                # dec_word += letters[mov]
        return ''.join(dec_word)
    except IndexError:
        pass
        # print(dec_word)

#move 

n = 1
while n < 26:
    numbering = '{}'.format(n)
    print(numbering, rot('payzgmuujurjigkygxiovnkxlcgihubb',n))
    n+=1 




