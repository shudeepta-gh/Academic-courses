class Patient:

  def __init__(self, id, name, age, bloodgroup, next, prev):
    self.id = id
    self.name = name
    self.age = age
    self.bloodgroup = bloodgroup
    self.next = next
    self.prev = prev

class WRM:


  def __init__(self):

    self.dh = Patient(None,None,None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh
    self.length = 0

  def registerPatient(self,id, name, age, bloodgroup):

    newPatient = Patient(id,name,age,bloodgroup,None,None)
    tail = self.dh.prev
    tail.next=newPatient
    newPatient.prev = tail
    newPatient.next = self.dh
    self.dh.prev = newPatient
    self.length += 1
    print("Success registering patient")


  def servePatient(self):

    if(self.length==0):
      print("No patient to serve")
      return

    else:
      firstPatient = self.dh.next
      self.dh.next = firstPatient.next
      firstPatient.next.prev = self.dh
      print(f"{firstPatient.name} has been served")

      self.length -= 1


  def showAllPatient(self):
    if(self.length==0):
      print("No patient to show")


    else:
      temp = self.dh.next
      while(temp != self.dh):
        print(temp.name)
        temp = temp.next


  def canDoctorGoHome(self):
    if(self.length==0):
      return "Yes"

    else:
      return "No"



  def cancelAll(self):
    self.dh.next = self.dh
    self.dh.prev = self.dh
    self.length = 0
    print("Appointments are cancelled")


  def ReverseTheLine(self):

    if self.length <= 1:
        print("Nothing to reverse.")
        return


    pointer = self.dh.next
    lastPatient = self.dh.prev
    while(pointer != self.dh):
      temp = pointer.next
      pointer.next = pointer.prev
      pointer.prev = temp
      pointer = pointer.prev

    self.dh.next = lastPatient
    self.dh.prev = lastPatient.prev

    print("Successfully reversed")



#Tester Code
print("Welcome to waiting room management system")
wrm=WRM()
while True:
   print("Choose an option")
   print("1. RegisterPatient()\n2. ServePatient()\n3. CancelAll()\n4. CanDoctorGoHome()\n5. ShowAllPatient()\n6. reverseTheLine()\n7. Exit")
   choice = int(input("Enter your choice: "))

   if(choice==1):
    print("Executing RegisterPatient()...")
    id=int(input("Enter ID: "))
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    bloodgroup=input("Enter Blood Group: ")
    wrm.registerPatient(id,name,age,bloodgroup)

   elif(choice==2):
    print("Executing servePatient()...")
    wrm.servePatient()

   elif(choice==3):
    print("Executing cancelAll()...")
    wrm.cancelAll()

   elif(choice==4):
    print("Executing canDoctorGoHome()...")
    print(wrm.canDoctorGoHome())

   elif(choice==5):
    print("Executing showAllPatients()...")
    wrm.showAllPatient()

   elif(choice==6):
    print("Executing ReverseTheLine...")
    wrm.ReverseTheLine()

   elif(choice==7):
    break

   else:
    print("Invaid choice.Try again")
