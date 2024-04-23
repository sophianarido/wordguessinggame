# Word Guessing Game
import random
def start():
    num_players = int(input("Enter the number of players (1 or 2): "))
    word_list = ["PUDDING", "CAKE", "FLAN", "TIRAMISU", "BROWNIE"]
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    
    print("Secret Word:", "_ " * word_length)
    print("")

 # Initialize variables to track game state
    guesses = []
    max_guesses = 3

    while True:
        print("Welcome to the Word Guessing Game!")
        guess_word = input("Choose a word from the list:").upper()
            if guess_word in word_list: # type: ignore
                    print("You chose:", guess_word) 
                    break
            else:
                print("That is not a word in the list. Please try again.")

# Game loop for player(s)
num_players = int(input("Enter the number of players (1 or 2): "))
word_list = ["PUDDING", "CAKE", "FLAN", "TIRAMISU", "BROWNIE"]
secret_word = random.choice(word_list)
word_length = len(secret_word)

guesses = []
max_guesses = 3


for player in range(1, num_players + 1):
        print(f"Player {player}'s turn:")
        