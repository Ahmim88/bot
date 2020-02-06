#!/usr/bin/python3
#salutation = ['massil', 'ahmim', 'insim', 'bachelor', 'dev', 'web', 'python', 'juv', 'azul', 'amazigh', 'bay']
question = input("bonjour, je suis votre bot, veuillez donner un mot\n")

proposition = ["salut","bonjour","bonsoir"]

if (question.lower() in proposition):
    print("salut mon ami")
else:
    print("je ne comprend pas")

