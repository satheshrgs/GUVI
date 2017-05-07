'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to find sum of N numbers")
try:
    nsum=0
    num=int(input("Enter the N value..."))
    print("Enter the numbers...")
    for i in range(0,num):
        nsum += int(input())
    print("The sum is ",nsum)
except:
    print("Enter a valid number")