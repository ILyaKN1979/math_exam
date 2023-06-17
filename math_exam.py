# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:08:00 2023

@author: IlYA
"""
import sys
import random
import time
import os
clear = lambda: os.system('cls')

def generate_questions(start, finish, count):
    a=[]
    b=[]
    z=[]
    for i in range(0,count):
        a1=random.randint(start,finish)
        b1=random.randint(start, finish)
        if random.randint(0, 1)==0:
            z.append('+')
            a.append(a1)
            b.append(b1)
        else:
            if a1-b1>=0:
                z.append('-')
                a.append(a1)
                b.append(b1)
            else:
                z.append('-')
                a.append(b1)
                b.append(a1)

    return a,b,z


def start_exam(a, b, z, count):
    res = []
    for i in range(count):
        s = input(f'{i+1}) {a[i]} {z[i]} {b[i]} = ')
        while not s.isdigit():
            print('It is not a number!')
            s = input(f'{i+1}) {a[i]} {z[i]} {b[i]} = ')
        res.append(int(s))
    return res 

def check_exam(a,b,z,res):
    s=0
    for i in range(0, len(a)):
        if z[i]=='+':
            if a[i] + b[i] == res[i]:
                print(f'{i}) Good! :)')
            else:
                print(f'{i}) Error! :(')
                s+=1
        else:
            if a[i] - b[i] == res[i]:
                print(f'{i+1}) Good! :)') 
            else:
                print(f'{i+1}) Error! :(') 
                s+=1
    print(f'Total errors = {s} ')
                
  
# start exam 
def main(count):
    clear()
    print("Let's start the exam!")
    print("--------------------")
    
    
    
    #count = 10
    
    start_time= time.time()
    
    a,b,z = generate_questions(0, 99, count)
    
    res = start_exam(a, b, z, count)
    
    
    print('-----------------')
    
    check_exam(a, b, z, res)
        
    
    print("You are doing the exam during  %s seconds!" % round((time.time() - start_time)))    



if __name__ == "__main__":
    if len(sys.argv) > 1:
        param = sys.argv[1]
        if param.isdigit():
            main(int(param))
        else: 
            print('It is not a number!')    
    else:
        print('You have to give information about how many mathematical tasks you want to solve!')
        print ('Example: "math_exam.py" 10')