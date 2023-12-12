# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

from collections import Counter
names_list=[]
for name in students:
    names_list.append(name['first_name'])
cnt=Counter(names_list)

for name in cnt:
    print(f"{name}: {cnt[name]}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

from collections import Counter
names_list=[]
for name in students:
    names_list.append(name['first_name'])
cnt=Counter(names_list).most_common(1)
print(f"Самое частое имя среди учеников: {cnt[0][0]}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
from collections import Counter
for index, classes in enumerate(school_students):
    names_list=[]
    for name in classes:
        names_list.append(name['first_name'])
    cnt=Counter(names_list).most_common(1)
    print(f"Самое частое имя в классе {index+1}: {cnt[0][0]}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

from collections import Counter

def know_gender_bool(name_dict):
    return is_male.get(name_dict['first_name'])

def know_gender(gender_bool):
    if gender_bool:
        return 'мальчики'
    else:
        return 'девочки'

def add_gender(students_list):
    for names in students_list:
        names['gender']=know_gender(know_gender_bool(names))
    return students_list

def students_list_gender_count(students_list):
    students_list_gender=add_gender(students_list)
    gender_list=[]
    for name in students_list_gender:
        gender_list.append(name['gender'])
    cnt=Counter(gender_list)
    return cnt

for classes in school:
    students_list=classes['students']
    a=add_gender(students_list)
    b=students_list_gender_count(a)
    print(f"Класс {classes['class']}: девочки {b['девочки']}, мальчики {b['мальчики']}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

max_girls=0
max_boys=0

for classes in school:
    students_list=classes['students']
    a=add_gender(students_list)
    b=students_list_gender_count(a)
    classes['девочек']=b['девочки']
    classes['мальчиков']=b['мальчики']
    del classes['students']
    
    if b['девочки']>=max_girls:
        max_girls=b['девочки']
    else: pass

    if b['девочки']>=max_boys:
        max_boys=b['мальчики']
    else: pass

for classes in school:
    if classes['девочек']==max_girls:
        print(f"Больше всего девочек в классе {classes['class']}")
    elif classes['мальчиков']==max_boys:
        print(f"Больше всего мальчиков в классе {classes['class']}")
    else: pass

