from conta import *

class Banco:
  def __init__(self):
    self.contas = []
    
  def criarConta(self, id, saldo):
    conta = Conta(id, saldo)
    self.contas.append(conta)
    
  def obterConta(self, id):
    for conta in self.contas:
      if conta.id == id:
        return conta
      return None
    