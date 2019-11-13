import csv
import pandas as pd
# with open('test.csv','r',encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
df = pd.read_csv('test.csv')
print(df)