def kirkification(fname):
    print(fname +  ' Kirk')

kirkification('Charlie')
kirkification('Donald')

##########################

def greets(name):
    print(f'Hello, {name}')

greets("Mr. Drun")
greets("Teacher")

##########################
def greets(name, sname = 'Oshanov'):
    print(f'Hello, {name} {sname}')

x = input()

greets(x)

###########################
def hello_f(name = "friend"):
    print(f'Hello, {name}')

hello_f()
hello_f(name = 'Ali')

#########################
def naming(lis):
    count = 0
    for x in lis:
        print(x)
        if x % 2 == 0:
            count += 1
    print(f'Even numbers count is {count}')

lsi = [1,2,3,4]
naming(lsi)

#########################
def greets2(person):
    print("Name:", person['name'])
    print("Surname:", person['sname'])

person = dict(name = 'John', sname = 'Snow')
greets2(person)