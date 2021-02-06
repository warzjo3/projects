# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:06:36 2021

@author: johnw
"""

from numpy.random import randint as ri

#def alarm(d = input("difficulty, 1-5: "), n = input("number of questions: ")):
''' 
no1 = ri(1,9)
no2 = ri(1,9)
answer = 0
while answer != no1+no2:
    answer = int(input(f'{no1} + {no2} = '))
print('correct')
'''   
def alarm(n = int(input("number of questions: ")), d = int(input("difficulty 1-6: "))):
    if d == 1 :        
        for no in range(0,n):
            no1 = ri(1,9)
            no2 = ri(1,9)
            answer = 0
            while answer != no1+no2:
                answer = int(input(f'{no+1}: {no1} + {no2} = '))
            print('correct')
        print('good morning!')
    if d == 2 :        
        for no in range(0,n):
            no1 = ri(10,99)
            no2 = ri(10,99)
            answer = 0
            while answer != no1+no2:
                answer = int(input(f'{no+1}: {no1} + {no2} = '))
            print('correct')
        print('good morning!')
    elif d == 3 :
        for no in range(0,n):
            no1 = ri(10,99)
            no2 = ri(10,99)
            no3 = ri(10,99)
            answer = 0
            while answer != no1+no2+no3:
                answer = int(input(f'{no+1}: {no1} + {no2} + {no3} = '))
            print('correct')
        print('good morning!')
    elif d == 4 :
        for no in range(0,n):
            no1 = ri(10,99)
            no2 = ri(1,9)
            no3 = ri(10,99)
            answer = 0
            while answer != no1*no2 + no3:
                answer = int(input(f'{no+1}: ({no1} * {no2}) + {no3} = '))
            print('correct')
        print('good morning!')
    elif d == 5 :
        for no in range(0,n):
            no1 = ri(10,99)
            no2 = ri(10,19)
            no3 = ri(100,999)
            answer = 0
            while answer != no1*no2 + no3:
                answer = int(input(f'{no+1}: ({no1} * {no2}) + {no3} = '))
            print('correct')
        print('good morning!')
    elif d == 6 :
        for no in range(0,n):
            no1 = ri(100,999)
            no2 = ri(10,99)
            no3 = ri(1000,9999)
            answer = 0
            while answer != no1*no2 + no3:
                answer = int(input(f'{no+1}: ({no1} * {no2}) + {no3} = '))
            print('correct')
        print('good morning!')
alarm()       

