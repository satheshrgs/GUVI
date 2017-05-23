'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to find sum of numbers upto n")
try:
    num=int(input("Enter the number..."))
    if num < 0:
        raise Exception
    nsum=0
    for i in range(1,num+1):
        nsum=nsum+i
    print("The sum is ",nsum)
except:
    print("Enter a valid number")