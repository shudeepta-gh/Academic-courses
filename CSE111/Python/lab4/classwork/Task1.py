class Customer:
  def __init__(self):
    print("Welcome to ABC Memorial Park")
    self.count=0
    self.price=0




  def buyTicket(self,name,age):
    self.name=name
    self.age=age
    if self.count>=3:
      print("You can't buy more than 3 tickets")
    else:
      print(f"Successfully purchased a ticket for {self.name}")
      self.count+=1
      if self.age>10:
        self.price+=100
      else:
        self.price+=50


  def showDetails(self):
      print(f"Amount of tickets: {self.count}")
      print(f"Total price={self.price}")



print("1-------------------------")
customer1 = Customer()
print("2-------------------------")
customer1.buyTicket("Bob", 23)
customer1.buyTicket("Henry", 7)
customer1.buyTicket("Alexa", 30)
customer1.buyTicket("Jonas", 43)
print("3-------------------------")
customer1.showDetails()
print("4-------------------------")
customer2 = Customer()
print("5-------------------------")
customer2.buyTicket("Harry", 60)
customer2.buyTicket("Tomas", 28)
print("6-------------------------")
customer2.showDetails()
