from statistics import mean
from sys import exit
def main():
  grades = [10, 9, 10]
  print(round_mean(grades))

def round_mean(numbers:list):
  try:
    if [float(number) for number in numbers]:
      return round(mean(numbers), 4)
  except ValueError:
      exit('Not number(s).')

if __name__ == '__main__':
  main()
