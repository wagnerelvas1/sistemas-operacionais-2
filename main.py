# Trabalho desenvolvido por:
# - Ana Clara Souza Gibson
# - Barbara Campos Mercez
# - Robert Barreto Vieira
# - Wagner José Nascimento Relvas

from banco import *
from transacao import *
import random

def simularTransacoes(banco, transacoes, numTransacoes):
  for _ in range(numTransacoes):
    origem = random.choice(banco.contas)
    destino = random.choice(banco.contas)
    while (origem.id == destino.id):
      destino = random.choice(banco.contas)
    valor = random.randint(1, 150)
    transacoes.transferir(origem, destino, valor)

numContas = int(input('Insira o número de contas a serem criadas: '))
numThreads = int(input('Insira o número de threads concorrentes: '))
numTransacoesThread = int(input('Insira o número de transações bancárias por thread: '))

banco = Banco()
transacoes = TransacaoBancaria()

for x in range(1, numContas + 1):
  banco.criarConta(x, random.randint(100, 1050))

threads = []
for _ in range(numThreads):
  thread = threading.Thread(target=simularTransacoes, args=(banco, transacoes, numTransacoesThread))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

transacoes.printarLog()
