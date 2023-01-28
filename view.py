def show_menu():
    print("выберите операцию:")
    print("1.Добавление нового студента")
    print("2.Добавление предмета")
    print("3.Показ списка учеников")
    print("4.Показ листа оценок конкретного ученика")
    print("5.Добавить оценку ученику")
    print("6.Сгенирировать учеников")
    print("8.Выход из программы")

def show_student(data):
    students = [student for student in data]
    print(students)
    for number, student in enumerate(students):
        print(number, student)

def show_student_ratting(student, data):
    if student in data:
        print(data[student])
        return True
    else:
        return False