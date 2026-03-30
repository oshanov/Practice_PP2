vowel = ['a', 'e', 'i', 'o', 'u']

s = input().lower()

if any(char in vowel for char in s):
    print('Yes')

else: 
    print('No')
