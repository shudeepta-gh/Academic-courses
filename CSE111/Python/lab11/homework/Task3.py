class PokemonBasic:

  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type

  def get_type(self):
    return 'Main type: ' + self.type

  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'

  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):
  def __init__(self,name,hp,weakness,type1,type2=None,moves="Unknown"):
    super().__init__(name,hp,weakness)
    self.type=type1
    self.secondary_type=type2
    self.moves=moves

  def get_type(self):
    if self.secondary_type==None:
      return super().get_type()

    else:
      return super().get_type()+", Secondary type: " + self.secondary_type


  def get_move(self):

    if self.moves=="Unknown":
      return super().get_move()

    else:
      self.moves=list(self.moves)
      return f"{super().get_move()} \nOther move: {', '.join(self.moves)}"

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
