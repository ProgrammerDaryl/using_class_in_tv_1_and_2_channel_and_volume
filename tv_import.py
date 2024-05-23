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

    #operations for TV2
    tv_two.turnOn()
    tv_two.setChannel(3)
    tv_two.setVolume(2)
    tv_two.channel.Up()

    #output
    print("\n")
    print(f"{tv_one.name}'s channel is {tv_one.getChannel()} and volume level is {tv_one.getVolume()}")
    print(f"{tv_two.name}'s channel is {tv_two.getChannel()} and volume level is {tv_two.getVolume()}\n")
    