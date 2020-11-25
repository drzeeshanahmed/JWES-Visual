import ensembl_rest
import requests 
import csv

fileOut = open('Links_Genes.txt', 'w') 
h = {"ACE2":"hs2 54872470 54872470",
"CCR9":"hs2 109744940 109744940",
"CD147":"hs2 164617410 164617410",
"CXCR6":"hs2 219489880 219489880",
"FYCO1":"hs3 31162977 31162977",
"IFNAR1":"hs3 86035447 86035447",
"IFNAR2":"hs3 140907917 140907917",
"IFNG":"hs3 195780387 195780387",
"IL6":"hs4 52630427 52630427",
"IRF3":"hs4 107502897 107502897",
"IRF7":"hs4 162375367 162375367",
"IRF9":"hs7 26093561 26093561",
"LZTFL1":"hs7 80966031 80966031",
"MIF":"hs7 135838501 135838501",
"RAG1":"hs11 31572308 31572308",
"RAG2":"hs11 86444778 86444778",
"SLC6A20":"hs12 6310732 6310732", 
"STAT1":"hs12 61183202 61183202",
"STAT2":"hs12 116055672 116055672",
"TBK1":"hs14 37076247 37076247",
"TICAM1":"hs14 91948717 91948717",
"TLR3":"hs19 39471647 39471647",
"TMPRSS2":"hs21 35215134 35215134",
"TMPRSS4":"hs22 41957709 41957709",
"TRAF3":"hsX 45525613 45525613",
"UNC93B1":"hsX 100398083 100398083",
"XCR1":"hsX 155270553 155270553"}

with open('Genes_Detail.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #print( row[9])
            variants = row[9].split(",")
            for variant in variants:
                values = variant.split("|")
                if values[3] in h:
                    value = h[values[3]]
                    fileOut.write(value + " " + "hs" + row[1][3:] + " " + row[2] + " " + row[2] + " " + "color=hs" + row[1][3:] + "\n")
            line_count += 1

