import requete as rq
import requests, json
from collections import OrderedDict
from math import *

def champ(): #Les champions les plus joué
    dic={}
    array=[]
    for i in range(len(rq.liste_match.json())): #30 max
        url_match0='https://europe.api.riotgames.com/lol/match/v5/matches/'+rq.liste_match.json()[i]+'?api_key='+rq.api_key
        requete_match=requests.get(url_match0)
        requete_match.json()
        a=rq.index_joueur_avg(requete_match.json())
        champ=requete_match.json()['info']['participants'][a]['championName']
        if champ in dic:
            dic[champ]+=1
        else:
            dic[champ]=1
    #Tri du dictionnaire par valeur decroissante
    d=dict(sorted(dic.items(), key=lambda t: t[1]))
    d0 = OrderedDict(reversed(list(d.items()))) 
    c=0
    #print("Les 5 champions les plus joué en ranked par "+rq.nametmp+" sur les "+str(len(rq.liste_match.json()))+" dernières games (ranked):")
    for k, v in d0.items():
        if c!=5:
            print(k,":", v,"games")
            array.append(str(k)+" : "+str(v)+" games")
            c+=1
    return array


def profil():
    return [
        "Pseudo du joueur : "+str(rq.nametmp),"Niveau du compte : Niveau "+str(rq.info_player.json()['summonerLevel']),
        "Rang du compte : "+str(rq.requete_rank.json()[rq.index_rank_type()]['tier'])+' '
        +str(rq.requete_rank.json()[rq.index_rank_type()]['rank'])+' '
        +str(rq.requete_rank.json()[rq.index_rank_type()]['leaguePoints'])+" LP ",rq.three_mastery(),champ()]

def mastery_print():
    print("Pseudo du joueur :",rq.nametmp)
    print("Niveau du compte : Niveau",rq.info_player.json()['summonerLevel'])
    print("Rang du compte : "+str(rq.requete_rank.json()[rq.index_rank_type()]['tier'])+str(rq.requete_rank.json()[rq.index_rank_type()]['rank'])+str(rq.requete_rank.json()[rq.index_rank_type()]['leaguePoints'])+" LP")
    rq.three_mastery()

def avg():
    #Les stats en moyenne sur les 30 dernières games
    print(rq.nametmp+"'s statistics for 30 last games")
    #CS
    cs=0
    for i in range(len(rq.liste_match.json())):
        url_match0='https://europe.api.riotgames.com/lol/match/v5/matches/'+rq.liste_match.json()[i]+'?api_key='+rq.api_key
        requete_match=rq.requests.get(url_match0)
        requete_match.json()
        a=rq.index_joueur_avg(requete_match.json())
        cs+=requete_match.json()['info']['participants'][a]['totalMinionsKilled']
        cs/=len(rq.liste_match.json())
    return cs

def requete():
    url_match0='https://europe.api.riotgames.com/lol/match/v5/matches/'+rq.liste_match.json()[0]+'?api_key='+rq.api_key
    requete_match=rq.requests.get(url_match0)
    print(requete_match.json())

def matchdata():
    array=[["","Poste","VS","KDA","DAMAGE","PO","WIN"]]
    ennemi=''
    for i in range(len(rq.liste_match.json())): #Parcourir chaque match du joueur
        url_match0='https://europe.api.riotgames.com/lol/match/v5/matches/'+rq.liste_match.json()[i]+'?api_key='+rq.api_key
        requete_match=requests.get(url_match0)
        ind=rq.index_joueur_avg(requete_match.json())
        ennemi='Inconnu'
        for j in range(10): #Trouver le champion ennemi
            if requete_match.json()['info']['participants'][j]["individualPosition"]==requete_match.json()['info']['participants'][ind]["individualPosition"] and ind!=j:
                ennemi=requete_match.json()['info']['participants'][j]["championName"]
                break
            else:
                continue
        kda=requete_match.json()['info']['participants'][ind]['challenges']['kda']
        champ=requete_match.json()['info']['participants'][ind]["championName"]
        poste=requete_match.json()['info']['participants'][ind]["individualPosition"]
        dmg=requete_match.json()['info']['participants'][ind]["totalDamageDealtToChampions"]
        gold=requete_match.json()['info']['participants'][ind]['goldEarned']
        if requete_match.json()['info']['participants'][ind]['win']==True:
            issue="WIN"
        else:
            issue='LOSS'       
        array.append([champ,poste,ennemi,float(round(kda,2)),dmg,gold,issue])
    return array

