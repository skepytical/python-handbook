import json

def main():
  name = input('type a name: '.capitalize()).strip().title()
  print('\'Commas\'')
  print(hello())
  print(hello(name))
  print(hello()[:5])
  print(hello(name)[-3:]) 
  
  n1 = 1
  n2 = 2
  print(n1, n2)

  # Print a new line
  print()
  
  decimals = json_open('jsons/decimals.json')

  # Print a value in json
  print(items_formatter(decimals))

def hello(name='world'):
  # print('Hello,', name, end='\n', sep=' ')
  return f'Hello, {name}'

def json_open(path):
  with open(path, 'r') as file:
    return json.load(file)

def items_formatter(nested_list):
  return f'{', '.join(str(value) for key in nested_list for i in nested_list[key] for value in i)}'

if __name__ == '__main__':
  main()
