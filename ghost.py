from string import ascii_uppercase
# 3) The game of ghost is played by taking turns
#    with a partner to add a letter to an increasingly
#    long word. The first person to make a valid scrabble word
#    of length 3 or more loses.
#    You must be thinking of a valid word when you name a letter.
#    write a game that implements ghost
#    addendum: write a bot to play ghost against you.

'''
notes to self: bot wants word to be odd letters (num turns even if zero indexing)
for each starting letter, build list of words with odd letters


'''

# preprocesses words so that the new list contains only the shortest words
def preprocess(all_words):
	reduced = set()
	for word in all_words:
		is_shortest = True
		for index in range(len(word)):
			if word[:index] in all_words:
				is_shortest = False
				break
		if is_shortest:
			reduced.add(word)
	return reduced

# returns set of all possible words starting with prefix
def words_that_could_be(prefix, all_words):
	length = len(prefix)
	possible_words = set()
	for word in all_words:
		if word[:length] == prefix:
			possible_words.add(word)
	return possible_words

# builds a dictionary with the starting prefix, and length of all options from there
def get_possibilities(prefix, all_words):
	dictionary = {}
	for c in ascii_uppercase:
		dictionary[c] = set()
		for word in all_words:
			if word.startswith(prefix+c):
				#print(word)
				dictionary[c].add(len(word))
	return dictionary



'''
assumes that the word itself is not valid
'''
def could_be_valid(prefix, all_words):
	return bool(words_that_could_be(prefix, all_words))

# checks if word is a valid scrabble word
def is_valid(word, all_words):
	if word in all_words:
		return True
	return False

# loads words from file into a set
def load_words(filename):
	f = open(filename, "r")
	all_words = set()
	for line in f:
		all_words.add(line.rstrip('\n'))
	return preprocess(all_words)

# bad bot, does it randomly
def reply(prefix, all_words):
	words = words_that_could_be(prefix, all_words)
	if words:
		for w in words:
			return w[len(prefix)]
	return words

# works with the dumb "bot"
def play_game(all_words):
	print(len(all_words))
	for c in ascii_uppercase:
		print(c + ": ")
		print(get_possibilities(c, all_words))
		print("------------------")
	
	game_over = True
	word = ""

	while not game_over:
		letter = input("enter uppercase letter: \n")
		while letter.islower():
			letter = input("uppercase please... \n")
		word += letter.upper()
		if is_valid(word, all_words):
			print("you lose lmao. word: " + word + "\n")
			game_over = True
			break
		bot_letter = reply(word, all_words)
		if bot_letter:
			print(bot_letter)
			word += bot_letter.upper()
		else:
			print("bruh that aint a word. you lose. dont try me\n")
			game_over = True
			break

def initialize_game():
	all_words = load_words("words.txt")
	reply = input("play ghost? y/n\n")
	if reply == "y":
		play_game(all_words)
	else:
		print("then why'd you run this program?? dumbass")

initialize_game()
