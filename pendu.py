# -*-coding:Latin-1 -*

from fonctions import *

""" Jeu du Pendu """

# les scores des joueurs
scores = charger_scores()
print(scores)

# Récupere les données depuis le fichier
chances, liste_mots = lire_donnees()

# le nom du joueur
nom = demander_nom()
print("")

#jouer()
#while rejouer():
#    jouer()
#quitter(scores)

while rejouer():
    # Choisi un mot au hasard parmis la liste de mots
    mot = choisir_mot(liste_mots).upper()
    # mot que le joueur doit trouver
    mot_a_trouver = cacher_mot(mot)
    # le score du joueur
    score = chances
    
    #i = chances
    # tant que le mot n'est pas trouvé et qu'il reste au moins une chance de rejouer
    while score > 0 and not trouve(mot_a_trouver):
        print("Quel est ce mot : {} ".format(mot_a_trouver))
        lettre = choisir_lettre()
        while mot.count(lettre) > 0:
            indice = mot.find(lettre)
            mot_a_trouver = remplacer_lettre(mot_a_trouver, lettre, indice)
            mot = remplacer_lettre(mot, "*", indice)
        score -= 1
        # i -= 1
    mise_a_jour(scores, nom, score)
    
quitter(scores)
print(scores)
