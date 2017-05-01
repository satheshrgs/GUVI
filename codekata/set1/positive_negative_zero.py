'''
Created on 01-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a number is positive or negative or zero")
try:
    num=int(input("Enter a number.."))
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    elif num == 0:
        print("The Number is zero")
except:
    print("Enter a valid Number")
