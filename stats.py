def get_character_count(file_conntents: str) -> dict[str, int]:
    character_count = {}
    for character in file_conntents:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def get_word_count(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)
