def main():
  a = 1
  b = 4
  if a == b:
    print("Equal numbers.")
  else:
    print("Unequal numbers.")

  if 1 <= a <= 100:
    print(f"{a} is a number inclusively between 1 and 100")

  if (even(b)):
    print(f"{b} is even.")

    match b:
      case 1:
        print(f"B is 1.")
      case 2 | 3:
          print(f"B is 2 or 3")
      case _:
        print(f"B is not 1, 2, nor 3.")

def even(number):
  return number % 2 == 0

# def isEven(number):
#   return True if number % 2 == 0 else False

main()
