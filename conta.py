import threading

class Conta:
  def __init__(self, id, saldo):
    self.id = id
    self.saldo = saldo
    self.lock = threading.Lock()
    