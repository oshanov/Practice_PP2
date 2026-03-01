import json

J = json.loads(input())

q = int(input())


def parse(s):
    res = []
    i = 0

    while i < len(s):
        if s[i].isalpha() or s[i] == '_':
            j = i
            while j < len(s) and (s[j].isalnum() or s[j] == '_'):
                j += 1
            res.append(s[i:j])
            i = j

        elif s[i] == '[':
            j = i + 1
            while s[j] != ']':
                j += 1
            res.append(int(s[i+1:j]))
            i = j + 1

        else:
            i += 1

    return res


for _ in range(q):
    query = input()
    cur = J

    try:
        for step in parse(query):
            cur = cur[step]

        print(json.dumps(cur, separators=(',', ':')))
    except:
        print("NOT_FOUND")