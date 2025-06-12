class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team


class Player(SportsPerson):
  def __init__(self,team_name,name,role,goal,match):
    super().__init__(team_name,name,role)
    self.total_goal=goal
    self.total_match=match

  def calculate_ratio(self):
    self.ratio=self.total_goal/self.total_match
    self.earning_per_match+= (self.total_goal * 1000) + (self.total_match * 10)


  def print_details(self):
    print(f"{super().get_name_team()} \nTeam Role: {self.role} \nTotal Goal: {self.total_goal}, Total Played: {self.total_match} \nGoal Ratio: {self.ratio} \nMatch Earning: {self.earning_per_match}K")


class Manager(SportsPerson):
  def __init__(self,team_name,team,role,win):
    super().__init__(team_name,team,role)
    self.total_win=win
    self.earning_per_match+=(self.total_win*1000)



  def print_details(self):
    print(f"{super().get_name_team()} \nTeam Role: {self.role} \nTotal Win: {self.total_win} \nMatch Earning: {self.earning_per_match}K")



player_one = Player('Al-Nassr', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
