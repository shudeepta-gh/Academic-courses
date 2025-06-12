class Farmer:
  def __init__(self, a = None):
    if type(a) == str:
      print(f'Welcome to your farm, {a}!')
    elif type(a) == int:
      print(f'Welcome to your farm. Your farm ID is {a}!')
    else:
      print('Welcome to your farm!')

    self.crops = []
    self.fishes = []
  def addCrops(self,*crops):
    if len(crops) == 0:
      print('No crop(s) added.')
      return
    for crop in crops:
      self.crops.append(crop)
    print(f'{len(crops)} crops(s) added.')

  def addFishes(self, *fishes):
    if len(fishes) == 0:
      print('No fish added.')
      return
    for fish in fishes:
      self.fishes.append(fish)
    print(f'{len(fishes)} fish(s) added.')

  def showGoods(self):
    if len(self.crops) == 0:
      print("You don't have any crop(s)")
    else:
      print(f'You have {len(self.crops)} crops(s).')
      items_str = ''
      print(','.join(self.crops))  #join function converts a list into a string if all the elements inside the list are string
      

    if len(self.fishes) == 0:
      print("You don't have any fish(s).")
    else:
      print(f'You have {len(self.fishes)} fish(s):')
      print(",".join(self.fishes))
      
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
