import pandas as pd
from typing import List

""" Napisac klase / funkcjonalnosc ktora dostarczy dataframe z danymi okreslajacymi
stany z maksymalnymi i minimalnymi wartosciami w kolumnie percent

1) Klasa
    1)Funkcja Min
    2)Funkcja Max"""

print('---------orginal data---------')
input_data = pd.read_csv('../../data/governors_county.csv')
print(input_data.head(6))
print('-------------------------')

class VotesValidator:
    """ OPIS Modulu/Klasy DataFrame
    Creates data from gov data with raws with min and max values in cal percent for each state
    :param input_data: gov. data as pd.DataFrame
    """
    def __init__(self, input_data: pd.DataFrame) -> None:
        self.input_data = input_data

    def _clean_data(self):
        self.input_data['percent'] = self.input_data['current_votes'] / self.input_data['total_votes'] * 100
        self.input_data['percent'] = self.input_data['percent'].round(2)
        self.input_data['percent'] = self.input_data[self.input_data['percent'] <= 100]
        # print(self.input_data)
        self.input_data['test']='test'

    def min_max_percent(self):

        self.input_data = self.input_data.groupby('state').agg({'precent':['min', 'max']})
        self.input_data.columns = ['max_percent', 'min_percent']
        return self.input_data

    def get_indiana_votes(self):
        pass


