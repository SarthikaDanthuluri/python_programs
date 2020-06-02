# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:54:49 2020

@author: Lenovo
"""

def factorial(n): 
      
  
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  

num = 5; 
print("Factorial of",num,"is", 
factorial(num)) 