'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to print the count of characters,numbers,alpha numeric characters in string")
s=input("Enter the string..")
alpha=0
num=0
alnum=0
for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1
    elif i.isalnum():
        alnum+=1
alnum=alpha+num
print("Alphabets...",alpha)
print("Numbers...",num)
print("Alphanumerical...",alnum)