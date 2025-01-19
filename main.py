def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_chars = sort_char_dict(char_dict)

    print(f"--- Report of {book_path} ---")
    print(f"This book contains: {word_count} words")

    for character in sorted_chars:
        if character[0].isalpha():
            print(f"The {character[0]} appears {character[1]} times")

    print(f"---End of Report---")

def get_book_text(path_of_book):
    with open(path_of_book) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    for letter in text:
        lowercased = letter.lower()
        if lowercased in character_dict:
            character_dict[lowercased] += 1
        else:
            character_dict[lowercased] = 1
    return character_dict

def sort_char_dict(char_count_dict):
    characters = list(char_count_dict.items())
    sorted_char_list = sorted(characters, key=lambda x: x[1], reverse=True)
    return sorted_char_list

main()