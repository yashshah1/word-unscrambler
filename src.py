import sys
def usage():
	"""
	Prints usage
	"""
	print "python src.py <word>"
def is_valid_word(word):
	"""
	returns a bool to test whether a word is 'valid' or not
	criteria:
		len > 2
		shouldn't have anyother character than alphabets
	"""
	if "'" in word or len(word) <= 2:
		return 0
	for i in word:
		if not i.isalpha():
			return 0
	return 1
def builddict(lang):
	"""
	rudimentary implemenatation, needs work
	works only for british at the moment, should change when we add
	more wordlists.

	creates and returns a python dict(hash) after reading from a wordlist
	file, where the key is the length of the word, and the value is an array
	containing all the `valid` words of that length
	
	calls is_valid_word()
	"""
	d = dict()
	try:
		f = open("./wordlists/" + lang, "r")
	except IOError:
		print "Invalid wordlist"
		sys.exit(-2)
	
	word = f.readline().strip()
	word_len = len(word)
	while word:
		if is_valid_word(word):
			if not d.has_key(word_len):
				d[word_len] = []
			d[word_len].append(word.lower())
		word = f.readline().strip()
	f.close()
	return d
def get_all_possible_words(word_list, word, length):
	"""
	what this does is go through word_list, and returns an iterable object 
	of all possible words in word_list that can be formed from the alphabets of word of length l

	Big question: how?
	"""
	
def main(word):
	"""
	Main function()
		1. Builds the dict with the language, currently hard coded
		2. prints all possible words!
			2.1 iters through all the possible word lengths and does the 
				following two steps for all the possible words
			2.2 gets all possible words by calling get_all_possible_words()
			2.3 passes to a print function that makes it readable
	"""
	d = builddict("british")
	word_len = len(word)
	
	if word_len == 3:
		"""
		passing 3 in our case gets redundant as the word_list contains words only that 
		are 3 alphabets long, but to make the code more re-usable, meh, whatever!
		"""
		L = get_all_possible_words(d[3], word, 3)
		print_words(L, 3)
		return 1
	for counter in range(3, word_len + 1):
		L = get_all_possible_words(d[counter], word, counter)
		print_words(L, counter)
	return 1
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()
		sys.exit(-1)
	main(sys.argv.pop(1))
