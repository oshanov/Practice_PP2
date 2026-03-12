import os

if not os.path.exists('my_new_directory'):
    os.mkdir('my_new_directory')        #makes one folder

if not os.path.exists('my\\new\\directory'):
    os.makedirs('my\\new\\directory')       #makes nested folders

#######################

print("String format :", os.getcwd())       #Возвращает текущий путь к папке (стр)
print("Byte string format :", os.getcwdb())     #Возвращает текущий путь (байты)

######################

print("Current directory :", os.getcwd())
os.chdir('my\\new')         # Changing directory
print("Current directory :", os.getcwd())

######################

print(os.listdir('C:\\git_practice\\Practice6'))        #Lists all files and subdirectories in the given path (non-recursive)
for x in os.walk('C:\\git_practice\\Practice6'):
    print(x)

#######################

#os.rmdir('')       Removes empty directory

print(os.path.exists('C:\\git_practice'))
print(os.path.isdir('C:\\git_practice'))        #Same as os.path.exists
    