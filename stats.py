def word_count(book):
    lst = book.split()
    return len(lst)

def letter_count(book):
    letters = {}
    for char in book.lower():
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters

def sort_on(dict):
    return dict["num"]

def sorted_list(input_data):
    new_dict = []
    for key, value in input_data.items():
        new_item = {"char": key, "num": value}
        
        new_dict.append(new_item)

    new_dict.sort(reverse=True, key=sort_on)
    for item_dict in new_dict:
        character = item_dict["char"]
        number = item_dict["num"]
        if character.isalpha():
            print(f"{character}: {number}")