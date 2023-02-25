class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married


    def introduce_myself(self):
        print(f'introduce_myself: {self.fullname}  age: {self.age}  is_married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks:dict):
        super(). __init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
            return sum(self.marks.values()) / len(self.marks.values())


class Teacher(Person):
    salary = 50000

    def __int__(self, fullname, age, is_married, experience):
            super().__init__(fullname, age, is_married)
            self.experience = experience

    def sum_salary(self):
        if self.experience > 3:
            new_salary = (self.salary / 100 * 5) * (self.experience - 3)
            print(new_salary)

def create_students():
    student_1 = Student("Kulov Manas", 25, "no", {"Eng": 5, "Math":5, "Phys":5})
    student_2 = Student("Averkina Natalya", 17, "no", {"Eng":4,"Math":4, "Phys":4})
    student_3 = Student("Borbiev Ulan", 25, "yes", {"Eng": 3,"Math":3, "Phys":3})
    result = [student_3, student_1, student_2]

    return result

for i in create_students():
    print(i.introduce_myself(),i.average())




