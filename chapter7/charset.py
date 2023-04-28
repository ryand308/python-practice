# utf-8

#               ****** encode ******
snowman = '\u2603'
print(snowman) # '☃'
len(snowman) #len is 1 in unicode

ds = snowman.encode('utf-8')
len(snowman) #len is 3 in utf-8, b'\xe2\x98\x83'

#Different length is the coding to edit that is not the same. If the code's length how to know, when you decode use to.

'''
ds = snowman.encode('ascii')
    Traceback(most recent call last):...
UnicodeEncodeError:...
'''

# encode - ignore
snowman.encode('ascii','ignore')  #b''  take out
# encode - replace
snowman.encode('ascii','replace') #b'?'
# encode - backslashreplace
snowman.encode('ascii', 'backslashreplace') #b'\\u2603'  'ascii'->'Unicode'
# encode - xmlcharefreplace
snowman.encode('ascii','xmlcharrefreplace') #b'&#9731' use to web 'strings'

#               ****** decode ******
place = 'caf\u00e9' # café
type(place)         # <class 'str'>

place_bytes = place.encode('utf-8')
print(place_bytes)
type(place_bytes)   # >class 'bytes'>

place2 = place_bytes.decode('utf-8')
print(place2)

place3 = place_bytes.decode('ascii','replace') # place3 = place_bytes.decode('ascii') 'ascii' Error
print(place3)

place4 = place_bytes.decode('latin-1')
place5 = place_bytes.decode('windows-1252')
print(place4, place5)