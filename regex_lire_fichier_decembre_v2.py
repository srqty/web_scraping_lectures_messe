#clear python interpreter «ctrl + l»
#prochaine étape 1) mettre le code dans un fonction
#2) Écrire remplacer7 dans un fichier.

import re

pattern1 = re.compile(r'([> ]1 décembre 2018|[> ]8 décembre 2018|[> ]15 décembre 2018|[> ]22 décembre 2018|[> ]29 décembre 2018)')
pattern2 = re.compile(r'([> ]2 décembre 2018|[> ]9 décembre 2018|[> ]16 décembre 2018|[> ]23 décembre 2018|[> ]30 décembre 2018)')
pattern3 = re.compile(r'([> ]3 décembre 2018|[> ]10 décembre 2018|[> ]17 décembre 2018|[> ]24 décembre 2018|[> ]31 décembre 2018)')
pattern4 = re.compile(r'([> ]4 décembre 2018|[> ]11 décembre 2018|[> ]18 décembre 2018|[> ]25 décembre 2018)')
pattern5 = re.compile(r'([> ]5 décembre 2018|[> ]12 décembre 2018|[> ]19 décembre 2018|[> ]26 décembre 2018)')
pattern6 = re.compile(r'([> ]6 décembre 2018|[> ]13 décembre 2018|[> ]20 décembre 2018|[> ]27 décembre 2018)')
pattern7 = re.compile(r'([> ]7 décembre 2018|[> ]14 décembre 2018|[> ]21 décembre 2018|[> ]28 décembre 2018)')

with open('premier_décembre.txt', 'r') as lf:
#Lire le contenu du fichier
    lf_contents = lf.read()
    #matches = pattern.finditer(f)
    remplacer1 = pattern1.sub(r' samedi\1', lf_contents)
    remplacer2 = pattern2.sub(r' dimanche\1', remplacer1)
    remplacer3 = pattern3.sub(r' lundi\1', remplacer2)
    remplacer4 = pattern4.sub(r' mardi\1', remplacer3)
    remplacer5 = pattern5.sub(r' mercredi\1', remplacer4)
    remplacer6 = pattern6.sub(r' jeudi\1', remplacer5)
    remplacer7 = pattern7.sub(r' vendredi\1', remplacer6)
    print(type(remplacer7), end='')
    
    
    with open('outfile', 'w') as ef:
        ef.write(remplacer7)
        #explications https://stackoverflow.com/questions/18703525/attributeerror-str-object-has-no-attribute-write
        #remplacer7.write()
        print('"ef" est du type: ', type(ef))
        
        
    
    
