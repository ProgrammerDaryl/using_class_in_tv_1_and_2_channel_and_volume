#add import methods
from tv import TV

def main():
    tv_one = TV("tv1")
    tv_two = TV("tv2")

    #operations for TV1
    tv_one.turnOn()
    tv_one.setChannel(30)
    tv_one.setVolume(3)
    tv_one.channelUp()

