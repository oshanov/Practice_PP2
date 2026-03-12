import os, shutil

if not os.path.exists('C:\\git_practice\\some\\my\\new'):   #Find files by extension
    os.makedirs('some\\my\\new')    #Create nested directories
    with open('C:\\git_practice\\some\\my\\new\\example.txt', 'w') as f:
        f.write('something')
    

if os.path.exists('C:\\git_practice\\some'):
    for i in os.walk('C:\\git_practice\\some'):
        print(*i)       #List files and folders

shutil.move(                                            #Move/copy files between directories
    'C:\\git_practice\\some\\my\\new\\example.txt',
    'C:\\git_practice\\Practice6\\directory_management'
)




