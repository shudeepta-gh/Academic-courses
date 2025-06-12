class Teacher:
  def __init__(self,name,dept):
    self.student_name=name
    self.student_dept=dept
    self.course_list=[]



  def addCourse(self,course):
    self.course=course
    self.course_list.append(self.course)


  def printDetail(self):
    print("====================================")
    print(f"Name: {self.student_name}")
    print(f"Department: {self.student_dept}")
    print("List of courses")
    print("=====================================")
    for i in self.course_list:
      print(i.course_name)


class Course:
  def __init__(self,course_name):
    self.course_name=course_name


t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()
