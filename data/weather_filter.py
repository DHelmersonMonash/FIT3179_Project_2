import csv
import pandas as pd

data = pd.read_csv('unprocessed/weather.csv')
print()
data[data['Severity']=='Severe'].to_csv('data/weather.csv', columns=['Type', 'StartTime(UTC)', 'EndTime(UTC)', 'LocationLat', 'LocationLng'], index=False)
print('done')