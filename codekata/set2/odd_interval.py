'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to display odd numbers between two intervals")
try:
    print("Enter the starting and ending intervals")
    si=int(input())
    ei=int(input())
    print("The odd numbers between",si,"and",ei,"are")
    for i in range(si,ei+1):
        if i % 2 != 0:
            print(i)
except:
    print("Enter a valid number")