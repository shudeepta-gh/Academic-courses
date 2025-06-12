class Player:
  total=0
  player_list=[]
  def __init__(self,name="Unknown",number=10,team="Unknown"):
      self.__name=name
      self.__team=team
      self.__number=number
      Player.total+=1

      if self.__name!="Unknown":
        Player.player_list.append(self.__name)

  def set_name(self,updated_name):
    self.updated_name=updated_name
    self.__name=self.updated_name
    Player.player_list.append(self.__name)


  def set_team(self,updated_team):
    self.updated_team=updated_team
    self.__team=self.updated_team


  def set_number(self,updated_number):
    self.updated_number=updated_number
    self.__number=self.updated_number

  def player_detail(self):
    return (f"Player Name:{self.__name} \nJersey Number:{self.__number} \nCountry:{self.__team}")
  @classmethod
  def info(cls):
    print(f"Total number of players:{cls.total}")
    print(f"Players enlisted so far:{', '.join(Player.player_list)}")

print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()
