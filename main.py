import sys

from stats import word_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = read_book(book_path)
    words = word_count(text)
    letters = letter_count(text)
    letters_list = dict_to_list(letters)
    letters_list.sort(reverse=True, key=sort_on)
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------"""
    )



    for items in letters_list:
        print(f"{items['char']}: {items['num']}")
    print("============= END ===============")


def sort_on(dict):
    return dict["num"]


def dict_to_list(letters):
    dict_letters = []
    for letter in letters:
        if letter.isalpha():
            dict_letters.append({"char": letter, "num": letters[letter]})
    return dict_letters


def read_book(path):
    with open(path) as f:
        return f.read()


def letter_count(text):
    text_lower = text.lower()
    letters = {}
    for letter in text_lower:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()
