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

def sort_character_count(character_count):
    characters = []
    for key in character_count:
        dict_entry = {"char": key, "count": character_count[key]}
        characters.append(dict_entry)
    #print(unsorted_characters)
    # list.sort() sorts in-place and returns None, so call it and then
    # return the list itself. Sort by 'count' (highest first).
    characters.sort(key=lambda x: x['count'], reverse=True)
    return characters
