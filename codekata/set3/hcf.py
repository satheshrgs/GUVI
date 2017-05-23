'''
Created on 10-May-2017

@author: Sathesh Rgs
'''
print("Program to find HCF or GCD")
try:
    num=int(input("Enter the number..."))
    for i in range(1,num+1):
        if num % i == 0:
            gcd=i
    print("The GCD of",num,"is",gcd)
except:
    print("Enter a valid number")
    
