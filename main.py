from machine import Pin,I2C,PWM
import utime
from time import sleep
from pico_i2c_lcd import I2cLcd
button1 = Pin(7, Pin.IN, Pin.PULL_UP)
button2 = Pin(5, Pin.IN, Pin.PULL_UP)
button3 = Pin(6, Pin.IN, Pin.PULL_UP)
Led_R = PWM(Pin(2))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(4))
Led_R.freq(2000)   
Led_G.freq(2000)   
Led_B.freq(2000) 
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]    
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
state1 = 0
state2 = 0
state3 = 0
sR = "OFF"
sG = "OFF"
sB = "OFF"
Led_R.duty_u16(0)
Led_G.duty_u16(0)
Led_B.duty_u16(0)

while True:
    if button1.value() == 0:       
        if state1==0: 
            Led_R.duty_u16(65535)
            while button1.value() == 0:
                state1=1
                sR = "ON"
        else:
            Led_R.duty_u16(0)
            while button1.value()== 0:
                state1=0
                sR = "OFF"
                
    if button2.value() == 0:       
        if state2==0: 
            Led_G.duty_u16(65535)
            while button2.value() == 0:
                state2=1
                sG = "ON"
        else:
            Led_G.duty_u16(0)
            while button2.value()== 0:
                state2=0
                sG = "OFF"
                
    if button3.value() == 0:       
        if state3==0: 
            Led_B.duty_u16(65535)
            while button3.value() == 0:
                state3=1
                sB = "ON"
        else:
            Led_B.duty_u16(0)
            while button3.value()== 0:
                state3=0
                sB = "OFF"
                
                
    lcd.move_to(0,0)
    lcd.putstr("R : " + sR)
    lcd.move_to(8,0)
    lcd.putstr("G : " + sG)
    lcd.move_to(0,1)
    lcd.putstr("B : " + sB)
    sleep(0.2)
    lcd.clear()

    
                
    

