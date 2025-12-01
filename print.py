def main():
  name = input("type a name: ".capitalize()).strip().title()
  print("\"Commas\"")
  hello()
  hello(name)

def hello(name="world"):
  print(f"Hello, {name}")
# print("hello,", name, end="\n", sep=" ")

main()
