#Importation
import requests, json
from collections import OrderedDict
from math import *
import champion as ch
import item as it

#Formation de la requete principale
api_key='RGAPI-2364154d-a020-48c6-a539-07dbde235019'
nametmp=input("Entrer un pseudo League of Legends sur le serveur EUW : ")
name=nametmp.replace(" ","+")
urltmp="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
url=urltmp+name+"?api_key="+api_key
print(url)

#Requete pour info joueur
info_player=requests.get(url)
info_player.json()
summ_id=info_player.json()['id']
acc_id=info_player.json()['accountId']
pid=info_player.json()['puuid'] #Liste of match

#Requete pour liste des match
url_list='https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+pid+'/ids?type=ranked&start=0&count=25&api_key='+api_key
liste_match=requests.get(url_list)
liste_match.json()

#Contenu du dernier match
def content():
    id_match=input("ID du match sur le serveur EUW : ")
    url_match_content='https://europe.api.riotgames.com/lol/match/v5/matches/'+id_match+'?api_key='+api_key
    if id_match=='LAST':
        url_match_content='https://europe.api.riotgames.com/lol/match/v5/matches/'+liste_match.json()[0]+'?api_key='+api_key
    contenu_match=requests.get(url_match_content)
    return contenu_match.json()

#Requete numero de joueur dans la game

def index_joueur(rqt):
    requete_tmp=rqt['info']['participants']
    for i in range(len(requete_tmp)):
        if rqt['info']['participants'][i]["summonerName"]==nametmp:
            return i
        else:
            continue


#Requete pour mastery
url_mas='https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'+summ_id+"?api_key="+api_key
requete_mastery=requests.get(url_mas)
requete_mastery.json()

#Prend seulement les 3 premiers
def three_mastery():
    array=[]
    for i in range(3):
        a=ch.get_champions_name(requete_mastery.json()[i]['championId'])
        #print(i+1,":",a,"- Niveau",requete_mastery.json()[i]['championLevel'], "-",requete_mastery.json()[i]['championPoints'],' points.')
        array.append(str(i+1)+" : "+str(a)+" - Niveau "+str(requete_mastery.json()[i]['championLevel'])+ " - "+str(requete_mastery.json()[i]['championPoints'])+' points.')
    return array
requete_mastery.json()

#Requete pour le rang d'un compte
url_rk="https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+summ_id+"?api_key="+api_key
requete_rank=requests.get(url_rk)
requete_rank.json()

def index_rank_type():
    for i in range(len(requete_rank.json())):
        if requete_rank.json()[i]['queueType']=='RANKED_SOLO_5x5':
            return i
        else:
            continue
#Requete pour le rang d'un compte (utilisé dans la moyenne)
def index_joueur_avg(rqt):
    for i in range(len(rqt['info']['participants'])): #Parcours le nombre de joueur
            if rqt['info']['participants'][i]["summonerName"]==nametmp:
                return i
            else:
                continue

