import random
import string

words = [
	'awesome', 'not', 'positive', 'letter', 'space', 'guard', 'moon', 'trip', 'partner',
	'dark', 'light', 'code', 'helicopter', 'nap', 'twilight', 'mind', 'hesitate',
	'cap', 'lost', 'temple', 'like', 'accent', 'sum', 'master', 'lavender', 'find',
	'have', 'give', 'man', 'women', 'capture', 'percentage', 'pomegranate', 'apple',
	'orange', 'red', 'past', 'future', 'present', 'solve', 'zero', 'oracle', 'verbal',
	'best', 'camp', 'heist', 'temptation', 'enthusiastic', 'finger', 'body', 'cast', 'happy'
]

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)

	return word

def hangman():
	word = get_valid_word(words).upper()
	word_letters = set(word.upper())
	alphabet = set(string.ascii_uppercase)
	used_letters = set()

	while len(word_letters) > 0:
		print(f"You have used following letters: {' '.join(used_letters)}")

		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current word: ', ' '.join(word_list))

		user_letter = input('Guess letter:  ').upper()

		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
		elif user_letter in used_letters:
			print(f'You have already used this letter ({user_letter}). Please use another letter.')
		else:
			print('Invalid character. Please try again.')

hangman()