import numpy as np
from math import *

print("Question 1")

def multiple_spt():
    try:
        debut = int(input("Valeur de debut : "))
        fin  = int(input("Valeur de fin : "))
        liste = []
        for i in range(debut,fin):
            if((i % 7 == 0) and (i % 5 != 0)):
                liste.append(i)
        return liste
    except:
        return "Entrez une valeur valide !"

print(multiple_spt())

print("Question 2")

def factorial() :
    try:
        nbr = input("Entrez votre nombre : ")
        x = 1
        while (nbr != 0):
            x *= nbr
            nbr -= 1
        return x
    except:
        return "Veuillez entrer une valeur valide ! "

print(factorial())

print("Question 3")

def fonction_qst(k):
    try:
        k = int(input("Valeur : "))
        dictionnaire = {}
        for i in range(1,k+1):
            dictionnaire[i] = i**2
        return dictionnaire
    except:
        return "Veuillez entrer une valeur valide ! "
print(fonction_qst())

print("Question 4")

def miss_str():
    try:
        mot = str(input("Mot : "))
        v = int(input("Valeur : "))
        try:
            liste = list(mot)
            del liste[v]
            motf = ""
            for i in liste:
                motf += i
            return motf
        except:
            return "La valeur choisi est trop grande pour votre mot ou est négative."
    except:
        return "Veuillez entrer un mot valide et/ou une valeur valide !"

print(miss_str())

print("Question 5")

def convert_array_list(arrays):
    try:
        liste_principale = []
        for column in arrays:
            liste_secondaire = []
            for i in column:
                liste_secondaire.append(i)
            liste_principale.append(liste_secondaire)
        return liste_principale
    except:
        return "Veuillez entrer une array valide !"


arrays = np.array([[1, 2], [3, 4]])
print(convert_array_list(arrays))

print("Question 6")

def covarriance_matrice(p,s):
    z = np.stack((p,s), axis=0)
    return np.cov(z)

print(covarriance_matrice([0,1,2],[2,1,0]))

print("Question 7")

def formula():
    try:
        c = 50
        h = 30
        d = input("Sequence : ")
        d_liste = d.split(",")
        liste_f = []
        for i in d_liste:
            q = round(sqrt((2*c*int(i))/h))
            liste_f.append(q)
        return liste_f
    except:
        return "Veuillez entrer un nombre entier ou une séquence de nombre entiers."

print(formula())