import shutil, os

x = open('C:\\git_practice\\Practice6\\file_handling\\default.txt')
print(x.read())         #1) Read and print content

with open('C:\\git_practice\\Practice6\\file_handling\\default.txt', 'a') as f:
    f.write('Some update')
    f.write('Some update 2')            #Append new lines and verify content


print(x.read()) 


if os.path.exists('C:\\git_practice\\default.txt'):
    os.remove('C:\\git_practice\\default.txt') #Delete files safely



if not os.path.exists('C:\\git_practice\\default.txt'):
    shutil.copy('C:\\git_practice\\Practice6\\file_handling\\default.txt', 'C:\\git_practice') #Copy and back up files using shutil


