#!/usr/bin/env python
print("************************start Program*********************************")

# Define a filename.
filename = 'vasteplantTest.csv'
filename = 'vasteplanteOriginal05062021.csv'

import re


def search_Pattern(SearchString, complexString):
    #find until next "," patern
    returnString ="null"
    for match in re.finditer(SearchString, complexString):
        returnString = match.group(1)
        
    return returnString

#pattern = re.compile("[1-9][1-9][1-9][1-9][1-9][1-9][1-9][1-9][1-9][1-9]-\d{4,5}(.*?)[1-9][1-9][1-9][1-9][1-9][1-9][1-9][1-9][1-9]", re.DOTALL)
pattern = re.compile("\d{10}-\d{4,5}(.*?)\d{10}-\d{4,5}", re.DOTALL)
#pattern = re.compile("Tuintips(.*?)Tuintips", re.DOTALL)

#remove all new lines: output = re.sub('\s', ' ', text)

#main
total = 0
file_t = open(filename)
file_text= file_t.read()

with open('readme.txt', 'w') as targetFile:
    targetFile.write("reference,Nr,PlantNaam,Licht,Vochtigheid,Plantdichtheid,Habitat,Kleur,Hooghte,bladhooghte,bloei")
    targetFile.write('\n')

    for match in re.finditer(pattern, file_text):
        total = total + 1
        noLines = re.sub('\s', ' ', match.group())
        #print(noLines)
        print("Plantname:",total, " ", search_Pattern("page=\d{1,2}\",\"(.+)\"\,\"https", noLines), end = '')
        #print("Licht: ",search_Pattern("bodem en standplaats  licht :  (.*)bodem : ", noLines), end = '')
        #print("Vochtigheid: ", search_Pattern("vochtigheid :          (.*)habitat", noLines))
        #print("Plantdichtheid: ", search_Pattern("plantdichtheid(.*)\",\"[A-Z][A-Z]", noLines))
        #print("Habitat: ", search_Pattern("habitat (.*)extra informatie", noLines))
        #print("hoogte: ", search_Pattern("hoogte :(.*)bladhoogte : ", noLines))
        #print("bladhooghte: ", search_Pattern("bladhoogte :(.*)bloei :", noLines))
        #print("bloei: ", search_Pattern("bloei :(.*)\",\"Plantomschrijving", noLines))
        #print("kleur: ", search_Pattern("kleur :(.*)bladkleur", noLines))
        for match in re.finditer("\d{10}-\d{4,5}", noLines):
            reference =match.group(0)
        #reference = search_Pattern("\d{10}-\d{4,5}(.*?)\d{10}-\d{4,5}",noLines)
        Plantname = search_Pattern("page=\d{1,2}\",\"(.+)\"\,\"https",noLines)
        targetFile.write("\""+ reference+"\",\""+ str(total)+"\",\""+Plantname + "\",\"")
        
        Licht = search_Pattern("bodem en standplaats  licht :  (.*?)bodem : ",noLines)
        targetFile.write( Licht + "\",\"" )

        Vochtigheid = search_Pattern("vochtigheid :          (.*?)habitat", noLines)
        targetFile.write( Vochtigheid + "\",\"" )

        Plantdichtheid = search_Pattern("plantdichtheid   (.*?)\",\"", noLines)
        targetFile.write( Plantdichtheid + "\",\"" )

        Habitat = search_Pattern("habitat         (.*?)\",\"", noLines)
        targetFile.write( Habitat + "\",\"" )

        kleur = search_Pattern("kleur :  (.*?)bladkleur", noLines)
        targetFile.write( kleur + "\",\"" )

        hoogte = search_Pattern("hoogte :   (.*?)bladhoogte", noLines)
        targetFile.write( hoogte + "\",\"" )

        bladhooghte = search_Pattern("bladhoogte :(.*?)bloei", noLines)
        targetFile.write( bladhooghte + "\",\"" )

        bloei = search_Pattern("bloei :(.*?)\",\"", noLines)
        targetFile.write(  bladhooghte + "\",\"" + bloei)
        targetFile.write('\n')
        

 
print ("totalMatch:", total)
targetFile.close()
