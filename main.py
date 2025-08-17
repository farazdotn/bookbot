from stats import get_word_count
from stats import get_char_count
from stats import sort_order
import re
import sys 

def main():
    if not ((len(sys.argv)) == 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    my_text = get_book_text(sys.argv[1])
    print(
f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_word_count(my_text)} total words
--------- Character Count -------"""
    )
    the_beautiful_dict = sort_order(get_char_count(my_text))
    for char in the_beautiful_dict:
        print(f"{char}: {the_beautiful_dict[char]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as t:
        t = t.read()
        return t
    

main()