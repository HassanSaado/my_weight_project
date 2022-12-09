
import datetime
import csv
import pandas as pd
from matplotlib import pyplot as plt


def getDatum():
    return datetime.date.today()


def getViktUser():
    regVikt = input("Vill registrera dagens vikt? svara (ja/nej)")
    if regVikt == "ja":
        return input("Vad är din vikt idag oxe?(inga , tack):")


def sparaVikt():
    idag = getDatum()  # skriver in dagens datum och vikt
    vikt = getViktUser()
    #filepath = os.path.join("/", "Users", "User", "Onedrive", "Python projekt", "Min_vikt1.csv")
    with open("min_vikt1.csv", "a", newline="") as f:
        datum_vikt = (idag, vikt)
        writer = csv.writer(f)
        writer.writerow(datum_vikt)
        f.close


def openCsv():
    #filepath = os.path.join("/", "Users", "User", "Onedrive", "Python projekt", "Min_vikt1.csv")
    df = pd.read_csv("min_vikt1.csv", header=None)  # databehandling
    df = df.iloc[1:]
    return df


def getDataPandas():
    data = openCsv()
    yvalue = data[1].tolist()
    yvalue = [float(x) for x in yvalue]
    xvalue = data[0].tolist()
    return xvalue, yvalue


def plott():
    plotta = input("vill du ha graf på din vikt? svara med (ja/nej):")
    if plotta == "ja":
        xDatum, yVikt = getDataPandas()
        fig, ax = plt.subplots()
        ax.plot(xDatum, yVikt, 'o-')
        ax.set_title("Vikt över tid", fontsize=16)
        ax.set_xlabel("Datum", fontsize=14)
        ax.set_ylim((65, 78))
        ax.set_ylabel("Vikt[kg]", fontsize=14)
        plt.show()
    else:
        print("jalla JiaaaPP Bizzlord")


def main():
    sparaVikt()
    plott()


main()
