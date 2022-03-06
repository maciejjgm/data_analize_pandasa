import pandas as pd

print('---------orginal data---------')
gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))
print('-------------------------')

#Grupowanie danych - groupby()
#maksymalna wartosc w kolumnie current votes dla kazdego z stanow
max_current_votes_per_state_df = gov_county.groupby()