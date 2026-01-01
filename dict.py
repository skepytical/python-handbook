def main():
  user = {
    'name': 'Joao silva'
  }

  celsius_measures = {
  '1': '1',
  '2': '50',
  '3': '100'  
}
  
  celsius_values = [float(celsius_value) for celsius_value in celsius_measures.values()]
  kelvin_list = celsius_to_kelvin(celsius_values)
  
  for c, k in zip(celsius_measures.values(), kelvin_list):
    print(f'{c} C is {k} K')
  print()  

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

def celsius_to_kelvin(celsius_list:list):
  kelvin_list = [(celsius + 273.15) for celsius in celsius_list]
  return kelvin_list

main()
