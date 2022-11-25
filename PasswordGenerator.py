import string
import random


#Initialisation variables
Lowercase_String, Upperccase_String, Symbol_String = string.ascii_lowercase, string.ascii_uppercase, string.punctuation

Lowercase=[]
Upperccase=[]
Numbers=[]
Symbol=[]



#Mise en place dans les listes
for letters in Lowercase_String:
    Lowercase.append(letters)
for letters in Upperccase_String:
    Upperccase.append(letters)
for letters in Symbol_String:
    Symbol.append(letters)
for i in range(10):
    Numbers.append(i)


ask=int(input("\n Insérez un nombre de caractères: "))

#Generateur

o=ask
Mdp=[]


#Ajout en liste les choix aléatoires entre Majuscules / Minuscules / Nombres le nombre de caractere donné
while o > 0:
    RdmChoice = random.randint(0,3)
    
    if RdmChoice == 0:
        Mdp.append(random.choice(Upperccase))
    elif RdmChoice == 1:
        Mdp.append(random.choice(Lowercase))
    elif RdmChoice == 2:
        Mdp.append(random.choice(Symbol))
    else:
        Mdp.append(random.randint(0,9))
            

    o -= 1

#Mot de passe en liste
Mdp.append(random.choice(Upperccase))

#Conversion mot de passe en chaine de caractere
Mot_De_Passe=""
for i in range(ask+1):
    Mot_De_Passe+=str(Mdp[i])
    
    
#Affichage Mot de passe généré
print(f"\nMot de passe généré: {Mot_De_Passe}")