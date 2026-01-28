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

  print()
  
  decimals = json_open('jsons/decimals.json')

  for nest in decimals.values():
    for d in nest:
      print(*d)

def hello(name='world'):
  # print('Hello,', name, end='\n', sep=' ')
  return f'Hello, {name}'

def json_open(path):
  with open(path, 'r') as file:
    return json.load(file)

if __name__ == '__main__':
  main()
