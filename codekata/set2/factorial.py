'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to find the factorial of a number")
try:
    num=int(input("Enter a number..."))
    fact=1
    if num < 0:
        print("Factorial can't be performed for negative numbers")
    else:
        for i in range(1,num+1):
            fact *= i
    print("The factorial of",num,"is",fact)
except:
    print("Enter a valid number")