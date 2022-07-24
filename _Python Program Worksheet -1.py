#!/usr/bin/env python
# coding: utf-8

# # # python worksheet
# 

# 11. Write a python program to find the factorial of a number.

# In[3]:


a=int(input("enter a number"))
f=1
for i in range(1,a+1):
     f=f*i
print(f"  The factor of the number is: {f}")    


# 12. Write a python program to find whether a number is prime or composite.

# In[5]:


a=int(input("enter a number: "))
b=list (range(2,a))
for i in b:
        if a%i==0:
            print(a,"Is not a prime number")
        else:
            print(a,"Is  a prime number")
        break

    
    
   


# 13. Write a python program to check whether a given string is palindrome or not.

# In[6]:


x='madam'
w=' '
for i in x:
    w = i + w
    
if (x == w):
    print("The string is palindrome")
else:  
    print("The string is not palindrome")


# 14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[7]:


#hypotaneous
from math import sqrt
print(" input the lenght of shorter triangle side: ")
a=float(input("enter a: "))
b=float(input("enter b: "))
c=sqrt(a**2+b**2)
print("The lenght of hypotaneous side is:",c)


# 15. Write a python program to print the frequency of each of the characters present in a given string

# In[4]:


inp_str=input("Enter a string")
x=set()
result=''
for i in inp_str:
    if i not in x:
        x.add(i)
        result=result+str(inp_str.count(i))+i
print("The count of letter in string:  ",result)      

