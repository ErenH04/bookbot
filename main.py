def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text) 
    num_letters = count_letters(text)
    sort_dict_fun = sort_dict(num_letters)

    print(f"--- begin report of {book_path} ---")
    print(f"{num_words} words found in the document.")
    print()
    
    for item in sort_dict_fun:
        if not item["char"].isalpha():
            continue 
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End Report ---")

def sort_on(d):
    return d["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read() 

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    char = {}
    for c in text:
        lower_case = c.lower()
        if lower_case in char:
            char[lower_case] += 1
        else:
            char[lower_case] = 1
    return char

def sort_dict(num_letters):
    final_ls = []
    for ch in num_letters:
        final_ls.append({"char": ch, "num": num_letters[ch]})
    final_ls.sort(reverse=True, key=sort_on)
    return final_ls       

main()