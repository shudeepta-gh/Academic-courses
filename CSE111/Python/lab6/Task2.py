class Student:
  def __init__(self,name,id,cgpa):
    self.student_name=name
    self.student_id=id
    self.student_cgpa=cgpa


  def setId(self,id):
    self.id=id


class Department:
  def __init__(self,dept):
    self.dept=dept
    self.student_list=[]#s1,s2,s3




  def addStudent(self,*students):
    self.students=students
    for student in self.students:
      if student in self.student_list:
        print("Student with the same ID already exists, Please try with another ID")


      else:
        self.student_list.append(student)
        print(f"Welcome to CSE department {student.student_name}")




  def findStudent(self,id):
    self.id=id
    for student in self.student_list:
      if student.student_id==self.id:
        print(f"Student info:")
        print(f"Student Name: {student.student_name}")
        print(f"ID: {student.student_id}")
        print(f"CGPA: {student.student_cgpa}")

      elif student.student_id!=self.id:
        print("Student with this ID doesn't exist, Please give a valid ID")

    if len(self.student_list)==0:
        print("Student with this ID doesn't exist, Please give a valid ID")




  def details(self):
        print("Department Name:", self.dept)
        print("Number of student:", len(self.student_list))
        print("Details of the students:")
        for student in self.student_list:
          print(f"Student name: {student.student_name} , ID:, {student.student_id} , cgpa: {student.student_cgpa}")






s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)

print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()
