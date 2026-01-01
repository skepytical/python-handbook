import re

def main():
  email = input('Type an email: ').strip()
  
  if email := email_regex(email):
    print(f'{email.group()} is a valid email.')
  
def email_regex(email):
  return re.search(r'^\w+@(\w+\.)*\w\.\w+$', email, re.IGNORECASE)

if __name__ == '__main__':
  main()
