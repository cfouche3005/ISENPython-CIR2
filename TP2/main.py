capital = float(input("entrer le capital : "))
duree = int(input("entrer le duree : "))
taux = float(input("entrer le taux : "))/100

def mensualité(capital,duree,taux):
    return (capital*((taux)/12))/(1-pow(1+((taux)/12), -duree))
def emprint(capital,duree,taux):
    output=[]
    reste = capital
    print(reste)
    interet_cum = 0
    for i in range(duree):
        interet_mois = reste*(taux/12)
        interet_cum = interet_cum + interet_mois
        reste = reste - mensualité(capital,duree,taux) + interet_mois
        output.append([round(max(0,reste),2), round(interet_cum,2), round(interet_mois,2)])
    return output


print(emprint(capital,duree,taux))