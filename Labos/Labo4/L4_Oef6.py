"""chrijf een functie decoder ( tekening , teken )  
die twee keer een string als argument krijgt: een gecodeerde 
tekening en een karakter waarmee de tekening kan ontcijferd 
worden.  
De functie geeft de originele tekening terug. 
 
Elke lijn in de gecodeerde tekening is als volgt gecodeerd: 
 
Gecodeerde lijn :   456789#123 
 
Je decodeert elke lijn in de tekening door de regel te splitsen aan het 
teken (#) en het eerste deel te wisselen met het tweede deel. 
 
De originele lijn was dus : 123456789   
"""



def decoder( tekening , teken ):
    lijnen = tekening.splitlines()
    originele_lijnen = []
    for lijn in lijnen:
        delen = lijn.split(teken)
        if len(delen) == 2:
            originele_lijn = delen[1] + delen[0]
        else:
            originele_lijn = lijn  # In case there's no split, keep the line as is
        originele_lijnen.append(originele_lijn)
    originele_tekening = "\n".join(originele_lijnen)
    return originele_tekening

def main():
    file = open("./tekening3.txt", "r")
    gecodeerde_tekening = file.read()
    print("Gecodeerde tekening:")
    print(decoder(gecodeerde_tekening, "#"))
    
if __name__ == "__main__":
    main()