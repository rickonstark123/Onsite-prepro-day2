"""python"""

def main():
    """python"""
    txt = input()
    for i in txt:
        letter = ord(i)
        if i.isupper():
            print(chr(90-(letter-65)), end="")
        elif i.islower():
            print(chr(122-(letter-97)), end="")
        else:
            print(i, end="")
main()
