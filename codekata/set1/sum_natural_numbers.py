'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to find sum of natural numbers")
try:
    num=int(input("Enter the number upto which sum is to be found..."))
    nsum=0
    for i in range(1,num+1):
        nsum=nsum+i
    print("The sum is ",nsum)
except:
    print("Enter a valid number")