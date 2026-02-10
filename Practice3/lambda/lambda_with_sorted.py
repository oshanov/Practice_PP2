words = ['apple','kiwi','ok', 'university']
sorted_words = list(sorted(words, key= lambda a: len(a)))
print(sorted_words)
asorted_words = list(sorted(words, key= lambda a: len(a),reverse=True))
print(asorted_words)


######################

numbers = [7,65,3,57,9,0,2,-4,6,-100]
sorted_numbers = list(sorted(numbers, key=lambda x: x))
print(sorted_numbers)

######################

anti_sorted_numbers = list(sorted(numbers, key=lambda x:x, reverse=True))
print(anti_sorted_numbers)

#######################
wrds = ['apple', 'knockout', 'salam', 'norway', 'amaz']
last = list(sorted(wrds, key=lambda x: x[0]))
print(last)

#######################
tuples = [(1, 3), (2, 2), (4, 1)]
srt = list(sorted(tuples, key=lambda x: x[-1]))
print(srt)