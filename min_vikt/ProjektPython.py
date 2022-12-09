import datetime
import csv
import pandas as pd
from matplotlib import pyplot as plt


idag = datetime.date.today()                 #skriver in dagens datum och vikt
spara_vikt = input("Vill registrera dagens vikt? svara (ja/nej)")
if spara_vikt == "ja":  
    vikt = input("Vad är din vikt idag oxe?(inga , tack):")

    with open("Min_vikt1.csv", "a", newline="") as f:
            datum_vikt = (idag,vikt)
            writer = csv.writer(f)
            writer.writerow(datum_vikt)
            f.close


df = pd.read_csv("Min_vikt1.csv", header=None) #databehandling
print(df.head())
df = df.iloc[1:]
yvalue = df[1].tolist() 
yvalue = [float(x) for x in yvalue]
xvalue = df[0].tolist() 


plotta = input("vill du ha graf på din vikt? svara med (ja/nej):")

if plotta == "ja":                  #plotten
    fig, ax = plt.subplots()
    ax.plot(xvalue, yvalue, 'o-')
    ax.set_title("Vikt över tid", fontsize=14)
    ax.set_xlabel("Datum", fontsize=14)
    ax.set_ylabel("Vikt[kg]", fontsize=14)
    plt.show()
else: 
    print("jalla JiaaaPP Bizzlord")
  


    




