import threading

class TransacaoBancaria:
  def __init__(self):
    self.semaforo = threading.Semaphore(3)  # Limita a 3 transferências simultâneas
    self.log = []  # Log de transações
    
  def transferir(self, contaOrigem, contaDestino, valor):
    """Realiza a transferência de uma conta para outra com controle de concorrência."""
    with self.semaforo:  # Limita a 3 transferências simultâneas
      if not contaOrigem or not contaDestino or contaOrigem == contaDestino:
        return

      # Ordena as contas para evitar deadlocks
      if (contaOrigem.id < contaDestino.id):
        primeira = contaOrigem
        segunda = contaDestino
      else:
        primeira = contaDestino
        segunda = contaOrigem
      
      # Adquire os locks para garantir acesso exclusivo
      with primeira.lock:
        with segunda.lock:
          if contaOrigem.saldo >= valor:  # Verifica se há saldo suficiente
            contaOrigem.saldo -= valor
            contaDestino.saldo += valor
            self.log.append(f"Transferência de {valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}. Saldo final: {contaOrigem} | {contaDestino}")
          else:
            self.log.append(f"Falha na transferência de {valor} da Conta {contaOrigem.id} para Conta {contaDestino.id}: saldo insuficiente.")
    
  def printarLog(self):
    for registro in self.log:
      print(registro)