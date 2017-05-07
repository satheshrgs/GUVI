'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to find the largest among three numbers")
print("Enter the three numbers..")
try:
    num1=int(input())
    num2=int(input())
    num3=int(input())
    if num1 > num2:
        if num1 > num3:
            print(num1,"is the greatest number")
        else:
            print(num3,"is the greatest number")
    elif num2 > num3:
        print(num2,"is the greatest number")
    else:
        print(num3,"is the greatest number")
except:
    print("Enter a valid number")