#tutorial vidéo à https://www.youtube.com/results?search_query=python+programming+tutorial+-+27+-+how+to+build+a+web+crawler+%283%2F3%29

#Écrire et ajouter à un fichier Mathes p. 199.
#Schafer montre où placer le code pour ajouter à un fichier.

import re
from bs4 import BeautifulSoup
import urllib.request
url = 'https://www.aelf.org/calendrier/romain/2019/02'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
  
"""Reçoit: url de lecture du jour +
    Retourne type string:  le texte qui contient les lectures avec la date"""
def chercher_texte_dans_lien(lien_du_messe):
    url_lecture = lien_du_messe
    req_lecture = urllib.request.Request(url_lecture, headers={'User-Agent': 'Mozilla/5.0'})
    html_lecture = urllib.request.urlopen(req_lecture).read()
    return(html_lecture)

"""Reçoit: url de lecture du jour +
    Retourne: Objet du type BeautifulSoup avec la date et balises html"""
def chercher_date_du_jour(texte_de_messe):
    soup_lecture = BeautifulSoup(texte_de_messe, 'html.parser')
    date = soup_lecture.find('h4', class_='date')
    print('Variable date est du type: ', type(date))
    return(date)

"""Reçoit: url de lecture du jour +
    Retourne: string. Le texte du jour"""
def chercher_texte_du_jour(texte_de_messe):
    soup_lecture = BeautifulSoup(texte_de_messe, 'html.parser')
    texte_complet_liste = [] #créer une liste qui contiendra le texte

    for texte in soup_lecture.find_all('div', {'id':re.compile('messe1_lecture[0-9]')}):  #Voire Mitchell, faut noter tous les éléments texte_complet_liste.append(texte) 
        #Ajouter les lectures du jour. Voire «List append() in for loop [duplicate]» \ https://stackoverflow.com/questions/41452819/list-append-in-for-loop 
        #Convertir la liste dans un seul string 
        #«Python map() function» https://www.journaldev.com/22960/python-map-function 
        return("".join(map(str, texte_complet_liste)))

"""Enlever balises html +
Reçoit: objet du type BeautifulSoup. Date avec balises html +
Retourne: objet BeautifulSoup qui contient la date sans balises"""
def enlever_balises_html(date_du_jour_avec_balises):
    return(date_du_jour_avec_balises.get_text())
        
"""Ajouter le jour de la semaine à la date.""" 
"""Reçoit: Objet BeautifulSoup avec  la date sans jour de la semaine + 
Retourne: string qui contient la date avec le jour de la semaine"""
def ajouter_jour_de_la_semaine(date_sans_jour):
    pattern1 = ('<h4 class="date">1 février 2019</h4>', '<h4 class="date">8  février 2019</h4>', '<h4 class="date">15 février 2019</h4>', '<h4 class="date">22 février 2019</h4>', '<h4 class="date">28 février 2019</h4>)') 
    pattern2 = ('<h4 class="date">2 février 2019</h4>', '<h4 class="date">9 février 2019</h4>', '<h4 class="date">16 février 2019</h4>', '<h4 class="date">23 février 2019</h4>', '<h4 class="date">30 février 2019</h4>)')
    pattern3 = ('<h4 class="date">3 février 2019</h4>', '<h4 class="date">10 février 2019</h4>', '<h4 class="date">17 février 2019</h4>', '<h4 class="date">24 février 2019</h4>', '<h4 class="date">31 février 2019</h4>)') 
    pattern4 = ('<h4 class="date">4 février 2019</h4>', '<h4 class="date">11 février 2019</h4>', '<h4 class="date">18 février 2019</h4>', '<h4 class="date">25 février 2019</h4>)') 
    pattern5 = ('<h4 class="date">5 février 2019</h4>', '<h4 class="date">12 février 2019</h4>', '<h4 class="date">19 février 2019</h4>', '<h4 class="date">26 février 2019</h4>)')
    pattern6 = ('<h4 class="date">6 février 2019</h4>', '<h4 class="date">13 février 2019</h4>', '<h4 class="date">20 février 2019</h4>', '<h4 class="date">27 février 2019</h4>)')
    pattern7 = ('<h4 class="date">7 février 2019</h4>', '<h4 class="date">14 février 2019</h4>', '<h4 class="date">21 février 2019</h4>', '<h4 class="date">28 février 2019</h4>)')

    if str(date_sans_jour) in pattern1:
        date_du_jour_sans_balises = enlever_balises_html(date_sans_jour)
        return("<p>le vendredi " + str(date_du_jour_sans_balises) + "</p>")


"""Reçoit: string. Texte à ajouter au fichier +
    Retourne: rien. Écrit le text au fichier avec balises html."""
def ajouter_texte_fichier(texte_ajouter):
    with open('messes_du_jour.html', 'a') as af:     
       # print(type(texte_ajouter)) # Pour savoir le type de variable       
        af.write(str(texte_ajouter))

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
        lecture_texte_complet = chercher_texte_dans_lien(ligne)
        
        """Extraire la date de la page web"""
        date_du_jour = chercher_date_du_jour(lecture_texte_complet)
        print('"date_du_jour" est du type: ', type(date_du_jour))      
        """Ajouter le jour de la semaine à la date"""
        date_avec_jour = ajouter_jour_de_la_semaine(date_du_jour)
        
        ajouter_texte_fichier(date_avec_jour)

        """Extraire le texte de la page web"""
        texte_du_jour = chercher_texte_du_jour(lecture_texte_complet)
        ajouter_texte_fichier(texte_du_jour)
        break
#    with open('outfile', 'w') as ef:
#        ef.write(remplacer7)
#        #explications https://stackoverflow.com/questions/18703525/attributeerror-str-object-has-no-attribute-write
#        #remplacer7.write()
#        print('"ef" est du type: ', type(ef))
        
        
    
    
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
            

