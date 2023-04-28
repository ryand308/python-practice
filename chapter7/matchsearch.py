import re #regex

result = re.match('You', 'Young Frankenstein')
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstenin')


'''
    match()
    search()
    findall()
    split()
    sub()
'''
# comment add
Substring ='string'
 
 
String1 ='''We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))