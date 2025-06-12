class Department:
  def __init__(self,dept="ChE Department",sections=5):
    self.department=dept
    self.sections=sections
    self.average_students=0
    self.merged_result=0

    print(f"The {self.department} has {self.sections} sections.")


  def add_students(self,*number_of_sections):
    self.result=0
    self.number_of_sections=number_of_sections
    if len(self.number_of_sections)==self.sections:
      for number in self.number_of_sections:
        self.average_students+=number
      self.result+=self.average_students/self.sections
      print(f"The {self.department} has an average of {self.result} students in each section.")

    else:
      print(f"The {self.department} doesnt have {self.sections} sections.")


  def merge_Department(self,*dept_names):

    self.dept_names=dept_names
    for dept in dept_names:
      self.average_students=self.average_students+dept.average_students
      self.merged_result=self.average_students/self.sections

      print(f"{self.department} is merged to {dept.department}")
    return f"Now the {self.department} has an average of {self.merged_result} students in each section."




d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))
