from math import sqrt

def bereken_functiewaarde (x: float):
    value = round(sqrt(x) -1,1)
    return value

def toon_lijst(lijst):
    print(*lijst, sep="  ")
    return

def main():
    ONDERWAARDE = 2
    BOVENWAARDE = 6
    OPDELING = 10

    differnce = BOVENWAARDE - ONDERWAARDE
    step = differnce/OPDELING

    lijstx = []
    lijsty = []
    for i in range(OPDELING):
        newnum = ONDERWAARDE + i * step
        lijstx.append(round(newnum,1)) 
        lijsty.append(bereken_functiewaarde(newnum))

    
    toon_lijst(lijstx)
    toon_lijst(lijsty)

if __name__ == "__main__":
    main()