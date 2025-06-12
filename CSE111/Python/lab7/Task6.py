class Library:
  def __init__(self,library_name,books):
    self.library_name=library_name
    self.books_availability_dict=books
    self.borrower_details_dict={}


  def details(self):
    print(f"{self.library_name} Library details")
    print(f"Borrower details: \n{self.borrower_details_dict}")
    print(f"Books availability: \n{self.books_availability_dict}")



class Reader:
  def __init__(self,borrower_name):
    self.borrower_name=borrower_name
    self.book_count=0
    self.selected_genre={}

  def borrow(self,library,*genres):
    self.library=library
    self.genres=genres

    for genre in self.genres:
      if self.book_count<5:

         if self.library.books_availability_dict[genre]!=0:
            self.library.books_availability_dict[genre]-=1
            print(f"{genre} book is borrowed successfully.")
            self.book_count+=1

            if genre not in self.selected_genre:
               self.selected_genre[genre]=1

            else:
               self.selected_genre[genre]+=1

         else:
          print(f"{genre} books are not available at the moment.")

      else:
        print("You cannot borrow more than 5 books.")

      self.library.borrower_details_dict[self.borrower_name]=self.book_count





  def readerInfo(self,genre=None):
    self.genre=genre
    if self.genre==None:
      print(f"{self.borrower_name}, you have {self.book_count} book(s) with you.")
      for genre in self.selected_genre.keys():
        print(f"Books on {genre} : {self.selected_genre[genre]}")


    else:
      print(f"{self.borrower_name},you have {self.selected_genre[self.genre]} {self.genre} book(s) with you.")




L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
