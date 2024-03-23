#!/usr/bin/env python
# coding: utf-8

# In[9]:


def exchange(mn):
    n500 = mn // 500
    mn %= 500
    n100 = mn // 100
    mn %= 100
    n50 = mn // 50
    mn %= 50
    n10 = mn // 10
    print('500원 동전의 개수:',n500)
    print('100원 동전의 개수:',n100)
    print('50원 동전의 개수:',n50)
    print('10원 동전의 개수:',n10)

def get_integer(prompt):
   return int(input(prompt))

mn = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(mn)

