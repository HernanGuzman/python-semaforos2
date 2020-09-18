import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
offset = 40

cantVacas = 6
cantLiebres = 3
cantTortugas = 1
semaforoPuente = threading.Semaphore(4)


class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.7)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      if self.posicion == inicioPuente -4:
        semaforoPuente.acquire()
      if self.posicion == inicioPuente + largoPuente:
        semaforoPuente.release()
      if self.posicion == offset:
        self.posicion = 0
      self.avanzar()

class Liebre(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.8, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐰') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      if self.posicion == inicioPuente -4: 
        semaforoPuente.acquire()
      if self.posicion == inicioPuente + largoPuente:
        semaforoPuente.release()
      if self.posicion == offset:
        self.posicion = 0
      self.avanzar()


class Tortuga(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.2, 0.4)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐢') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      if self.posicion == inicioPuente -4: 
        semaforoPuente.acquire()
      if self.posicion == inicioPuente + largoPuente:
        semaforoPuente.release()
      if self.posicion == offset:
        self.posicion = 0
      self.avanzar()
    

vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

liebres = []
for i in range(cantLiebres):
  l = Liebre()
  liebres.append(l)
  l.start()

tortugas = []
for i in range(cantTortugas):
  t = Tortuga()
  tortugas.append(t)
  t.start() 

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  for l in liebres:
    l.dibujar()
  for t in tortugas:
    t.dibujar()
  dibujarPuente()
  time.sleep(0.2)
