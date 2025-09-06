import sys
if len(sys.argv) < 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = ""
		file_contents = f.read()
		book_text = file_contents
	return book_text
book_text = get_book_text(sys.argv[1])
from stats import get_num_words
from stats import get_num_characters
from stats import order_dictionary
word_count = get_num_words(book_text)
Dictionary = get_num_characters(book_text)
Ordered_Dictionary = order_dictionary(Dictionary)
print ("============ BOOKBOT ============")
print (f"Analyzing book found at {sys.argv[1]}...")
print ("----------- Word Count ----------")
print (f"Found {word_count} total words")
print ("--------- Character Count -------")
for pair in Ordered_Dictionary:
	if pair["char"].isalpha():
		print (f"{pair['char']}: {pair['num']}")
print ("============= END ===============")
