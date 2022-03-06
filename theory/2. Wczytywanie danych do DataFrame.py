import pandas as pd
# pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',50)
# szerokość DF (wyświetlanie)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', 100)

read_settings = {"name":str,"prep_time":int}
indian_food = pd.read_csv('../data/indian_food.csv',
                          dtype= read_settings)
                            # header = 4
                          # index_col=2)

# print(indian_food.shape)
# print(indian_food)
# print(indian_food['prep_time'].dtypes)

# https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv
# df_serv = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')
# print(df_serv)

indian_food_excel = pd.read_excel('../data/indian_food_excel.xlsx',
                                  sheet_name=0)

xlsx = pd.ExcelFile('../data/indian_food_excel.xlsx')
# df = pd.read_excel(xlsx)
# odczytywanie wybranej zakłdaki Excel z obiektu ExcelFile
# print(xlsx.parse(sheet_name='Sheet1'))
#pokazywanie nazw akruszy w wybranym pliku excel
# print(xlsx.sheet_names)
allowed_sheets = ['food','names','Sheet1']
current_file_sheet_list = xlsx.sheet_names
# print(current_file_sheet_list)
"""
odczytać/pokazać jako dataframe tylko arkusze których nazwy istnieją w
 allowed_sheets w pliku excel
"""
# [print(xlsx.parse(sheet)) for sheet in current_file_sheet_list if sheet in allowed_sheets]

#  List Comprehension
new_list_for=[]
for sheet in allowed_sheets:
    new_list_for.append(sheet.upper())
print(new_list_for)

print('List Comprehension:')
new_list = [sheet.upper() for sheet in allowed_sheets]
print(new_list)

# PICKLE read and write
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html
indian_food.to_pickle('../data/indian_food_pickle.pkl')
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html
new_indian_food = pd.read_pickle('../data/indian_food_pickle.pkl')