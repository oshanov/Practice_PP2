nums = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 == 0, nums))

print(*even)

#####################

words = ['hello', 'zdravstvuyte', 'hi', 'salem', 'no','wha', 'way']
longs = list(filter(lambda x: len(x) >= 4, words))
print(longs)

####################
numbers = [-22,53,-9,9,0,4,-32,-1,6]
positive = list(filter(lambda x: x >= 0, numbers))
print(*positive)

################
odd = list(filter(lambda x: x % 2 == 1, nums))
print(*odd)
