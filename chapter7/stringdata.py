n = name = 'Curtis Kai'
a = age = 35
s = sex = "male"
t = tall = 174.5
'''
%s String
%d Decimal
%x Hex
%o Octal
%f Fix point(float)
%e Scientific
%g General
%% Percentage
'''
print("What you name\n My name is %s,\n So how old!\n I'm %d years old and %s."%(name, age, sex))

print(f"What you name\n My name is {name},\n So how old!\n I'm {age} years old and {sex}.")

print("sex is {2},name is {0}, age is {1}, tall is {3}".format(name, age, sex, tall))
#---------------------------------------------------------------------------------------------
dic ={'n':'Curits Kai', 'a':35, 's':'male', 't':174.5}

print("{0[n]}, {0[a]}, {0[s]}, {0[t]}, {1}".format(dic,'other'))

print('{n}, {a}, {s}, {t}'.format(**dic))

print(f"{dic['n']}, {dic['t']}")
#--------------------------------------------------------------------
'''
 :s String format
 :d Decimal format
 :f fix point number format
 .
 .
 .
'''

print('{0:s} is {3:0.2f}cm, {2:s} and age is {1:d}'.format(n, a, s, t))