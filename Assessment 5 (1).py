#!/usr/bin/env python
# coding: utf-8

# ##calculate bonous of the employee.

# In[ ]:


y_o_s= int(input("Enter your year of service"))
if(y_o_s>5):
    salary=int(input("Enter your salary"))
    bonous=((5/100)*salary)
    print("Bonous for the employee",bonous)
else:
    print("Less then five years")


# # Take length and breath check if it is square or not.

# In[ ]:


l=int(input("Enter the lenght value"))
b=int(input("Enter the breath value"))
if(l==b):
    print("It is square")
else:
    print("It is rectangle")


# Take three people age and find oldest and youngest among them.

# In[ ]:


a,b,c=list(map(int,input("Enter the three people age details").split(" ")))
print("Oldest age is",max(a,b,c))
print("Youngest age is",min(a,b,c))


# ###Enter the Mark to know the Grade.

# In[ ]:


user=int(input("Enter the mark to know your Grade"))
if(user<25):
    print("Your Grade is F")
elif user>=25 and user<=45:
    print("Your Grade is E")
elif user>45 and user<=50:
    print("Your Grade is D")
elif user>50 and user<=60:
    print("Your Grade is C")
elif user>60 and user<=80:
    print("Your Grade is B")
elif user>80:
    print("Your Grade is A")
else:
    print("Enter the valid mark THANKYOU")


# Write the program to print Hello python ten times

# In[ ]:


x=10
for x in range (10):
    print("Hello python")


# write a program to print the number from 1 to 10

# In[ ]:


for x in range(1,11):
    print(x)


# calculate first ten number

# In[ ]:


sum=0
for x in range(1,11):
    sum=sum+x
print(sum)    


# write a program to print N number.

# In[ ]:


user=int(input("Enter the number to print N number"))
while True:
    print(user)


# In[ ]:


a=int(input("Enter the value"))
sum=0
for x in range(1,a):
    sum=sum+x
print(sum)   


# write a program to print table of a number.

# In[ ]:


for x in range(1,11):
    print("2 x",x,"=",2*x)


# Factorial of the number

# In[3]:


X=int(input("Enter a number for factorial"))
fact=1
for i in range(1,X+1):
    fact=fact*i
print(fact)    


# Write a program to print even number between 1 to 100

# In[4]:


for x in range(2,100,2):
    print(x)


# Write a program to print odd number between 1 to 100

# In[5]:


for x in range(1,100,2):
    print(x)


# Given number is palindrome or not

# In[2]:


n=int(input("Enter the number to check given number is palindrome or not"))
sum=0
temp=n
while n>0:
    x=n%10 #remainder
    sum=x+sum*10
    n=n//10
if(temp==sum):
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")
    


# Factorial of the number

# In[3]:


n=int(input("Enter the number"))
fact=1
for x in range(1,n+1):
    fact=fact*x
print(fact)    


# check the given number is prime or not

# In[29]:


num=int(input("Enter the number to check prime or not"))
if(num==1):
    print("Not a prime number")
for x in range(2,num):
    if(num%x==0):
        print("Not a prime number")
        break
    else:
        print("Prime number")
        break


# #Print prime number between the range

# In[23]:


n=2
m=100
for x in range(2,101):
    for y in range(2,101):
        if(x%y==0):
            break
    if(x==y):
        print(x,end=" ")


# In[19]:


for x in range(1,6):
    for y in range(1,x+1):
        print(y,end="")
    print()  


# In[20]:


for x in range(1,6):
    for y in range(1,x+1):
        print(x,end="")
    print()


# In[36]:


for x in range(0,6):
    for y in range(5,x,-1):
        print(y,end="")
    print()


# In[41]:


for x in range(6,0,-1):
    for y in range(1,x):
        print(y,end="")
    print()    


# In[45]:


for x in range(5,0,-1):
    for y in range(x,0,-1):
        print(y,end="")
    print() 


# In[46]:


for x in range(1,6):
    for y in range(1,x+1):
        print("*",end="")
    print()


# In[47]:


for x in range(1,6):
    for y in range(1,6):
        print("*",end="")
    print()


# In[51]:


for x in range(0,6):
    for y in range(5,x,-1):
        print("*",end="")
    print()


# In[22]:


for x in range(1,6):
    for y in range(0,x):
        print(chr(65+y),end="")
    print()


# In[19]:


for x in range(6):
    for y in range(x+1):
        print(chr(65+x),end="")
    print()    
  


# In[25]:


for x in range(5,0,-1):
    for y in range(0,x):
        print(chr(65+y),end="")
    print()    


# In[30]:


for x in range(4,-1,-1):
    for y in range(0,x+1):
        print(chr(65+x),end="")
    print() 


# In[ ]:




