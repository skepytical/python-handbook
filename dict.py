def main():
  user = {
    'name': 'Joao silva'
  }

  user['email'] = 'example@mail.com'
  user.update({'id': 1, 'zip': 27587})

  formatted_user = format_user(user)
  print(formatted_user, end='')

  user['password'] = 'flag1234'
  if 'password' in user.keys():
    user.pop('password')    

  print(f'Password: {user.get('password', 'Unknown')}')

  print()
  for value in user.values():
    print(value)

  isDeleted = input('Delete user? Y/N\n').strip().lower()
  user.clear() if isDeleted in 'y' else print('User not deleted.')

  if user:
    for keys, values in user.items():
      print(f'{keys.capitalize()}: {values}')
  else:
    print('Empty user.')

def format_user(user):
  formatted_user = ''
  for key in user.keys():
    formatted_user += f'{key.capitalize()}: {user[key]}\n'
  return formatted_user

main()