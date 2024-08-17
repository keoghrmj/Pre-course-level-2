def num_obj(s):
    dictionaries = []
    for number in s:
        dictionary = {}
        dictionary[str(number)] = chr(number)
        dictionaries.append(dictionary)
    return dictionaries


print(num_obj([101, 121, 110, 113, 113, 103]))
