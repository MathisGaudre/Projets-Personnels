import requests
import webbrowser
import folium
import time

# URL de l'API Irigo
api_url = "https://data.angers.fr/api/records/1.0/search/?dataset=bus-tram-position-tr&q=&facet=novh&facet=mnemoligne&facet=nomligne&facet=dest"

# Fonction pour récupérer les informations d'un bus
def get_bus_info(bus_id):
  response = requests.get(f"{api_url}/buses/{bus_id}")
  if response.status_code != 200:
    return None
  data = response.json()
  return data

def coord():
    ligne=input("Definissez votre ligne : ")
    for i in range(len(bus)):
        if bus[i]['fields']['mnemoligne']==ligne:
            lat=bus[i]['fields']['coordonnees'][0]
            lon=bus[i]['fields']['coordonnees'][1]
            return lat,lon

def bus_dispo():
    for i in range(len(bus)):
        print(bus[i]['fields']['mnemoligne'])

bus1_info = get_bus_info(1)
bus=bus1_info["records"]