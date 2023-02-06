from mesonbuild.mlog import green

villes = {
    "Pierre": "Nantes",
    "Marie": "Brest",
    "Paul": "Nantes",
    "Nathalie": "Nantes",
    "Jean": "Brest",
    "Isabelle": "Brest",
    "Nicolas": "Rennes"
}

def lieu_habitations(nom_personne, villes):
    return villes[nom_personne] if nom_personne in villes else "?"

print( lieu_habitations("Marie", villes))
print( lieu_habitations("Toto", villes))

def nom_personne(nom_villes,  villes):
    out = []
    for ville in villes.items():
        if ville[1]==nom_villes :
            out.append(ville[0])
    return out

print( nom_personne("Rennes", villes))
print( nom_personne("Quimper", villes))
print( nom_personne("Brest", villes))

def occurrences_lettres(mot) :
    out = {}
    for letter in mot:
        if letter in out:
            out[letter] += 1
        else :
            out[letter] = 1
    return out

print( occurrences_lettres("ANTICONSTITUTIONNELLEMENT"))

trad_en_de = {"red": "rot", "green": "grün", "blue": "blau", "yellow": "gelb"}
trad_en_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}

def creer_trad_en_fr(trad_en_de,trad_en_fr) :
    out={}
    for word in trad_en_de.keys():
        out[word] = trad_en_fr[trad_en_de[word]]
    return out

print( creer_trad_en_fr(trad_en_de,trad_en_fr))

points_lettres = {
1 : ["E", "A", "I", "N", "O", "R", "S", "T", "U", "L"],
2 : ["D", "M", "G"],
3 : ["B", "C", "P"],
4 : ["F", "H", "V"],
8 : ["J", "Q"],
10 : ["K", "W", "X", "Y", "Z"]
}

def creer_lettres_points(points_lettres):
    out = {}
    for point in points_lettres :
          for letter in points_lettres[point] :
              out[letter] = point
    return out

print( creer_lettres_points(points_lettres))

def calculer_score(mot, points_lettres) :
    lettres_points = creer_lettres_points(points_lettres)
    out = 0
    for letter in mot:
        out += lettres_points[letter]
    return out

print( calculer_score("POMME", points_lettres) )
print( calculer_score("JUKEBOX", points_lettres) )