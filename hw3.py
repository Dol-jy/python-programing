#!/usr/bin/env python
# coding: utf-8

# In[21]:


def get_fixed_price(price):
    result = price / (1 -(discount/100)) # 할인된 가격 / (1-할인율)
    return result

discount = int(input('할인율은?'))
price1 = int(input('A 상품의 할인된 가격은?'))
price2 = int(input('B 상품의 할인된 가격은?'))
print('A 상품의 정가는',int(get_fixed_price(price1)),'원')
print('B 상품의 정가는',int(get_fixed_price(price2)),'원') # 소수점 없애기 위해 int사용

