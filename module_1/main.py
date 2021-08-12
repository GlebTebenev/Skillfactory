import pandas as pd

data = pd.read_csv('movie_bd_v5.csv')
pd.set_option('display.max_columns', None)
# print(data)

# фильм с самым большим бюджетом
q_1 = data.original_title[data['budget'] == data['budget'].max()]
print('1. Film with MAX budget -', q_1)

# самый длинный фильм в минутах
q_2 = data.original_title[data.runtime == data.runtime.max()]
print('2. Longest film -', q_2)

# самый короткий в минутах
q_3 = data.original_title[data.runtime == data.runtime.min()]
print('3. Shortest film -', q_3)

# средняя длительность фильмов
q_4 = data.runtime.mean()
print('4. Mean -', q_4)

# медианное значение фильмов
q_5 = data.runtime.median()
print('5. Median -', q_5)

# самый прибыльный
data['profit'] = data.revenue - data.budget
q_6 = data.original_title[data.profit == data.profit.max()]
print('6. Film with MAX profit -', q_6)

# самый убыточный
q_7 = data.original_title[data.profit == data.profit.min()]
print('7. Film with MIN profit -', q_7)

# количество прибыльных фильмов
q_8 = data.original_title[data.profit > 0].count()
print('8. Count of profitable films -', q_8)

# самый прибыльный в 2008 году
q_9 = data.groupby(['release_year'])['profit'].max().loc[2008]
q_9 = data.original_title[data.profit == q_9]
print('9. The most profitable film -', q_9)

# самый убыточный фильм с 2012 по 2014 год
q_10 = data[(data.release_year <= 2014) & (data.release_year >= 2012)].profit.min()
q_10 = data.original_title[data.profit == q_10]
print('10. The most unprofitable film -', q_10)