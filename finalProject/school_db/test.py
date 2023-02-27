import sqlite3 as db
from datetime import date

connection = db.connect('school.db')
cursor = connection.cursor()

fileRes = open('record_example.txt','a')

items = cursor.execute('''
    SELECT 
    schedule.time_start,
    schedule.time_finish,
    subjects.subject_name,
    teachers.last_name,
    students.student_id,
    students.last_name,
    students.first_name,
    students.middle_name,
    students.year_birth,
    students.class_id
    FROM schedule,teachers,students,subjects
    UNION
    SELECT * FROM record_cabinet
    ;
''').fetchall()

for item in items:
    fileRes.write(f'{item}\n')
fileRes.close()

# подстановка данных из одной таблицы в другую по ключу с доп.условием:
# SELECT students.last_name, students.year_birth, students.month_birth,students.day_birth, genders.gender
# FROM students
# JOIN genders
# ON students.gender_id = genders.gender_id
# WHERE students.year_birth = 2013

# выборка учебного дня определенного студента
# SELECT 
# schedule.time_start,
# schedule.time_finish,
# students.last_name,
# students.first_name,
# students.middle_name,
# record_cabinet.row,
# record_cabinet.column,
# record_cabinet.option
# FROM record_cabinet,students,schedule
# ON schedule.schedule_id=record_cabinet.schedule_id
# AND record_cabinet.student_id=students.student_id
# WHERE students.student_id=77;