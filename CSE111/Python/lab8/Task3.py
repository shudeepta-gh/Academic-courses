class Travel:
  count=0
  def __init__(self,source,destination):
    self.__source=source
    self.__destination=destination
    self.__time=1
    Travel.count+=1


  def set_time(self,updated_time):
    self.__time=updated_time

  def set_source(self,updated_source):
    self.__source=updated_source


  def set_destination(self,updated_destination):
    self.__destination=updated_destination


  def display_travel_info(self):
    return (f"Source: {self.__source} \nDestination: {self.__destination} \nFlight Time: {self.__time}:00")


print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)
