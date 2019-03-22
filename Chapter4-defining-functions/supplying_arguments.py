def echo(user) :
        print('User: ', user)

echo('Mike')

def echo(user, lang, sys) :
        print('User:', user, 'Language:', lang, 'Platform:', sys)

echo('Mike', 'Python', 'Linux')

echo(lang = 'Python', user = 'Mike', sys = 'Linux')

def echo(user, lang, sys = 'Linux') :
        print('User:', user, 'Language:', lang, 'Platform:', sys)

echo('Mike', 'Python')

echo('Mike', 'Python', 'Windows')


def mirror(user = 'Carole', lang = 'Python') :
        print('\nUser:', user, 'Language:', lang)

mirror()
mirror(lang = 'Java')
mirror(user = 'Tony')
mirror('Susan', 'C++')