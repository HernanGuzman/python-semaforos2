import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
offset = 40
cantPuentes = 0

cantVacas = 10

cantPuentes = int(input("Ingrese la cantidad de puentes?"))
semaforoPuente = threading.Semaphore(2)


class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

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
    

   
        
        
        
    
    
      

vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

def puente():
    dibujarPuente()
    for v in vacas:
        v.dibujar()
    dibujarPuente()

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()

  for v in range(cantPuentes):
      puente()
  time.sleep(0.2)