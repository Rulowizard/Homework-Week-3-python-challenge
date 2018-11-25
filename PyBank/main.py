import os
import csv

csvpath = os.path.join("budget_data.csv")

#Variable que guarda el número de meses
months=0
#Variable que guarda el ingreso neto
net_profit=0
#Arreglo que guardará las variaciones entre los meses y el valor del mes
#Se define de un tamaño de 2 columnas y 0 filas (está vacío)
#Más adelante el código agregara las filas de información
month_change_2=[[0 for x in range(2)] for y in range(0) ] 

#Variable temporal que guarda el valor de la Perdida/Ganancia del mes anterior
prev_month=0

#Flag para saltarme el primer elemento en el análisis de las variaciones
flag= False

with open(csvpath,"r") as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        income= float(row[1])
        months = months +1
        net_profit = net_profit + income

        if flag==False:
            flag= True
        elif flag==True:
            #Este pedazo de código se encarga de calcular las variaciones entre los meses
            #El primer valor es la variación mientras que el segundo guarda la info del mes
            month_change_2.append([income-prev_month,row[0]])
        #Actualizo la información de la variable temporal
        prev_month=income

    #Uso comprenhension lists para iterar sobre la suma de los meses
    avg_change = sum(row[0] for row in month_change_2)/len(month_change_2)
    #Usando CL encuentro el máximo
    max_val = max(row[0] for row in month_change_2)
    #Usando CL encuentro el mes del máximo
    max_mes= [month[1] for month in month_change_2 if month[0]==max_val ]
    #Usando CL encuentro el máximo
    min_val = min(row[0] for row in month_change_2)
    #Usando CL encuentro el mes del máximo
    min_mes= [month[1] for month in month_change_2 if month[0]==min_val ]
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total net Profit/Losses: {net_profit}")
    print(f"Average Change: {avg_change}")
    print(f"Greatest Increase in Profits: {max_mes} ({max_val}) ")
    print(f"Greatest decrease in Profits: {min_mes} ({min_val}) ")

with open("output_file.csv","w") as csvfile:
    filewriter = csv.writer(csvfile,delimiter=",")
    filewriter.writerow(["Financial Analysis"])
    filewriter.writerow(["----------------------------"])
    filewriter.writerow(["Total Months:",months])
    filewriter.writerow(["Total net Profit/Losses:", net_profit])
    filewriter.writerow(["Average Change:", avg_change])
    filewriter.writerow(["Greatest Increase in Profits:", max_mes, max_val ])
    filewriter.writerow(["Greatest decrease in Profits:", min_mes, min_val ])