import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

end_of_game = False
lives = 6

random_word_list = random.choice(word_list)

underline = []
len_list = len(random_word_list)
for n in range(len_list):
    underline += "_"

while not end_of_game:
  string_underline = " ".join(underline)
  user_input = input(f"Guess a letter: {string_underline}\n").lower()

  if user_input in underline:
    print(f"You have already guessed {user_input}!")

  for position in range(len_list):
      letter = random_word_list[position]
      if letter == user_input:
          underline[position] = letter

  if user_input not in random_word_list:
    print(f"\nYou guessed {user_input}, and it is wrong. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"\nYou Lose! The correct word is \"{random_word_list}\".")
    
  if "_" not in underline:
      end_of_game = True
      print("Congratulations, you won!")

  print("\n" + stages[lives])
