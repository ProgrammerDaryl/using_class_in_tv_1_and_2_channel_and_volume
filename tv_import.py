#add import methods
from tv import TV

def main():
    tv1 = TV("tv1")
    tv2 = TV("tv2")

    #operations for TV1
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
    tv1.channelUp()

    #operations for TV2
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
    tv2.channelUp()

    #output
    print("\n")
    print(f"{tv1.name}'s channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"{tv2.name}'s channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}\n")

if __name__ == "__main__":
    main()
