class Strings:
    def __init__(self):
        self.user_string = None

    def get_string(self):
        self.user_string = input('Enter a string to convert to capital: ')
        return
    def print_string(self):
        upper_string = self.user_string.upper()
        print(upper_string)
        return

class Rectangles:
    def __init__(self):
        self.width = None
        self.length = None

    def calculate_area(self):
        self.width = int(input('Enter the WIDTH: '))
        self.length = int(input('Enter the LENGTH: '))
        area = self.width * self.length
        print('AREA: ', area)
        return

class Person:
    def __init__(self, name, gender):
        self.gender = gender
        self.name = name
        self.age = None
        self.marks = None

    def getGender(self):
        print(self.gender)
        return

class Student:
    def __init__(self, name, roll_number, gender):
        self.name = name
        self.roll_number = roll_number
        self.gender = gender
    def display(self):
        print('Student Name :', self.name)
        print('Student Gender :', self.gender)
        print('Student Age :', self.age)
        print('Student Marks :', self.marks)

    def set_age(self):
        self.age = input('Enter the students age: ')
        return
    def set_mark(self):
        self.marks = input('Enter the students marks: ')
        return

student1 = Student('Alister', 'S269461', 'Male')
student1.set_age()
student1.set_mark()
student1.display()

stringClass = Strings()
stringClass.get_string()
stringClass.print_string()

rectangle = Rectangles()
rectangle.calculate_area()

person1 = Person('taryn', 'female')
person1.getGender()
