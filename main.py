# Importieren der notwendigen Module
import machine
import time
from machine import Pin
from time import sleep
from servo import Servo
import random

# Definieren der Pins
motor = machine.Pin(15, machine.Pin.OUT)  # Motor definieren
led = Pin(25, Pin.OUT)  # LED definieren
buton = button = Pin(14, Pin.IN, Pin.PULL_UP)
servo0=Servo(pin=0)
servo1=Servo(pin=1)
led = Pin(25, Pin.OUT)


# Definiere Variablen 
def wigle1():
    servo1.move(180)
    time.sleep(0.3)
    servo1.move(90)
    
def wigle0():
    servo0.move(0)
    time.sleep(0.3)
    servo0.move(90)
    
mode = 0
rand = random.randint(10, 25)  # Startwert für zufälliges Intervall
last_wiggle_time = time.time()  # Zeitpunkt der letzten Aktion

# Start (Alles zurücksetzen)
servo1.move(0)
time.sleep(2)
servo1.move(90)
servo0.move(0)
time.sleep(2)
servo0.move(90)

# Code
while True:
   
    if rp2.bootsel_button() == 1:
        
        if mode == 0:
            mode = 1
            print("Mode Changed to (Random)")
            led.on()
            
        elif mode == 1:
            mode = 0
            print("Mode Changed to (Button)")
            led.off()
            
        time.sleep(0.3)  

    
    # Random_Mode
    if mode == 1:
        current_time = time.time()
        if current_time - last_wiggle_time >= rand:  
            wigle1()
            wigle0()
            print("wigled UwU")
            rand = random.randint(5, 10)  
            last_wiggle_time = current_time





    # Finished
    # Button-Mode
    if mode == 0:
        if button.value() == 0:
            wigle1()
            wigle0()
            print("wigled UwU")
            time.sleep(0.2)  
