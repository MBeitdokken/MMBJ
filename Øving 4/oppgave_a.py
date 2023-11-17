from datetime import datetime
import csv
import numpy as np

#klasse for å håndere data fra csv filen
class Vaardata:
    def __init__(self, navn, stasjon, tid, snodybde, nedbor, temperatur, skydekke, middelvind):
        self.navn = navn
        self.stasjon = stasjon
        self.tid = datetime.strptime(tid, '%d.%m.%Y')
        self.snodybde = float(snodybde)
        self.nedbor = float(nedbor)
        self.temperatur = float(temperatur)
        self.skydekke = float(skydekke)
        self.middelvind = float(middelvind)
    
    def __str__(self):
        formatert_dato = self.tid.strftime('%d.%m.%Y')
        return f'{self.navn} {self.stasjon} {formatert_dato} {self.snodybde} {self.nedbor} {self.temperatur} {self.skydekke} {self.middelvind}'

#leser csv filen og returnerer en liste med alle verdiene   
def les_fil(filnavn):
    with open(filnavn, 'r') as file:
        linjer = list(csv.reader(file, delimiter=';'))
        vaardata = []
        for linje in linjer[1:-1]:
            linje = ['nan' if value == '-' else value.replace(',', '.') for value in linje]
            vaardata.append(Vaardata(*linje))
    return vaardata

#lager en dictionary med alle verdier for et år
def dict_vaardata_aar():
    vaardata = les_fil('snoedybder_vaer_en_stasjon_dogn.csv')
    vaardata_aar = {}
    for data in vaardata:
        aar = data.tid.year
        if aar not in vaardata_aar:
            vaardata_aar[aar] = []
        vaardata_aar[aar].append(data)
    for aar in vaardata_aar:
        vaardata_aar[aar] = sorted(vaardata_aar[aar], key=lambda data: data.tid)
    return vaardata_aar

#lager en dictionary med alle verdier for en sesong
def dict_vaardata_sesong(filnavn = 'snoedybder_vaer_en_stasjon_dogn.csv'):
    vaardata = les_fil(filnavn)
    vaardata_sesong = {}
    for data in vaardata:
        aar = data.tid.year
        sesong = None
        if data.tid.month >= 10:
            sesong = aar
        elif data.tid.month <= 5:
            sesong = aar-1
        if sesong:
            if sesong not in vaardata_sesong:
                vaardata_sesong[sesong] = []
            vaardata_sesong[sesong].append(data)
    for sesong in vaardata_sesong:
        vaardata_sesong[sesong] = sorted(vaardata_sesong[sesong], key=lambda data: data.tid)
    return vaardata_sesong

#lager en dictionary med alle verdier for en måned i hver år
def dict_vaardata_maaned_aar():
    vaardata = les_fil('snoedybder_vaer_en_stasjon_dogn.csv')
    vaardata_maaned_aar = {}
    for data in vaardata:
        aar = data.tid.year
        maaned = data.tid.month
        if aar not in vaardata_maaned_aar:
            vaardata_maaned_aar[aar] = {}
        if maaned not in vaardata_maaned_aar[aar]:
            vaardata_maaned_aar[aar][maaned] = []
        vaardata_maaned_aar[aar][maaned].append(data)
    for aar in vaardata_maaned_aar:
        for maaned in vaardata_maaned_aar[aar]:
            vaardata_maaned_aar[aar][maaned] = sorted(vaardata_maaned_aar[aar][maaned], key=lambda data: data.tid)
    return vaardata_maaned_aar

#lager en dictionary for alle år, hvor året er nøkkelen og en liste med alle verdier for en variabel.
#f.eks. alle verdier for snødybde for alle år dict_aar_en_variabel('snodybde')
def dict_aar_en_variabel(variabel1):    
    dict_aar = {}
    vaardata = dict_vaardata_aar()
    for aar in vaardata:
        dict_aar[aar] = [getattr(data, variabel1) for data in vaardata[aar] if not np.isnan(getattr(data, variabel1))]
    return dict_aar

#lager en dictionary for alle sesonger, hvor sesongen er nøkkelen og en liste med alle verdier for en variabel.
#f.eks. alle verdier for snødybde for alle sesonger dict_sesong_en_variabel('snodybde')
def dict_sesong_en_variabel(variabel1):
    dict_sesong = {}
    vaardata = dict_vaardata_sesong()
    for sesong in vaardata:
        dict_sesong[sesong] = [getattr(data, variabel1) for data in vaardata[sesong] if not np.isnan(getattr(data, variabel1))]
    return dict_sesong

#lager en dictionary for alle måneder i hvert år, hvor året er nøkkelen og en liste med alle verdier for en variabel.
#f.eks. alle verdier for snødybde for alle måneder i hvert år dict_maaned_aar_en_variabel('snodybde')
def dict_maaned_aar_en_variabel(variabel1):
    dict_maaned_aar = {}
    vaardata = dict_vaardata_maaned_aar()
    for aar in vaardata:
        dict_maaned_aar[aar] = {}
        for maaned in vaardata[aar]:
            dict_maaned_aar[aar][maaned] = [getattr(data, variabel1) for data in vaardata[aar][maaned] if not np.isnan(getattr(data, variabel1))]
    return dict_maaned_aar


def main():
    #demo av funksjonene
    dict_aar = dict_aar_en_variabel('snodybde')
    print(dict_aar[2019])
    print("\n")

    dict_sesong = dict_sesong_en_variabel('snodybde')
    print(dict_sesong[2019])
    print("\n")

    dict_maaned_aar = dict_maaned_aar_en_variabel('snodybde')
    print(dict_maaned_aar[2019][10])
    print("\n")
    
    vaardata_aar = dict_vaardata_aar()
    print(vaardata_aar[2019][0])

    vaardata_sesong = dict_vaardata_sesong()
    print(vaardata_sesong[2019][0])

    vaardata_maaned_aar = dict_vaardata_maaned_aar()
    print(vaardata_maaned_aar[2019][10][0])

if __name__ == "__main__":
    main()


