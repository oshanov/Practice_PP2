#First: Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

x = datetime.now()
y = x - timedelta(days=5)
print(y)

#Second: Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta
x = date.today()
yes = x - timedelta(days=1)
tom = x + timedelta(days=1)
print(yes, x, tom)

#Third: Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta
x = datetime.now()
nomicro = x - timedelta(microseconds=x.microsecond)
print(nomicro)

#Fourth: Write a Python program to calculate two date difference in seconds.
from datetime import datetime
x = input()
x1 = datetime.strptime(x, "%d.%m.%Y" )   #Formating from string to date
y = input()
x2 = datetime.strptime(y, "%d.%m.%Y" )

diff = abs((x2 - x1).total_seconds())
print(int(diff))




