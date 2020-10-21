# Built Heart
from turtle import *

color('red', 'pink')
begin_fill()
left(140)
forward(111.65)
for i in range(200):
    right(1)
    forward(1)
left(120)
for i in range(200):
    right(1)
    forward(1)
forward(111.65)
end_fill()
done()

from comp import list_s

print(list_s)
import random
import datetime
import timeit

print('-'.join(str(n) for n in range(10000)))
print(timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000))

# x = random.randint(1,10)
# print(x)
#
# date = datetime.datetime.now()
# print(date)
#
#
# dob = datetime.date(1991,3,11)
#
# today = datetime.date.today()
# age = today-dob
# print(age)