import pandas as pd
# pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
# szerokosc DF(wy<swietlanie)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

gov_county = pd.read_csv('../data/governors_county.csv')

print('Orginal data:')
print(gov_county.head(5))
print('DF INFO')
print(gov_county.info())
print('___________________')

# gov_county['current_total_votes_sum'] = gov_county['']

#Przypisywanie wartosci z innej kolumny do nowej
gov_county['prev_votes'] = gov_county['current_votes']
# Odejmowanie wybranej wartosci
gov_county['prev_votes'] = gov_county['prev_votes'].sub(100)
# gov_county['prev_votes'] = gov_county['prev_votes'] - 100
# gov_county['prev_votes'] = gov_county['prev_votes'] - gov_county['total_votes']
#suma dwoch kolumn
gov_county['random_votes'] = gov_county['prev_votes'] + gov_county['total_votes']
#mnozenie
gov_county['random_votes'] = gov_county['prev_votes'].mul(100)
#dzielenie: div()
gov_county['random_votes'] = gov_county['prev_votes'].div(100)

#wartość minimalna w danej kolumnie
print(gov_county['total_votes'].min())
print(gov_county['total_votes'].max())

# pokazanie sumy wszystkich wartosci w kolumnie
print(sum(gov_county['total_votes']))

#srednia wszystkich wartosci w kolumnie
print(gov_county['total_votes'].mean())


#mediana wszystkich wartosci w kolumnie
print(gov_county['total_votes'].median())

# print(gov_county.head(5))