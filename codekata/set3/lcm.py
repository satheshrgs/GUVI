'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to find LCM of two numbers")
try:
    a=int(input("Enter the first number.."))
    b=int(input("Enter the second number.."))
    m=a if a>b else b
    for i in range(1,m+1):
        if a % i == 0 and b % i == 0:
            gcd = i 
    lcm=(a*b)//gcd
    print("The LCM is",lcm)
except:
    print("Enter a valid number")
    