from homework import Homework
from exam_grade import Exam
from weakrefer import ExamR

g = Homework()
g.grade = 95
assert g.grade == 95

print(f'ocena {g.grade}')

print("__________________________________________")

e1 = Exam()
e1.first_part = 67
e1.second_part = 77
e1.third_part = 23

print(f'egzamin: 1 = {e1.first_part}, 2 - {e1.second_part}, 3 - {e1.third_part}')

e2 = Exam()
e2.first_part = 70
e2.second_part = 79
e2.third_part = 55

print(f'egzamin: 1 = {e2.first_part}, 2 - {e2.second_part}, 3 - {e2.third_part}')

print(f'archiwum............ podejście 1')
print(f'egzamin: 1 = {e1.first_part}, 2 - {e1.second_part}, 3 - {e1.third_part}')

print("__________________________________________")

e1 = ExamR()
e1.first_part = 12
e1.second_part = 45
e1.third_part = 3

print(f'egzamin R: 1 = {e1.first_part}, 2 - {e1.second_part}, 3 - {e1.third_part}')

e2 = ExamR()
e2.first_part = 60
e2.second_part = 72
e2.third_part = 45

print(f'egzamin R: 1 = {e2.first_part}, 2 - {e2.second_part}, 3 - {e2.third_part}')

print(f'archiwum............ podejście 1')
print(f'egzamin R: 1 = {e1.first_part}, 2 - {e1.second_part}, 3 - {e1.third_part}')
