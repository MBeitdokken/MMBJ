import pandas as pd
import matplotlib.pyplot as plt

# Les CSV-filen
data = pd.read_csv('liste.csv', delimiter=';')

# Erstatt komma med punktum i den aktuelle kolonnen
column_index = 7  # Indeks for 'Høyeste middelvind (døgn)'
data.iloc[:, column_index] = data.iloc[:, column_index].str.replace(',', '.')

# Konverter til numerisk format, håndter ugyldige verdier som NaN
data.iloc[:, column_index] = pd.to_numeric(data.iloc[:, column_index], errors='coerce')

# Fjern rader med NaN-verdier
data = data.dropna(subset=[data.columns[column_index]])

# Konverter datokolonnen til datetime-format
data['Tid(norsk normaltid)'] = pd.to_datetime(data['Tid(norsk normaltid)'], format='%d.%m.%Y')

# Filtrer ut gyldige år med minst 300 dager med vinddata
gyldige_år = data.groupby(data['Tid(norsk normaltid)'].dt.year).filter(lambda x: len(x) >= 300)

# Finn høyeste middelvind og medianen for vindstyrke for hvert år
resultater = []
for år, gruppe in gyldige_år.groupby(gyldige_år['Tid(norsk normaltid)'].dt.year):
    høyeste_vind = gruppe.iloc[:, column_index].max()
    median_vind = gruppe.iloc[:, column_index].median()
    resultater.append({'År': år, 'Høyeste middelvind': høyeste_vind, 'Median Vind': median_vind})

# Lag en DataFrame av resultatene
resultater_df = pd.DataFrame(resultater)

# Plott resultatene
plt.figure(figsize=(10, 6))
plt.plot(resultater_df['År'], resultater_df['Høyeste middelvind'], label='Høyeste Middelvind')
plt.plot(resultater_df['År'], resultater_df['Median Vind'], label='Median Vind')
plt.xlabel('År')
plt.ylabel('Vindstyrke (m/s)')
plt.title('Høyeste Middelvind og Median Vindstyrke for Hvert År')
plt.legend()
plt.show()
