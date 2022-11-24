opties = ["Frietjes","Pizza","Kebab"]
print("kies uit volgende opties a b c",opties)
keuze = input("")
aantal_keuzes =[0,0,0]
while(keuze != "stop"):
    if keuze.lower() == "a":
        aantal_keuzes[0] += 1
    elif keuze.lower() == "b":
        aantal_keuzes[1] += 1
    elif keuze.lower() == "c":
        aantal_keuzes[2] += 1
    else:
        print("Foutieve invoer")
    keuze = input("geef je keuze")
print(opties)
print(aantal_keuzes, end="\t")
