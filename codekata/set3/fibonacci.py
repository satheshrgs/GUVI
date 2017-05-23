'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to print fibonacci numbers")
try:
    f1=0
    f2=1
    num=int(input("Enter a number upto which fibonacci series to be found.."))
    if num < 0:
        raise Exception
    for i in range(0,num):
        print(f1)
        f3=f1+f2
        f1=f2
        f2=f3
except:
    print("Enter a valid number")
    
    
    
    '''0 1 1 2 3 5 8 13 '''