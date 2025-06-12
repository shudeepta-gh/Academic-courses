class Author:
  def __init__(self,name="Unknown"):
    self.name=name
    self.book_dict={}
    self.count=0

    if self.name=="Unknown":
      print("A book can not be added without author name")
    else:
      self.name=name

  def addBook(self,book_title,book_genre):
    self.book_title=book_title
    self.book_genre=book_genre


    if self.book_genre not in self.book_dict:
      self.book_dict[self.book_genre]=[self.book_title]
      self.count+=1
    else:
      self.book_dict[self.book_genre]+=[self.book_title]
      self.count+=1

  def setName(self,name):
    self.name=name
  def printDetail(self):
    print(f"Number of books(s):{self.count}")
    print(f"Author Name:{self.name}")
    for k in self.book_dict.keys():
      print(k,":", ",".join(self.book_dict[k]))

a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")
