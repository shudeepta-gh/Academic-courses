class StudentDatabase:
  def __init__(self,name,id):
    self.name=name
    self.student_id=id
    self.grades={}
  def calculateGPA(self,courses,semester):
    self.courses=courses
    self.semester=semester
    self.courses_list=[]
    overall_cgpa=0

    self.semester_grade={}
    for each_course in self.courses:
      course,cgpa=each_course.split(": ")

      self.courses_list.append(course)
      overall_cgpa+=float(cgpa)*3

    grade_point=f"{overall_cgpa/(len(self.courses_list)*3) :.2f}"

    self.semester_grade[tuple(self.courses_list)]=float(grade_point)
    self.grades[self.semester]=self.semester_grade


  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.student_id}")
    for semester,all_courses in self.grades.items():
      print(f"Courses taken in {semester}")
      for courses,gpa in all_courses.items():
        for course in courses:
          print(course)
        print(f"CGPA: {gpa}")

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
