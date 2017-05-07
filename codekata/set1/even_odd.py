'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a number is odd or even")
try:
    num=int(input("Enter the number..."))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd number")
except:
    print("Enter a valid number")