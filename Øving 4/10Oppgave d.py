"""
Plott snødybde og trend i samme plott, med året skisesongen starter på x-aksen og antall dager med skiføre på 
y-aksen. For å plotte trenden, bruk formelen y = ax+b til å regne ut to punkter, ett for året datasettet starter 
og ett for året datasettet slutter. Inkluder bare år hvor det er data om snødybde for mesteparten av skisesongen,
det må være data for minst 200 dager i hver skisesong.
"""

from oppgave_a import dict_sesong_en_variabel
from oppgave_b import sesong_snodybde_over_20
from funksjoner_fra_del1 import trend
import matplotlib.pyplot as plt
import numpy as np


def main():
    dict_sesong_snodybde = dict_sesong_en_variabel('snodybde')

    gyldige_sesonger = {}
    for sesong, snodybde_list in dict_sesong_snodybde.items():
        if len(snodybde_list) >= 200:
            gyldige_sesonger[sesong] = snodybde_list
            print(f'Gyldig sesong {sesong}/{sesong+1} med {len(snodybde_list)} dager med data')
        else:
            print(f'Fjerner sesong {sesong}/{sesong+1} {len(snodybde_list)} fordi det er for få dager med snødybde')
    
    skifore = sesong_snodybde_over_20(gyldige_sesonger)
    for sesong in skifore:
        print(f'Sesong {sesong}/{sesong+1} har {skifore[sesong]} dager med skiføre')
    x_liste, y_liste = zip(*skifore.items())
    x_liste = list(map(int, x_liste))
    y_liste = list(map(int, y_liste))
    a, b = trend(x_liste, y_liste)

    x_array = np.array(x_liste)

    print(f'a = {a}, b = {b}')
    plt.figure(figsize=(10, 6))
    plt.plot(x_liste, y_liste)
    plt.plot(x_liste, a * x_array + b)
    plt.xlabel('År')
    plt.ylabel('Antall Dager med Skiføre')
    plt.title('Antall Dager med Skiføre per År')
    plt.xticks(rotation=45)
    plt.show()

    pass


if __name__ == '__main__':
    main()