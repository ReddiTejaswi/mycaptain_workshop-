# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:45:04 2021

@author: Dell
"""

#task1
n=int(input("Enter the number of digits you need in the series"))   

n1,n2=0,1
s=0
if n<0:
    print("Enter a valid positive integer")
elif n==0:
    print("Fibonacci series:",n1)
        
elif n==1:
    print("Fibonacci series upto",n, "terms are",n1,n2)
else:
    print("fibonacci series:")
    while s<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        s=s+1
       
       

        
        
        
        
        
    
    

     
         
    
    