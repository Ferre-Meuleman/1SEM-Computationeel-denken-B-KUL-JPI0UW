import pickle 

volledige_inhoud = ""

with open("pi.txt", "r") as f:
    volledige_inhoud = f.read()

with open("onleesbaar.pkl", "wb") as f:
    pickle.dump(volledige_inhoud, f)
    
with open("onleesbaar.pkl", "rb") as f:
    inhoud = pickle.load(f)
    print(inhoud)

