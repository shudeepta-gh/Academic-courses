class Shopidify:
  def __init__(self, name = 'Guest'):
    self.name = name
    self.cart = {}
    self.history = {}
    self.transaction = 0

    if name == 'Guest':
      print('Welcome to Shopidify')
    else:
      print(f'Welcome {self.name} to Shopidify')

  def add_to_cart(self, order, quantity = 1):
    if type(order) == list:
      for i in range(0, len(order), 2):
        if order[i] in self.cart:
          self.cart[order[i]] += order[i +1]
        else:
          self.cart[order[i]] = order[i + 1]
    else:
      if order in self.cart:
        self.cart[order] += quantity
      else:
        self.cart[order] = quantity

  def display_cart(self):
    print(f'Items in the cart for {self.name}:')
    for key, value in self.cart.items():
      print(f'-{key}: {value}x')

  def display_history(self):
    print(f'Purchase history for {self.name}:')
    print(f'Transaction: {self.transaction}')
    for key, value in self.history.items():
      print(f'-{key}: {value}x')

  def checkout(self):
    self.transaction += 1
    for key,value in self.cart.items():
      if key in self.history:
        self.history[key] += value
      else:
        self.history[key] = value
    self.cart = {}
    print(f'Checkout completed for {self.name}')

guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
