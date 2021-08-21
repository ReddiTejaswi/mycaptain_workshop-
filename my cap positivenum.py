# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:38:51 2021

@author: Dell
"""

#task 2
n= input("Enter elements to add in  list1 separted by comma")
list1=n.split(",")
updated_list=[]
for x in list1:
    if int(x)>0:
        updated_list.append(int(x))        
print(*updated_list,sep=",")

n1= input("Enter elements to add in  list2 separted by comma")
list2=n.split(",")
updated_list2=[];
for x in list2:
    if int(x)>0:
        updated_list2.append(int(x))
print(updated_list2)
    