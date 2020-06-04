
specials = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

# definition for replacing a string
def replace_special(string, toBeReplaces):
    for e in toBeReplaces:
        if e in string:
            string = string.replace(e, '')
    return string


def word_count(s):
    count = {}
    new_s = replace_special(s, specials)
    new_s = new_s.split()
    for i in range(len(new_s)):
        new_s[i] = new_s[i].lower()
        if new_s[i] in count:
            count[new_s[i]] += 1
        elif new_s[i] != '':
            count[new_s[i]] = 1
    return count
        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))