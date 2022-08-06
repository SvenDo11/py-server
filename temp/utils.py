from torch import rand


try:
    import Adafruit_DHT

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    
    def get_humidity_temperature():
        return Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

except ImportError:
    print("Adafruit lib could not be imported!")
    import random
    def get_humidity_temperature():
        return random.randint(30, 70), random.randint(20, 30)


