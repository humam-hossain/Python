#! /usr/bin/env python3

"""
Bruteforce solution to the following assigment

1. Estimate how long it's going to take you, before you do it, and let us know what your guess is.
2. Time yourself at the end, compare results.
Guidelines and requirements:
-Do it in a pythonic, readable way. Readability is the priority.
-Instead of 1, 3, 4, 6, accept any user input for n integers or floas.
-Instead of 24, accept any user input for 1 integer or float.
-Show how many total permutations there are
-Show how many solutions there are
-Graph all the permutations in order of value. X axis: iteration # (arbitrary), Y axi value.
-Error handling.
-Find out how long your program takes for each iteration on average.
Use each of the numbers 1, 3, 4, and 6 exactly once with any of the four basic math operations 
(addition, subtraction, multiplication, and division) to total 24. Each number must be used once and 
only once, and you may define the order of operations; for example, 3 * (4 + 6) + 1 = 31 is valid, 
however incorrect, since it doesn't total 24.


This program use each of the numbers in src_numbers exactly once 
with any of the four basic math operations 
(addition, subtraction, multiplication, and division) to total target_number. 
Each number must be used once and only once!

Running complexity of this algorithm is approximately

    n! * S^n

where n is src_numbers and S is symbol_set
"""

import sys
from itertools import permutations, product

show_plot = True

try:
    import matplotlib.pyplot as plt
except ImportError:
    show_plot = False
    print('matplotlib is not installed! Plot wont be shown')


if len(sys.argv) < 4:
    print('Too few arguments specified!')
    print('Usage: ./problem24.py <source_numbers> ... <target_number>')
    exit(1)

# User's command line arguments
target_number = float(sys.argv[-1:][0])
src_numbers = sys.argv[1:-1]

symbol_set = ['+','-','/','*','(',')','/(','*(','-(','+(',')/',')*',')+',')-']
permutation_list = []

def is_invalid_parenthesis(symbols):
    
    for i in range(1, len(symbols)):

        prev_symbol = symbols[i-1][-1:][0]
        cur_symbol = symbols[i][:1][0]
        
        if  prev_symbol == '(' and cur_symbol == ')':
            return True

    return False

count = 0
for symbols in product(symbol_set, repeat=len(src_numbers)+1):

    first_symbol = symbols[0][:1][0]

    if first_symbol == '-':
        continue

    if is_invalid_parenthesis(symbols):
        continue

    for numbers in permutations(src_numbers):

        current_expression = ''
        
        # Add digits to each symbol to form final expression
        for i, j in zip(symbols, numbers):
            current_expression += i + str(float(j))

        current_expression += symbols[-1:][0]

        try:
            answer = eval(current_expression)
        except Exception as e:
            break  # Expression failed to avalute. Skip it

        permutation_list.append((count, answer))
        count += 1

        if answer == target_number:            
            # Trim redundant + sign at the begining of the expression
            if current_expression.startswith('+'):
                current_expression = current_expression[1:]
            print(current_expression)

if show_plot:
    # Sort by expression value
    perm_by_value = sorted(permutation_list, key=lambda tup: tup[1])

    # Plot
    plt.scatter(*zip(*perm_by_value))
    plt.show()