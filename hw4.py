#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rep_char(c,n):
    print(c*n)

def draw_line_string():
    st = input('Input his/her name:')
    msg1 = f' Hello {st}, '
    msg2 = f' Welcome to Seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(msg1)
    print(msg2)
    rep_char('-',nstr)

draw_line_string()

