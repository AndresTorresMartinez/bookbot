import sys
from stats import count_words, count_characters, sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_content = get_book_text(file_path=file_path)
    num_words = count_words(book_content)
    char_dict = count_characters(book_content)
    sort_chars = sorted_dict(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sort_chars:
        print(f"{dict["char"]}: {dict["num"]}")
    
    
    
    
main()