'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a number is palindrome or not")
try:
    num=int(input("Enter a number.."))
    num1=num
    rnum=0
    while num > 0:
        rem = num % 10
        rnum = rnum * 10 + rem
        num = num // 10
    if num1 == rnum:
        print("Palindrome")
    else:
        print("Not a palindrome")
except:
    print("Enter a valid number")
        
        