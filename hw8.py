#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 개념 확인 과제
def buy(dic):
    item = input('상품명?')
    if (item != ''):
        count = input('수량은?' )
        dic[item] = count
        print(f'장바구니에 {item} {count}개가 담겼습니다.')
        print()
    else:
        return False

def show(dic):
    print(f'\n>>> 장바구니 보기: {dic}')

def find(dic):
    print('\n[검색]')
    search = input('장바구니에서 확인하고자 하는 상품은? ')
    if search in dic:
        print(f'{search}은(는) {dic[search]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {search}은(는) 없습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)

