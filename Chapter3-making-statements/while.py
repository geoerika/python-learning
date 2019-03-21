a, b = 0, 1

while b < 100 :
  print(b)
  a, b = b, a + b

i = 1
while i < 4 :
  print('\nOuter Loop Iteration:', i)
  i += 1
  j = 1
  while j < 4 :
      print('\tInner Loop Iteration:', j)
      j += 1

