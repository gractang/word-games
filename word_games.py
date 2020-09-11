# 3) The game of ghost is played by taking turns
#    with a partner to add a letter to an increasingly
#    long word. The first person to make a valid scrabble word
#    of length 3 or more loses.
#    You must be thinking of a valid word when you name a letter.
#    write a game that implements ghost
#    addendum: write a bot to play ghost against you.

def words_that_could_be(prefix, all_words):
	length = len(prefix)
	possible_words = set()
	for word in all_words:
		if word[:length] == prefix:
			possible_words.add(word)
	return possible_words

'''
assumes that the word itself is not valid
'''
def could_be_valid(prefix, all_words):
	return bool(words_that_could_be(prefix, all_words))

def is_valid(word, all_words):
	if word in all_words:
		return False
	return True

def load_words(filename):
	f = open(filename, "r")
	all_words = set()
	for line in f:
		all_words.add(line.rstrip('\n'))
	return all_words

def play_game(all_words):
	game_over = False
	while not game_over:
		letter = input("enter letter: \n")


def initialize_game():
	all_words = load_words("words.txt")
	reply = input("play ghost? y/n\n")
	if reply == "y":
		play_game(all_words)
	else:
		print("then why'd you run this program?? dumbass")

initialize_game()
