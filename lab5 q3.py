class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Printdetails(self):
        print(f"Your name is : {self.name} \nYour age is : {self.age} ")
class Student(Person):
    def __init__(self,name,age,student_id,roll_no):
        super().__init__(name,age)
        self.student_id = student_id
        self.roll_no = roll_no
    def Printdetails(self):
        super().Printdetails()
        print(f"Your Student id is : {self.student_id} \nYour roll no. is : {self.roll_no} ")
class Resident(Student):
    def __init__(self,name,age,student_id,roll_no,house_no):
        super().__init__(name,age,student_id,roll_no)
        self.house_no = house_no
    def Printdetails(self):
        super().Printdetails()
        print(f"Your House no. is : {self.house_no}")
Hasnain = Resident("Muhammad Ali Hasnain",19,"cs-21068",68,681)
Hasnain.Printdetails()
