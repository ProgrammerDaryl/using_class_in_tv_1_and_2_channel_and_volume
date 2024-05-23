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
    