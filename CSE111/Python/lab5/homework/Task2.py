class Foodie:
  def __init__(self, name):
    self.name = name
    self.items = []
    self.spent = 0

  def show_orders(self):
    result = ''
    result += (f'{self.name} has {len(self.items)} items(s) in the cart') + '\n'
    result += (f"items: {str(self.items)}") + '\n'
    result += (f'Total spent: {self.spent}')

    return result

  def order(self,*args):
    for ord in args:

      item,quantity=ord.split("-")
      quantity=int(quantity)
      if item not in self.items:
        self.items.append(item)

      print(f'Ordered - {item}, quantity - {quantity}, price(per unit) - {menu[item]}.')
      print(f'total price - {menu[item] * quantity}')
      self.spent += menu[item] * quantity

  def pay_tips(self, tip = 0):
    if tip == 0:
      print('No tips to the waiter.')
    else:
      print(f'Gives {tip}/- tips to the waiter.')
      self.spent += tip

menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())
