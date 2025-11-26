from random import randint
import numpy as np


def genereer_matrix():

    matrix = np.random.randint(0, 9, (3,3))
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
             

def main():
    matrix = genereer_matrix()
    toon_matrix(matrix)
    transposed = transponeer_matrix(matrix)
    print("transposed:")
    toon_matrix(transposed)


if __name__ == "__main__":
    main()
