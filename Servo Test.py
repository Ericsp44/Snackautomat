


import machine
from machine import Pin
from lcd_api import   LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from servoLib import Servo
import time

sdaPIN=machine.Pin(21)  #for ESP32
sclPIN=machine.Pin(22)

WaitTimeBetweenMove = 0.2


I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c=machine.I2C(sda=sdaPIN, scl=sclPIN, freq=10000)  

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
motor=Servo(pin=26)

def NewServoPosition(angle):
  lcd.clear()
  lcd.putstr("Servo to " + str(angle) + " Deg")
  time.sleep(0.5)
  motor.move(angle)
  
 
while True: 
  lcd.clear()
  lcd.putstr("Willkommen!!")
  time.sleep(5)
  lcd.clear()
  lcd.putstr("Was wollen Sie  kaufen?")
  time.sleep(5)
  if eingabefeld == 1:
    lcd.clear()
    lcd.putstr("Ihr Snickers wird runtergelassen")
    
  elif eingabefeld == 2:
    lcd.clear()
    lcd.putstr("Ihr Mars wird runtergelassen")
    
  elif eingabefeld == 3:
    lcd.clear()
    lcd.putstr("Ihr Kinderpinguin wird runtergelassen")
    
  elif eingabefeld == 4:
    lcd.clear()
    lcd.putstr("Ihre Maltesers werden runtergelassen")
    
  else:
    lcd.clear()
    lcd.putstr("Die Nummer wurde nicht gefunden")
    time.sleep(10)
    lcd.putstr("Geben Sie eine andere ein")




