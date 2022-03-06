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


# ************ PTK 3 *****************
"""
zad 3. Stworzenie ramki danych ze srednia procentowa postepu,
    ORAZ minimalna wartosc aktualnych glosow dla kazdego stanu
"""
#Grupowanie danych - groupby()
#maksymalna wartosc w kolumnie current votes dla kazdego z stanow
max_current_votes_per_state_df = gov_county.groupby(['state'], as_index=False)['current_votes'].max()
min_current_votes_per_state_df = gov_county.groupby(['state'], as_index=False)['current_votes'].min()
mean_percent_per_state_df = gov_county.groupby(['state'], as_index=False)['percent'].mean()

#iterowanie po grupach
#max_current_votes_per_state_df = gov_county.groupby(['state']
#print(group)

print(max_current_votes_per_state_df)
print('-----')
print(min_current_votes_per_state_df)
print(mean_percent_per_state_df)

#grupowanie oraz agregacja - osobne obliczenia dla
#wybranych kolumn w wybranej grupie danych wewnatrz dataframe'u

agg_gov_county = gov_county.groupby('state').agg({'current_votes': 'max',
                                          'total_votes': 'min',
                                          'percent': 'mean'})
agg_gov_county.columns = ['max_current_votes',
                          'min_total_votes',
                          'mean_percent']
print(agg_gov_county)

#zadanie 3 rozwianiaznie:

gov_county_mean_min_group = gov_county.groupby('state').agg({'percent': 'mean', 'current_votes': 'min'})
gov_county_mean_min_group.columns = ['mean_percent', 'min_current_votes']
print(gov_county_mean_min_group)

# Zadanie 4

gov_county['state'] = gov_county['state'].str.upper()
print(gov_county)

#Zadanie 5

gov_county_mean_min_group.to_csv('../data/gov_county_mean_min_group.csv')
# gov_county['J'] = '80%'
# gov_county['T'] = '20%'
# # print(gov_county.groupby('state'))
# gov_county = gov_county.drop_duplicates('state')
# print(gov_county[['state','J','T']])

""" Napisac klase / funkcjonalnosc ktora dostarczy dataframe z danymi okreslajacymi
stany z maksymalnymi i minimalnymi wartosciami w kolumnie percent"""

