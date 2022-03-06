import pandas as pd

"""
zad 1. Nazwy hrabstw z najwiekszą i najmniejszą ilością ukończonych liczeń głosów [%]
zad 2. Sprawdzenie średniej procentowej dla stanu Indiana
zad 3. Stworzenie ramki danych ze średnią procentową postępu,
 ORAZ minimalna wartość aktualnych głosów dla każdego stanu
zad 4. Zmiana nazw stanów na duże litery
zad 5. Zapisanie wyników zadania nr.3 jako plik csv
"""
print('----------original data--------------')
gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))
print('---------------------------------')
# Zauważono błąd, w kolumnie percent - wartości nie są poprawnie policzone
# poprawiamy wartości w kolumnie percent

gov_county['percent'] = (gov_county['current_votes'] / gov_county['total_votes']) * 100
# zaokrąglanie wartości w kolumnie
gov_county['percent'] = gov_county['percent'].round(2)
# zauważono ,ze w kolumnie percent wartości posiadają więcej niz 100%,
# usuwamy je - zakładamy ,że to błędne dane
# jeżeli chcemy zachować dane nie pasujące do wytycznych możemy je zapisać w osobnej ramce danych - bad_data
# bad_data = gov_county[gov_county['percent'] > 100]
# print(bad_data)
gov_county = gov_county[gov_county['percent'] <= 100]
# pd.Series = pd.DataFrame
# print(gov_county['percent'])

# ********* ptk 1. rozwiązanie **************
# wyznaczanie zmiennych określających minimalną oraz maksymalną wartość w kolumnie percent
max_vote_percent = gov_county['percent'].max()
min_vote_percent = gov_county['percent'].min()
# wyznaczanie nowej ramki danych z maksymalnymi wartościami
gov_county_max_percent = gov_county[gov_county['percent'] == max_vote_percent]
# print(gov_county_max_percent)
# wyznaczanie nowej ramki danych z minimalnymi wartościami
gov_county_min_percent = gov_county[gov_county['percent'] == min_vote_percent]
# print(gov_county_min_percent)

# wyznaczanie tylko nazw stanów z maksymalną wartością liczeń
max_states_names = gov_county_max_percent['state']
max_states_names = set(max_states_names.tolist())
print(max_states_names)

# ************ PTK 2 *****************

gov_county_indiana_mean_percent = gov_county[gov_county['state'] == 'Indiana']
gov_county_indiana_mean_percent = gov_county_indiana_mean_percent['percent'].mean().round(2)
print(f'srednia wartosc w kolumnie percent dla stanu indiana: {gov_county_indiana_mean_percent}')
# print(gov_county_indiana)

# print(gov_county.head(6))