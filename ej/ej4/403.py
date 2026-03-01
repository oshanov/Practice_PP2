def punk(n):
    count = 0
    while count <=n:
        if count % 3 == 0 and count % 4 == 0:
            yield count
        count += 1
z = int(input())
print(*punk(z), sep=' ')