import pandas as pd

from exercises.validators.data_validators import VotesValidator

#print docstring
#print(VotesValidators.__doc__)

input_data_gov = pd.read_csv('../../data/governors_county.csv')

votes_validator = VotesValidator(input_data_gov)
print(votes_validator.min_max_percent())