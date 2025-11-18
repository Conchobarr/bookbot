def word_count(text):
    num_words = len(text.split())
    return num_words

def get_character_count(text):
    num_characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char not in num_characters:
            num_characters[f'{char}'] = 1
        else:
            num_characters[f'{char}'] += 1
        
    return num_characters