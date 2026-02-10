n = int(input())

lsi = []
for i in range(n):
    lsi.append(input())

first_index = dict()
    
for i in range(n):
    s = lsi[i]
    if s not in first_index:
        first_index[s] = i
    

for key, value in first_index.items():
    print(key, value + 1)