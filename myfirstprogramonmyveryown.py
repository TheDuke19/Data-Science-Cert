# The 5 minute notebook game
import random, sys, time



print('Choose a number between 1 and 3, or q to quit program')  # Character selection using while loop and elif statements
while True:
    global playerSelection   #I had to assign this as a global variable to call it later for the inventory to work
    playerSelection = input()
    if playerSelection == 'q':  # my first use of import code in sys
        sys.exit()
    elif playerSelection == '1':
        print('You are a Cleric of Damascia')  # Suffering is the only True Path
    elif playerSelection == '2':
        print('You are the last Dragon Tamer')  # The underdog
    elif playerSelection == '3':
        print('You are a Mage in the Guild of Eternal Flame')  # The annhilator
    break


def itemList():#I should really try and improve this to a grid layout like an actual tic tac toe, and assign keyboard items to the items. just give items, dont allow them to select them, and code it so that when they are used, they are removed from the list
    print('**Best to choose your equipment before you head out')
    print('(Hint! -make a tic tac toe box on paper and write this down, because its the only time youll get the chance! \n')
    itemAssingment()

questItems = [['Healing Herbs', 'Armor Repair Kit', 'Weapon Repair Kit'],
              ['The Holy Hand Grenade', 'Master of Disguise', 'Calamity'],
              ['A Traveling Cat', 'An Old Shovel', 'Throwing Daggers','Rope', 'Hammer and Chisel', 'An Ordinary Towel']]


def itemAssingment():
    while True:
        time.sleep(2)
        print (questItems[0]) #This first list is assigned. I want a counter for them as well. all items are single use
        print('These first 3 items are standard equipment')
        if playerSelection == '1':         #These are the charachter dependent items using specific calls to items in lists
          print (questItems[1][0])
          print('This is your charachters special item')

        elif playerSelection == '2':
          print (questItems[1][1])
          print('This is your charachters special item')

        elif playerSelection == '3':
          print (questItems[1][2])
          print('This is your charachters special item')

        print (questItems[2])   #inventory appears.. the last 5 items are selected, and we move on with the quest
        print('You can only carry 5 more items with you, choose wisely')
        time.sleep(1)
        print('Each item is single use only')
      # calltoContinue()
        break
    #calltoContinue def statement here. pres C to continue or else..


def questClericA():  # definitions of what the charachters will do and time calls for effect
    print('Damascia, your hometown, is in the middle of a horrifying plague. Go there and quell the outbreak \n')
    time.sleep(2.1)
    itemList()         #call item list to start picking items.
def questClericB():
    print('A group of wandering nomads asks you to train them to become Clerics')
    time.sleep(2.1)
    print('Give them the strength they need \n')
    time.sleep(2.1)
    itemList()
def questClericC():
    print('The Horrid Witch has been devouring children by the dozen!')
    print('Kill it! Kill it! Kill it!!!! \n')
    time.sleep(2.1)
    itemList()
def questTamerA():
    print('Wake up son.. Grab your things')
    time.sleep(2.1)
    print('Its time for the sacrifice to begin. \n')
    time.sleep(2.1)
    itemList()
def questTamerB():
    print('Wake up son.. Grab your things')
    time.sleep(2.1)
    print('Its time for the sacrifice to begin. \n')
    time.sleep(2.1)
    itemList()
def questTamerC():
    print('Get outta bed you lazy clout! You slept clear through the sacrifice!')
    time.sleep(2.1)
    print('Go get us dinner for tonight as your punishment! \n')
    time.sleep(2.1)
    itemList()
def questMageA():
    print('The unwilling will be bound in Eternal Flame!')
    time.sleep(1.8)
    print('Gather your belongings and march towards victory! \n')
    time.sleep(2.6)
    itemList()
def questMageB():
    print('A disquieting thought escapes your lips.. as you utter in tounges unknown, your hand moves swiftly to your satchel \n')
    time.sleep(4)
    itemList()
def questMageC():
    print('The Flame has only burnt a hollow shell inside..')
    time.sleep(2.1)
    print('It is time to find new meanings to existence \n')
    time.sleep(3)
    itemList()

