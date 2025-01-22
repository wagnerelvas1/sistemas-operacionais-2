import threading

class TransacaoBancaria:
  def __init__(self):
    self.semaforo = threading.Semaphore(3)
    self.log = []
    
  def transferir(self, contaOrigem, contaDestino, valor):
    with self.semaforo:
      if not contaOrigem or not contaDestino:
        return None

      if (contaOrigem.id < contaDestino.id):
        primeira = contaOrigem
        segunda = contaDestino
      else:
        primeira = contaDestino
        segunda = contaOrigem
      
      with primeira.lock:
        with segunda.lock:
          if contaOrigem.saldo >= valor:
            contaOrigem.saldo -= valor
            contaDestino.saldo += valor
            self.log.append(f"Transferência de R${valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}. Saldo final conta {contaOrigem.id} = R${contaOrigem.saldo} ; Saldo final conta {contaDestino.id} = R${contaDestino.saldo}")
          else:
            self.log.append(f"Falha na transferência de R${valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}. Saldo insuficiente.")
    
  def printarLog(self):
    for registro in self.log:
      print(registro)