def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_each_letter(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    sorted_letters = sort_letter_count(letter_count)
    for char in sorted_letters:
        if not char['letter'].isalpha():
            continue
        print(f"{char['letter']} : {char['num']}")

    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
   
def count_words(text):
    return len(text.split())

def count_each_letter(text):
    lowercase_text = text.lower()
    letter_count = {}
    for letter in lowercase_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_letter_count(letter_count):
    sorted_list = []
    for ch in letter_count:
        sorted_list.append({"letter": ch, "num": letter_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
