def main():
  fruits = [
    '  apple',
    '  banana',
    '  mango'
  ]
  format_fruits = []

  fruits.extend(['watermelon', 'pineapple'])
  fruits.insert(0, 'peach')
  fruits.reverse()

  format_fruits = [fruit.strip().capitalize() for fruit in fruits if len(fruit) > 0]

  print(', '.join(format_fruits))

  print(f'Apple appeared {format_fruits.count('Apple')} times')
  format_fruits.clear()

main()
