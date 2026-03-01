import json

a = json.loads(input())
b = json.loads(input())

ans = []

def diff(a,b,path):
    if type(a) == dict and type(b) == dict:
        for i in sorted(set(a.keys()) | set(b.keys())):
            if i in a:
                na = a[i]
            else:
                na = '<missing>'
            if i in b:
                nb = b[i]
            else:
                nb = '<missing>'

            new_path = i if path == "" else path + '.' + i
            diff(na,nb, new_path)
    
    else:
        if a != b:
            if a != '<missing>':
                a = json.dumps(a, separators=(',', ':'))
            if b != '<missing>':
                b = json.dumps(b, separators=(',', ':'))

            ans.append(path + ' : ' + str(a) + ' -> ' + str(b))

diff(a,b,"")
if ans:
    for s in sorted(ans):
        print(s)
else:
    print("No differences")
                