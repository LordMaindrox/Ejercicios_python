from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(my_str)

my_str = my_datetime.strftime('%H:%M:%S')
print(my_str)