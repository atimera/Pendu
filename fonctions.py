# -*-coding:Latin-1 -*

import os
import pickle
import random




def sauvegarder(scores):
    """ Enregistre les scores dans un fichier scores """
    if type(scores) is not dict:
        print("le parametre doit etre un dictionnaire")
    else:
        with open("scores", "wb") as fichier:
            pick = pickle.Pickler(fichier)
            pick.dump(scores)


def charger_scores():
    """  Utiliser pour charger les scores depuis un fichier """
    try:
        with open("scores", "rb") as fichier:
            pick = pickle.Unpickler(fichier)
            scores = pick.load()
    except FileNotFoundError:
        print("Le fichier scores n'est pas trouvé")
        scores = dict()
    return scores
        

def mise_a_jour(scores, nom, score):
    """ met à jour le dictionnaire des scores aprés chaque tour de jeux """
    if not(est_deja_joueur(nom,scores)):
        scores[nom] = score
    else:
        scores[nom] += score
    


def lire_donnees():
    """ Charge les données (nombre de chance et liste de nots) depuis un fichier
        Retourne un tuble de 2 élement le nombre de chance (chances) et la liste des mots (mots)
    """
    #ouverture du fichier en lecture seule
    with open("donnees.py", "r") as fichier:
        donnees = fichier.read().splitlines() # liste de lignes
        chances = int(donnees[0])
        mots = donnees[1].split(";")
    return chances, mots

def demander_nom():
    """ Demande à l'utilisateur son nom de joueur
        Retourne le nom du joueur
    """
    nom = input("Quel est votre nom de joueur ? ")
    while len(nom) <= 1:
        print("Votre nom doit contenir au mois 2 caractère ")
        nom = input("Quel est votre nom de joueur ? ")
    return nom
        
def est_deja_joueur(nom, scores):
    """ Prend un nom de joueur et les scores (un dictionnaire)
        et teste si le nom apparait parmis les clés
        Retourne True si oui, False sinon
    """
    if nom in scores.keys():
        return True
    return False

def choisir_mot(liste):
    indice = random.randrange(0,len(liste))
    return liste[indice]

def cacher_mot(mot):
    cache = list()
    i = 0
    while i < len(mot):
        cache.append("*")
        i += 1
    cache = "".join(cache)
    return cache

def choisir_lettre():
    lettre = input("choisir une lettre : ")
    while len(lettre) != 1 :
        print("Vous devez taper un seul caractère et appuis sur ENTER")
        lettre = input("choisir une lettre : ")
    return lettre.upper()

def remplacer_lettre(mot, lettre, indice):
    if indice >= len(mot) or indice < 0:
        print("indice trop grand ou trop petit")
        return mot
    res = mot[:indice] + lettre + mot[indice+1:]
    return res


def trouve(mot):
    """ Renvoie True si le mot est trouvé c'est-à-dire s'il n'y plus de '*' """
    if mot.count("*") > 0:
        return False
    return True
    
def quitter(scores):
    choix = input(" Voulez-vous sauvegarder la partie ?\
                    \nTaper 'o' si oui, 'n' si non : ")
    while choix.lower() != 'n' and choix.lower() != 'o':
        choix = input(" Voulez-vous sauvegarder la partie ?\
                        \nTaper 'o' si oui, 'n' si non : ")
    if choix == "n":
        print("\nMerci d'avoir jouer")
    if choix == "o":
        try:
            sauvegarder(scores)
            print("\nPartie sauvegardée !!\nA bientot !!")
        except NameError:
            print("La variable global scores n'existe pas")


def rejouer():
    choix = input("Taper 'R' pour rejouer ou 'Q' pour quitter ")
    while choix.lower() != 'r' and choix.lower() != 'q':
        choix = input("Taper 'R' pour rejouer ou 'Q' pour quitter ")
    if choix == 'r':
        return True
    if choix == 'q':
        return False


































