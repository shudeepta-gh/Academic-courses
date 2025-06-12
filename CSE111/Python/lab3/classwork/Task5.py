class CellPackage:
 def __init__ (self, price, data, talktime, msg, cashback, validity):
    self.data= int(data[ :-3])*1024
    self.price= price
    self.talktime= talktime
    self.sms= msg
    self.cashback= int(int(cashback[ :-1])*price/100)
    self.validity = validity

class checker :

  def __init__(self,packages):


      if packages.data!=0:
         print(f"Data = {packages.data}")

      if packages.talktime!=0:
         print(f"Talktime = {packages.talktime}")

      if packages.validity!=0:
         print(f"Validity = {packages.validity} Days")

      if packages.price!=0:
         print(f"---> Price = {packages.price} tk")

      if packages.cashback!=0:
         print(f"Buy now to get {packages.cashback} tk cashb



# Subtask 1: Write the CellPackage Class

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('===========Package 1=============')
checker(pkg)
# Subtask 2: Check each attribute and print

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('===========Package 2=============')
checker(pkg2)
# Subtask 3: Check each attribute and print

pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============Package 3============')
checker(pkg4)
# Subtask 4: Check each attribute and print
