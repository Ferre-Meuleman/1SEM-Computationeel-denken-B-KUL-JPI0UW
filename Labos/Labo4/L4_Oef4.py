def splits_woord(dier: str):
    klinkers = "aeiouAEIOU"
    prefix = ""
    suffix = ""
    for i in range(len(dier)):
        if dier[i] in klinkers:
            prefix = dier[:i]
            suffix = dier[i:]
            break
    return {'prefix': prefix, 'suffix': suffix}

def nieuwe_kruising(dier_1: str, dier_2: str):
    dier1_gesplitst = splits_woord(dier_1)
    dier2_gesplitst = splits_woord(dier_2)
    nieuwe_naam = dier1_gesplitst['prefix'] + dier2_gesplitst['suffix']
    return nieuwe_naam


def main():
    dier_1 = input("Geef een eerste dier: ")
    dier_2 = input("Geef een tweede dier: ")
    nieuwe_dier = nieuwe_kruising(dier_1, dier_2)
    print(f"De naam van het nieuwe nageslacht is: {nieuwe_dier}")

if __name__ == "__main__":
    main()
