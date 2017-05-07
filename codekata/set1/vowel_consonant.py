'''
Created on 07-May-2017

@author: Sathesh Rgs
'''
print("Program to check whether a character is vowel or consonant")
char=input("Enter a character...")
vowel=('a','e','i','o','u')
if char.isalpha() and len(char)==1:
    for i in vowel:
        if char == i:
            val=1
        else:
            val=0
    if val == 1:
        print("Vowel")
    elif val == 0:
        print("Consonant")
else:
    print("Enter a valid character")