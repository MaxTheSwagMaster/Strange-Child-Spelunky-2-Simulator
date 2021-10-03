# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def run():
    run_results = random. randint(0,15000)
    if run_results <= 1000:
        print('Got shot by an arrow and reset immediately. Classic. ')
    elif run_results > 1000 and run_results <= 1500:
        print('Bad shop. Or you just fucked up robbing it. Again. ')
    elif run_results > 1500 and run_results <= 2000:
        print('Moleman got you, so you reset out of anger. ')
    elif run_results > 2000 and run_results <= 2500:
        print('Forgot you pissed off shopkeepers. Only a couple floors until they forgave you, too. ')
    elif run_results > 2500 and run_results <= 2750:
        print('Got rolled from offscreen. Big armadillo man has your number. ')
    elif run_results > 2750 and run_results <= 3000:
        print('Knocked back from a magma man into lava? Couldn\'t be me. ')
    elif run_results > 3000 and run_results <= 3200:
        print('Shopkeep slam dunked you into the lava in the mech caves. Turns out his name was Kobe. ')
    elif run_results > 3200 and run_results <= 3500:
        print('One lava speck fell while you were going down the drill. You gotta wait, man! ')
    elif run_results > 3500 and run_results <= 3750:
        print('Wow, a vampire knocked you onto the conveyor belt in vlad\'s apartment. Best way to go. ')
    elif run_results > 3750 and run_results <= 3850:
        print('Mantrap. ')
    elif run_results > 3850 and run_results <= 4000:
        print('Olmec kinda fucked you up. Doesn\'t happen that much anymore. ')
    elif run_results > 4000 and run_results <= 4250:
        print('Ankha\'s curse has claimed you. Seriously did it by herself. (Also I swear there is some seinfeld base in that song.) ')
    elif run_results > 4250 and run_results <= 4500:
        print('(thwomp noise) ')
    elif run_results > 4500 and run_results <= 4750:
        print('You were rockin\' but blocked by the crocodile rock. (Yeah) ')
    elif run_results > 4750 and run_results <= 4850:
        print('THAT was embarrassing! You were doing the torch challenge and threw one up. Came back down while you were at 1 health. ')
    elif run_results > 4850 and run_results <= 4950:
        print('Rare miss in the ice caves. At least the yeti\'s dad isn\'t home, so they can game. ')
    elif run_results > 4950 and run_results <= 5150:
        print('Missed the alien hideout. Dumbass.')
    elif run_results > 5150 and run_results <= 5500:
        print('Died in Neo Bab. Shot your plasma cannon, got reflected, direct hit across the map. You lived until you got crushed by a random elevator. ')
    elif run_results > 5500 and run_results <= 6000:
        print('You though jetpacks were fun. You kno what else is fun? That flying brain that knocked into you, instantly making you explode. Winners don\'t use the jetpack ')
    elif run_results > 6000 and run_results <= 6500:
        print('Thought it would be funny to piss off (and on) Madame Tusk and her goonies. It WAS funny, but you died for it. Worth it, though. ')
    elif run_results > 6500 and run_results <= 8000:
        print('Missed the big boy skip to the moon. Where great runs come to die. ')
    elif run_results > 8000 and run_results <= 8500:
        print('Poisoned on the moon. Sucks to suck. ')
    elif run_results > 8500 and run_results <= 9000:
        print('Dude, you gotta pay attention when you break those blocks on the moon. Crushed again. ')
    elif run_results > 9000 and run_results <= 9500:
        print('Looped by Moon Spear Trap. A slow and extremely painful way to go. ')
    elif run_results > 9500 and run_results <= 10500:
        print('Died in the sun challenge. Guess your strat didn\'t work. ')
    elif run_results > 10500 and run_results <= 11000:
        print('Got knocked into a spike pit on the moon. I thought you were better than that, man. ')
    elif run_results > 11000 and run_results <= 12500:
        print('Got portal 1\'ed. You gotta shoot the portal next to you before you get incinerated. And the plasma cannon blew up. :( ')
    elif run_results > 12500 and run_results <= 13000:
        print('Died in the first few floors of the Cosmic Ocean due to bad jellyfish dodging. Hey, at least you got there! :) ')
    elif run_results > 13000 and run_results <= 13500:
        print('Got rando boomeranged near 20-30 of the Cosmic Ocean. Hey, it came back! ')
    elif run_results > 13500 and run_results <= 14000:
        print('Wooooaaaah, you got halfway there. Wooooooooooah, sQuIdWaRd oN a cHaIr! ')
    elif run_results > 14000 and run_results <= 14100:
        print('Power went out midway through the Cosmic Ocean. Time to turn it back on. Ugh... ')
    elif run_results > 14100 and run_results <= 14250:
        print('BRO YOU DIED ON FLOOR 69 LET\'S FUCKING GOOOOOOOO! ')
    elif run_results > 14250 and run_results <= 14500:
        print('You fell forever and died around floor 80. Sooooooooooo... Clooooose... ')
    elif run_results > 14500 and run_results <= 14750:
        print('Ice Caves self destructed at floor 90. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH! ')
    elif run_results > 14750 and run_results <= 14995:
        print('MY BALLS! You died like 5 floors away. Come on, man! ')
    elif run_results > 14995 and run_results <= 15000:
        print('You did it. You actually finally did it. I\'m in shock. After a whole year you finally didn\'t fuck it up. ')
    else:
        print('I am error. Press the any key to continue. 404 or some shit I don\'t fucking know.')
    if run_results == 69:
        print('If you are seeing this you rolled exactly 69/15000. The gods have smiled apon you today. ')
if __name__ == '__main__':
    start = input('Ready to go? (Y/N) ')
    if start == 'n' or start == 'N':
        print('Good choice. Go touch some grass instead. ')
    elif start == 'Y' or start == 'y':
        while start == 'Y' or start == 'y':
            run()
            start = input('Another try? (Y/N) ')
        print('That\'s enough runs for the day... ')
    else:
        print('What did you type? Gonna tell me? No? Ok... :( ')
    input(' ')