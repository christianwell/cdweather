import time
from machine import I2C, Pin
from bme280 import BME280

# Initialize I2C
i2c = I2C(1, scl=Pin(9), sda=Pin(8))  # Adjust pins as needed (e.g., SCL=22, SDA=21)

# Initialize BME280
bme = BME280(i2c=i2c)

while True:
    # Read data from the BME280
    temperature = bme.temperature
    pressure = bme.pressure
    humidity = bme.humidity

    # Print data to the console
    print("Temperature:", temperature)
    print("Pressure:", pressure)
    print("Humidity:", humidity)
    

    time.sleep(2)  # Wait 2 seconds before the next reading

  

  

