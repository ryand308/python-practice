
import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'

data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'+\
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24]) # LL 是格式化字串，負責指數unpack()解釋它的byte輸入序列
    print("Valid PNG, width", width, "height", height)
else:
    print("Not a valid PNG")

# valid_png_header 裡面有 8-byte序列，標記有效的 PNG 檔的開頭
# width 是從第 16-20個byte取出的，height 第21-24個byte

print(data[16:20])
print(data[21:24])
print(0x9a)
print(0x8d)
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

print(struct.unpack('>2L', data[16:24])) #  >2L 代表 >LL
print(struct.unpack('>16x2L6x', data))
'''
使用big-endian 整數格式 (>)
跳過16個byte (16x)
讀取8個byte一兩個不帶符號的長整數(2L)
跳過最後的6個byte(6x)
'''