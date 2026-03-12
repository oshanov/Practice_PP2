with open('C:\\git_practice\\Practice6\\file_handling\\def2.txt', 'a') as f: #adds(appedns) some text
    f.write(' Now file has more content')

with open('C:\\git_practice\\Practice6\\file_handling\\def2.txt') as f:
    print(f.read())

###################################

with open('C:\\git_practice\\Practice6\\file_handling\\def2.txt', 'w') as f: #overwrites all data to your message
    f.write('Oops! I`ve deleted all content')

with open('C:\\git_practice\\Practice6\\file_handling\\def2.txt') as f:
    print(f.read())

################################### New filing

with open('C:\\git_practice\\Practice6\\file_handling\\mynew.txt', 'x') as f:
    pass