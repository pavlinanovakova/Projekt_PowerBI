import pandas as pd

# Načtení dat
porodnost = pd.read_csv('porodnost.csv', delimiter=',', dtype=str, low_memory=False, encoding='utf-8')

# Přejmenování sloupců
porodnost.rename(columns={
    'Věk matky (jednoleté a pětileté skupiny)': 'Věk matky',
    'ČR, regiony, kraje, okresy-Stát': 'Stát',
    'ČR, regiony, kraje, okresy-Region': 'Region',
    'ČR, regiony, kraje, okresy-Okres': 'Okres',
    'ČR, regiony, kraje, okresy-Kraj': 'Kraj',
    'Roky': 'Rok',
    'Hodnota': 'Počet'
}, inplace=True)

# Odstranění nepotřebných sloupců
columns_to_drop = ['Ukazatel', 'IndicatorType', 'VEKM15X', 'PORDITE', 'RODSTAVM',
                   'Uz0123h2.STAT', 'Uz0123h2.REGION', 'Uz0123h2.KRAJ', 'Uz0123h2.OKRES', 'CasR']
porodnost.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Odstranění řádků, kde jsou všechny tři sloupce 'Celkem'
porodnost = porodnost[
    ~(porodnost['Věk matky'].eq('Celkem') & porodnost['Pořadí narození'].eq('Celkem') & porodnost['Rodinný stav matky'].eq('Celkem'))
]

# Konverze typů dat
porodnost['Rok'] = porodnost['Rok'].astype(int)
porodnost['Počet'] = pd.to_numeric(porodnost['Počet'], errors='coerce')

# Export finálního datasetu
porodnost.to_csv('porodnost_cleaned.csv', index=False)

print("Data byla úspěšně zpracována a exportována do 'porodnost_cleaned.csv'")

