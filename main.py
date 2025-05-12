
import sys
from stats import get_num_words, get_character_stats, sorted_character_stats

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        book_contents = f.read()
        return book_contents

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    total_book_text = get_book_text(path_to_book)
    get_num_words(total_book_text)
    unsorted_dict = get_character_stats(total_book_text)
    sorted_dict = sorted_character_stats(unsorted_dict)
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")