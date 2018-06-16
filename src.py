import sys
def usage():
	"""
	Prints usage
	"""
	print "python src.py [words]"
def is_valid_word(word):
	"""
	returns a bool to test whether a word is 'valid' or not
	criteria:
		len > 2
		shouldn't have anyother character than alphabets
	"""
	if "'" in word or len(word) <= 2:
		return False
	for i in word:
		if not i.isalpha():
			return False
	return True
def build_dict(lang):
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
	
	word = f.readline()
	word = word[:len(word) - 2:]
	word_len = len(word)
	while word:
		if is_valid_word(word):
			if not d.has_key(word_len):
				d[word_len] = []
			d[word_len].append(word.lower())
		word = f.readline()
		word = word[:len(word) - 2:]
		word_len = len(word)
	f.close()
	return d
def is_answer(word1, word2):
	"""
	make a frequency array for the first word for each alphabet
	keep subtracting from there for word2, if any index gets to -1, return 0
	at the end, return 1
	"""
	L = [0 for i in range(26)]
	for i in word1:
		index = ord(i) - 97
		L[index] += 1
	for i in word2:
		index = ord(i) - 97
		if L[index] == 0:
			return 0
		L[index] -= 1
	return 1
	
		
def get_all_possible_words(word_list, word, length):
	"""
	what this does is go through word_list, and returns an iterable object 
	of all possible words in word_list that can be formed from the alphabets of word of length l

	Big question: how?
		1. Iter through word_list
		2. See if the word is the desired length
		3. pass it to a checker function to see if alphabets match, 
			yield and repeat
	"""
	for iterator in (word_list):
		if len(iterator) == length:
			if is_answer(word, iterator):
				yield iterator	

def print_words(list_of_words, length):
	"""
		Formats and prints
	"""
	print str(length) + " letter words"
	count = 0
	for i in list_of_words:
		print i + ", ",
		count += 1
		if count == 5:
			print
			count = 0
	print 
	print

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
	d = build_dict("british")
	word_len = len(word)
	print "All possible combinations for " + word + ": "
	if word_len == 3:
		"""
		passing 3 in our case gets redundant as the word_list contains words only that 
		are 3 alphabets long, but to make the code more re-usable, meh, whatever!
		"""
		word_list = list(set(list(get_all_possible_words(d[3], word, 3))))
		if len(word_list) != 0:
			print_words(word_list, 3)
		return 1
	for counter in range(3, word_len + 1):
		word_list = list(get_all_possible_words(d[counter], word, counter))
		if len(word_list) != 0:
			print_words(word_list, counter)
	print
	return 1
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
		sys.exit(-1)
	for i in sys.argv[1::]:
		main(i)
