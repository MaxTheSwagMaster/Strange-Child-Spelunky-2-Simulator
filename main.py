# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def run():
    run_results = random. randint(0,15000)
    if run_results <= 100:
        print('Got shot by an arrow and reset immediately. Classic.')
    elif run_results > 100 and run_results <= 600:
        print('Bad shop. Or you just fucked up robbing it. Again.')
    elif run_results > 600 and run_results <= 1500:
        print('Got rolled from offscreen. Armadillo man has your number')
    elif run_results > 1500 and run_results <= 2500:
        print('Knocked back from a magma man into lava? Couldn\'t be me')
    elif run_results > 2500 and run_results <= 2700:
        print('Wow, a vampire knocked you onto the conveyor belt in vlad\'s apartment. Best way to go.')
    elif run_results > 2700 and run_results <= 3200:
        print('Olmec kinda fucked you up. Doesn\'t happen that much anymore')
    elif run_results > 3200 and run_results <= 4000:
        print('Anka\'s curse has claimed you. Seriously did it by herself. (Also I swear there is some seinfeld base in that song.)')
    elif run_results > 4000 and run_results <= 4500:
        print('Rare miss in the ice caves. At least the yeti\'s dad isn\'t home, so they can game.')
    elif run_results > 4500 and run_results <= 5250:
        print('Died in Neo Bab. Shot your plasma cannon, got reflected, direct hit across the map. You lived until you got crushed by a random elevator.')
    elif run_results > 5250 and run_results <= 8000:
        print('Missed the big boy skip. Where great runs come to die.')
    elif run_results > 8000 and run_results <= 8750:
        print('Dude, you gotta pay attention when you break those blocks. Crushed again.')
    elif run_results > 8750 and run_results <= 9300:
        print('Got portal 1\'ed. You gotta shoot the portal next to you before you get incinerated. And the plasma cannon blew up. :(')
    elif run_results > 9300 and run_results <= 10000:
        print('Died in the first few floors of the cosmic ocean due to bad jellyfish dodging. Hey, at least you got there! :)')
    elif run_results > 10000 and run_results <= 11500:
        print('Got rando boomeranged near 20-30. Hey, it came back!')
    elif run_results > 11500 and run_results <= 12500:
        print('Wooooaaaah, you got halfway there. Wooooooooooah, sQuIdWaRd oN a cHaIr!')
    elif run_results > 12500 and run_results <= 13000:
        print('BRO YOU DIED ON FLOOR 69 LET\'S FUCKING GOOOOOOOO!')
    elif run_results > 13000 and run_results <= 14000:
        print('Sooooooooooo... Clooooose...')
    elif run_results > 14000 and run_results <= 14750:
        print('MY BALLS! You died like 5 away. Come on, man.')
    elif run_results > 14750 and run_results <= 15000:
        print('You did it. You actually finally did it. I\'m in shock. After a whole year you finally didn\'t fuck it up.')
    else:
        print('I am error. Press the any key to continue. 404 or some shit I don\'t fucking know.')
if __name__ == '__main__':
    start = input('Ready to go? (Y/N)')
    if start == 'n' or start == 'N':
        print('Good choice. Go touch some grass instead.')
    elif start == 'Y' or start == 'y':
        while start == 'Y' or start == 'y':
            run()
            start = input('Another try? (Y/N)')
        print('That\'s enough runs for the day...')
    else:
        print('What did you type? Gonna tell me? No? Ok... :(')