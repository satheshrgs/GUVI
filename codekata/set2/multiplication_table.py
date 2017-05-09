'''
Created on 09-May-2017

@author: Sathesh Rgs
'''
print("Program to generate multiplication table")
try:
    num=int(input("Enter the number..."))
    for i in range(1,11):
        print(num,"X",i,"=",i*num)
except:
    print("Enter a valid number")