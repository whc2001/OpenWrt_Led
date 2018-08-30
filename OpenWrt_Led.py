import os

class Led():
    __name = ""
    __brightness = 0
    __maxBrightness = 1

    __brightnessPath = ""
    __maxBrightnessPath = ""

    @property
    def Brightness(self):
        return self.__brightness

    @Brightness.setter
    def Brightness(self, value):
        if value < 0 or value > self.__maxBrightness:
            raise ValueError("Brightness value out of range")
        else:
            self.__brightness = value
            self.__UpdateBrightness()

    @property
    def MaxBrightness(self):
        return self.__maxBrightness

    @property
    def Name(self):
        return self.__name

    def __UpdateBrightness(self):
        with open(self.__brightnessPath, "w") as fs:
            fs.write(str(self.Brightness))

    def __init__(self, deviceDir):
        self.__brightnessPath = deviceDir + "/brightness"
        self.__maxBrightnessPath = deviceDir + "/max_brightness"
        self.__name = os.path.split(deviceDir)[-1]
        if os.path.isfile(self.__brightnessPath):
            with open(self.__brightnessPath, "r") as fs:
                self.__brightness = int(fs.read().strip())      # 读当前亮度
            if os.path.isfile(self.__maxBrightnessPath):
                with open(self.__maxBrightnessPath) as fs:
                    self.__maxBrightness = int(fs.read().strip())
        else:
            raise IOError("Cannot find file \"brightness\", please check whether the dir is for led!")

class SystemLeds():
    __leds = {}

    @property
    def Leds(self):
        return self.__leds

    def GetLed(self, name):
        return self.__leds.get(name)

    def __init__(self):
        ledsPath = "/sys/class/leds/"
        ledsDirs = [dir for dir in os.listdir(ledsPath) if os.path.isdir(os.path.join(ledsPath, dir))]
        for ledDir in ledsDirs:
            try:
                led = Led(ledsPath + ledDir)
                self.__leds[led.Name] = led
            except Exception as ex:
                print(ex)