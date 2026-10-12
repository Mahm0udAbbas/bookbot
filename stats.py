def get_words_count(text:str) -> int:
    words_count = len(text.split())
    return words_count

def get_num_chars(text:str)-> dict[str , int]:
    chars = {"a": 0}
    for char in text:
        lower_char = char.lower()
        if lower_char not in chars:
            chars[lower_char] = 1
        else:    
            chars[lower_char] += 1
    return chars


def sort_on(char:tuple[str, int]) -> int:
    return char[1]


def chars_dict_to_sorted_list(chars: dict[str , int])-> list[tuple[str , int]]:
    new_list = []
    for char , num in chars.items():
        new_list.append((char , num))
    sorded_list = sorted(new_list , reverse=True , key=sort_on)    
    return sorded_list


def print_report(book_path:str , words_count:int , sorted_list:list[tuple[str , int]])-> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print("Found {words_count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
