def inlezen_lijst() -> list:
    numbers = []
    while True:
        numinput = input("Give next number: ")
        if numinput != "":
            numbers.append(int(numinput))
        else:
            break

    return numbers


def bepaal_gemiddelde(lijst) -> float:
    gemiddelde = sum(lijst)/len(lijst)
    return gemiddelde


def toon_lijst(lijst):
    print(*lijst, sep=", ")
    return


def main():
    lijst = []
    lijst = inlezen_lijst()
    gemiddelde = bepaal_gemiddelde(lijst)
    print(f"Gemiddelde van volgende lijst is {gemiddelde}")
    toon_lijst(lijst)


if __name__ == "__main__":
    main()
