import requests

def get_api():
    url = 'https://api.example.com/data'
    response = requests.get(url)

    if response.status_code == 200:
        # Afficher les données de la réponse
        data = response.json()
        print(data)
    else:
        print('Erreur lors de la lecture de l\'API')
