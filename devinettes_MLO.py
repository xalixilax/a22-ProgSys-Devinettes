#!/usr/bin/env python3

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import re

ROUGE = "\33[31m"
JAUNE = "\33[33m"
BLEU = "\33[34m"
VERT = "\33[32m"
DEFAULT = "\33[m"
INITIAL = f"  {ROUGE}MLO{DEFAULT}"


def partie_gagne(essais):
    print(f"{INITIAL}> {VERT}Bravo, vous avez deviné le nombre!")
    print(f"{INITIAL}> Vos essais: {BLEU}{essais}\n")


def partie_perdu(nb_essai: int, rdn: int, essais):
    print(f"{INITIAL}> Désolé, vous avez échoué après {BLEU}{nb_essai}{ROUGE} tentatives.")
    print(f"{INITIAL}> Le nombre choisi était: {BLEU}{rdn} ")
    print(f"{INITIAL}> Vos essais: {BLEU}{essais}\n")


def partie():
    nb_essai = 1
    essais = []
    rdn = random.randrange(1, 101)

    while nb_essai <= 10:
        print(f"  {DEFAULT}Essai {BLEU}{nb_essai}:{VERT}", end=' ', flush=True)
        essai = input()

        if essai == "PPP":
            essais.append(essai)
            partie_perdu(nb_essai, rdn, essais)
            break

        if essai == "GGG":
            essais.append(essai)
            partie_gagne(essais)
            break

        if re.match(r' *[+-]?[0-9]+ *$', essai) is None:
            print(f"{INITIAL} >>> {ROUGE}ERREUR: Entrez un nombre entier svp!")
        elif int(essai) == rdn:
            essais.append(int(essai))
            partie_gagne(essais)
            break
        elif int(essai) in essais:
            print(f"{INITIAL} >>> {JAUNE}Ce nombre a déjà été essayer: {BLEU}{essais}")
        else:
            print(f"{INITIAL}> Votre nombre est trop", end=' ', flush=True)
            if int(essai) < rdn:
                print(f"{BLEU}petit{DEFAULT}...")
            else:
                print(f"{BLEU}grand{DEFAULT}...")
            essais.append(int(essai))
            nb_essai += 1
        print()
    else:
        partie_perdu(nb_essai, rdn, essais)


def main():
    quitter = ["n", "non"]
    continuer = ["o", "oui"]
    rejouer = ""

    print(f'{INITIAL}: {JAUNE}Jeu de devinettes...')
    print(f'{INITIAL}: {JAUNE}Devinez le nombre entier entre 1 et 100\n')
    partie()

    while rejouer not in quitter:
        print(f"{INITIAL}: {JAUNE}Voulez-vous rejouer? [O/N]{VERT}", end=" ", flush=True)
        rejouer = input().lower()

        if rejouer in continuer:
            print()
            partie()
        elif rejouer not in quitter:
            print(f"{INITIAL}> {ROUGE}Choix invalide.\n")

    print(f"{INITIAL}: {JAUNE}Au revoir!")


if __name__ == '__main__':
    main()
