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
    origem = random.choice(banco.contas)                                 # Escolhe uma conta de origem aleatória do array de contas do banco
    destino = random.choice(banco.contas)                                # Escolhe uma conta de destino aleatória do array de contas do banco
    while (origem.id == destino.id):                                     # Caso a mesma conta seja selecionada como origem e destino...
      destino = random.choice(banco.contas)                              # ... É selecionada uma nova conta de destino (até que contas diferentes sejam selecionadas)
    valor = random.randint(1, 150)                                       # Define um valor aleatório para transferência
    transacoes.transferir(origem, destino, valor)                        # Realiza a transferência

numContas = int(input('Insira o número de contas a serem criadas: '))    # Número de contas
numThreads = int(input('Insira o número de threads concorrentes: '))     # Número de threads concorrentes
numTransacoesThread = int(input('Insira o número de transações bancárias por thread: '))  # Número de transações por thread

banco = Banco()                                                          # Salva na variável banco a instância da classe Banco
transacoes = TransacaoBancaria()                                         # Salva na variável transacoes a instância da classe TransacaoBancaria

for x in range(1, numContas + 1):                                        # Realiza um loop entre um e o número de contas especificado pelo usuário
  banco.criarConta(x, random.randint(100, 1050))                         # Cria contas com saldo aleatório (entre 100 e 1050)

threads = []
for _ in range(numThreads):                                              # Realiza um loop para o número de threads especificado pelo usuário
  thread = threading.Thread(target=simularTransacoes, args=(banco, transacoes, numTransacoesThread))  # Cria cada thread para executar a funcao simularTransacoes
  threads.append(thread)                                                 # Adiciona ao array de threads cada thread criada
  thread.start()                                                         # Inicia a execução de cada thread

for thread in threads:
  thread.join()                                                          # Finaliza a execução de cada thread

transacoes.printarLog()                                                  # Exibe o log final
