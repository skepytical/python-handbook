from sys import exit
import requests


def main():
  try:
    response = requests.get('link')
    response.raise_for_status()

  except requests.RequestException as e:
    exit(f'GET Error: {e}')

  try:
    print(get_content(get_contents(response), 'key'))
  except ValueError:
    exit('JSON error.')
  except KeyError:
    exit('JSON Key error.')



def get_contents(response):
  return response.json()

def get_content(contents, key:str):
  content = [item[key] for item in contents if key in items]
  return content

if __name__ == '__main__':
  main()  
