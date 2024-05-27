def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = word_count(text)
    letters = letter_count(text)
    letters_list = dict_to_list(letters)
    letters_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for items in letters_list:
        print(f"The '{items["char"]}' character was found {items["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def dict_to_list(letters):
    dict_letters = []
    for letter in letters:
        if(letter.isalpha()):
            dict_letters.append({"char": letter, "num": letters[letter]})
    return dict_letters

def read_book(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text_lower = text.lower()
    letters = {}
    for letter in text_lower:
        if(letter in letters):
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
        
main()