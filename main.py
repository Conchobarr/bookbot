from stats import word_count, get_character_count, sort_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    num_characters = get_character_count(book)
    print(f"Found {word_count(book)} total words")
    #print(num_characters)
    print(sort_character_count(num_characters))

main()