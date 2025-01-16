def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return words

def count_character_instances(words):
    character_instances = {}
    for word in words:
        for c in word:
            if c.isalpha():
                if not c in character_instances:
                    character_instances[c] = 1
                else:
                    character_instances[c] += 1
    return character_instances

def dict_to_list_of_tuple(dict):
    output_list = []
    for k in dict:
        output_list.append((k, dict[k]))
    return output_list

def sort_by_second_element(tuple):
    return tuple[1]

def print_count(list):
    for char_num in list:
        print(f"The '{char_num[0]}' character was found {char_num[1]} times")

def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    words = count_words(lowered_text)
    count_dict = count_character_instances(words)
    count_list = dict_to_list_of_tuple(count_dict)
    count_list.sort(reverse=True, key=sort_by_second_element)
    print_count(count_list)
main()