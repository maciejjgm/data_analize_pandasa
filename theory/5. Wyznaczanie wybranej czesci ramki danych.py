import pandas as pd
# pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
# szerokosc DF(wy<swietlanie)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

gov_county = pd.read_csv('../data/governors_county.csv')
print('_______Orgina data________')
print(gov_county.head(5))
print('data len:')
print(len(gov_county))
print('__________________________')

#wyznaczenie czesci ramki danych dla wybranego stanu - filtorwanie przez stan
# print(gov_county['state'] == 'Delaware')
# #wyznaczenie czesci ramki danych dla wybranego stanu - filtorwanie przez stan Delaware only
# only_delaware_df = gov_county[gov_county['state'] == 'Delaware']
# print(only_delaware_df)

# gov_county = gov_county[(gov_county['current_votes'] > 1000)
#                         & (gov_county['total_votes'] > 15000)
#                         & (gov_county['state'] != 'West Virginia')]

gov_county = gov_county[(gov_county['state'] == 'Delaware')
                        | (gov_county['state'] == 'Indiana')]
print(gov_county)

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
gov_county = gov_county[gov_county['state'].str.startswith('De')]

#wyznaczenie danych dla dla warunku gdzie dane zawieraja szukana fraze na poczatku
# gov_county = gov_county[gov_county['state'].str.contains('^Del')]
gov_county = gov_county[gov_county['state'].str.endswith('ana')]

print(gov_county)