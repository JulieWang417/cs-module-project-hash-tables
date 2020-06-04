# Your code here

def replace_special(main, replaced, new_words):
    for elem in replaced:
        if elem in main:
            main = main.replace(elem, new_words)
    return main


def process_input(file):
    specials = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '!', '?']
    with open(file) as f:
        words = f.read()
        words = replace_special(words, specials, '')
        words = words.lower()
        words = words.split()
        words = sorted(words)
    return words


def histogram(file):
    words = process_input(file)
    dictionary = {}

    for word in words:
        if word in dictionary:
            dictionary[word] += '#'
        else:
            dictionary[word] = '#'

    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def print_histogram(dictionary):
    max_len = 0
    for item in dictionary:
        max_len = len(item[0]) if len(item[0]) > max_len else max_len

    for item in dictionary:
        result = ''
        result += item[0]
        for i in range(max_len - len(item[0]) + 2):
            result += ' '
        result += item[1]
        print(result)


if __name__ == '__main__':
    sorted_list = histogram('robin.txt')
    print_histogram(sorted_list)