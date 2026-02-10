numbers = [1,2,3,4,5,6,7,8]
doubled = list(map(lambda x: x * 2, numbers))
print(*doubled)

########################

words = ['apple', 'banana', 'cherry']
upper_words = list(map(lambda x: x.upper(), words ))
print(*upper_words)

#####################

w2 = ['supremacy', 'Kazakhstan', 'KBTU']
len = list(map(lambda x: len(x), w2))
print(*len)

##################

lsi = [1,2,3,4,5,6,7,8,9,10]
even = list(map(lambda x : x % 2 == 0, lsi))
print(*even)

###################

