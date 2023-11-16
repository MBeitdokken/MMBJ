import matplotlib.pyplot as plt
import numpy as np
from oppgave_a import dict_vaardata_aar, Vaardata
from datetime import datetime

def lengste_null_sekvens(min_liste):
    maks_lengde = 0  # Variabel for å lagre lengden på den lengste sekvensen
    gjeldende_lengde = 0  # Variabel for å lagre lengden på den gjeldende sekvensen

    for tall in min_liste:
        if tall == 0:
            gjeldende_lengde += 1
            # Oppdaterer maks_lengde hvis den gjeldende sekvensen er lengre
            if gjeldende_lengde > maks_lengde:
                maks_lengde = gjeldende_lengde
        else:
            gjeldende_lengde = 0  # Nullstiller den gjeldende sekvensen hvis vi ikke har en 0

    return maks_lengde

def main():
    data = []
    vaardata_aar = dict_vaardata_aar()
    for aar in vaardata_aar:
        for verdi in vaardata_aar[aar]:
            if not np.isnan(verdi.nedbor):
                data.append((verdi.tid, verdi.nedbor))


    gyldige_år = {}
    for tid, nedbør in data:
        år = tid.year
        if år not in gyldige_år:
            gyldige_år[år] = {'nedbørdata': []}
        gyldige_år[år]['nedbørdata'].append(nedbør)

    resultater = []
    for år, data in gyldige_år.items():
        nedbørdata = data['nedbørdata']
        if len(nedbørdata) >= 300:
            lengste_tørke = lengste_null_sekvens(nedbørdata)
            resultater.append((år, lengste_tørke))

    minst_nedbør_år = None
    minst_nedbør = float('inf')
    for år, data in gyldige_år.items():
        nedbørdata = data['nedbørdata']
        total_nedbør = sum(nedbørdata)
        if total_nedbør < minst_nedbør:
            minst_nedbør = total_nedbør
            minst_nedbør_år = år

    if minst_nedbør_år is not None:
        print(f'Året med minst nedbør var {minst_nedbør_år} med totalt {minst_nedbør:.2f} mm nedbør.')
    else:
        print('Ingen gyldige år med nedbørdata funnet.')

    år_liste, tørkeperiode_liste = zip(*resultater)

    plt.figure(figsize=(10, 6))
    plt.bar(år_liste, tørkeperiode_liste)
    plt.xlabel('År')
    plt.ylabel('Lengste Tørkeperiode (dager)')
    plt.title('Lengste Tørkeperiode per År')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()