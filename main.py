import random

print("G'day mate!")
Name = input("\nWhats ya name? ")
print(f'\nAlright, {Name} it is then.')
print('\nI got 3 passkeys here for ya try and guess the right one')

choice = random.choice(['key','bagel','cat','dog']) 

print('\nYour options are...')
answer = input('key, bagel, cat, and dog: ')
while answer != choice:
  print('So close!')
  answer = input('Try again bud!: ')

print("\nGood job!Let's keep going!")


list2 = ['shoe','quack','float','clock','bed','sock','bin','bottle','water']

Answer2 = random.choice(list2)

for word in list2:
    if word == Answer2:   
      print(word.capitalize())
    else:
      print(word)
  
Guess2 = input('\nGuess which one is the correct one.(Hint:Look at the capitals):')
while Guess2 != Answer2:
  print('Try again')
  Guess2 = input('Guess again: ')

print('\nGreat job, this will be the final test, a dark room.Try and escape.')

room = [
  'xxxxxxxxxxx',
  'x........ex',
  'x.......xxx',
  'x.......x',
  'xxxxxxxxx',
] 



def announce_walls(current_row, current_col):
  if room[current_row - 1][current_col] == 'x': 
    print('\nThere is a wall upwards. ')
  if room[current_row + 1][current_col] == 'x': 
    print('\nThere is a wall downwards. ')
  if room[current_row][current_col - 1] == 'x': 
    print('\nThere is a wall to your left. ')
  if room[current_row][current_col + 1] == 'x': 
    print('\nThere is a wall to your right. ')
      
def move(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col

  if direction == 'up':
    new_row -= 1
  elif direction == 'down':
    new_row += 1
  elif direction == 'left':
    new_col -= 1
  elif direction == 'right':
    new_col += 1
  else:
    print(f'\nYou can not move {direction_choice}. Try up, down, left, or right')

  if room[new_row][new_col] == 'x': 
    print('\nYou can not move that way')
    return current_row, current_col
  
    return new_row, new_col 

  return new_row, new_col

player_row = 3
player_col = 1

while room[player_row][player_col] != 'e':
  announce_walls(player_row, player_col)
  direction_choice = input('What direction would you like to move? ')
  player_row, player_col = move(player_row, player_col, direction_choice)
  print(f'\nNew row is {player_row}')
  print(f'\nNew col is {player_col}')

print('\nYou escaped,Congrats!')


    




  