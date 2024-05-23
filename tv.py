#make a blueprint
class TV():
    #add data members (instance variables)
    def __init__(self, name):
        self.name = name
        self.channel = channel = 1
        self.volume = volume = 1
        self.power = False

    #add instance method for power on
    def turnOn(self):
        self.is_on = True

    #add instance method for power off
    def turnOff(self):
        self.is_on = False

    #add instance method for getting channel
    def getChannel(self):
        return self.channel
    
    #add instance method to set the channel
    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
    
    #add instance method for getting volume
    def getVolume(self):
        return self.volume
    
    #add instance method to set the volume
    def setVolume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume
    