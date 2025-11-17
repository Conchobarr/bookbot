from stats import word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    print(f"Found {word_count(get_book_text(file_path))} total words")



main()