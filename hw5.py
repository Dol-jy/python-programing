#!/usr/bin/env python
# coding: utf-8

# In[32]:


def read_single_digit(n):
    if n == '0':
        return '영'
    elif n == '1':
        return '일'
    elif n == '2':
        return '이'
    elif n == '3':
        return '삼'
    elif n == '4':
        return '사'
    elif n == '5':
        return '오'
    elif n == '6':
        return '육'
    elif n == '7':
        return '칠'
    elif n == '8':
        return '팔'
    elif n == '9':
        return '구'

def read_number(d):
    length = len(d)
    if length == 3:
        hundred = read_single_digit(d[0])
        ten = read_single_digit(d[1])
        one = read_single_digit(d[2])
        return f'{hundred} {ten} {one}'
    elif length == 2:
        ten = read_single_digit(d[0])
        one = read_single_digit(d[1])
        return f'영 {ten} {one}'
    elif length == 1:
        one = read_single_digit(d[0])
        return f'영 영 {one}'

num = input('세 자리 정수 입력: ')
print(read_number(num))  

