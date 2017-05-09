'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a number is Armstrong or not")
try:
    num=int(input("Enter a number.."))
    num1=num
    asum=0
    digit=0
    while num1 != 0:
        num1=num1//10
        digit += 1
    num1=num
    while num1 != 0:
        rem = num1 % 10
        asum=asum + (rem ** digit)
        num1 = num1 // 10
    if asum == num:
        print("Armstrong number")
    else:
        print("Not an armstrong number")
except:
    print("Enter a valid number")
        