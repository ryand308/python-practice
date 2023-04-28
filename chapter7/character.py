# Unicode  https://bit.ly/unicode-plane
'''
lookup() receive the name is not the letter of type, turns to back for character of Unicode.
name() receive the character of Unicode, turns to back from the upper case of the letter.
'''
import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"'%(value, name , value2))

#------------------------------------
unicode_test('A')
# ASCII 
unicode_test('$')
# Unicode
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
#-------------------------------------
unicodedata.name('\u00e9') #'LATIN SMALL LETTER E WITH ACUTE'

place = 'caf\u00e9'
u_umlaut = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
drink = 'Gew'+u_umlaut+'rztraminoer'
print('Now I can finally have my'+drink,'in a '+place)