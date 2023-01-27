import requests

def get_data(ville):
    url='https://api.openweathermap.org/data/2.5/weather?q='+ville+'&appid=0e233c2decfef6a6d360a523c95bfa3f&units=metric&lang=fr'
    lecture=requests.get(url)
    data=lecture.json()
    return data

def format(ville):
    rows=get_data(ville)
    print("Température: "+str(rows["main"]["temp"])+"°C\nRessenti: "+str(rows["main"]["feels_like"])+"°C\nHumidité: "+str(rows["main"]["humidity"])+"%\n"+rows["weather"][0]["description"])