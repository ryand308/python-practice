# special charcacter
import string
import re

printable = string.printable
print(len(printable))
#print(printable) all the printable word
number = re.findall('\d', printable)
print( number )

char = re.findall('\w', printable)
print( char )

space = re.findall('\s', printable)
print( space )

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
find = re.findall('\w', x)
print( find )