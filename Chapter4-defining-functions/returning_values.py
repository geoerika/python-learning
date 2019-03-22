def sum(a, b) :
  return a + b

total = sum(8, 4)
print('Eight Plus Four Is:', total)

print('Eight Plus Four Is:', sum(8, 4))

def sum(a, b) :
  if a < 5 :
    return
  return a + b

total = sum(3, 4)
print('Total:', total)

num = input('Enter An Argument:')

def square(num) :
    if not num.isdigit() :
        return 'Invalid Entry'
    num = int(num)
    return num * num

print(num, 'squared is: ', square(num))