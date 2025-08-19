from stats import get_num_words
from stats import get_char_counts
from stats import print_report
from stats import sort_on
import sys

def main():
	book = sys.argv[1] if len(sys.argv) > 1 else print("Usage: python3 main.py <path_to_book>") & sys.exit(1)
	file_contents = get_book_text(book)
	num_words = get_num_words(file_contents)
	chars_dict = get_char_counts(file_contents)
	num_words = get_num_words(file_contents)
	#print(chars_dict.items())
	chars = [{"char": char, "num": count} for char, count in chars_dict.items()]
	chars.sort(key=sort_on, reverse=True)
	print(chars)
	print_report(num_words, chars, book)

def get_book_text(book):
	with open(f"{book}") as f:
		file_contents = f.read()
		return file_contents

if __name__ == "__main__":
	main()
