from node import Node
from row import Row

row = Row()

row.queue(13)
row.queue(5)
row.queue(38)
row.queue(34)
row.queue(90)
print(row)

_temp = row.dequeue()
print(_temp)
print(row)

_temp = row.dequeue()
print(_temp)
print(row)

_temp = row.dequeue()
print(_temp)
print(row)

_temp = row.dequeue()
print(_temp)
print(row)

_temp = row.dequeue()
print(_temp)
print(row)
