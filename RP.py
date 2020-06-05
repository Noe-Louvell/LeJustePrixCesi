#!/usr/bin/env python
# -- coding: utf­-8 ­--

import random
import time
import requests, json



randNumb = random.randint(1.0, 101.0)
Numb = None
begin = time.time()

print("Bonjour et bienvenue sur le Juste Prix ! ")
print("Nous avons choisi un prix entre 1 et 101 a vous de le découvrire pour gagner !")
print(randNumb)


while int(Numb != randNumb):
    if not (begin <= time.time() <= begin + 40):
        print("Le temps est ecoulé vous avez perdu !")
        print("Le juste prix était de " + str(randNumb) + " Euros")
        break
    try:
        Numb = int(input("Donnez moi votre prix : "))
    except ValueError:
        print("Merci de saisir une valeur numérique !")
    except TypeError:
        print("Merci de saisir une valeur numérique !")
    except NameError:
        print("Merci de saisir une valeur numérique !")
    finally:
        print("Vous m'avez dit " + str(Numb) + " ?")

    if Numb > randNumb:
        print(str(Numb) + "  c'est moins ! ")
    elif Numb < randNumb:
        print(str(Numb) + "  c'est plus !")
    elif Numb == randNumb:
        print(str(Numb) + ".  .  .  .  Et c'est un juste prix vous avez gagner !")