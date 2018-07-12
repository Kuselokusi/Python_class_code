#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:42:00 2018

@author: kusi
"""

import random

vec=['kusi', 'jack', 'banana', 'sack']

    
while True:
    print('''
            1-list random words
            2-add random word
            3-remove random word
            4-pick random word
            ''')    
    select = input('Please select option: ')
    
    if select=='1':
        for i in vec:
            print(i)
    elif select=='2':
        inNo = input('word you want to add: ')
        vec.append(inNo)
    elif select=='3':
        inNo = input('word you want to remove: ')
        vec.remove(inNo)
    elif select=='4':
        print(vec[random.randint(0,len(vec)-1)])
    elif select=='5':
        break
    else:
        print('Error please select 1 to 5')