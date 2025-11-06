

def decoder ( geheim:str , sleutel:str ):
    decoded = ""
    for i in geheim:
        if i in sleutel:
            decoded += sleutel[i]
        else:
            decoded += i
    return decoded

def encoder( geheim:str , sleutel:str ):
    encoded = ""
    for i in geheim:
        if i in sleutel.values():
            for key, value in sleutel.items():
                if i == value:
                    encoded += key
                    break
        else:
            encoded += i
    return encoded


def main():
    sleutel = { 
    '&' : 'n' , 
    '@' : 'a' , 
    '€' : 'e' , 
    '0' : 'o' , 
    '!' : 'i', 
    'g' : 'd' , 
    'd' : 'g' , 
    'H' : 'f' , 
    'w' : 'b' 
}   
    zin = "k0HH!€ !s wl!jkw@@r h€t €cht€ vl0€!w@r€ d0ug"
    zin_clean = decoder(zin, sleutel)
    print(f"{zin_clean}")

    zin = input("Geef een zin in om te coderen: ")
    zin_encoded = encoder(zin, sleutel)
    print(f"{zin_encoded}")

if __name__ == "__main__":
    main()
