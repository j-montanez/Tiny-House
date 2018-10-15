# Jose Montanez
# Senior Design
# This script collects temperature and humidity readings then output them to console.
# Saves data it collected into an excel file.

import datetime
import time
import os
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

# Pin I'm using is pin 16 on the Raspberry Pi which is GPI023
# You need to declare it as pin 23
pin = 23

# This variable holds the delay time in seconds
# Change it if you want
SLEEP = 5

# infinite loop
while True :
    # To get a sensor reading
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Formula that converts celsius to fahrenheit
    fahrenheit = ((9 / 5 ) * temperature ) + 35
    
    # Check to see if we can get a valid reading
    if humidity is not None and temperature is not None:
        print ('Temp= {0:0.1f}*F  Humidity= {1:0.1f}%'.format(fahrenheit, humidity))
    else:
        print('Sensor Error')
    time.sleep(10)
    
    # This section saves the data in a csv file
    file = open("tempAndHumidity.csv", "a")
    # Checks to see if the file exists
    if (os.path.getsize("tempAndHumidity.csv") == 0):
        file.write("Date and Time\tTemperature\tHumidity\n")
    from datetime import datetime
    file.write(str(datetime.now()))
    file.write("\t")
    file.write(str(fahrenheit))
    file.write("\t")
    file.write(str(humidity))
    file.write("\n")
    file.close()
    print("Data collected successfully\n")
    time.sleep(SLEEP)


