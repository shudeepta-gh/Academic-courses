class MangoTree:
  def __init__(self,v):
    self.variety=v
    self.height=1
    self.number_of_mangoes=0




mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

print("updated value after 5 years")
print("========================================")
print(f"Variety: {mangoTree1.variety}")
mangoTree1.height=(mangoTree1.height)+(3*5)
print(f"Height: {mangoTree1.height} meter(s)")
mangoTree1.number_of_mangoes=(mangoTree1.height)*10
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")

print("=========================================")
print(f"Variety: {mangoTree2.variety}")
mangoTree2.height=(mangoTree2.height)+(3*5)
print(f"Height: {mangoTree2.height} meter(s)")
mangoTree2.number_of_mangoes=(mangoTree2.height)*15
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")

