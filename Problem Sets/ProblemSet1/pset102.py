# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:08:10 2016

@author: james.hussey
"""

s = 'azcbobobegghakl'
word = "bob"
count = 0
start = 0

for start in range(len(s)):
        if s[start:start+len(word)] == word:
            count += 1
            start += 1
        else:
            start += 1
        
print("The word %s appears %s times in the string." % (word, count))