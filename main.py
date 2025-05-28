from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookpath = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book = get_book_text(bookpath)
    num_words = word_count(book)
    print("----------- Word Count ----------")
    letters = letter_count(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list(letters)
    print("============= END ===============")

main()