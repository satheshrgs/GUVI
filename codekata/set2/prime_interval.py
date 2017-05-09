'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to display odd numbers between two intervals")
try:
    print("Enter the starting and ending intervals")
    si=int(input())
    ei=int(input())
    print("The prime numbers between",si,"and",ei,"are")
    for i in range(si,ei+1):
        count=0
        for i1 in range(1,i+1):
            if i % i1 == 0:
                count += 1
        if count == 2 and i != 1:
            print(i)
except:
    print("Enter a valid number")
        