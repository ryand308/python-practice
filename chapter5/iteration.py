# itertools  (http://bit.ly/itertools)

import itertools

for item in itertools.chain([1, 2],['a', 'b']):
    print(item)

for item in itertools.accumulate(range(1,10)):
    print(item)

#----------------------------------------------
def multiply(a, b):
    return a*b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)