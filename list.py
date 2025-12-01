def main():
  fruits = [
    "  apple",
    "  banana",
    "  mango"
  ]
  format_fruits = []

  for fruit in fruits:
    format_fruit = fruit.strip().capitalize()

    print(format_fruit)
    format_fruits.append(format_fruit)

  print(', '.join(format_fruits))

main()
