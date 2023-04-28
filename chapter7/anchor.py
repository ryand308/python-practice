import re
source = '''I wish I may, I wish might
...Have a dish of fish tonight.'''

wish = re.findall("wish", source)
both = re.findall("wish|fish", source)
print(wish, '\n', both)

begin = re.findall('^wish', source) #find is None, because source is ''' I wish ...
start = re.findall ('^I wish', source)
print(begin, '\n', start)

end = re.findall('fish tonight.$', source) # .$ is match ending of any word.
over = re.findall('fish tonight\.$', source) # It's right
print(end , 'different to', over)

title = re.findall('[wf]ish', source) # first word is 'w' or 'f'
print(title)

single = re.findall('[wsh]+', source)
print(single)

W = re.findall('ght\W', source)
print(W)

re.findall("I(?=wish)", source)  # find before wish's 'I'
re.findall("(?<=I) wish", source) # find I after of 'wish'

re.findall('\bfish', source) # \b original string is back word , the result is []
fish = re.findall(r'\bfish', source) # r' ' is close \b \n ... of original string
print(fish)

# appoint the matching output 

m = re.search(r'(dish\b).*(\bfish)', source)
print(m.group())
print(m.groups()) # is tuple

M = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
M.group() # 'dish of fish'
M.groups() # ('a dish', 'fish')
print(M.group('DISH'))
print(M.group('FISH'))