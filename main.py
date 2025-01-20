from banco import *
from transacao import *
import random
import time

def simularTransacoes(banco, transacoes, numTransacoes):
  for _ in range(numTransacoes):
    origem = random.choice(banco.contas)  # Escolhe uma conta de origem
    destino = random.choice(banco.contas)  # Escolhe uma conta de destino
    while (origem.id == destino.id):
      destino = random.choice(banco.contas)
    valor = random.randint(1, 100)  # Define um valor aleatório para transferência
    transacoes.transferir(origem, destino, valor)  # Realiza a transferência
    time.sleep(random.uniform(0.01, 0.1))  # Introduz um pequeno atraso para simular concorrência

# Configuração inicial
numContas = int(input('Insira o número de contas a serem criadas: '))  # Número de contas
numThreads = int(input('Insira o número de threads concorrentes: '))  # Número de threads concorrentes
numTransacoesThread = int(input('Insira o número de transações bancárias por thread: '))  # Número de transações por thread

banco = Banco()
transacoes = TransacaoBancaria()

for x in range(1, numContas + 1):
  banco.criarConta(x, random.randint(100, 500))  # Cria contas com saldo aleatório

# Execução concorrente
threads = []
for _ in range(numThreads):
  thread = threading.Thread(target=simularTransacoes, args=(banco, transacoes, numTransacoesThread))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()  # Aguarda todas as threads terminarem

# Exibição dos logs das transações realizadas
transacoes.printarLog()
