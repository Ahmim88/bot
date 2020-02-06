#!/usr/bin/python3
#import random
import datetime 
import re
#salutation = ['massil', 'ahmim', 'insim', 'bachelor', 'dev', 'web', 'python', 'juv', 'azul', 'amazigh', 'bay']
#reponse = input("bonjour, je suis votre bot, veuillez donner un mot\n")
categories = ["voiture","telephone","ordinateur"]
exclure = ["un","une","des","les","je","nous","svp","bonjour","merci"]
#proposition = ["salut","bonjour","bonsoir"]
requete = input ("bonjour, je suis votre asisstant mybot,que desirez vous achetez? \n ")
decoupe = (re.findall(r"[a-zA-Z]+", requete))
print(decoupe)
final = list(set(decoupe)-set(exclure))
finale = [mot.lower() for mot in final if len(mot) > 2]
print(finale)

if ("voiture" in finale):
    print("voici le catalogue de voiture")
elif("telephone" in finale):
    print("voici le catalogue des telephones")
elif("ordinateur" in finale):
    print("voici les ordinateurs de premier choix")
else:
    print("vu a {0}". format(datetime.datetime.now()))



#if (reponse.lower() in proposition):
 #   print(random.choice(salutation) + " mon ami")
#else:
 #   print("je ne comprend pas")

