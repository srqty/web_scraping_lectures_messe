#tutorial vidéo à https://www.youtube.com/results?search_query=python+programming+tutorial+-+27+-+how+to+build+a+web+crawler+%283%2F3%29

#Écrire et ajouter à un fichier Mathes p. 199.
#Schafer montre où placer le code pour ajouter à un fichier.

import requests 
import webbrowser
from bs4 import BeautifulSoup
    
#def chercher_date_du_jour(url_date):
#    with open('liens_lectures_du_mois.txt', 'r') as liens_html:
#        for messe-du_jour in liens_html:               
#            soup = BeautifulSoup(messe_du_jour, 'lxml')
#            date = soup.h4
#            return(date)
#
#def ajouter_texte_fichier(texte_ajouter)
#    with open('messes_du_jour.html', 'a') as messes_du_jour_html:
#        messes_du_jour_html.write(text_ajouter)


if __name__ == "__main__":
    """Extraire les liens sur la page du mois"""
    with open('liens_lectures_du_mois.txt', 'a') as af:

        url = 'https://www.aelf.org/calendrier/romain/2018/11'
        source_code = requests.get(url)
        source_code.raise_for_status()
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.find('a', {'title': 'Accéder aux messes'}):
            href = "https://www.aelf.org" + link.get('href')
            af.write(href + "\n")
    #Créer un fonction qui cherche le text désiré. Schafer montre comment faire.
    #Ajouter le text désiré au fichier.         
            #ouvrir_onglets_dans_navigateur(href)
            # chercher_text_dans_url(href)
            
    #Faire appelle au regex qui ajoute le jour de la semaine.         

    #def ouvrir_onglets_dans_navigateur(url):
        """ouvrir les onglets dans la navigator"""

       # webbrowser.open_new_tab(url)
#What is the perfect counterpart in Python for “while not EOF” https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof    
#    with open('liens_lectures_du_mois.txt', 'r') as lf: 
#         for ligne in lf:
#            date_du_jour = chercher_date_du_jour()
#            ajouter_texte_fichier(date_du_jour)
#            texte_du_jour = chercher_texte_du_jour()
#            ajouter_texte_fichier(texte_du_jour)



