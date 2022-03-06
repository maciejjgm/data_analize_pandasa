import pandas as pd
from typing import List

""" Napisac klase / funkcjonalnosc ktora dostarczy dataframe z danymi okreslajacymi
stany z maksymalnymi i minimalnymi wartosciami w kolumnie percent

1) Klasa
    1)Funkcja Min
    2)Funkcja Max"""

print('---------orginal data---------')
gov_county = pd.read_csv('../data/governors_county.csv')
print(gov_county.head(6))
print('-------------------------')


class VotesValidator():
    pass


    def __init__(self):
        pass


    def csv_to_excel_convert(csv_file_path: str, csv_file_columns: List[str], excel_file_output_path: str, excel_file_columns: List[str]):
                        input_csv_df = pd.read_csv(csv_file_path, usecols=csv_file_columns)
                        input_csv_df.to_excel(excel_file_output_path, columns=excel_file_columns)

print('wykonanie csv to excel conv')
VotesValidator.csv_to_excel_convert()