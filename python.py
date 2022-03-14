from operator import index
from numpy import NaN
import pandas as pd

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 1. Відкрити та зчитати файл з даними. 
data = pd.read_csv('Weather.csv')
# print(data)


# 2. Визначити  та  вивести  кількість  записів  та  кількість  полів  у  кожному записі.
count = data.shape
# print(count)

# альтернатива с рядами
# row_count = sum(1 for row in data)
# print(row_count)


# 3. Вивести 5 записів, починаючи з М-ого (число М – місяць народження студента, має бути визначено як змінна), та кожен N-ий запис, де число N визначається як 500 * М для місяця з першого півріччя та 300 * М для місяця з другого півріччя. 

M  = 6
N = 500 * M
M_rows = data.iloc[M : M + 5]

N_rows = data.iloc[N-1::N]
# print(M_rows)
# print(N_rows)

# 4. Визначити та вивести тип полів кожного запису.

# types = data.info()
types = data.dtypes
# print(types)



# 5. Замість поля СЕТ ввести нові текстові поля, що відповідають числу, місяцю та року. Місяць та число повинні бути записані у двоцифровому форматі.

data['Year'], data['Month'], data['Day'] = data['CET'].str.split('-', 2).str 
del data['CET']
# print(data)

# data['Month'] = data['Month'].astype(int)
# data['Day'] = data['Day'].astype(int)

data["Month"]= data.Month.astype(int).map("{:02}".format)
data["Day"]= data.Day.astype(int).map("{:02}".format)
# print(data)


# 6.1. Визначити та вивести кількість днів із порожнім значенням поля Events; 

is_null = data[data[' Events'].isnull()]
print(is_null)

count_day = is_null['Day'].count()
print("** Визначити та вивести кількість днів із порожнім значенням поля Events**")
print("Days with NaN Events:", count_day)


# 6.2. День, у який середня вологість була мінімальною, а також швидкості вітру в цей день

meanhumidity = data[ data[' Mean Humidity'] == data[' Mean Humidity'].min() ]
# print(str)
print("\n** День, у який середня вологість була мінімальною, а також швидкості вітру в цей день**")
print("Day with mean humidity:", meanhumidity["Day"].to_string(index=False))
print("Max Wind SpeedKm/h:", meanhumidity[" Max Wind SpeedKm/h"].to_string(index=False))
print("Mean Wind SpeedKm/h:", meanhumidity[" Mean Wind SpeedKm/h"].to_string(index=False))

# 6.3. Місяці, коли середня температура від нуля до п’яти градусів..


meamtemperature = data[(data['Mean TemperatureC'] >= 0) & (data['Mean TemperatureC'] <= 5.0)]
print(meamtemperature)
print("\nМісяці, коли середня температура від нуля до п’яти градусів")
print("Months:", meamtemperature["Month"].drop_duplicates().to_list())




