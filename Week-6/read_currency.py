import csv
with open('./Data/currencyrates.csv','r') as file:
     
    lines=csv.reader(file)
    for line in lines:
         if 'Bangladesh' in line[0]:
             BDT=float(line[3])
             doller=float(line[2])
    taka=50 * BDT
    US_doller=doller*10000
    print(BDT)
    print(taka)
    print(US_doller)
        
      