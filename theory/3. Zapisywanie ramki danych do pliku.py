from typing import List

import pandas as pd
# pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
# szerokosc DF(wy<swietlanie)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

indian_food = pd.read_csv('../data/indian_food.csv',
                          usecols=['name', 'ingredients', 'diet', 'prep_time', 'cook_time'], #ograniczenie kolumn w pliku do wskazanych
                          dtype={'name': str,
                                 'prep_time': int})
# df1 = pd.DataFrame(data= [
#     ['Piotr', 'Kowaslki'],
#     ['Adam','Słoń'],
#     ['Maria','Kowalska'],
#     ['Michal','Micha'], ])

#Zapis do pliku Excel
#indian_food.to_excel('../data/indian_food_excel.xlsx', sheet_name='my_food', index=False)

#zapis wyznaczonych kolumn do pliku excel
# print(indian_food.columns)
print(indian_food[['diet', 'ingredients']])

indian_food[['diet', 'ingredients']].to_excel('../data/indian_food_excel.xlsx',
                                              sheet_name='wybrane jedzenie',
                                              index=False)

"""
napisz funkcje która konwertuje plik csv do pliku excel, u
żytkownik powinien móc sam zdefiniować jakie kolumny odczytuje z pliku i jakie chce zapisać
"""

def csv_to_excel_convert(csv_file_path: str, csv_file_columns: List[str],
                         excel_file_output_path: str, excel_file_columns: List[str]):

    input_csv_df = pd.read_csv(csv_file_path,usecols=csv_file_columns)
    input_csv_df.to_excel(excel_file_output_path, columns=excel_file_columns)
   # print(input_csv_df)


#Pierwsza metoda wywołania
# csv_to_excel_convert(csv_file_path='../data/indian_food.csv',
#                      csv_file_columns=['name', 'ingredients', 'diet'],
#                      excel_file_output_path='../data/my_output_file.xlsx',
#                      excel_file_columns=['name','diet']
#                      )

# #Druga metoda wywołania - bez kluczowych znaków[keyword]
# csv_to_excel_convert('../data/indian_food.csv',
#                      ['name', 'ingredients', 'diet'],
#                      '../data/my_output_file.xlsx'
#                      )

#Zapisywanie wielu ramek danych do wybranych arkuszy w pliku Excel

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [3, 4, 5]
})
df2 = pd.DataFrame({
    'C': [1, 2, 3],
    'D': [3, 4, 5]
})

with pd.ExcelWriter('../data/two_dataframes.xlsx') as writer:
    df1.to_excel(writer, sheet_name='df1',index=False)
    df2.to_excel(writer, sheet_name='df2',index=False)