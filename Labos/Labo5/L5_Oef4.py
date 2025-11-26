import matplotlib.pyplot as plt
import math


def bereken_functiewaarde(x: float):
    value = math.sin(x)
    return value


def toon_lijst(lijst):
    print(*lijst, sep="  ")
    return


def main():
    ONDERWAARDE = -4 * math.pi
    BOVENWAARDE = 4 * math.pi
    OPDELING = 100

    differnce = BOVENWAARDE - ONDERWAARDE
    step = differnce/OPDELING

    lijstx = []
    lijsty = []
    for i in range(OPDELING):
        newnum = ONDERWAARDE + i * step
        lijstx.append(newnum)
        lijsty.append(bereken_functiewaarde(newnum))

    plt.plot(lijstx, lijsty)
    plt.show()


if __name__ == "__main__":
    main()
