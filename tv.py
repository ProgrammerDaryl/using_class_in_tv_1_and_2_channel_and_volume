#make a blueprint
class TV:
    #add data members (instance variables)
    def __init__(self, name):
        self.name = name
        self.channel = 1
        self.volume = 1
        self.is_on = False

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
        else:
            print("Invalid channel number! Channel must be between 1 and 20 only!")
    
    #add instance method for getting volume
    def getVolume(self):
        return self.volume
    
    #add instance method to set the volume
    def setVolume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume
        else:
            print("Invalid volume level! The volume level must be between 1 and 7 only!")
    
    #add different instance methods for setting the minimum and maximum channels and volumes
    def channelUp(self):
        self.channel = min(120, self.channel)
    
    def channelDown(self):
        self.channel = max(1, self.channel)
    
    def volumeUp(self):
        self.volume = min(7, self.volume + 1)
    
    def volumeDown(self):
        self.volume = max(1, self.volume - 1)
