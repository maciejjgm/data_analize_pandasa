import pandas as pd
# pd.set_option('display.max_rows', 500)
from pandas._testing import iloc

pd.set_option('display.max_columns', 50)
# szerokosc DF(wy<swietlanie)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

# gov_county = pd.read_csv('../data/governors_county.csv')
# print('_______Orgina data________')
# print(gov_county.head(5))
# print('data len:')
# print(len(gov_county))
# print('__________________________')

#wyznaczenie czesci ramki danych dla wybranego stanu - filtorwanie przez stan
# print(gov_county['state'] == 'Delaware')
# #wyznaczenie czesci ramki danych dla wybranego stanu - filtorwanie przez stan Delaware only
# only_delaware_df = gov_county[gov_county['state'] == 'Delaware']
# print(only_delaware_df)

# gov_county = gov_county[(gov_county['current_votes'] > 1000)
#                         & (gov_county['total_votes'] > 15000)
#                         & (gov_county['state'] != 'West Virginia')]

# gov_county = gov_county[(gov_county['state'] == 'Delaware')
#                         | (gov_county['state'] == 'Indiana')]
# print(gov_county)

#wyznaczenie czesci ramki danych na podstawie elementow z listy
# my_states = ['Delaware','Indiana']
# gov_county = gov_county[gov_county['state'].isin(my_states)]
# #przyklad z negacja "~"
# gov_county = gov_county[~gov_county['state'].isin(my_states)]
#wyznaczenie dla wartosci które zawiejraą część wybranej frazy (regex)
# gov_county = gov_county[gov_county['state'].str.contains('awa')]

#wyznaczenie danych dla dla warunku gdzie dane zawieraja szukana fraze na poczatku
# gov_county = gov_county[gov_county['state'].str.contains('^Del')]
# gov_county = gov_county[gov_county['state'].str.contains('delaware',
#                                                           regex=False,
#                                                           case=False)] #wylacza sprawdzanie wilkosci liter
# gov_county = gov_county[gov_county['state'].str.startswith('De')]
#
# #wyznaczenie danych dla dla warunku gdzie dane zawieraja szukana fraze na poczatku
# # gov_county = gov_county[gov_county['state'].str.contains('^Del')]
# # gov_county = gov_county[gov_county['state'].str.endswith('ana')]
# #
# # print(gov_county)

#wyznaczanie rzedow okreslonych indexem numerycznym

#iloc[index_number, column_number]
#wyznaczenie pierwszego rzedu jako pd.Series (gdy jest jeden rzad), lub [[]] jako DataFrame
# print(gov_county, iloc[0])

#wyznaczenie zakresu ramki danych w osi Y (wg indexu)

print('nowy print')
# print(gov_county.iloc[0:,2:4])

#wyznaczanie zakresu ramki danych w osi Y (wg indexu)
# print(gov_county.iloc[0:5])
# wyznaczanie ostanich 3 rzędów
# print(gov_county.iloc[-3:])

# wyznaczanie rzędów zaczynających się od 3 dla kolumny 4
# print(gov_county.iloc[3:,4])


#wyznaczenie konkret wartosci w okreslonej lini dla okreslonej kolumny
# col_idx = 2
# print(gov_county.iloc[3, col_idx])


# ****************** loc[index_name, column_name

# df = pd.DataFrame({'kolumna_imie':['Piotr','Adam','Maria','Michal'],
#                     'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska','Micha']
#                    },
#                     index = ['male','male','female', 'male'])
# print(df)
# print(df.loc['male'])
# kobitky = df.loc['female']
# print(f'Wyszukaj po kobitkach: {kobitky}')

# ****** loc[index_name, column_name] *******

# df_male_female_index = pd.DataFrame({'kolumna_imie':['Piotr','Aadam','Maria','Michal'],
#                    'kolumna_nazwisko':['Kowalski','Słon','Kowalska','Micha']},
#                   index=['male','male','female','male'])
# print(df_male_female_index)

# print(df_male_female_index.loc['male'])

df_names_index = pd.DataFrame({'kolumna_imie':['Piotr','Aadam','Maria','Michal'],
                   'kolumna_nazwisko':['Kowalski','Słon','Kowalska','Micha']},
                  index=['pawel','adam','maria','ada'])
print(df_names_index)

# zakres indexu od wyznaczonych wartości (nazw indexu)
print(df_names_index.loc['pawel':'maria'])

# zakres indexu od wyznaczonych wartości (nazw indexu) dla danej kolumny
# print(df_names_index.loc['pawel':'maria', 'kolumna_nazwisko'])
# print(df_names_index.loc['pawel':'maria'][['kolumna_nazwisko']])

