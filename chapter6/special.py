# special methods as (magic/Dunder) methods
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.upper() == word2.text.upper()
#------------------------------------------------------
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'+self.text+'")'
#-----------------------------------
first = Word('ha')
second = Word("HA")
third = Word('eh')
#-----------------------------------
print(first==second) #True
print(first==third)  #False

#print(first) #<__main__.Word object at 0x000001C4AC83FFD0>
#------------------------------------------------------------
#>>> first -> Word("ha") #uses __repr__
print(first)  # uses __str__


'''
class Word():
    def __init__(self, text):
        self.text = text
    
    def equals(self, word2):
        return self.text.lower() == word2.text.lower() #lower() 字串小寫
    
#---------------------------------------
first = Word('ha')
second = Word("HA")
third = Word('eh')
#----------------------------------------
print(first.equals(second))  #True
print(first.equals(third))   #False

'''
#the equals() just __qu__ methods

'''
list of magic methods:

Binary Operators:

    Operator     |        Method
+  add                object.__add__
-  subtract           object.__sub__
*  multiply           object.__mul__ 
// floor_divided      object.__floordiv__
/  divided            object.__div__
%  modulo/modulus     object.__mod__
** power              object.__pow__
<< left_shift         object.__lshift__
>> right_shift        object.__rshift__
&  and                object.__and__
|  or                 object.__or__
^  Exclusize or       object.__xor__

Assignment Operators:

    Operator     |        Method
+=                    object.__iadd__
-=                    object.__isub__
*=                    object.__imul__
/=                    object.__idiv__
//=                   object.__ifloordiv__
%=                    object.__imod__
**=                   object.__ipow__
<<=                   object.__ilshift__
>>=                   object.__irshift__
&=                    object.__iand__
|=                    object.__ior__
^=                    object.__ixor__

Unary Operators:

    Operator     |        Method
-                    object.__neg__(self)
+                    object.__pos__(self)
abs()                object.__abs__(self)
~                    object.__invert__(self)
complex()            object.__complex__(self)
int()                object.__int__(self)
long()               object.__long__(self)
float()              object.__float__(self)
oct()                object.__oct__(self)
hex()                object.__hex__(self)

Comparison Operators:

    Operator              |        Method
<  less than(smaller than)  object.__lt__(self, other)
== equals                   object.__eq__(self, other)
<= less than or equals      object.__le__(self, other)
!= not equal                object.__ne__(self, other)
>= greater than or equals   object.__ge__(self, other)
>  more then(greater than)  object.__gt__(self, other)

Other Operators:

      Operator       |        Method
str  string               object.__str__
repr representation       object.__repr__
len  lengths              object.__len__


'''


