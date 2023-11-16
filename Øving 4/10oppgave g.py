from oppgave_a  import dict_aar_en_variabel
import matplotlib.pyplot as plt

"""
Finn antall penværsdager for hvert år og plott dette. Man kan finne antall penværsdager 
ved å sjekke gjennomsnittlig skydekke. Hver dag med verdi 3 eller lavere er en penværsdag.
Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data 
for minst 300 dager for at et år skal være gyldig.
"""

def main():
    dict_aar_skydekke = dict_aar_en_variabel('skydekke')

    gyldige_aar = {}
    for aar, skydekke_list in dict_aar_skydekke.items():
        if len(skydekke_list) >= 300:
            gyldige_aar[aar] = sum(1 for skydekke in skydekke_list if skydekke <= 3)

    aar_liste, penvaersdager_liste = zip(*gyldige_aar.items())

    plt.figure(figsize=(10, 6))
    plt.plot(aar_liste, penvaersdager_liste)
    plt.xlabel('År')
    plt.ylabel('Antall Penværsdager')
    plt.show()

if __name__ == "__main__":
    main()