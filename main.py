from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = word_count(file_contents)

    char_list = cleaning_dictionary(count_characters(file_contents))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()