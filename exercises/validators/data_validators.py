import pandas as pd
#
# """ Napisać klasę / funkcjonalność która dostarczy dataframe z danymi określającymi
# stany z maxymalnymi i minimalnymi wartościami w kolumnie percent
# input: dataframe"""
# gov_county = pd.read_csv('../../data/governors_county.csv')
# # print(gov_county)

class VotesValidator:
    """
    Creates data from gov data with rows with min and max values in col percent for each state
    """
    def __init__(self, input_data: pd.DataFrame):
        self.input_data = input_data

    def _clean_data(self, data_to_be_cleaned: pd.DataFrame):
        cleaned_data = data_to_be_cleaned
        cleaned_data['percent'] = (cleaned_data['current_votes'] / cleaned_data['total_votes']) * 100
        cleaned_data['percent'] = cleaned_data['percent'].round(2)
        cleaned_data = cleaned_data[cleaned_data['percent'] <= 100]
        return cleaned_data

    def min_max_percent(self):
        cleaned_data = self._clean_data(self.input_data)
        cleaned_data = cleaned_data.groupby('state').agg({'percent': ['min', 'max']})
        cleaned_data.columns = ['max_percent', 'min_percent']
        return cleaned_data

