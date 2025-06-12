class BracuStudent:
  def __init__(self,name,home):
    self.name=name
    self.home=home
    self.bus_pass= False


  def show_details(self):
    print(f"Student Name:{self.name}")
    print(f"Lives in {self.home}")
    print(f"Have bus pass?{self.bus_pass}")




  def get_pass(self):
    if self.bus_pass== False:
      self.bus_pass= True

    else:
      self.bus_pass= False




class BracuBus:
  def __init__(self,destination,passenger_count=2):
    self.destination=destination
    self.passenger_count=passenger_count
    self.passenger_list=[]


  def board(self,*students):
    self.students=students
    self.count=0
    if len(self.students)==0:
      print("No passenger!")
    else:
      for student in self.students:
         if student.bus_pass==False:
           print("You don't have a bus pass!")
         else:
           if student.home!=self.destination:
              print("You got on the wrong bus!")

           else:
              if self.count<self.passenger_count:
                  print(f"{student.name} boarded on the bus")
                  self.passenger_list.append(student.name)
                  self.count+=1

              else:
                print("Bus is full!")



  def show_details(self):
    print(f"Bus Route:{self.destination}")
    print(f"Passenger Count:{len(self.passenger_list)} (Max:{self.passenger_count})")
    print(f"Passengers On Board:{self.passenger_list}")



st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
