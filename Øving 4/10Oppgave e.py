import matplotlib.pyplot as plt
import numpy as np
from oppgave_a import dict_vaardata_aar, Vaardata
import matplotlib.pyplot as plt
import csv


def main():
    data = []
    vaardata_aar = dict_vaardata_aar()
    for aar in vaardata_aar:
        for verdi in vaardata_aar[aar]:
            if not np.isnan(verdi.nedbor):
                data.append((verdi.tid, verdi.nedbor))


   
    def plante_vekst(temperatur_liste):
        summen = 0
        for element in temperatur_liste:
            if element >= 5:
                ny_sum = element - 5
                summen += ny_sum
        return summen

    
    def les_fil(filnavn):
        with open(filnavn, 'r') as file:
            linjer = list(csv.reader(file, delimiter=';'))
            vaardata = []
            for linje in linjer[1:-1]:
                linje = ['nan' if value == '-' else value.replace(',', '.') for value in linje]
                vaardata.append(Vaardata(*linje))
        return vaardata

    

    gyldigeår = {}
    for tid, temperatur in data:
        year = tid.year
        if year not in gyldigeår:
            gyldigeår[year] = {'temperaturdata': []}
        gyldigeår[year]['temperaturdata'].append(temperatur)

    
    plantevekst_per_år = []

    for year, data in gyldigeår.items():
        temperaturdata = data['temperaturdata']
        if len(temperaturdata) >= 300:
            plantevekst_verdi = plante_vekst(temperaturdata)
            plantevekst_per_år.append((year, plantevekst_verdi))
            print(f"Planteveksten for år {year} er {plantevekst_verdi}")

    
    år, plantevekst = zip(*plantevekst_per_år)
    plt.figure(figsize=(10,6))
    plt.plot(år, plantevekst, marker='o')
    plt.xlabel('År')
    plt.ylabel('Plantevekst')
    plt.title('Plantevekst for hvert år')
    plt.xticks (rotation=45)
    plt.show()

if __name__ == "__main__":
    main()