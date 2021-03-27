#!/usr/bin/env python
# coding: utf-8

# In[1]:


from BasicInfo import *
import pandas as pd
from TreeBuild import *


display_string=''
def tree_search(parent,layer):
    global display_string 
    display_string += ('  '*layer + '--'+ alist[parent.idx]['姓名'])
    if parent.spouse != -1:
        display_string += (' '+ alist[family[parent.spouse].idx]['姓名'])
    display_string+='\n'    
    str2 = display_string
    print(str2)
    if len(parent.kids) == 0:
        return
    for kid in parent.kids:
        display_string=''
        str2 = tree_search(family[kid],layer+1)
        

