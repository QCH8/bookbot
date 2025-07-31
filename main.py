from stats import word_count, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(file_contents)
    print(f"{num_words} words found in the document")

    print(count_characters(file_contents))

main()