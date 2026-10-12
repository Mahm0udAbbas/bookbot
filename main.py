import sys
from stats import get_words_count , get_num_chars ,chars_dict_to_sorted_list ,print_report

def main() -> None:
   
    book_path = sys.argv[1]
    print(book_path)
    text = get_book_text(book_path)
    num_words = get_words_count(text)
    num_chars = get_num_chars(text)

    sorted_list = chars_dict_to_sorted_list(num_chars)
    print(f"Found {num_words} total words")
    # print(num_chars)
    print_report(book_path ,num_words ,sorted_list)




def get_book_text(file_path : str)-> str:
    with open(file_path) as f:
        file_content = f.read()    
    return file_content


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:     
    main() 