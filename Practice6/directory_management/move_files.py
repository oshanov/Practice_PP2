import os, shutil, re

# os.rename('my_new_directory', 'Some')       #Simple rename
# os.renames('my\\new\\directory', 'some\\peace\\world')

# shutil.move('my_new_directory', '\\trash')

s = r'C:\git_practice\trash'
d = r'C:\git_practice'

for file in os.listdir(s):
    if re.search(r'\.txt$', file):
        shutil.move(os.path.join(s, file), d)