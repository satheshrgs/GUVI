'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to find the power of a number")
try:
    x=int(input("Enter a number..."))
    y=int(input("Enter the power..."))
    apow=x ** y
    print(x,"raised to the power",y,"is",apow)
except:
    print("Enter a valid number")