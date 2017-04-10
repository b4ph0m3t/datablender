import string
import csv

#FILTRO

lista = open("scaflist.txt", "r")
scaffold = lista.read().splitlines()
d = {}
for item in scaffold:
    d[item]=[]




#CARICAMENTO ASSOCIAZIONI
with open("raw_output.csv", newline='') as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        gene = str(row[0])
        cluster = str(row[1])
        if cluster in d.keys():
            d[cluster].append(gene)

print(d.keys())

#LETTURA MATRICE
top_cov = open("top_coverages.csv", "w")
headline="gene,GALF1 normalized coverage,GALF2 normalized coverage,GALF3 normalized coverage,ITAF1 normalized coverage,ITAF2 normalized coverage,ITAF3 normalized coverage,Lola normalized coverage,Pura_normalized coverage,GALM1 normalized coverage,GALM2 normalized coverage,GALM3 normalized coverage,ITAM1 normalized coverage,ITAM2 normalized coverage,ITAM3 normalized coverage,CLUSTER"
genes = []
top_cov.write("%s\n" %headline)
with open("normalized_coverages.csv", newline='') as matrix:
    reader = csv.reader(matrix, delimiter=',')
    for row in reader:
        name = str(row[0])
        name = name[:-2]
        for key in d:
            if name in d[key]:
                stringa = (','.join(row) + "," + key)
                #print(stringa)
                top_cov.write("%s\n" %stringa)
