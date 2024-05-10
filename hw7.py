#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 개념확인 과제
shopping_bag = {}    # 장바구니
while True:
    item = input('상품명?')
    if (item == ''):
        break
    count = input('수량은?' )
    shopping_bag[item] = count
    print(f'장바구니에 {item} {count}개가 담겼습니다.')
    print()

print(f'>>> 장바구니 보기: {shopping_bag}')
print('\n[검색]')
search = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{search}은(는) {shopping_bag[search]}개 담겨 있습니다.')

