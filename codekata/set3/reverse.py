'''
Created on 23-May-2017

@author: Sathesh Rgs
'''
import sys
print("Program to reverse  a number")
try:
    rev=0
    i=0
    c=0
    num=int(input("Enter a number.."))
    while num > 0:
        rev=(rev*10)+num%10
        if num%10 == 0 and i == 0:
            c+=1
        else:
            i=1
        num=num//10
    print("The reverse is...")
    for i in range(0,c):
        sys.stdout.write("0")
    print(rev)
except:
    print("Enter a valid number")