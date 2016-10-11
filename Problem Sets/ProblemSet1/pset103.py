# -*- coding: utf-8 =-*-
"""
Created on Wed Aug 31 15:08:10 2016

@author: james.hussey
"""


#s = "azcbobobegghakl"
s = "ggdfsgfsgdfgsdfhjyujrrtewvcccvvaeqwqwqwrtjlighfsgdgdfghdsg"

start = 0
tempSub = s[start]
finalSub = ""

for letter in s:
    if start > len(s) - 2:
        break
    elif s[start + 1] >= s[start]:
        tempSub += s[start +1] 
        start += 1       
    else:
        if len(tempSub) > len(finalSub):
            finalSub = tempSub
        start += 1
        tempSub = s[start]
if len(tempSub) > len(finalSub):
    finalSub = tempSub
print("Longest substring in alphabetical order is: %s" % (finalSub))

#) if your new letter in the iteration comes after (is larger) 
# the last letter stored in your current word, they're alphabetical and you 
#can add that letter to your current word. 
#Keep adding letters to the current word as long as they're alphabetical. 
#Always compare the new letter with the last letter in your current word.

#) if they aren't alphabetical compare the lengths of your two stored words

#) save the longest one to your longest word variable, but if they're of equal
# length don't save the new word created, keep the old one.

#) reset the current word so that you start with the letter in the string that 
# comes after your previous 'current word' so you can build fresh

#) exit loop and do one more comparison of word lengths to make sure you've 
#stored the longest word.

#) output your longest alphabetical word


#Longest substring in alphabetical order is: abc

