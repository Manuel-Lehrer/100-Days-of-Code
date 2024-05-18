# r = range(1,4)
# range_list = [n*2 for n in r]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 4]
from random import randint
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name: randint(1,100) for name in names}

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}

print(passed_students)