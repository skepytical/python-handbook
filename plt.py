import pandas as pd
import matplotlib.pyplot as plt

def main():
  create_graph('logs/test.log', 'graphs/graph.png')

def extract_log(filename):
  return pd.read_csv(filename, sep=' ', header=None).rename(columns={0:'tempo', 1:'referencia', 2:'sinal'})

def create_graph(source, destination):
  plt.figure(figsize=(10,6))

  axis = extract_log(source)

  plt.plot(axis['tempo'], axis['referencia'])
  plt.plot(axis['tempo'], axis['sinal'])
  plt.savefig(destination)
  print(f'Gráfico salvo em: {destination}')

main()