# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import collections
import string

def read_f(file):
    with open(file) as f:
        words = f.read()
    return words


def freq(words):
    freq = [0] * 26

    for c in words:
        freq[ord(c) - ord('A')] += 1

    total = sum(freq)

    for i in range(0, len(freq)):
        freq[i] /= (float(total) / 100)

    return freq


def translate(filename):
    answer = ""
    words = read_f(filename)
    translation = freq(words)
    caesar_dictionary = {word[0]: word[1:] for word in translation}

    for letter in words:
        if letter not in caesar_dictionary:
            answer += letter
        else:
            answer += caesar_dictionary[letter][0]
    return answer


if __name__ == '__main__':
    print(translate('/Users/julie/Desktop/computer_science/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt'))