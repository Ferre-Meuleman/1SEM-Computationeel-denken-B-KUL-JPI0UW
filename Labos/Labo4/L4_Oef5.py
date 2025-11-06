puntenlijst = [ 
    { 
        "naam" : "Jan" , 
        "familienaam" : "Janssen" , 
        "score" : 15 , 
    }, 
    { 
        "naam" : "William" , 
        "familienaam" : "Williamson ", 
        "score" : 6 , 
    }, 
    { 
        "naam" : "Bill" , 
        "familienaam" : "Beaux" , 
        "score" : 11 , 
    }, 
    { 
        "naam" : "Amy" , 
        "familienaam" : "Stake" , 
        "score" : 19 , 
    }, 
 
    { 
        "naam" : "Miss" , 
        "familienaam" : "Chin" , 
        "score" : None , 
    } 
] 
 
boodschap = { 
   0 :   ["Edde gij gestudeerd? " , "Je bent niet geslaagd." ], 
   10 :   ["Geslaagd, " , "Met de hakken over de sloot." ], 
   14 :   ["Proficiat, " , "Doe zo verder!" ], 
   18 :   ["Uitmuntend, " , "Heel goed gedaan!" ], 
    None :  ["Beste " , "Maak een afspraak om de test in te halen." ] 
}

def main():
    for student in puntenlijst:
        score = student["score"]
        naam = student["naam"]
        familienaam = student["familienaam"]
        
        if score is None:
            boodschap_key = None
        elif score < 10:
            boodschap_key = 0
        elif score < 14:
            boodschap_key = 10
        elif score < 18:
            boodschap_key = 14
        else:
            boodschap_key = 18
        
        aanhef, bericht = boodschap[boodschap_key]
        print(f"{aanhef}{naam} {familienaam}, {bericht} Jouw score is {score} op 20.")
        
if __name__ == "__main__":
    main()