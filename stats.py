def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return(len(words))

def count_occurance(text):
    text_lc = text.lower()
    occurance = {}

    for ch in text_lc:
        if ch in occurance:
            occurance[ch] += 1
        else:
            occurance[ch] = 1
    return occurance


def sort_dict(dict):
    list_of_dicts = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True,key=return_num)

    return list_of_dicts

def return_num(dict):
    return dict["num"]

