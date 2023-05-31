


import machine
import time
from machine import Pin
from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd


I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

sdaPIN=machine.Pin(21)  #for ESP32
sclPIN=machine.Pin(22)

i2c=machine.I2C(sda=sdaPIN, scl=sclPIN, freq=10000)  

# Initialisierung des I2C-Bus für das LCD1602-Modul

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Pinbelegung für das Membranschaltermodul
MATRIX = [[1, 2, 3, 'A'],
          [4, 5, 6, 'B'],
          [7, 8, 9, 'C'],
          ['*', 0, '#', 'D']]

ROW_PINS = [34, 35, 32, 33]  # Pins für die Zeilen
COL_PINS = [27, 26, 25, 14]  # Pins für die Spalten

# Initialisierung der Pins als Input-Pins mit Pull-Up-Widerstand
row_pins = [Pin(pin_num, Pin.IN, Pin.PULL_UP) for pin_num in ROW_PINS]
col_pins = [Pin(pin_num, Pin.OUT) for pin_num in COL_PINS]


#Listcomprehensions

#Tuple

# Funktion zum Überprüfen, welche Taste gedrückt wurde
def check_button():
    for col_num, col_pin in enumerate(col_pins):
        col_pin.value(0)  # Setze die Spalte auf LOW
        for row_num, row_pin in enumerate(row_pins):
            if row_pin.value() == 0:  # Überprüfe, ob die Taste gedrückt ist
                return MATRIX[row_num][col_num]
        col_pin.value(1)  # Setze die Spalte wieder auf HIGH

    return None  # Wenn keine Taste gedrückt ist, gibt None zurück

# Hauptprogramm
while True:
    pressed_button = check_button()

    if pressed_button is not None:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Gedrückt: " + str(pressed_button))
    
    time.sleep(0.1)  # Kleine Verzögerung für Stabilität






