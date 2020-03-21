import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #Yo siempre uso BCM, vosotros podeis usar BOARD si prefieren.
GPIO.setwarnings(False)

def hacer(pin, algo):
    if algo == "out":
       GPIO.setup(pin, GPIO.OUT)
       GPIO.output(pin, GPIO.LOW)
    elif algo == "in":
       GPIO.setup(pin, GPIO.IN)

reles = [3,4,14,15,17,18,27,22,23,24,10,9,25,11,8,7] #Aqui van los numeros de los GPIOS donde enchufaste tus reles, al ser posible en orden, para asi tenerlos ordenados.


def ejemplo():
   for rele in reles:
      hacer(rele,"out")
      time.sleep(1)
   for releoff in reles:
      hacer(releoff, "in")
      time.sleep(1)

def quitarTodos():
   for x in reles:
      hacer(x,"in")

def kill():
    quitarTodos()
    quit()

if __name__ == '__main__':
    try:
        ejemplo()
    except KeyboardInterrupt:
        kill()

