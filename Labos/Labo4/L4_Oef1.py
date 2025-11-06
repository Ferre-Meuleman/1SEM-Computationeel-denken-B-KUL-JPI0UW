def gemeenschappelijke_letters(woord_1: str, woord_2: str):
    lettersword1 = set(woord_1)
    lettersword2 = set(woord_2)
    letters = ""
    for (letter) in lettersword1:
        if letter in lettersword2:
            letters += " " + letter
    return letters


def main():
    word1 = input("Geef het eerste woord: ")
    word2 = input("Geef het tweede woord: ")
    letters = gemeenschappelijke_letters(word1, word2)
    print(f"De gemeenschappelijke letters zijn:{letters}")


if __name__ == "__main__":
    main()
