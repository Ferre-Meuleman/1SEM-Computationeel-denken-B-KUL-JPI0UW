def get_schone_string (zin: str):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in zin:
        if i not in alphabet:
            zin = zin.replace(i, " ")

    return zin


def main():
    zin = input("Geef een geheime zin in: ")
    zin_clean = get_schone_string(zin)
    print(f"{zin_clean}")


if __name__ == "__main__":
    main()
