class Employee:

  def __init__(self,name,id,dept):
    self.employee_name=name
    self.employee_id=id
    self.dept=dept
    self.salary=30000
    self.employee_type="Regular"


  def employeeDetails(self):
    print(f"Name: {self.employee_name}, Dept {self.dept} \nEmployee id: {self.employee_id}, Salary: {self.salary}")


  def workDistribution(self,dept):
    if self.dept=="Human Resource":
      print("Collect work distribution from the manager")

    else:
      print("Collect work distribution loads from the HR department")


  def increment(self):
    if self.employee_type=="Regular" :
      self.salary+=(self.salary*(10/100))

    elif self.employee_type=="Foreign":
      self.salary+=(self.salary*(15/100))


    else:
      print(f"Sadly, there is no increment for the part time employees!!!")

class Foreign_employee(Employee):

  def __init__(self,name,id,dept):
    super().__init__(name,id,dept)
    self.employee_type="Foreign"

  def employeeDetails(self):
    super().employeeDetails()
    print(f"Employee_type: {self.employee_type}")


class Part_time_employee(Employee):
  def __init__(self,name,id,dept):
    super().__init__(name,id,dept)
    self.employee_type="Part Time"
    self.salary=15000


  def employeeDetails(self):
    super().employeeDetails()
    print(f"Employee_type: {self.employee_type}")

print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()
