# first_name = 'Ana'
# last_name = 'Yunita'
# full_name = f'{first_name} {last_name}'
# print(full_name)

from datetime import datetime

today = datetime.now()
# print(today)

date_time = today.strftime('%Y-%m-%d-%H-%M-%S')

print(date_time)