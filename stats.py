def get_num_words(book_text):
	words = str.split(book_text)
	number = len(words)
	print(f"There are {number} words found in the document.")
	return number
def get_num_characters(book_text):
	book_text = book_text.lower()
	from collections import Counter
	Dictionary = Counter(book_text)
	print(Dictionary)
	return Dictionary
def sort_on(items):
	return items["num"]
def order_dictionary(Dictionary):
	Lists = []
	for list in Dictionary:
		new_dict = {"char": list, "num": Dictionary[list]}
		Lists.append(new_dict)
	Lists.sort(reverse=True, key=sort_on)
	return Lists
