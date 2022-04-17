import requete as rq
from collections import OrderedDict
from math import *
import requests, json


mat=rq.content()
index=rq.index_joueur(mat)
requete=mat['info']['participants'][index]

def match(): #Donne les informations du joueur sur le match demandé
    
    index=rq.index_joueur(mat)
    requete=mat['info']['participants'][index]

    print("Nom du champion :",requete["championName"])
    print("Mode de jeu :",mat['info']["gameMode"])
    print("Lane :",requete["individualPosition"])
    print("KDA :",round(requete['challenges']['kda'],2))
    print("Kills/Deaths/Assists :",requete["kills"],"/",requete["deaths"],"/",requete['assists'])
    print("CS :",requete['totalMinionsKilled'])
    print("A gagné la game ? :",requete["win"])

    secondes=mat['info']['gameDuration']
    minutes, secondes = divmod(secondes, 60)
    if minutes<10:
        minutes="0"+str(minutes)
    if secondes<10:
        secondes='0'+str(secondes)

    print("Durée de la game : "+str(minutes)+":"+str(secondes))

match()