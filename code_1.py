import json

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        letter_soup = [line.strip().split() for line in lines[:5]]  # La sopa de letras
        words = [line.strip() for line in lines[5:]]  # Las palabras a buscar
    return letter_soup, words

def find_word(letter_soup, word):
    count = 0
    for i in range(len(letter_soup)):
        k = 0
        for j in range(len(letter_soup[i])):
            if count == len(word):
                return True
            elif letter_soup[i][j] == word[k]:
                count += 1
                k += 1
            else:
                count = 0
                k = 0

    for i in range(len(letter_soup)):
        k = 0
        for j in range(len(letter_soup)-1, -1, -1):
            if count == len(word):
                return True
            elif letter_soup[i][j] == word[k]:
                count += 1
                k += 1
            else:
                count = 0
                k = 0

    for i in range(len(letter_soup)):
        k = 0
        m = 0
        while m < len(letter_soup):
            if count == len(word):
                return True
            elif letter_soup[m][i] == word[k]:
                count += 1
                k += 1
            else:
                count = 0
                k = 0
            m += 1

    for i in range(len(letter_soup)):
        k = 0
        for j in range(len(letter_soup[i])-1, -1, -1):
            if count == len(word):
                return True
            elif letter_soup[j][i] == word[k]:
                count += 1
                k += 1
            else:
                count = 0
                k = 0

    m = len(letter_soup) - 1
    for i in range(len(letter_soup)):
        if count == len(word):
            return True
        elif letter_soup[i][m] == word[k]:
            count += 1
            k += 1
        else:
            count = 0
            k = 0
        m -= 1

    m = len(letter_soup) - 1
    for i in range(len(letter_soup)):
        if count == len(word):
            return True
        elif letter_soup[m][i] == word[k]:
            count += 1
            k += 1
        else:
            count = 0
            k = 0
        m -= 1

    for i in range(len(letter_soup)):
        if count == len(word):
            return True
        elif letter_soup[i][i] == word[k]:
            count += 1
            k += 1
        else:
            count = 0
            k = 0

    for i in range(len(letter_soup)-1, -1, -1):
        if count == len(word):
            return True
        elif letter_soup[i][i] == word[k]:
            count += 1
            k += 1
        else:
            count = 0
            k = 0
    return False

def find_words(letter_soup, words):
    result = {}
    for word in words:
        result[word] = find_word(letter_soup, word)
    return result

# Leer datos del archivo
letter_soup, words = read_input('input.txt')

# Buscar palabras y convertir a JSON
result = find_words(letter_soup, words)
print(json.dumps(result, indent=4))
