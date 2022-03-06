"""
zad 1. Nazwy hrabstw z najwieksza i najmniejsza iloscia ukonczonych liczen glosow [%]
zad 2. Sprawdzenie sredniej procentowej dla stanu Indiana
zad 3. Stworzenie ramki danych ze srednia procentowa postepu,
    ORAZ minimalna wartosc aktualnych glosow dla kazdego stanu
zad 4. Zmiana nazw stanow na duze litery
zad 5. zapisanie wynikow zadania nr.3 jako plik csv
"""

import pandas as pd

print('---------orginal data---------')
gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))
print('-------------------------')

#poprawienie kolumny percent - ma bledne dane

gov_county['percent'] = gov_county['current_votes'] / gov_county['total_votes'] * 100
#zaokraglenie wartosci w kolumnie
gov_county['percent'] = gov_county['percent'].round(2)
#zauwazono ze w kolumnie precent wart posiada wiecej niz 100%,
#usuwamy je - zakladamy ze to bledne dane
#jezeli chcemy zachowac dane nie pasujace do wytycznych mozemy je zapisac w osobnej ramce danych - bad_data
# bad_data = gov_county[gov_county['percent'] > 100]
# print(bad_data)
gov_county = gov_county[gov_county['percent'] <= 100]
# pd.Series = pd.DataFrame
# print(gov_county['percent'])
# print(gov_county)

#wyznaczenie zmiennych okreslajacych min i max wartosc w kolumnie precent

max_vote_percent = gov_county['percent'].max()
min_vote_percent = gov_county['percent'].min()
print(max_vote_percent)
print(min_vote_percent)
# wyznaczenie ramki danych z max wartosciami
gov_county_max_percent = gov_county[gov_county['percent'] == max_vote_percent]
print(gov_county_max_percent)
# wyznaczenie ramki danych z min wartosciami
gov_county_min_percent = gov_county[gov_county['percent'] == min_vote_percent]
print(gov_county_min_percent)
# print(gov_county.head(6))
#wyznaczanie tylko nazw stanow z max wart liczen

max_states_names = gov_county_max_percent['state']
max_states_names = set(max_states_names.tolist())
print(f"MAX % Value in: {max_states_names}")


# ************ PTK ****************

# gov_county_indiana = gov_county[gov_county['state'] == 'Indiana']
# gov_county_indiana_mean_percent = gov_county_indiana['percent'].mean().round(2)
# print(f'srednia wartosc w kolumnie percent dla stanu indiana: {gov_county_indiana_mean_percent}')
# # print(gov_county_indiana)

# ************ PTK 2 *****************

gov_county_indiana_mean_percent = gov_county[gov_county['state'] == 'Indiana']
gov_county_indiana_mean_percent = gov_county_indiana_mean_percent['percent'].mean().round(2)
print(f'srednia wartosc w kolumnie percent dla stanu indiana: {gov_county_indiana_mean_percent}')
# print(gov_county_indiana)

# print(gov_county.head(6))