class GreenPhone:
  def __init__(self,name,version,cameras):
    self.phone_company="GreenPhone"
    self.model_name=name
    self.android_version=version
    self.number_of_cameras=cameras

  def showSpecification(self):
    print(f"Phone Company: {self.phone_company}")
    print(f"Model Name: {self.model_name}")
    print(f"Android Version: {self.android_version}")
    print(f"Number of Cameras: {self.number_of_cameras}")

  def updatePhone(self):
    if self.model_name=='A1':
       if self.android_version<14:
          self.android_version+=1
          print(f"Your phone Greenphone A1 is upgraded to Android Version:{self.android_version}")
       else:

          print("Your phone GreenPhone A1 is already up to date")


    if self.model_name=='M11':
      if self.android_version<15:
        self.android_version+=1
        print(f"Your phone GreenPhone M11 is upgraded to android version:{self.android_version}")
      else:
        print(f"Your phone Greenphone M11 is up to date")


    if self.model_name=='U20':
      if self.android_version<16:
        self.android_version+=1
        print(f"Your phone GreenPhone M11 is upgraded to android version:{self.android_version}")
      else:
        print(f"Your phone Greenphone M11 is up to date")


print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