print('What type of quest would you like to go on today? (select A, B, or C: any other key quits program)')  # Quest selection
while playerSelection == '1':
    print('A: Save a village from a plague...')   #By killing everyone that exists. a Pyhric victory
    print('B: Teach a group of wayward souls the True Path') # only one survives the training rituals out of like 7 or 8
    print('C: Defeat the Horrid Witch of Squalid Lagoon') #you survive.. only to become the next horror of the land
    questSelect = input()
    if questSelect == 'A':
        questClericA()
    if questSelect == 'B':
        questClericB()
    if questSelect == 'C':
        questClericC()
    break
while playerSelection == '2':
    print('A: Save a sacrificial victim..')  #If you choose this, you will tame a dragon
    print('B: Sacrifice a victim!')   # the victim winds up being a lost family member, you kill the tribal leader (your father) that stole you
    print('C: Try and catch a dragon!')  # the 2 minute ride. you die quickly half wit. try to catch a dragon.. lol
    questSelect = input()
    if questSelect == 'A':
        questTamerA()
    if questSelect == 'B':
        questTamerB()
    if questSelect == 'C':
        questTamerC()
    break
while playerSelection == '3':
    print('A: Initiate the unwilling')  # a demon possesses you and you unleash hell
    print('B: Destroy the chains that bind you') #you learn a spell that allows you to manifest at will, and the world becomes yours. (what you literally make it to be)
    print('C: Break off and start a new enclave') #societal pressure dictates you now must overthrow the world and become supreme leader. total destruction ensues.
    questSelect = input()
    if questSelect == 'A':
        questMageA()
    elif questSelect == 'B':
        questMageB()
    elif questSelect == 'C':
        questMageC()
    break

#call to continue
def calltoContinue():
    while True:
        print('Press c to continue')
        input()
        if input() == 'c' or 'C':
            break
        else:
           print('No, really, press c to continue')


calltoContinue()

#main charchter quest story lines. true (campsite) leads the story on, false (inn) leads to ambush/game. game failure will end session (player death)
def ClericAbeg():
    print('''The blighted path has led you to your first rest stop along
            your 2 day journey back to Damascia. You come upon an inn, and could do
            with some food, drink and a nice bed to sleep in. \n
            You were, however, hoping to get a little farther in your journey
            and have some provisions and bedding with you for an improvised campsite
            further down the road.

            Which will you choose? The inn or the campsite?''')


def ClericBbeg():
    print('''As you are preparing for your morning rituals, a group of traveling nomads
            appear outside your camp. Seven in total, with the smallest amongst them at the
            lead. As they approach, you are tempted to grab your mace and show them why they
            should use their voices first.
            The group halts as your hand moves to the pommel, and the leader approaches alone;
            slowly..''')  #easy game to beat the leader, then they ask you to teach them.

def ClericCbeg():
    print('''Along your weary travels, you come across a hastily written scroll nailed to an oak tree.

                                NOTICE! NOTICE! NOTICE!
                    To any brave souls willing to traverse the uncharted bog
                    of eternal stinkyness, we, the Village Elders of Camp
                    Rowdy Beard, require AID in removing a HoRRor from our
                    lands! The HoRRor in the forest has eaten too many of us
                    in order for us to help ouselves!
                    Payment will be in GODL! We are willing to offer 5,000 GODL
                    to the first Slayer of the HoRRor in our midst \n''')
    print('''Since you had nothin better to do today, guess whats up? \n''')
    print(''''After talking with the Village Elders of Camp Rowdy Beard, you begin your descent
              into the fobidden, uncharted, and stinky, very very stinky, wow like borderline stank
             that your always going to remember in your mind bog.. Your gonna wanna make a map.. \n(**In your notebook!)''') #This is the coordinate game i wanna make

