def word_count(text):
    num_words = len(text.split())
    return num_words

def get_character_count(text):
    num_characters = {
    }
    lowered_text = text.lower()
    for char in lowered_text:
        num_characters[char] += 1
    return num_characters