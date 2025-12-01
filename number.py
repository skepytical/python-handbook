def main():
  number = square(getNumber())
  print(f"{number} squared is {number:,}")

def getNumber():
  return float(input("Type a number: "))

def square(number):
  return round(number ** 2, 3)

main()
