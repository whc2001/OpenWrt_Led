import time, random
from OpenWrt_Led import *

r = None
g = None
b = None

def Setup():
    global r, g, b
    leds = SystemLeds()
    r = leds.GetLed("z1:red:tricolor0")
    g = leds.GetLed("z1:green:tricolor0")
    b = leds.GetLed("z1:blue:tricolor0")

def Loop():
    r.Brightness = random.randint(0, r.MaxBrightness)
    g.Brightness = random.randint(0, g.MaxBrightness)
    b.Brightness = random.randint(0, b.MaxBrightness)
    time.sleep(0.1)

if __name__ == '__main__':
    Setup()
    while True:
        Loop()
