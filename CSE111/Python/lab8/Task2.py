class Passenger:
  count=0
  def __init__(self,passenger_name):
    self.passenger_name=passenger_name
    Passenger.count+=1
    self.bus_fare=450
    self.__weight=0

  def set_bag_weight(self,bag_weight):
    self.bag_weight=bag_weight
    self.__weight=self.bag_weight
    if self.__weight<=20:
      self.bus_fare+=0
    elif 20<self.__weight<=50:
      self.bus_fare+=50

    else:
      if self.__weight>50:
        self.bus_fare+=100


  def printDetail(self):
    print(f"Name: {self.passenger_name}")
    print(f"Bus Fare: {self.bus_fare}")


print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
