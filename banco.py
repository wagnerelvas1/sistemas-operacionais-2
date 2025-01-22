from conta import *

class Banco:
  def __init__(self):
    self.contas = []                      # Array de contas
    
  def criarConta(self, id, saldo):
    conta = Conta(id, saldo)              # Cria um objeto da classe Conta
    self.contas.append(conta)             # Adiciona o objeto no array de contas
    
  def obterConta(self, id):
    for conta in self.contas:
      if conta.id == id:                  # Verifica se o objeto possui o id especificado
        return conta                      # Retorna a conta
      return None                         # Caso não possua retorna none