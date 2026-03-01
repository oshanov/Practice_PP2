# ^ - starts with
# $ - ends with
# . - any character
# * - smth repeats zero or more times
# + - smth repeats one or more times
# {n} - smth repeats EXACTLY n times
# \s - matches to whitespaces
# \S - matches non-whitespace char
# [abcd] - matches a single char that in list
# [^abcd] - matches a single char that not in list
# [0-9] - matches any digit in this range
# [0-5][0-9] - matches any digit in range 00 - 59
# re.search('pat', str) - finds exactly one and first match
# re.match('pat',str) - finds one match at the beginning
# re.fullmatch('pat',str) - checks if pattern is active all over string
# re.findall('pat', str) - finds all matches and creates a list of them
# re.split('pat', str, maxsplit) - returns a list where the string has been split at each match
# re.sub('pat', substr, str, count) - replaces the matches with the text of your choice
import re

txt = "The rain in Spain"
x = re.search('^The.*Spain$', txt)
if x: 
    print('yes')
else:
    pass

print(len(re.findall('ai',txt)))

print(re.findall('\w+', txt))

print(re.split('\s', txt, 1))

print(re.sub('\s', '20', txt, 2))
###################
# hand = open('trash\some.txt')
# for i in hand:
#     i = i.rstrip()
#     if re.search('^X-\S+:', i):
#         print(i)
# ####################
# x = 'MY fav 2 numbers are 41 and 67'
# y = re.findall('[0-9]+', x)
# print(y)
# print(re.findall('[A-Z]+', x))

# print(re.match(r'MY', x))                       #FINDS ONLY AT THE BEGINNING
# print(re.fullmatch(r'\d+', x))                  #CHECKS IF ALL STR GOES OVER PATTERN
# print(re.split(r'\s+', x))                      #DIVIDES ALL STR BY SPACES
##########################

# letter = 'From: ali.oshanovv@gmail.com Sat Jan 5 09:14:16 2007'
# x = re.findall('\S+@\S+', letter)
# print(x)
#########################

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)

# sppos = data.find(' ', atpos)
# print(sppos)

# mail = data[atpos+1 : sppos]
# print(mail)

# words = data.split()
# mail = words[1]
# pieces = mail.split('@')
# name = pieces[0]
# print(name)

# x = re.findall('\S+@[^ ]+', data)
# print(*x)

fufu = 'We received $10.00 from cookies today'
y = re.findall('\$[0-9.]+', fufu)
print(y)