import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def beregn_differanser(liste):
    differanser = []
    for i in range(len(liste) - 1):
        differanse = liste[i + 1] - liste[i]
        differanser.append(differanse)
    return differanser

temperaturer = pd.read_csv('liste.csv', delimiter=';')

# Erstatt komma med punktum i den aktuelle kolonnen
column_index = 5 # Indeks for 'Høyeste middelvind (døgn)'
temperaturer.iloc[:, column_index] = temperaturer.iloc[:, column_index].str.replace(',', '.')

# Konverter til numerisk format, håndter ugyldige verdier som NaN
temperaturer.iloc[:, column_index] = pd.to_numeric(temperaturer.iloc[:, column_index], errors='coerce')

datoer = ["01.08.1980", "02.08.1980", "03.08.1980", ...]

datoer = [datetime.strptime(dato, "%d.%m.%Y") for dato in datoer]

# Beregn differanser i temperaturer
differanser_temperatur = beregn_differanser(temperaturer)

# Plot gjennomsnittstemperaturer
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(datoer, temperaturer, marker='o')
plt.title('Gjennomsnittstemperaturer gjennom året')
plt.xlabel('Dato')
plt.ylabel('Temperatur (°C)')

# Plot differanser i temperaturer
plt.subplot(2, 1, 2)
plt.plot(datoer[:-1], differanser_temperatur, marker='o', color='r')
plt.title('Differanser i temperaturer mellom måneder')
plt.xlabel('Dato')
plt.ylabel('Temperaturdifferanse (°C)')

plt.tight_layout()
