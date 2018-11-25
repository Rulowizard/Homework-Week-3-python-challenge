import os
import csv

csvpath = os.path.join("election_data.csv")
num_votos=0
#Declaro un diccionario nulo
cand={}

with open(csvpath,"r") as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")

    csv_header = next(csvreader)

    #Creo lista de candidatos
    candidatos= list( set( [candidato[2] for candidato in csvreader ] ))

    #Creo un diccionario
    for candidato in candidatos:
        cand[str(candidato)]=0

    #Me muevo al principio del archivo
    csv_file.seek(0)
    #Desecho la fila de los headers
    csv_header = next(csvreader)

    #Itero dentro del archivo
    for row in csvreader:
        num_votos = num_votos +1
        cand[row[2]] += 1
    
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {num_votos}")
    print("----------------------------")
    mensajes =[ candidato+": "+ str(int(round(cand[candidato]*100/num_votos)))+"% " +"("+str(cand[candidato])+")"  for candidato in candidatos]
    for mensaje in mensajes:
        print(mensaje)
    print("----------------------------")
    ganador = max(cand,key=cand.get) 
    print(f"Winner: {ganador}")
    print("----------------------------")

with open("output_file.csv","w") as csvfile:
    filewriter = csv.writer(csvfile,delimiter=",")
    filewriter.writerow(["Election Results"])
    filewriter.writerow(["----------------------------"])
    filewriter.writerow(["Total Votes:",num_votos])
    filewriter.writerow(["----------------------------"])
    for mensaje in mensajes:
        filewriter.writerow([mensaje])
    filewriter.writerow(["----------------------------"])
    filewriter.writerow(["Winner",ganador])
    filewriter.writerow(["----------------------------"])
