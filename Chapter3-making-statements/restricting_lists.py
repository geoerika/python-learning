# Tuple - values in the list cannot be changed
colours_tuple = ('Red', 'Green', 'Red')
a, b, c = colours_tuple

print(a, b, c)


# Set - unique values, duplication not allowed
phonetic_set = {'Alpha', 'Bravo', "Charlie"}

phonetic_set.add('Drum')
print(phonetic_set)

phonetic_set.update('Elves')
print(phonetic_set)

phonetic_set.pop()
print(phonetic_set)

phonetic_set.discard('Drum')
print(phonetic_set)

phonetic_set2 = {'Alpha'}

print(phonetic_set.intersection(phonetic_set2))
print(phonetic_set.difference(phonetic_set2))


zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))

bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print('Set:', bag, '\tLength:', len(bag))
print(type(bag))


print('\nIs Green In Bag Set?:', 'Green' in bag)
print('\nIs Orange In Bag Set?:', 'Orange' in bag)

box = {'Red', 'Purple', 'Yellow'}
print( '\nSet:', box, '\t\tLength', len(box))
print( 'Common to both sets:', bag.intersection(box))

