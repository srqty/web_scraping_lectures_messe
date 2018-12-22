#script pour ajouter le jour de la semaine aux lecture des messes du jour
#exectuer dans bash: sed -f script_messe_lectures.sed fichier_à_modifier.html >> fichier_de_sortie.html

s/[> ]1 décembre 2018\|[> ]8 décembre 2018\|[> ]15 décembre 2018\|[> ]22 décembre 2018\|[> ]29 décembre 2018/samedi&/g

s/[> ]2 décembre 2018\|[> ]9 décembre 2018\|[> ]16 décembre 2018\|[> ]23 décembre 2018\|[> ]30 décembre 2018/dimanche&/g

s/[> ]3 décembre 2018\|[> ]10 décembre 2018\|[> ]17 décembre 2018\|[> ]24 décembre 2018\|[> ]31 décembre 2018/lundi&/g

s/[> ]4 décembre 2018\|[> ]11 décembre 2018\|[> ]18 décembre 2018\|[> ]25 décembre 2018/mardi&/g

s/[> ]5 décembre 2018\|[> ]12 décembre 2018\|[> ]19 décembre 2018\|[> ]26 décembre 2018/mercredi&/g

s/[> ]6 décembre 2018\|[> ]13 décembre 2018\|[> ]20 décembre 2018\|[> ]27 décembre 2018/jeudi&/g

s/[> ]7 décembre 2018\|[> ]14 décembre 2018\|[> ]21 décembre 2018\|[> ]28 décembre 2018/vendredi&/g

