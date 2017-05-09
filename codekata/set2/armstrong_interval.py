'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to display armstrong numbers between two intervals")
try:
    print("Enter the starting and ending intervals")
    si=int(input())
    ei=int(input())
    print("The armstrong numbers between",si,"and",ei,"are")
    for num in range(si,ei+1):    
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
            print(asum)
except:
    print("Enter a valid number")
