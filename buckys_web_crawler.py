#tutorial vidéo à https://www.youtube.com/results?search_query=python+programming+tutorial+-+27+-+how+to+build+a+web+crawler+%283%2F3%29

#Écrire et ajouter à un fichier Mathes p. 199.
#Schafer montre où placer le code pour ajouter à un fichier.

import re
from bs4 import BeautifulSoup
import urllib.request
url = 'https://www.aelf.org/calendrier/romain/2018/11'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
  
"""Reçoit: url de lecture du jour +
    Retourne: le texte qui contient les lectures avec la date"""
def chercher_texte_dans_lien(lien_du_messe):
    url_lecture = lien_du_messe
    req_lecture = urllib.request.Request(url_lecture, headers={'User-Agent': 'Mozilla/5.0'})
    html_lecture = urllib.request.urlopen(req_lecture).read()
    return(html_lecture)

"""Reçoit: url de lecture du jour +
    Retourne: la date"""
def chercher_date_du_jour(texte_de_messe):
    soup_lecture = BeautifulSoup(texte_de_messe, 'html.parser')
    date = soup_lecture.find('h4', class_='date')
    return(date)

"""Reçoit: url de lecture du jour +
    Retourne: le texte du jour"""
def chercher_texte_du_jour(texte_de_messe):
    soup_lecture = BeautifulSoup(texte_de_messe, 'html.parser')
    texte_complet = [] #créer une liste
    for texte in soup_lecture.find_all('div', {'id':re.compile('messe1_lecture[0-9]')}):  #Voire Mitchell, faut noter tous les éléments
        texte_complet.append(texte) # Voire «List append() in for loop [duplicate]» \ https://stackoverflow.com/questions/41452819/list-append-in-for-loop
    return(texte_complet)

#def ajouter_texte_fichier(texte_ajouter)
#    with open('messes_du_jour.html', 'a') as messes_du_jour_html:
#        messes_du_jour_html.write(text_ajouter)


if __name__ == "__main__":
    #Python 3.4 urllib.request error (http 403) https://stackoverflow.com/questions/28396036/python-3-4-urllib-request-error-http-403
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
            af.write(href + "\n")
            
with open('liens_lectures_du_mois.txt', 'r') as lf:
    """Pour chacun des lignes dans le fichier, on effectue des opérations"""
    for ligne in lf:
        """Mettre le texte du liens dans un variable"""
        lecture_texte = chercher_texte_dans_lien(ligne)
        
        """Extraire la date de la page web"""
        date_du_jour = chercher_date_du_jour(lecture_texte)
        print(date_du_jour)
        
        """Extraire le texte de la page web"""
        texte_du_jour = chercher_texte_du_jour(lecture_texte)
        print(texte_du_jour)
        
        break
        
        #for link in lectures_liste:
            #lecture_mess_du_jour = 
            #href = "https://www.aelf.org" + link.get('href')
            
    #Créer un fonction qui cherche le text désiré. Schafer montre comment faire.
    #Ajouter le text désiré au fichier.         
            #ouvrir_onglets_dans_navigateur(href)
            # chercher_text_dans_url(href)
            
    #Faire appelle au regex qui ajoute le jour de la semaine.         

    #def ouvrir_onglets_dans_navigateur(url):
       # """ouvrir les onglets dans la navigator"""

       # webbrowser.open_new_tab(url)
##What is the perfect counterpart in Python for “while not EOF” https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof    
#    with open('liens_lectures_du_mois.txt') as lf:
#        while True:
#            #Problème est dans la boucle while
#            ligne = lf.readline()
#            print(ligne)
#            if "FIN" in ligne:
#                print('Terminé')
#                break
#            else:
#                date_du_jour = chercher_date_du_jour(ligne)
        #        print(date_du_jour)
        #            ajouter_texte_fichier(date_du_jour)
        #            texte_du_jour = chercher_texte_du_jour()
        #            ajouter_texte_fichier(texte_du_jour)
                #print(ligne, end='')
#                print(date_du_jour, end='')
            

