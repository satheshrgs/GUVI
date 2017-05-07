'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to print digits of a number")
try:
    count=0
    num=int(input("Enter a number.."))
    while num > 0:
        num=num//10
        count += 1
    print("Length is ",count)
except:
    print("Enter a valid number")