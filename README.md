# MascodeAPI
I use the Riot API to scout soloQ matches, to study statistics and propose solutions (pick, ban, strategies) to my team during tournaments.  
I organize tournaments every year, so with the Riot API i can manipulate all the datas from matches, to be able to elect the title of best player, to calculate performance from every player

# Organisation of files

main.py : In this file, there are all function that use requests (champ, profil, matchdata)  
requete.py : In this file, there are all requests I need (match_list, summoner_name, mastery, rank)  
requeteur.py : In this file, I can have all the information about one player, in one game with summoner_id and match_id  
champion.py : In this file, I can convert a champion_id to the champion name (return string)  
summary_match.py : In this file, I can have all informations about a match with a match_id (champion, role, kda, gold, items,..)
