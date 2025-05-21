def count_words(text):
    num_words = text.split()
    return len(num_words)

def count_characters(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_dict(dict):
    values_list = []
    for key, value in dict.items():
        if key.isalpha():
            values_list.append({"char": key, "num": value})
    
    def sort_par(dict):
        return dict["num"]
    
    values_list.sort(reverse=True, key=sort_par)
    
    return values_list