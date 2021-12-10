# Import

from random import *
from colorama import Fore, Back, Style

# Fonction chiffre aléatoire

def programme():
    n = randint(0,9)
    return n
i=programme()

# Liste de mot

choixmot=["massue","vivant","destin","maille","projet","objets","dessin","hasard","perdue","python"]

# On determine un mot dans la liste grace au chiffre aléatoire

#print (choixmot[i] )# <--- utilisé pour m'aider lors des tests

motchoisis=choixmot[i]

#Main programm

vie = 8
compteurdetour = 0
motaffiche= ""   # <--- utilisé pour m'aider lors des tests

    # Régles
print ("                                                  ")
print ("Si la lettre est a la bonne place elle sera rouge")
print ("Si la lettre est dans le mot mais a la mauvaise place elle sera jaune")
print ("Si la lettre n'est pas dans le mot elle sera bleu")
print ("Tu as 8 essais")
print ("Bonne chance !")
print ("                                                  ")

# Boucle du jeu

while compteurdetour !=8:
    
    motaffiche= ""
    motentré = input("Choississez un mot a 6 lettres --> ")
    for h in range (len(motentré)): # <-- On lit le mot entré lettre par lettre
        if motentré[h]==motchoisis[h]: 
            motaffiche += Fore.RED + motentré[h] # <-- On compare chaque lettre a celle qui est a la même position que le mot mystère
        elif motentré[h] == motchoisis[0] or motentré[h] == motchoisis[1] or motentré[h] == motchoisis[2] or motentré[h] == motchoisis[3] or motentré[h] == motchoisis[4] or motentré[h] == motchoisis[5]:
            motaffiche += Fore.YELLOW + motentré[h] # <-- On vérifie qu'une lettre a pu aussi etre positionnée autre part dans le mot
        else :
            motaffiche += Fore.BLUE + motentré[h] # <-- Si la lettre n'est pas dans le mot
    print (motaffiche) # <-- On affiche le mot qu'on a entré avec le bon code couleur des règles
    print(Style.RESET_ALL) # <-- on réinitialise les couleurs pour ne pas modifier la suite de l'affichage
    
    if motentré == motchoisis:
        print("VICTOIRE !")
        break

    compteurdetour += 1 
    vie -= 1 #On aurait pu enlever "compteurdetour" et le remplacer par "vie"
    print ("vie restantes --> ", vie) # ici c'est "compteurdetour" qui implique la défaite et "vie" ne sers qu'a l'affichage
    
    #print (compteurdetour) # <--- utilisé pour m'aider lors des tests
    
    if compteurdetour==8 :
        print ("DEFAITE !")
        break
# Fin de la boucle
