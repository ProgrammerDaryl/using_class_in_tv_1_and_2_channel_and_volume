#make a blueprint
class TV():
    #add data members (instance variables)
    def __init__(self, channel=1, volume=1):
        self.power = False
        self.channel = channel
        self.volume = volume
    
        