class Vaccine:
  def __init__(self,name,country,days):
    self.name=name
    self.country=country
    self.days=days
class Person:
  def __init__(self,name,age,person_type="General Citizen"):
    self.person_name=name
    self.person_age=age
    self.person_type=person_type
    self.first_dose=None
    self.second_dose=None


  def pushVaccine(self,vaccine,dose="1st Dose"):
    self.vaccine=vaccine
    self.dose=dose

    if self.person_age>=25 or self.person_age==21:
      if self.dose=="1st Dose":
        self.first_dose=self.vaccine.name
        print(f"1st dose done for {self.person_name}")

      else:
        if self.dose=="2nd Dose":
          self.second_dose=self.vaccine.name
          if self.first_dose==self.second_dose:
            print(f"2nd dose done for {self.person_name}")

          else:
            print(f"Sorry {self.person_name}, you can’t take 2 different vaccines")
    else:
      print(f"Sorry {self.person_name}, Minimum age for taking vaccines is 25 years now.")



  def showDetail(self):
    print(f"Name: {self.person_name} Age: {self.person_age} Type: {self.person_type}")
    print(f"Vaccine name: {self.vaccine.name}")

    if self.dose=="1st Dose":
      print("1st dose: Given")
      print(f"2nd dose:Please come after {self.vaccine.days} days")

    else:
      if self.dose=="2nd Dose":
       # if self.first_dose==self.second_dose:
           print("1st dose: Given")
           print("2nd dose: Given")





astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
