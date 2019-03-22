# a generator is a specific function that returns a "generator object" to the caller rather than a data value.
# retains the state of the function when it was last called

# yield

# repeatedly calling the generator object with the next() function continues execution of the function until it raises an exception

def incrementer() :
    i = 1
    while True :
        yield i
        i += 1

inc = incrementer()

print(next(inc))
print(next(inc))
print(next(inc))

def fibonacci_generator() :
    a = b = 1
    while True :
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

for i in fib :
    if i > 100 :
        break
    else :
        print('Generated:', i)