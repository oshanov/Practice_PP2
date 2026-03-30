n = int(input())

words = list(map(str, input().split()))
print(max(words, key=len))