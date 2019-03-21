basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']

print('Basket List:', basket)
print('Basket Elements:', len(basket))

basket.append('Damson')
print('Appended:', basket)

print('Last Item Removed:', basket.pop())
print('Basket List:', basket)

basket.extend(crate)
print('Basket Extended:', basket)

basket.sort();
print('Sorted Basket:', basket)


basket.reverse();
print('Reversed Basket:', basket)

del basket[1]
print('Item removed:', basket)

del basket[1:3]
print('Slice removed:', basket)

basket.insert(0, 'Pear')
print('Inserted one in Basket:', basket)

basket.remove('Bun')
print('Removed Bun from Basket:', basket)

print('Index of Grape:', basket.index('Grape'))

print('Number of Apple in Basket:', basket.count('Apple'))






