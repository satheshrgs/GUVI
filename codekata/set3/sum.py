'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to print sum of numbers from 1 to 15 and sum of odd numbers from 15 to 45")
sum1=0
sum2=0
for i in range(1,46):
    if i < 15:
        sum1 += i
    elif i > 15:
        if i % 2 !=0:
            sum2 += i
    elif i == 15:
        sum1 += i
        sum2 += i
print("The sum of numbers from 1 to 15 is",sum1,)
print("The  sum of odd numbers from 15 to 45 is",sum2)   