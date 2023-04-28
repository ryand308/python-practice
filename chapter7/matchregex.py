import re

# match()
source = 'Young Frankenstein'
m = re.match('You',source)

if m: # turn back the object, recheck match
    print(m.group())

#-------------------------------------------------------------
m = re.match('Frank',source) # the match want to from the start

if m:
    print(m.group)
#-------------------------------------------------------------
m = re.search("Frank", source) # used search() can be find
if m:
    print(m.group())
#-------------------------------------------------------------
m = re.match('.*Frank', source) # .* can before 'Frank' any charactoer
if m: #match returns an object
    print(m.group())

#search()
k = re.search('Frank',source)
if k:
    print(k.group())
#--------------------------------------------------------------
#findall()
m = re.findall('n', source)
print(m) # returns an list
print('Found',len(m),'matches')

m = re.findall('n.', source)
print(m) # because the final's 'n' is ending. then use ".?"

m = re.findall('n.?', source)
print(m)
#-------------------------------------------------------------
#split()
m = re.split("n",source)
print(m) # split returns a list
#-------------------------------------------------------------
#sub() just like replace()
m = re.sub("n",'!',source)
print(m) # sub returns a string

