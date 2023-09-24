import csv
import pandas as pd

data = pd.read_csv('unprocessed/accidents.csv')
data[data['Severity']==4].to_csv('data/accidents.csv', columns=['Start_Time', 'Start_Lat', 'Start_Lng'], index=False)
print('done')