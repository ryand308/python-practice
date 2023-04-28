# byte and bytearray
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

ascii = b'\x61'
print(ascii)
ascii = b'\x68\x71'
print(ascii)

print(b'\x01abc\xff')

#the_bytes[1] = 127 bytes make value is tuple of type.this's TypeError:...
the_byte_array[1] = 127
print(the_byte_array)
#-----------------------------------------
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
print(the_bytes)