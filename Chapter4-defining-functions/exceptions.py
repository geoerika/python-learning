title = 'Python in Easy Steps'

try :
      print(titel)
except NameError as msg :
      print(msg)

except( NameError, IndexError) as msg :
      print(msg)

day = 32

try :
      if day > 31 :
            raise ValueError('Invalid Day Number')
      # More statements to execute get added here
except ValueError as msg :
      print('The program found an', msg)
finally:
      print('But Today is Beautiful Anyway')

