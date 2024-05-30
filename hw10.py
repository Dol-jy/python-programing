#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pickle

def input_scores():
    lst = []
    n = 1
    
    while True:
        score = int(input(f'#{n}? '))
        if score > 0:
            lst.append(score)
        else:
            break
        n += 1
    
    return lst

def get_average(lst):
    result = 0
    
    for i in lst:
        result += i
    
    return result / len(lst)

def show_scores(lst):
    for i in lst:
        print(i, end=' ')

def save_scores(lst, filename):
    with open(filename, 'wb') as f:
        pickle.dump(lst, f)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        return None

filename = 'score.bin'
loaded_scores = load_scores(filename)

if loaded_scores is not None:
    print('[파일 읽기]')
    score_list = loaded_scores
else:
    print('[점수 입력]')
    score_list = input_scores()

score_mean = get_average(score_list)

print('\n[점수 출력]')
print('개인점수:', end=' ')
show_scores(score_list)
print(f'\n평균: {score_mean:.1f}')

save_scores(score_list, filename)

