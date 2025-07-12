from stats import get_word_count, get_book_text, get_character_count
if __name__ == "__main__":
    word_count = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(str(word_count) + " words found in the document")

    print(get_character_count(get_book_text("./books/frankenstein.txt").lower()))