def DTAbeg():
    print('''As you head out of your familys hut, you draw a cool breath against the wispy spring air.
            The thief had been caught red handed the night previous trying to get into the food stores.
            Looking up in the sky, and whistling a simple tune from memory past, you pass the stockade where
            the thief is being held. You stop at a farmer stand to satiate this mornings hunger and this afternoons.
            While haggling the price, you hear it.. Faintly at first, but with confidence. It is your tune that you
            whistle while you walk, but the end of it.. and more!

            Slowly, you realize it is coming from the prisoner, and an idea forms. You quickly buy
            a little more food..''')
    # simple game to move forward

def DTBbeg():   #false (let it go)you move forward, true (get necklace from prisoner)is game that can kill you.. do this one backwards
    print('''As you head out of your familys hut, you draw a cool breath against the wispy spring air.
            The thief had been caught red handed the night previous trying to get into the food stores.
            Looking up in the sky, and whistling a simple tune from memory past, you pass the stockade where
            the thief is being held. You stop at a farmer stand to satiate this mornings hunger and this afternoons.
            While haggling the price, you hear it.. Faintly at first, but with confidence. It is your tune that you
            whistle while you walk, but the end of it.. and more!

            Slowly, you realize it is coming from the prisoner.. How could that be, you wonder? This song is from
            my youth, not some thieves! As you become curious about this problem, you decide to take matters
            into your own hands, so you begin walking over to find out for yourself just what is going on.

            As you apporach the thief, a guard appears. From a distance, you notice a medallion hanging from the
            thiefs neck that resembles the necklace you have had since you were a child.. These coincidences must
            hold some meaning! Unfortunately, finding out means fighting with a guard.. are you ready for that
            consequence?''')

def DTCbeg(): #HAHAHA half wit.. just click 1 (cave) or 2 (valley) until you die lol
    print('''As you head out of your familys hut, you draw a cool breath against the wispy spring air.
            The thief had been caught red handed the night previous trying to get into the food stores,
            but that fool had already been found guilty and cut down.
            Looking up in the sky, and whistling a simple tune from memory past, you pass the back of your
            hut on the way up to the mountain side to gather herbs and berries for part of tonights meal.

            After several hours of gathering goods, you decide to take a quick break under the shade of
            a small grove of trees. Realizing you've never made it this far into the mountain side before,
            you decide to explore a bit. There is a cave off in the distance, which could provide medicinal
            mushrooms and clean water, or a small valley to the right which could provide fruits and fresh game.''')

def mageAbeg(): #easy word relation game to get through to next section
    print('''As a Mage of the Eternal Flame, it is always a requirement to gain more wisdom. As such,
            sacrifice is a necessity that we must all keep in mind while going through initation Rituals.
            The duty of the unwilling is to suffer so that We might gain Knowledge!
            Through Knowledge, comes Victory!
            Through Knowledge comes the boundless Eternal Flame! \n''')

def mageBbeg(): #maze game
    print('''You wake up on the floor, contents of your desk scattered across your chamber, clutching the
            piece of paper you were writing on. It looks like a new spell.. But written in a language you
            have never seen before. The inscriptions are there, the circle is complete, but the glyphs make
            no sense to you.

            How..?

            You have been a mage for over 20 years, and thought you had seen it all, but this is something
            you must take to the Sage for advice on. You have your bags packed already, but the path is shifting
            and unknown. Best to write the way down on something...''')

def mageCbeg(): # 1 (east, leads to them not trusting you and you kill them all for mutiny) or 2 (west, leads to you destroying the world with new treasures)
    print('''Abrupt endings sometimes lead to new and wonderful beginnings. Having mastered the art of your craft,
            it is time to wander the lands in search of new things to learn and be part of. You have often heard the
            West calling your name, your very soul towards it, but towards the East is full of promises of a new
            type of Knowledge.

            You are not alone either.

            A band of followers who see you as their new Sage has broken off to help you find new footing in this world.
            You can choose to accept their influence, or do your own thing, but each will have its own consequenses.

            You know with every fiber of your being that going West will satisfy your own personal reasons for leaving
            the enclave in the first place, but the band of followers needs the reassurance and promises of the East
            and its long sought after riches.

            What will you decide to do first? East or West?''')
