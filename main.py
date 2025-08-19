from stats import get_num_words
from stats import get_char_counts
from stats import print_report
from stats import sort_on

def main():
	
	file_contents = get_book_text()
	num_words = get_num_words(file_contents)
	chars_dict = get_char_counts(file_contents)
	num_words = get_num_words(file_contents)
	#print(chars_dict.items())
	chars = [{"char": char, "num": count} for char, count in chars_dict.items()]
	chars.sort(key=sort_on, reverse=True)
	print(chars)
	print_report(num_words, chars)

def get_book_text():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		return file_contents

if __name__ == "__main__":
	main()
