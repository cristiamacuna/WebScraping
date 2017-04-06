# coding=utf-8
from urllib import urlopen
from bs4 import BeautifulSoup

import re
import urlparse



webpage = urlopen('http://www.espnfc.com/scores').read()

soup = BeautifulSoup(webpage, "html.parser")

ligas = soup.find_all("h4")

results = []
class league:
    def __init__(self, name, url):
        self.name = name
        self.url = url
    def __str__(self):
        return self.name

for liga in ligas:
    #print liga.text + liga.a["href"]
    liga = league(liga.text,liga.a["href"])
    results.append(liga)

for result in results:
    #Imprimo las ligas
    print("Liga: " +result.name + " URL: " + result.url)
    webpagetest = urlopen(result.url).read()
    souptest = BeautifulSoup(webpagetest, "html.parser")
    #Imprimo los partidos por liga
    matches = souptest.find("div", class_="scores")
    matches2 = matches.find_all("a", class_="primary-link")
    for match in matches2:
        if match["href"][22] == "m":
            print "URL Partido: "+ match["href"]
            lineup = match["href"].replace("match","lineups")
            print "URL Alineacion: " + lineup
            page = urlopen(lineup).read()
            stlineup = BeautifulSoup(page,"html.parser")

            alineacion = stlineup.find_all("span",attrs={"class":"name"})
            #Estadisticas
            print "ALINEACION: "
            for player in alineacion:
                print player.get_text()

        #Imprimo el nombre de los equipos
        webstats = urlopen(match["href"]).read()
        soupStats = BeautifulSoup(webstats, "html.parser")
        stats = soupStats.find_all("span",{"class":"long-name"},limit=2)
        print "Equipos: "
        for stat in stats:
            print stat.get_text()


        score = soupStats.find_all("span",attrs={"class":"score"})
        print "Marcador: "
        for s in score:
            print s.get_text()

        datos = soupStats.find_all("td", attrs={"data-stat": "foulsCommitted"})
        if datos != []:
            print "Fouls casa " + datos[0].get_text() + " Fouls visita " + datos[1].get_text()
        tarjetas = soupStats.find_all("td", attrs={"data-stat":"yellowCards"})
        if tarjetas != []:
            print "Tarjetas amarillas Casa" + tarjetas[0].get_text() + ", tarjetas amarillas visita" + tarjetas[1].get_text()

        rojas = soupStats.find_all("td",attrs={"data-stat":"redCards"})
        if rojas != []:
            print "Rojas casa " + rojas[0].get_text() + "rojas visita " + rojas[1].get_text()

        offsides = soupStats.find_all("td",attrs={"data-stat":"offsides"})
        if offsides != []:
            print "offs casa " + offsides[0].get_text() + " offs visita" + offsides[1].get_text()
        corners = soupStats.find_all("td",attrs={"data-stat":"wonCorners"})
        if corners != []:
            print "Corners casa " + corners[0].get_text() + " corners visita: " + corners[1].get_text()
        saves = soupStats.find_all("td", attrs={"data-stat":"saves"})
        if saves != []:
            print "Saves casa: " + saves[0].get_text() + " saves visita: " + saves[1].get_text()



#---------------------------------------------------------------------------------------------#



