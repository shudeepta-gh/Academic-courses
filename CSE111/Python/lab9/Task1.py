class NikeBangladesh:
  branches=[]
  currently_stocked={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
  sold=0


  def __init__(self,place):
    self.place=place
    NikeBangladesh.branches.append(self.place)

  @classmethod
  def status(cls):
    print("Nike Bangladesh Status:")
    print(f"Branches Opened: {cls.branches}")
    print(f"Currently Stocked: {cls.currently_stocked}")
    print(f"Sold: {cls.sold}")


  def details(self):
    print(f"Nike {self.place} outlet")
    print(f"Products Currently Stocked: {NikeBangladesh.currently_stocked}")
    print(f"Sold: {NikeBangladesh.sold}")


  def restockProducts(self,new_stocked):
    self.new_stocked=new_stocked
    for product in NikeBangladesh.currently_stocked.keys():
      for new_product in self.new_stocked.keys():
          if product==new_product:
            NikeBangladesh.currently_stocked[product]+=self.new_stocked[new_product]

          else:
            NikeBangladesh.currently_stocked[product]+=0



  def productSold(self,new_sold):
    self.new_sold_products=new_sold




    for product in NikeBangladesh.currently_stocked.keys():
       for sold_product in self.new_sold_products.keys():
          if product==sold_product:
            NikeBangladesh.sold+=self.new_sold_products[sold_product]
            NikeBangladesh.currently_stocked[product]-=self.new_sold_products[sold_product]

          else:
            NikeBangladesh.currently_stocked[product]-=0


print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
