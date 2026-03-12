f = open('C:\\git_practice\\Practice6\\file_handling\\default.txt', 'r')
print(f.read())             #method for reading the content of the file

print('-'*30)########################################################################

with open('C:\\git_practice\\Practice6\\file_handling\\default.txt') as f:
    print(f.read())

print('-'*30)########################################################################

f = open('C:\\git_practice\\Practice6\\file_handling\\default.txt', 'r')
print(f.readline()) 
print(f.readline()) 
f.close()               #You must write a close statement in order to close the file

print('-'*30)########################################################################

with open('C:\\git_practice\\Practice6\\file_handling\\default.txt ') as f:
    print(f.read(7))
    for i in f: 
        print(i.rstrip())
