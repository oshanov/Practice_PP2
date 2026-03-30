import json, re

x = '''
{
 "Ali": "ali@gmail.com",
 "Dana": "dana.mail.com",
 "Arman": "arman@mail.ru",
 "Serega": "sergei@mail"
}
'''

data = json.loads(x)

for name, email in data.items():
    if re.search(r'\S+@\S+\.\S+', email):
      print(name)

######################

from datetime import datetime

dates = [
"2026-3-21",
"2026-4-10",
"2026-3-25",
"2026-5-1"
]
parsed = []
for i in dates:
   parsed.append(datetime.strptime(i,'%Y-%m-%d'))

diff = ((max(parsed) - min(parsed)).days)
print(diff)


x = '''
[
 {"name":"Ali","score":90},
 {"name":"Dana","score":85},
 {"name":"Arman","score":95},
 {"name":"Serega","score":70}
]
'''

data = json.loads(x)
# maxim = 0
# for i in data:
#    if i['score'] > maxim:
#       maxim = i['score']

print((max(data, key=lambda x: x['score']))['name'])

x = "Today I have 12 apples and 5 bananas and 100 oranges"
some = re.findall(r'\d+', x)
some = list(some)
for i in some:
   i = int(i)
print(sum(some))
