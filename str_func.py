def input_string(value):
    return value.upper()


def input_string_2(value):
    """
    Функция делает заглавными первые
    буквы каждого слова в строке
    """
    words = value.split()
    words_2 = []
    for word in words:
        words_2.append(word.capitalize())
    return " ".join(words_2)



