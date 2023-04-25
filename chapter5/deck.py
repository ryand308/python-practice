# 堆疊 + 序列 == deque， check palindrome?  deque = speak 'deck'

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True
            #popleft() to left return data, pop() from right.

print(palindrome("a"))    # None
print(palindrome("radar"))# True
print(palindrome("halibut")) # False
print('------------------')
def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome("radar"))  #True
print(another_palindrome("halibut"))#False