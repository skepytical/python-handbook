number = 1

def main():
  global number
  number = 2
  print(f'Sum is {sum(number, number)}')

def sum(a, b):
  return a + b
  
main()
