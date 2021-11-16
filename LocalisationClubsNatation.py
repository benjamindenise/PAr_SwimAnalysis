# -*- coding utf-8 -*-
import requests
import sqlite3
import csv

# Connexion à la BDD
con = sqlite3.connect("Bases de données\BUDAPEST_ROME_TOKYO.db")
cursor = con.cursor()

clubs = []

with open('clubs.csv', 'w', newline='', encoding='UTF8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['club', 'address', 'lat', 'lng'])
    for row in cursor.execute('SELECT club FROM nageurs'):
        clubName = row[0]
        if len(clubName) > 0:

            response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+clubName+'&region=France&key=???')
            try :

                response = response.json()["results"][0]
                lat = response["geometry"]["location"]["lat"]
                lng = response["geometry"]["location"]["lng"]
                address = response["formatted_address"]

                clubs.append([clubName,address, lat, lng])
                filewriter.writerow([clubName,address.replace(',', ' '), lat, lng])

            except :
                filewriter.writerow([clubName, '', '', ''])
