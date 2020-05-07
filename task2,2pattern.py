#!/usr/bin/env python
# coding: utf-8

# # printting pattern

# In[31]:


numrows=int(input("enter the umber of rows"))
for i in range(1,numrows):
    for j in range(i):
        print("*",end=" ")
    print()
#numrows=int(input("enter the umber of rows"))
for i in range(numrows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


# In[ ]:




