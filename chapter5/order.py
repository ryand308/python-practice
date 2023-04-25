# OrderedDict() 
# 在字典中的鍵的順序是無法預測的；你可以按照a, b, c 順序來加入鍵。

from collections import OrderedDict

quotes = {
    'Moe':'A wise guy, huh?',
    'Larry':'Ow!',
    'Curly':'Nyuk nyuk!',
}

for stooge in quotes:
    print(stooge)
print('--------------------')
quotes = OrderedDict(quotes)

for stooge in quotes:
    print(stooge)