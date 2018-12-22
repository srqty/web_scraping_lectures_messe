#tutorial vidéo à https://www.youtube.com/results?search_query=python+programming+tutorial+-+27+-+how+to+build+a+web+crawler+%283%2F3%29

#Écrire et ajouter à un fichier Mathes p. 199.
#Schafer montre où placer le code pour ajouter à un fichier.

import requests 
import webbrowser
from bs4 import BeautifulSoup

def extraire_liens():
    """Extraire les liens sur la page du mois"""

    url = 'https://www.aelf.org/calendrier/romain/2018/11'
    source_code = requests.get(url)
    source_code.raise_for_status()
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for link in soup.findAll('a', {'title': 'Accéder aux messes'}):
        href = "https://www.aelf.org" + link.get('href')
#Créer un fonction qui cherche le text désiré. Schafer montre comment faire.
#Ajouter le text désiré au fichier.         
        ouvrir_onglets_dans_navigateur(href)
        # chercher_text_dans_url(href)
        
#Faire appelle au regex qui ajoute le jour de la semaine.         

def ouvrir_onglets_dans_navigateur(url):
    """ouvrir les onglets dans la navigator"""

    webbrowser.open_new_tab(url)


def chercher_text_dans_url(url):
    code_source = requests.get(url)
    text = code_source.text
    # print(text)


extraire_liens()



