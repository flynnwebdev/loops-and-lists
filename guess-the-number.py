# Guess the number game
# You have 6 guesses to guess a random number between 1 and 20

# Import random module
import random
# Assign a random number to a variable
number = random.randint(1, 20)
# For guesses_left in 6..1
for guesses_left in range(6, 0, -1):
#   Ask for a guess
  guess = int(input(f'Take a guess ({guesses_left} left): '))
#   Display 'higher', 'lower' or 'correct'
  if guess < number:
    print('Too low!')
  elif guess > number:
    print('Too high!')
  else:
    print('Correct!')
    break

# If guess is incorrect
if guess != number:
  print(f'Sorry! The number was {number}')
