import threading

class TransacaoBancaria:
  def __init__(self):
    self.semaforo = threading.Semaphore(3)                    # Limita a 3 transferências simultâneas
    self.log = []                                             # Log de transações
    
  def transferir(self, contaOrigem, contaDestino, valor):
    with self.semaforo:                                       # Utiliza o semáforo para limitar o número de transferências simultâneas
      if not contaOrigem or not contaDestino:                 # Caso haja algum erro com as contas
        return None

      if (contaOrigem.id < contaDestino.id):                  # Definindo a conta com menor id como primeira e maior como segunda, para evitar deadlock
        primeira = contaOrigem
        segunda = contaDestino
      else:
        primeira = contaDestino
        segunda = contaOrigem
      
      with primeira.lock:                                     # Aplicando locks
        with segunda.lock:
          if contaOrigem.saldo >= valor:                      # Verifica se há saldo suficiente
            contaOrigem.saldo -= valor
            contaDestino.saldo += valor
            self.log.append(f"Transferência de R${valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}. Saldo final conta {contaOrigem.id} = R${contaOrigem.saldo} ; Saldo final conta {contaDestino.id} = R${contaDestino.saldo}")
          else:
            self.log.append(f"Falha na transferência de R${valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}. Saldo insuficiente.")
    
  def printarLog(self):
    for registro in self.log:
      print(registro)