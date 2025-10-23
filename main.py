from stats import get_book_text
from stats import count_words
from stats import count_occurance
from stats import sort_dict
from stats import return_num
import sys

def main():
    
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    char_count = count_occurance(text)
    sorted_char_count = sort_dict(char_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(sorted_char_count)
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue
    print("============= END ===============")

    
    
        

    
main()