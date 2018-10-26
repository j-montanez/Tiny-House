# Jose Montanez
# Senior Design
# This script collects temperature and humidity readings then output them to console.
# Saves data it collected into an excel file.
import paho.mqtt.client as mqtt
import datetime
import time
import os
import Adafruit_DHT
import RPi.GPIO as GPIO
import LiquidCrystalPi

sensor = Adafruit_DHT.DHT22

# Pin I'm using is pin 16 on the Raspberry Pi which is GPI023
# You need to declare it as pin 23
pin = 23

#lcd
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LCDleft= LiquidCrystalPi.LCD(37, 35, 33, 31, 29, 23) #rs, e, d4, d5, d6, d7 can be any gpio pins.
LCDleft.begin(16, 2)

# This variable holds the delay time in seconds
# Change it if you want
SLEEP = 2
mqttClient = mqtt.Client("SensorPi") 
broker_address="192.168.1.5"  
mqttClient.connect("192.168.1.5",1883,60) 
mqttClient.loop_start()
# infinite loop
while True :
    # To get a sensor reading
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Formula that converts celsius to fahrenheit
    fahrenheit = ((9 / 5 ) * temperature ) + 35
    
    #to round down from float to decimal
    humidityDisplay = str(round(humidity, 3))
    fahrenheitDisplay = str(round(fahrenheit, 3))
    
    LCDleft.clear()
    LCDleft.home()
    LCDleft.write("Humidity: ")
    LCDleft.write(humidityDisplay)
    
    LCDleft.nextline()
    LCDleft.write("Temp: ")
    LCDleft.write(fahrenheitDisplay)
    
    
    # Check to see if we can get a valid reading
    if humidity is not None and temperature is not None:
        print ('Temp= {0:0.1f}*F  Humidity= {1:0.1f}%'.format(fahrenheit, humidity))
    else:
        print('Sensor Error')
    time.sleep(SLEEP)
    
    # This section saves the data in a csv file
    file = open("tempAndHumidity.csv", "a")
    # Checks to see if the file exists
    if (os.path.getsize("tempAndHumidity.csv") == 0):
        file.write("Date and Time\tTemperature\tHumidity\n")
    from datetime import datetime
    file.write(str(datetime.now()))
    file.write("\t")
    file.write(str(fahrenheit))
    mqttClient.publish("rPi2/IR",str(fahrenheitDisplay))
    file.write("\t")
    file.write(str(humidity))
    mqttClient.publish("rPi2/HM",str(humidityDisplay))
    file.write("\n")
    file.close()
    print("Data collected successfully\n")
    time.sleep(SLEEP)


