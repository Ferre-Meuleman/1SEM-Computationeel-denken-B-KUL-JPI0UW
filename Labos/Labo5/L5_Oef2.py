def toon_lijst(lijst):
    print(*lijst, sep=", ")
    return

def main():
    ONDERWAARDE = 2
    BOVENWAARDE = 6
    OPDELING = 10

    differnce = BOVENWAARDE - ONDERWAARDE
    step = differnce/OPDELING

    lijst = []
    for i in range(OPDELING):
        newnum = round(ONDERWAARDE + i * step,1)
        lijst.append(newnum) 
    
    toon_lijst(lijst)

if __name__ == "__main__":
    main()