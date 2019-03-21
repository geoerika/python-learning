a = input( 'Enter a Number: ')
b = input( 'Now enter another number: ')

sum = a + b
print( '\nData Type sum: ', sum, type(sum))

sum = int(a) + int(b)
print( '\nData Type sum: ', sum, type(sum))

sum = float( sum )
print( '\nData Type sum: ', sum, type(sum))

sum = chr(int(sum))
print( '\nData Type sum: ', sum, type(sum))