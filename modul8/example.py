# map all objects to letter "a"

all_objects = input('provide letters: ')
print(''.join(map(lambda letter: 'a', all_objects)))

# map odd objects to letter "a" and even objects to letter 'b'
all_objects = input('provide letters: ')
print(''.join(map(lambda letter: 'a' if letter[0] % 2 else 'b', enumerate(all_objects))))
