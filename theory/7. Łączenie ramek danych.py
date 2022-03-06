import glob

import pandas as pd
pd.set_option('display.max_columns',50)
# szerokość DF (wyświetlanie)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', 100)

df = pd.DataFrame(
    {
        'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michał'],
        'kolumna_nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha']
    }
)



df2 = pd.DataFrame(
    data=[
        ['Piotr', 'Kowalski', 22],
        ['Adaś', 'Sowik', 12],
        ['Marysia', 'Słowik', 23],
        ['Michał', 'Micha', 54],
    ], columns=['imie', 'nazwisko', 'wiek']
)

# print(df)
# print("---------")
# print(df2)

# łączenie za pomoca funkcji merge, używając częsci wspólnych

merge_df_df2_outer = pd.merge(df,
                        df2,
                        left_on='kolumna_imie',
                        right_on='imie',
                        how='outer')

# merge_df_df2 = pd.merge(df,
#                         df2,
#                         on='kolumna_imie',
#                         #left_index=True
#                         how='outer'
#                         )
# print(merge_df_df2)

# *** Łączenie ramek danych o różnych rozmiarach przy pomocy concat()


# df3 = pd.DataFrame(
#     {
#         'kolumna_imie': ['Piotr', 'Adam', 'Maria', 'Michał'],
#         'kolumna_nazwisko': ['Kowalski', 'Słowik', 'Kowalska', 'Micha']
#     }
# )
#
#
#
# df4 = pd.DataFrame(
#     data=[
#         ['Piotr', 'Kowalski', 22],
#         ['Adaś', 'Sowik', 12],
#         ['Marysia', 'Słowik', 23],
#         ['Michał', 'Micha', 54],
#     ], columns=['imie', 'nazwisko', 'wiek']
# )
# concat_df3_df4 = pd.concat([df3,df4])
# print(concat_df3_df4)


"""
Zadanie
"""

# for file in glob.glob('../data/*.csv'):
#     print(file)
    # list = [file]
    # x1 = list[0]
    # x2 = list[1]
    # x3 = list[2]
    # print(x1)
    # print(f'lista nr 2:{x2}')
    # print(x3)


"""
połącz dane zawierające się w plikach (csv) z
 wybranego folderu do jednego Dataframe'u
"""

def merge_selected_files(path: str):
    df_list = []
    for file_path in glob.glob(path):
        df_list.append(pd.read_csv(file_path))
    return pd.concat(df_list)

print(merge_selected_files('../data/*.csv'))