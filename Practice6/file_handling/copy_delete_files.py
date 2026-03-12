import os

if os.path.exists('C:\\git_practice\\Practice6\\file_handling\\mynew.txt'): #Checks if file exists
    os.remove('C:\\git_practice\\Practice6\\file_handling\\mynew.txt')  #Deletes the file
else:
    print('File does not exist')

######################################

if os.path.exists('C:\\git_practice\\Practice6\\file_handling\\default.txt'):
    print('yes')
else:
    print('no')

#######################################

# os.makedirs('folder1/folder2/folder3')      #Creates many nested folders

if not os.path.exists('C:\\git_practice\\Practice6\\file_handling\\newfolder'):
    os.mkdir('C:\\git_practice\\Practice6\\file_handling\\newfolder')       #Creates new folder

    
if os.path.exists('C:\\git_practice\\Practice6\\file_handling\\newfolder'):
    os.rmdir('C:\\git_practice\\Practice6\\file_handling\\newfolder')       #Deletes folder
else:
    print('No such directory')



