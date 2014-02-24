#datetime test; http://www.pythonforbeginners.com/basics/python-datetime-time-examples

import datetime

date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
date = datetime.datetime.now().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H-%M")

print date_time
print date
print time 