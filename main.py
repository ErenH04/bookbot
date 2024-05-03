def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"{count_words} words found in the document.")

def get_book_text(path):
    with open(path) as f:
        return f.read() 

def count_words(text):
    words = text.split()
    return len(words)

main()