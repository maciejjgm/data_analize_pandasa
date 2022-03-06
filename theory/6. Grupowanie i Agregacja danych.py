import pandas as pd

print('---------orginal data---------')
gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))
print('-------------------------')

#Grupowanie danych - groupby()
#maksymalna wartosc w kolumnie current votes dla kazdego z stanow
max_current_votes_per_state_df = gov_county.groupby(['state'], as_index=False)['current_votes'].max()

#iterowanie po grupach
#max_current_votes_per_state_df = gov_county.groupby(['state']
#print(group)

print(max_current_votes_per_state_df)

#grupowanie oraz agregacja - osobne obliczenia dla
#wybranych kolumn w wybranej grupie danych wewnatrz dataframe'u

agg_gov_county = gov_county.groupby('state').agg({'current_votes': 'max',
                                          'total_votes': 'min',
                                          'percent': 'mean'})
agg_gov_county.columns = ['max_current_votes',
                          'min_total_votes',
                          'mean_percent']
print(agg_gov_county)