bool = True
if bool :
    print('Python in Easy Steps')
else :
    pass
    # Statements to be inserted here

title = '\nPython in Easy Steps\n'

for char in title : print(char, end = '')

for char in title :
    if char == 'y' :
        print('*', end = '') # print and asterix instead of y
        continue
    print(char, end = '')

for char in title :
    if char == 'y' :
        print('*', end = '') # inserts an asterix before y
        pass
    print(char, end = '')