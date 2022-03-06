import pandas as pd

df = pd.DataFrame({'kolumna_imie':['Piotr','Adam','Maria','Michal'],
                    'kolumna_nazwisko': ['Kowalski', 'Słon', 'Kowalska','Micha']
                   },
                    index = ['male','male','female', 'male'])
print(df)

df1 = pd.DataFrame(data= [
    ['Piotr', 'Kowaslki'],
    ['Adam','Słoń'],
    ['Maria','Kowalska'],
    ['Michal','Micha']

])
# print(df1)
# print(df.head(2))
# print(type(df))
#Lista kolumn w Ddataframe
print(df.columns)

#Konwersja do słownika
# print(df.to_dict('records'))
print(df.to_dict())

#Konwersja do słownika
my_dict = {'kolumna_imie': {'male': 'Michal', 'female': 'Maria'},
            'kolumna_nazwisko': {'male': 'Micha', 'female': 'Kowalska'}}

df_from_dict = pd.DataFrame.from_dict(my_dict)
print(df_from_dict)

#Pandas dtypes
#print(df.dtypes)

df['kolumna_imie'] = 'ADAM'
df_second = df.copy()
df['kolumna_imie'] = 'MARIA'
print(df)
print(df_second)

series = pd.Series(data=['Piotr','Adam','Maria','Aga'])
print(series)
# print(type(series))
# print(series.dtypes)

my_list = ['Piotr','Adam','Maria','Agata']
series_from_my_list = pd.Series(my_list)
print(series_from_my_list)

#konwersja pd.Series do pd.Dataframe

df_from_series = series_from_my_list.to_frame()
df_from_series2 = pd.DataFrame(series_from_my_list)
print(df_from_series)
print(type(df_from_series))
print(df_from_series2)
print(type(df_from_series2))




