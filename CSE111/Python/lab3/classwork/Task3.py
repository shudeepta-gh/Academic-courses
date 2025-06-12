class Contacts:
  def __init__(self,l1,l2):
    self.contactDict={}
    self.names=l1
    self.numbers=l2

    if len(l1)!=len(l2):
      print("Contacts cannot be saved. Length Mismatch!")
    else:
      print("Contacts saved successfully")
      for ind in range(len(l1)):
        self.contactDict[l1[ind]]=l2[ind]
        #self.contactDict.update({l1[ind]:l2[ind]}) #can use this way too




# Driver code
names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)
