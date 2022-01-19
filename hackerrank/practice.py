#!/bin/python3

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Mathematics', 'Physics']
info = {'name': 'Humam', 'age': 20}

print(*courses)
print(*info)
print()
student_info(*courses, **info)