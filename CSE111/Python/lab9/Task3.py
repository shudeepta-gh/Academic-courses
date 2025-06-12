class SultansDine:
  number_of_branch=0
  total_sell=0
  branches_list=[]


  def __init__(self,location):
    self.branch_location=location
    self.branch_sell=0
    SultansDine.number_of_branch+=1

    SultansDine.branches_list.append(self)


  @classmethod
  def details(cls):
    print(f"Total Number of branch(s):{cls.number_of_branch}")
    print(f"Total Sell:{cls.total_sell} Taka")
    for branch in SultansDine.branches_list:
      print(f"Branch Name:{branch.branch_location} , Branch Sell:{branch.branch_sell} Taka")
      print(f"Branch consists of total sell's: {((branch.branch_sell/SultansDine.total_sell)*100):.2f}%")


  def sellQuantity(self,quantity):
    self.quantity=quantity

    if self.quantity<10:
      self.branch_sell+=(self.quantity*300)


    elif 10<self.quantity<20:
      self.branch_sell+=(self.quantity*350)

    else:
      self.branch_sell+=(self.quantity*400)

    SultansDine.total_sell+=self.branch_sell


  def branchInformation(self):
    print(f"Branch Name:{self.branch_location}")
    print(f"Branch Sell:{self.branch_sell}")


SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
