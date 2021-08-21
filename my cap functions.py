# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:08:56 2021

@author: Dell
"""

def most_frequent(string):
    freq = {}
    for i in string:
        keys=freq.keys()
        if i in keys:
            freq[i] += 1;
        else:
            freq[i] = 1;
    return freq
    

string = input("Please enter a string ") 
dict = {}
dict = most_frequent(string.lower())

mydict_sorted = sorted(dict, key=dict.get, reverse=True)
for x in mydict_sorted:
    print(x,"=",dict[x],end=" ")
    