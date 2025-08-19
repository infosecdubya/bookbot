def get_num_words(file_contents):
	num_words = len(file_contents.split())
	#print(f"Found {num_words} total words")
	return num_words

def get_char_counts(file_contents):
	chars_dict = {}
	for char in file_contents:
		char = char.lower()
		if char in chars_dict:
			chars_dict[char] += 1
		else:
			chars_dict[char] = 1
	return chars_dict

def sort_on(chars_dict):
	return chars_dict["num"]

def print_report(num_words, chars):
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for bleh in chars:
		print(f"{bleh["char"]}: {bleh["num"]}")