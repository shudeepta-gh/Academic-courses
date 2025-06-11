def calculate_price(burger,place="Mohakhali"):
  delivery_cost=40
  if burger=="BBQ Chicken Cheese Burger":
    meal_cost=250
    tax=meal_cost*0.08
    if place!="Mohakhali":
      delivery_cost=60

  elif burger=="Beef Burger":
    meal_cost=170
    tax=meal_cost*0.08
    if place!="Mohakhali":
      delivery_cost=60

  elif burger=="Naga Drums":
    meal_cost=200
    tax=meal_cost*0.08
    if place!="Mohakhali":
      delivery_cost=60

  Total_price=meal_cost+delivery_cost+tax
  print(Total_price)

burger=input()
place=input()
if place=="":
  calculate_price(burger)
else:
  calculate_price(burger,place)
