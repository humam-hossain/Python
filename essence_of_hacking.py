import re
from itertools import permutations

# make calc with numbers: [1, 2, 4, 6] and ['(', ')', '+', '-', '*', '/']

def get_valid_exps():
    NUMS = ['1', '2', '4', '6']
    BRAKETS = ['(', ')']
    OPARETOR_SIGNS = ['+', '-', '*', '/']

    COLLECTIONS_NO_BRAKETS = list(permutations(NUMS + OPARETOR_SIGNS, 5))
    COLLECTIONS_BRAKETS = list(permutations(
        NUMS + OPARETOR_SIGNS + BRAKETS, 7))

    operations = COLLECTIONS_NO_BRAKETS + COLLECTIONS_BRAKETS

    valid_exps = []

    for each in operations:
        my_exp = ' '.join(each)
        try:
            # avoid parentheses contained number without expression(+-*/). eg: (3)
            if len(re.findall(r'\( (\d*?) \)', my_exp)) == 0:
                valid_exps.append({'exp': my_exp, 'result': eval(my_exp)})
        except:
            pass

    return valid_exps


get_valid_exps()


def find_equal_24():
    count = 0
    for each in get_valid_exps():
        if each['result'] == 24:
            count += 1
            print(f"{count}. {each['exp']} = {each['result']}")


find_equal_24()