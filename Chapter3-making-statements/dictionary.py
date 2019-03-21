dict = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
print('Dictionary: ', dict)

print( '\nReference:', dict['ref'])

print( '\nKeys:', dict.keys())

del dict['name']
dict['user'] = 'Tom'
print('Dictionary: ', dict)


print( '\nIs there a name key?:', 'name' in dict)
