#importing nanpy for Arduino connection

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#Arduinio pin definations
ledpin=7
buttonPin=8

#Current state of led and push_Button
ledState=False
buttonState=0

#Connecting to an Arduino
try:
    '''To start serial comm between raspi and arduino
       For multiple Arduino specify the arduinoin the serial Manager Function'''
    connection = SerialManager() 

    #Create an instance for ArduinoApi
    a = ArduinoApi(connection=connection)
    print("Connected")
except:
    print("Failed to connect to an arduino")


#Main code
    
#Setup pin modes

a.pinMode(ledpin, a.OUTPUT)
a.pinMode(buttonPin,a.INPUT)

try:
    while True:
        buttonState=a.digitalRead(buttonPin)
        
        if buttonState:
            
            if  ledState:
                a.digitalWrite(ledpin, a.LOW)
                ledState=False
                print("LED OFF")
                sleep(1)
            else:
                a.digitalWrite(ledpin, a.HIGH)
                ledState=True
                print("LED ON")
                sleep(1)
    
except:
    a.digitalPin(ledPin, a.LOW)

        
