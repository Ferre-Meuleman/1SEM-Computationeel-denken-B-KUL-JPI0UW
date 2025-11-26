from random import randint
import numpy as np


def genereer_matrix():

    matrix = np.random.randint(0, 9, (3, 3))
    return matrix


def toon_matrix(matrix):
    for rows in matrix:
        print(*rows, sep=" ")
    return


def transponeer_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            transposed[y][x] = matrix[x][y]

    return transposed


def spiegel_matrix_horizontaal(natrix):
    rows = len(natrix)
    cols = len(natrix[0])

    mirrored = [[0 for _ in range(cols)] for _ in range(rows)]

    for x in range(len(natrix)):
        for y in range(len(natrix[0])):
            mirrored[x][cols - y - 1] = natrix[x][y]

    return mirrored


def roteer_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rotated = [[0 for _ in range(rows)] for _ in range(cols)]

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            rotated[y][rows - x - 1] = matrix[x][y]

    return rotated


def toon_opties():

    keuze = ""
    geldige_keuzes = ["T", "H", "R", "S"]

    while keuze not in geldige_keuzes:

        keuze = input("maak uw keuze : \n"
                      "T \t ( transponeren ) \n"
                      "H \t ( voor horizontaal spiegelen ) \n"
                      "R \t ( voor roteren) \n"
                      "S \t ( stop ) \n"
                      )
        if keuze not in geldige_keuzes:
            print("ongeldige invoer")

    return keuze


def main():
    coise = toon_opties()

    matrix = genereer_matrix()
    toon_matrix(matrix)

    match coise:
        case "T":
            transposed = transponeer_matrix(matrix)
            print("transposed:")
            toon_matrix(transposed)

        case "H":
            mirrored = spiegel_matrix_horizontaal(matrix)
            print("mirrored:")
            toon_matrix(mirrored)

        case "R":
            rotated = roteer_matrix(matrix)
            print("rotated:")
            toon_matrix(rotated)

        case "S":
            quit()


if __name__ == "__main__":
    main()
