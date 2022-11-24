import math
"""def inhoud_c_liter(straal,hoogte,procent):
    if procent>0 and procent<101:
        return (straal*straal*hoogte*math.pi*1000)/100*procent
    else:
        return "Foutieve ingave"

aantal_liter = inhoud_c_liter(1,1,200)
print(aantal_liter)
"""

"""def procentstijging(oud,nieuw):
    return (nieuw-oud)/oud*100

print(procentstijging(15000,50000))"""

lijst = [8,5,12,5,3,4,7,15,8,3,1,2,3]
lijst.sort(reverse=True)
for i in range(0,3):
    print(lijst[i])
