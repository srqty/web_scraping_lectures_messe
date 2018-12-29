#tutorial vidéo à https://www.youtube.com/results?search_query=python+programming+tutorial+-+27+-+how+to+build+a+web+crawler+%283%2F3%29

#Écrire et ajouter à un fichier Mathes p. 199.
#Schafer montre où placer le code pour ajouter à un fichier.

from bs4 import BeautifulSoup
import urllib.request

#Python 3.4 urllib.request error (http 403) https://stackoverflow.com/questions/28396036/python-3-4-urllib-request-error-http-403
url = 'https://www.aelf.org/calendrier/romain/2018/11'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
  
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
        
        
#        source_code = requests.get(url)
#        source_code.raise_for_status()
#        plain_text = source_code.text
        #soup = BeautifulSoup(plain_text, 'html.parser')
        soup = BeautifulSoup(html, 'html.parser')
        lectures_tous = soup.find(id='right-col', \
                        class_='block-single-reading without-toolbar')
        #print(lectures_tous.prettify())
        for lectures_ligne in lectures_tous.find_all('div', class_='row m-b-10'):
            #print(lectures_ligne.prettify())
            #lectures_messe_et_heures = lectures_ligne.find('div', class_='col-sm-3')
            #print(lectures_messe_et_heures)
            lectures_messes = lectures_ligne.find('a', title='Accéder aux messes')
            href = "https://www.aelf.org" + lectures_messes.get('href')
            print(href)
            

        #for link in lectures_liste:
            #lecture_mess_du_jour = 
            #href = "https://www.aelf.org" + link.get('href')
            #af.write(href + "\n")
    #Créer un fonction qui cherche le text désiré. Schafer montre comment faire.
    #Ajouter le text désiré au fichier.         
            #ouvrir_onglets_dans_navigateur(href)
            # chercher_text_dans_url(href)
            
    #Faire appelle au regex qui ajoute le jour de la semaine.         

    #def ouvrir_onglets_dans_navigateur(url):
       # """ouvrir les onglets dans la navigator"""

       # webbrowser.open_new_tab(url)
#What is the perfect counterpart in Python for “while not EOF” https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof    
#    with open('liens_lectures_du_mois.txt', 'r') as lf: 
#         for ligne in lf:
#            date_du_jour = chercher_date_du_jour()
#            ajouter_texte_fichier(date_du_jour)
#            texte_du_jour = chercher_texte_du_jour()
#            ajouter_texte_fichier(texte_du_jour)



