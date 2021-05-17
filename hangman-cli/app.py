

#Hangman
########

from random import choice
from draws import get_case

class Hangman:
	def __init__(self):
		self.game_on = True
		self.words = ["cat", "computer", "tablet"]
		self.health = 6
		self.word = ""
		self.hidden_word = ""
		self.guessed_letters = []

	def clear(self, case=1):
		if case == 1:
			for _ in range(80):
				print("")

			print(f"  HP: {self.health}")
			get_case(self.health)
		if case == 2:
			for _ in range(80):
				print("")

	def get_random_word(self):
		return choice(self.words)

	def update_secret(self):
			self.hidden_word = ""
			for letter in self.word:
				if letter in self.guessed_letters:
					self.hidden_word += letter
				else:
					self.hidden_word += "*"

	def run(self):
		self.clear(2)
		ask_wannaplay = input("Do you wanna play Hangman? (y/n)> ")
		if ask_wannaplay == "y":
			self.clear()
			self.word = self.get_random_word()
			self.update_secret()

			#Start the game
			while self.game_on and self.health > 0 and self.word != self.hidden_word:
					print(f"Word: {self.hidden_word}")
					guess = input("Gimme letter> ")

					if guess in self.word and guess not in self.guessed_letters:
						self.clear()
						self.guessed_letters.append(guess)
						self.update_secret()
						continue

					else:
						self.health -= 1
						self.clear()
						continue
			if self.hidden_word == self.word:
				print("Grats, you win")
			elif self.health <= 0:
				print("You run out of guesses")

		else:
			print("Thanks for trying")

game = Hangman()

if __name__ == "__main__":
	game.run()
