def get_num_words(book_string):
    all_words = book_string.split()
    print("----------- Word Count ----------")
    print(f"Found {len(all_words)} total words")

def get_character_stats(book_string):
    all_characters = list(book_string.lower())

    character_dict = {}

    for character in all_characters:
        if character not in character_dict.keys():
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict

def sorted_character_stats(character_dict):
    character_list = []
    for key, value in character_dict.items():
        character_list.append({"char": key, "num": value})

    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(dict):
    return dict["num"]