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

print('\nGood job, you seem to be getting the hang of this')