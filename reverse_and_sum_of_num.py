#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = int(input("Enter the integer number: ")) 
revs_number = 0 
add = 0
while (number > 0): 
 
 remainder = number % 10
 add = add + remainder
 revs_number = (revs_number * 10) + remainder 
 number = number // 10 
 
print("The reverse number is : {}".format(revs_number))
print('sum of the digits is ',add)


# In[ ]:




