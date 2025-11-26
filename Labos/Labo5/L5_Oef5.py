from random import randint
import numpy as np


def genereer_matrix():
    matrix = np.random.randint(0, 9, (randint(0, 9), randint(0, 9)))
    return matrix


def toon_matrix(matrix):
    for rows in matrix:
        print(*rows, sep=" ")
    return


def main():
    matrix = genereer_matrix()
    toon_matrix(matrix)


if __name__ == "__main__":
    main()
