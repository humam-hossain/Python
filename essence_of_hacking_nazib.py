import re
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

numbers = ['6', '4', '3', '1']
opening_bracket = '('
closing_bracket = ')'
operators = ['/', '*', '-', '+']

operatorCombinations = list(combinations_with_replacement(operators, 3))
numberPermutations = list(permutations(numbers))

# print(len(numbers))
for permutedNumbers in numberPermutations:
    for oc in operatorCombinations:
        ocperm = list(set(permutations(oc)))
        for occ in ocperm:
            expression = []
            expression.append(permutedNumbers[0])
            for i in range(len(occ)):
                expression.append(occ[i])
                expression.append(opening_bracket)
                expression.append(permutedNumbers[i+1])
            print(expression)


# 