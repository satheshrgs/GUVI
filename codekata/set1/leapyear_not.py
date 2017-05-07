'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("program to find whether the entered year is leap year or not")
try:
    year=int(input("Enter the year.."))
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
except:
    print("Enter a valid year") 
