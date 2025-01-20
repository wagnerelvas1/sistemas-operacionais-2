import threading

class Conta:
  def __init__(self, id, saldo):
    self.id = id  # Identificador único da conta
    self.saldo = saldo  # Saldo da conta
    self.lock = threading.Lock()  # Lock para sincronização de acesso

  def __str__(self):
    return f"Conta {self.id}: Saldo {self.saldo}"