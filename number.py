def main():
  number = getNumber('Type a number: ')
  print(f'{number} squared is {square(number):,}')

def getNumber(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      pass

def square(number):
  return round(number ** 2, 3)

main()
