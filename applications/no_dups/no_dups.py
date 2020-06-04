def no_dups(s):
    # Python dictionary method fromkeys() creates a new dictionary with keys from seq and values set to value.
    # for example seq = ('name', 'age', 'sex')
    # dict = dict.fromkeys(seq)
    # return dict : {'age': None, 'name': None, 'sex': None}
    s = s.split()
    s = list(dict.fromkeys(s))
    s = " ".join(s)
    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))