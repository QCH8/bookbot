def word_count(file_contents):
    wordcount = file_contents.split()
    return len(wordcount)


def count_characters(file_contents):
    lower_file_contents = file_contents.lower()
    dict_count_characters = {}
    for letter in lower_file_contents:
        if letter in dict_count_characters:
            dict_count_characters[letter] += 1
        else:
            dict_count_characters [letter] = 1
    return dict_count_characters

