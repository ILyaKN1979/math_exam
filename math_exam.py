# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:08:00 2023

@author: IlYA
"""
import sys
import random
import time
import os

# A function to clear the console screen
clear = lambda: os.system('cls')

def generate_questions(start, finish, count):
    """
    Generate random arithmetic questions.

    Args:
        start (int): The lower bound of the number range.
        finish (int): The upper bound of the number range.
        count (int): The number of questions to generate.

    Returns:
        tuple: Three lists containing generated operands and operators.
    """
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
    """
    Start the exam and collect user answers for arithmetic questions.

    Args:
        a (list): List of first operands.
        b (list): List of second operands.
        z (list): List of operators.
        count (int): Number of questions.

    Returns:
        list: List of user answers.
    """
    
    res = []
    for i in range(count):
        s = input(f'{i+1}) {a[i]} {z[i]} {b[i]} = ')
        while not s.isdigit():
            print('It is not a number!')
            s = input(f'{i+1}) {a[i]} {z[i]} {b[i]} = ')
        res.append(int(s))
    return res 


def check_exam(a,b,z,res):
    """
    Check user answers against the correct results.

    Args:
        a (list): List of first operands.
        b (list): List of second operands.
        z (list): List of operators.
        res (list): List of user answers.

    Returns:
        tuple: List of errors and the total number of errors.
    """
    
    er=[]
    s=0
    for i in range(0, len(a)):
        if z[i]=='+':
            if a[i] + b[i] == res[i]:
                print(f'{i+1}) Good! :)')
            else:
                print(f'{i+1}) Error! :(')
                s+=1
                er.append([a[i],b[i],z[i]])
        else:
            if a[i] - b[i] == res[i]:
                print(f'{i+1}) Good! :)') 
            else:
                print(f'{i+1}) Error! :(') 
                s+=1
                er.append([a[i],b[i],z[i]])
    
    return er, s
                
  
# start exam 
def main(start, finish, count):
    
    """
    Run the main exam procedure.

    Args:
        start (int): The lower bound of the number range.
        finish (int): The upper bound of the number range.
        count (int): The number of questions to generate and check.
    """
    
    
    clear()
    print('')
    print('')
    
    print("Let's start the exam!")
    print(f"You have to answer {count} questions.")
    
    print('-----------------')

    start_time= time.time()
    
    a,b,z = generate_questions(start, finish, count)
    
    res = start_exam(a, b, z, count)
        
    print('-----------------')
    
    errors, total_errors = check_exam(a, b, z, res)
    
    count_e =len(errors) 

    while count_e>0:
        print("-----------------")
        print(f"You have {count_e} mistakes. Please fix them!")
        print('-----------------')

        ae=[]
        be=[]
        ze=[]
        for i in range(0, count_e):
            ae.append(errors[i][0])
            be.append(errors[i][1])
            ze.append(errors[i][2])
            
      
        
        res_e = start_exam(ae, be, ze, count_e)
        errors, count_e = check_exam(ae, be, ze, res_e)        
       
        
        total_errors+=count_e

                
    
    m=round((time.time() - start_time))//60
    s=round(time.time() - start_time)%60
    
    print(f'Total errors = {total_errors} ')
    print(f'You are doing the exam during {m} minutes and {s} seconds!')    



if __name__ == "__main__":
    if len(sys.argv) > 3:
        start = sys.argv[1]
        finish = sys.argv[2]
        count = sys.argv[3]
        if start.isdigit() and finish.isdigit() and count.isdigit():  
            main(int(start),int(finish), int(count))
        else: 
            print('It is not a number!')    
    else:
        print('Please provide the range of digits, and specify the number of mathematical tasks you would like to solve!')
        print ('Example: "math_exam.py" 0 100 10')