import model
import view
import os
from pprint import pprint


def add_student():
    name = input("Введите фамилию, имя (через пробел): ").strip()
    if not model.add_student(name):
        input('Студент уже существует. Нажмите Enter для продолжения')
    else:
        input('Студент добавлен. Нажмите Enter для продолжения..')


def add_lesson():
    lesson = input("Введите предмет: ").strip()
    if not model.add_lesson(lesson):
        input('Предмет уже существует. Нажмите Enter для продолжения')
    else:
        input('Предмет добавлен. Нажмите Enter для продолжения..')

def add_rating():  
    student = input("Введите фамилию, имя (через пробел): ").strip()
    lesson = input("Введите название предмета: ").strip()
    rating = int(input("Введите оценку: "))
    if not model.add_rating(lesson, student, rating):        
        input('Предмет или студент не существует. Нажмите Enter для продолжения..')


def show_student(data):
    view.show_student(data)
    input('Нажмите Enter для продолжения..')


def show_student_ratting(data):    
    student = input("Введите фамилию, имя (через пробел): ").strip()
    if not view.show_student_ratting(student, data):
        input('Студент не существует. Нажмите Enter для продолжения..')
    else:
        input('Нажмите Enter для продолжения..')

def add_random_students():
    model.add_random_students()    
    input('Студенты созданы. Нажмите Enter для продолжения..')


def start():
    while True:
        os.system("cls")
        view.show_menu()
        while True:
            menu_input = int(input())
            if 0 < menu_input < 9:
                break
            else:
                print("неправильный ввод")
        match menu_input:
            case 1:
                add_student()
            case 2:
                add_lesson()
            case 3:
                data = model.get_data()
                show_student(data)
            case 4:
                data = model.get_data()
                show_student_ratting(data) 
            case 5:
                data = model.get_data()
                add_rating() 
            case 6:
                data = model.get_data()
                add_random_students() 
            case 8:
                exit()
