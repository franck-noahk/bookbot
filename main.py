from stats import get_word_count, get_book_text, get_character_count, sort_dict_characters
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_word_count(get_book_text(path))
    word_count = "Found " + str(word_count) + " total words"
    characters = get_character_count(
        get_book_text(path).lower())
    display_character = sort_dict_characters(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")
    print(word_count)
    print("--------- Character Count -------")
    for entry in display_character:
        print(str(entry["char"]) + ": " + str(entry["num"]))
    print("============= END ===============")


if __name__ == "__main__":
    main()
