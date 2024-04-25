#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_multiplication_table():
    for k in range(2,10,4):
        if k == 6:
            print()
        for j in range(1,10):
            for i in range(k,k+4):
                print(f'{i} x {j} = {i*j:>2d}',end = '\t') # > 는 오른쪽 정렬, 2d는 두칸 띄우고
            print()


display_multiplication_table()

