import random
def playRockPaperScissor(rounds):
  player_moves = {'rock' : 1, 'paper': 2, 'scissor': 3}
  computer_moves = {'rock' : 4, 'paper': 2, 'scissor': 3}
  moves = ['rock', 'paper', 'scissor']
  player_score = 0
  computer_score = 0
  winner = ""
  for i in range(rounds):
    player_move = input("Whats your move?:")
    computer_move = random.choice(moves)
    print("Computer:",computer_move)

    if player_move == computer_move:
      continue
    elif computer_moves[computer_move]-player_moves[player_move]==1:
      computer_score += 1
    else:
      player_score += 1

  if player_score > computer_score:
    winner = "player"
  elif computer_score > player_score:
    winner = "computer"
  else:
    winner = "tie"

  return (player_score, computer_score, winner)

rounds = int(input('Rounds: '))
player_score, computer_score, winner = playRockPaperScissor(rounds)

print(f'Your Score: {player_score}')
print(f'Computer Score: {computer_score}')

if winner == "player":
  print("You have won the game!")
elif winner == 'computer':
  print("Computer has won the game!")
else:
  print("It's a tie!")
