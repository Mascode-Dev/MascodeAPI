import csv
import requests, json
import champion as ch
import item as it
from math import *


api_key='API_KEY'
id_match=input("ID du match sur le serveur EUW : ")
def summary(id):
    array=[["Numero Équipe","Pseudo","Champion","Poste","KDA","Gold","Damage","Item 1","Item 2","Item 3","Item 4","Item 5","Item 6","Issue"]]    
    url_match_content='https://europe.api.riotgames.com/lol/match/v5/matches/'+id+'?api_key='+api_key
    contenu_match=requests.get(url_match_content) #Contenu du match
    rqt=contenu_match.json()['info']['participants']
    team=0 #Initialisaton de team
    for i in range(len(rqt)): #Nombre de participant
        if rqt[i]['teamId']==100:
            team=1
        else:
            team=2
        pseudo=rqt[i]['summonerName']
        champion=rqt[i]['championName']
        poste=rqt[i]['individualPosition']
        kda=rqt[i]['challenges']['kda']
        gold=rqt[i]['goldEarned']
        damage=rqt[i]["totalDamageDealtToChampions"]
        item1=it.get_item(rqt[i]['item0'])
        item2=it.get_item(rqt[i]['item1'])
        item3=it.get_item(rqt[i]['item2'])
        item4=it.get_item(rqt[i]['item3'])
        item5=it.get_item(rqt[i]['item4'])
        item6=it.get_item(rqt[i]['item5'])
        issue=rqt[i]['win']
        array.append([team,pseudo,champion,poste,float(round(kda,2)),gold,damage,item1,item2,item3,item4,item5,item6,issue])
    
    with open(f"data_out/{contenu_match.json()['metadata']['matchId']}.csv","w") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(array)
    print("ECRITURE TERMINÉE !")

summary(id_match)
