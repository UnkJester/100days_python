# import csv
# with open(file='weather_data.csv') as file:
#     lines = file.readlines()
#
# data = lines[1:]
# print(data)
#
# with open('weather_data.csv') as file:
#     csv_data = csv.reader(file)
#     temperatures = []
#     for row in csv_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data.to_dict())
# temps = data['temp'].to_list()
# print('{:0,.2f}'.format(sum(temps) / len(temps)))
# print(data[data.temp == data['temp'].max()])
# print(data[data.day == 'Monday'].temp * 9/5 + 32)

# create a dataframe
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict)
print(data2)
data2.to_csv('new_data.csv')