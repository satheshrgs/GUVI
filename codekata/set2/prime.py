'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a number is prime or not")
try:
    num=int(input("Enter a number..."))
    count=0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1 
    if count == 2 and num !=1:
        print("Prime number")
    else:
        print("Not a prime number")
except:
    print("Enter a valid number")
        