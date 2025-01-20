from banco import *
from transacao import *
import random
import time

def simularTransacoes(banco, transacoes, numTransacoes):
  for _ in range(numTransacoes):
    origem = random.choice(banco.contas)  # Escolhe uma conta de origem
    destino = random.choice(banco.contas)  # Escolhe uma conta de destino
    valor = random.randint(1, 100)  # Define um valor aleatório para transferência
    transacoes.transferir(origem, destino, valor)  # Realiza a transferência
    time.sleep(random.uniform(0.01, 0.1))  # Introduz um pequeno atraso para simular concorrência

# Configuração inicial
numContas = 5  # Número de contas
numThreads = 10  # Número de threads concorrentes
numTransacoesThread = 20  # Número de transações por thread

banco = Banco()
transacoes = TransacaoBancaria()

for i in range(1, numContas + 1):
  banco.criarConta(i, random.randint(100, 500))  # Cria contas com saldo aleatório

# Execução concorrente
theads = []
for _ in range(numThreads):
  thread = threading.Thread(target=simularTransacoes, args=(banco, transacoes, numTransacoesThread))
  theads.append(thread)
  thread.start()

for thread in theads:
  thread.join()  # Aguarda todas as threads terminarem

# Exibição dos logs das transações realizadas
transacoes.printarLog()