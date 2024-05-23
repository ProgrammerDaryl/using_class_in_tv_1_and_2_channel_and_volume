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
    import pyfiglet
    from colorama import Fore

    tv1_styled = pyfiglet.figlet_format(f"\n{tv1.name}'s channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}", font = "doom")
    print(Fore.CYAN + tv1_styled + Fore.RESET)

    tv2_styled = pyfiglet.figlet_format(f"{tv2.name}'s channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}", font = "doom")
    print(Fore.RED + tv2_styled + Fore.RESET)

if __name__ == "__main__":
    main()
