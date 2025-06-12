class Spaceship:
  def __init__(self,name,capacity):
    self.name=name
    self.capacity=capacity
    self.cargos=[]
    self.sum=0


  def load_cargo(self,cargo):
    self.cargo=cargo


    if self.capacity>self.cargo.getWeight()+self.sum:
       self.cargos.append(self.cargo)
       self.sum+=cargo.getWeight()

    else:
       self.exceeded_capacity=(self.cargo.getWeight()+self.sum)-self.capacity
       print(f"Warning: Unable to load {self.cargo.getName()} inside {self.name}.\nExceeds capacity by {self.exceeded_capacity}.")


  def display_details(self):
    self.cargolist=[]

    print(f"Spaceship Name:{self.name}")
    print(f"Capacity:{self.capacity}")

    for cargo in self.cargos:
      
      self.cargolist.append(cargo.getName())

    print(f"Current Cargo Weight:{self.sum}")
    print(f"Cargo:{self.cargolist}")



class Cargo:
  def __init__(self,name,weight):
    self.__name=name
    self.__weight=weight



  def getWeight(self):
    return self.__weight

  def getName(self):
    return self.__name

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()
