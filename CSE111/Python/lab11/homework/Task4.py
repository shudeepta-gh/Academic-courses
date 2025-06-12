class Cakes:
  order_list={}
  feedback_dict={}
  def __init__(self,flavor,weight):
    self.flavor=f"{flavor} Cake"
    self.weight=weight
    self.weight_gm=f"{weight}gm"
    self.sugar="Moderate"
    self.cream_type="Whipped Cream"
    self.price=(1200*weight)/1000
    self.flavor_weight=self.flavor+" "+self.weight_gm


    if self.flavor_weight not in Cakes.order_list:
       Cakes.order_list[self.flavor_weight]=1

    else:

       Cakes.order_list[self.flavor_weight]+=1

  def cake_details(self):
    print(f"Flavor:{ self.flavor}, Weight: {self.weight} gm \nSweetness: {self.sugar} sugar, Cream Type: {self.cream_type} \nPrice: {self.price} Taka")


  def add_customization(self,sugar,cream):

    self.sugar=sugar
    self.cream_type=cream

  @classmethod

  def give_feedbacks(cls,name,feedback):
    print("Thanks for your valuable feedback!")

    if name not in cls.feedback_dict:
        cls.feedback_dict[name]=[feedback]

    else:
        cls.feedback_dict[name]+=[feedback]


  @classmethod
  def show_feedbacks(cls):
    print(cls.feedback_dict)


class Cheese_Cakes(Cakes):
  def __init__(self,flavor,weight,bake="Baked"):
    super().__init__(flavor,weight)
    self.cream_type="Cream Cheese"
    self.cake_type=bake
    self.price=(1500*weight)/1000


  def add_customization(self):
    print("Sorry! No customization available for cheese cakes.")


  def cake_details(self):
     print(f"Flavor:{ self.flavor}, Weight: {self.weight} \nSweetness: {self.sugar} sugar, Cream Type: {self.cream_type} \nCake Type: {self.cake_type}, Price: {self.price} Taka")




  @classmethod
  def give_feedbacks(cls,name,feedback):
    super().give_feedbacks(name,feedback)
    print("You will get 10% discount for your next purchase!")


order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()
