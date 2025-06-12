class Team:
  def __init__(self,country=None):
    self.__country=country
    self.__playerlist=[]


  def addPlayer(self,player):
    self.__player=player

    self.__playerlist.append(self.__player.player_name)



  def setName(self,newCountry):
    self.__country=newCountry


  def printDetail(self):
    print("=====================")
    print(f"Team:{self.__country}")
    print(f"List of players: \n{self.__playerlist}")
    print("=====================")


class Player:
  def __init__(self,name):
    self.player_name=name



b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
