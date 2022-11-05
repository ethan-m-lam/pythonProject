import sys
import tkinter as tk  # python 3
import tkinter.scrolledtext as st
from tkinter import font as tkfont
import random
import time


class character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.orighealth = 100
        self.base_damage = 10
        self.inventory = []
        self.location = "a5"
        self.main = []
        self.secondary = []
        self.game_over = False

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def attack(self, opponent):
        enemyBaseDamage = self.base_damage
        damage_dealt = enemyBaseDamage
        opponent.take_damage(damage_dealt)


myPlayer = character("name")
randlist = []
randlistten = []


class enemy:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.base_damage = 10
        self.orig_damage = 10
        self.special_damage = 0

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def attack(self, opponent):
        enemyBaseDamage = self.base_damage
        damage_dealt = enemyBaseDamage
        opponent.take_damage(damage_dealt)


class spider(enemy):
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.orighealth = 30
        self.base_damage = 10
        self.orig_damage = 10
        self.special_damage = 25
        self.basicmove = "bit"
        self.basicsingle = "bite"
        self.specialmove = "stung"
        self.failspecialmove = "sting"
        self.description = '''These spiders are not like the spiders you find in your house. These are encrusted in metal and have a vicious bite.'''


class wolf(enemy):
    def __init__(self, name):
        self.name = name
        self.health = 70
        self.orighealth = 70
        self.base_damage = 15
        self.orig_damage = 15
        self.special_damage = 35
        self.basicmove = "rammed"
        self.basicsingle = "ram"
        self.specialmove = "crunched"
        self.failspecialmove = "crunch"
        self.description = '''These metal wolves are ferocious! They use their metal helmet to ram you.'''


class rogue(enemy):
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.orighealth = 120
        self.base_damage = 20
        self.orig_damage = 20
        self.special_damage = 45
        self.basicmove = "slashed"
        self.basicsingle = "slash"
        self.specialmove = "shot"
        self.failspecialmove = "shoot"
        self.description = '''These rogues are humanoids. A sword is visible in their scabbard and they also have a holstered gun.'''


class bot(enemy):
    def __init__(self, name):
        self.name = name
        self.health = 180
        self.orighealth = 180
        self.base_damage = 25
        self.orig_damage = 25
        self.special_damage = 55
        self.basicmove = "whacked"
        self.basicsingle = "whack"
        self.specialmove = "grenaded"
        self.failspecialmove = "grenade"
        self.description = '''These automatons have strong metal armor. They carry a big gun and a grenade launcher in their hands at all times.'''


class boss(enemy):
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.orighealth = 250
        self.base_damage = 40
        self.orig_damage = 40
        self.special_damage = 65
        self.basicmove = "thunderbolted"
        self.basicsingle = "thunderbolt"
        self.specialmove = "wrecked"
        self.failspecialmove = "wreck"
        self.description = '''The boss is a cloaked figure who carries a mysterious staff, which outputs mass amounts of damage.'''


enemy1 = spider("spider")
enemy2 = wolf("wolf")
nocheatz = []
enemy3 = rogue("rogue")
enemy4 = bot("bot")
enemy5 = boss("boss")


def random_number(max_int):
    rand = random.randint(1, max_int)
    return rand


#
# def app:
#     if myPlayer.main[0] == "Fists":
#         mainwdamage = random.randint(10, 13)
#     if myPlayer.secondary[0] == "None":
#         secwdamage = 0


skip = False

ZONENAME = ''
DESCRIPTION = 'Description:'
RETURNED = 'Returned?'
SOLVE = 'Solved?'
LOCKED = 'Locked?'
ZONE = 'ZONE:'
yesno = nocheatz
UP = 'up'
DOWN = 'down'
LEFT = 'left'
nocheatz.append('big troll')
RIGHT = 'right'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                 'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False,
                 'f1': False, 'f2': False, 'f3': False, 'f4': False, 'f5': False,
                 'g1': False, 'g2': False, 'g3': False, 'g4': False, 'g5': False,
                 'h1': False, 'h2': False, 'h3': False, 'h4': False, 'h5': False,
                 'fc': False, 'dub': False
                 }

weapons = {
    1: {
        'name': 'Dagger',
        'description': "A small serrated knife that can be used to stab opposing enemies.",
        'action': "stabbed",
        'presaction': "stab",
        'damage': (random.randint(16, 18))},
    2: {

        'name': 'Sword',
        'description': "A sharp-edged blade that slices and slashes through enemies.",
        'action': "slashed",
        'presaction': "slash",
        'damage': (random.randint(20, 25))},
    3: {

        'name': 'Pistol',
        'description': "A small shooter that requires bullets to deal a small amount of damage.",
        'action': "shot",
        'presaction': "shoot",
        'damage': (random.randint(33, 38))},
    4: {
        'name': 'Rifle',
        'description': "A hefty weapon that sprays bullets. It has a moderate damage output.",
        'action': "gunned",
        'presaction': "gun",
        'damage': (random.randint(42, 50))},
    5: {

        'name': 'Sniper',
        'description': "A sharp-shooting rifle that uses bullets to do heavy damage to enemies.",
        'action': "sniped",
        'presaction': "snipe",
        'damage': (random.randint(65, 75))},
    6: {
        'name': 'Fist(s)',
        'description': "Your bare fists. They don't make much of an impact on enemies.",
        'action': "punched",
        'presaction': "punch",
        'damage': (random.randint(10, 1300))},
    7: {

        'name': 'None',
        'description': "Nothing is currently in this slot. Find a weapon to place here.",
        'action': "did nothing to",
        'presaction': "do nothing",
        'damage': 0},
}
# zones begin


gotten0 = False
gotten1 = False
gotten2 = False
donecodes = False

# on start


item = {
    1: {
        'name': 'Potion',
        'attribute': "+50 Health",
        'description': 'A flask containing a silver liquid with healing properties. (+50)',
    },
    2: {
        'name': 'Coin',
        'attribute': "Consumable",
        'description': "A metallic coin that can be redeemed for goods at the vending machine.",
    },
    3: {
        'name': 'Bullet',
        'attribute': "Consumable",
        'description': "A cartridge that can be fired from a pistol, rifle, or sniper.",
    },
    4: {
        'name': 'Elixir',
        'attribute': "+25 Health/+25 HP",
        'description': "A pot of golden liquid that raises your health and health limit by 25.",
    },
    5: {
        'name': 'Dihydrogen Monoxide',
        'attribute': "+2 Main Damage",
        'description': "A bottle of mysterious liquid that increases the amount of damage done with your main weapon. (+2)",
    },
}
coin = item[2]
potion = item[1]
bullet = item[3]
enemturn = False
youmiss = False
zonemap = {
    'a4': {
        ZONENAME: "Plaza Northwest",
        DESCRIPTION: '''The room is dim. It is illuminated by a sparking battery in a jar.\nRoom continues to the EAST and SOUTH.''',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '1',
        UP: 'fc',
        DOWN: 'a5',
        LEFT: 'fc',
        RIGHT: 'b4',
    },
    'a5': {
        ZONENAME: "Plaza Southwest",
        DESCRIPTION: 'This room is dark with small candles on the walls as a light source.\nThe room continues NORTH and EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '1',
        UP: 'a4',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'b5',
    },
    'b4': {
        ZONENAME: "Plaza Northeast",
        DESCRIPTION: 'This room is poorly lit; a single flickering light bulb is the source of light.\nThis room continues to the WEST and SOUTH. There is a door to your EAST.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '1',
        UP: 'fc',
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: 'c4',
    },
    'b5': {
        ZONENAME: "Plaza Southeast",
        DESCRIPTION: 'A weak flashlight in an upside down bucket lights the room.\nThe room continues to your WEST and NORTH.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '1',
        UP: 'b4',
        DOWN: 'fc',
        LEFT: 'a5',
        RIGHT: 'fc',
    },
    'c2': {
        ZONENAME: "West Chamber",
        DESCRIPTION: 'This room is well lit with multiple light bulbs. \nYou can return the way you came by going EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'd2',
    },
    'c4': {
        ZONENAME: "Main Hallway West",
        DESCRIPTION: 'The hallway has a dirt floor. It seems like something had been across this room before. 8 legged scratches are seen.\nThe Hallway continues to the EAST or you can return to the WEST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '2',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: 'b4',
        RIGHT: 'd4',
    },
    'd1': {
        ZONENAME: "Corner Room Northwest",
        DESCRIPTION: 'This room is bright. A pedestal sits in the middle of the room.\nYou can head down the hallway SOUTH, and there is a door to your EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: True,
        ZONE: '4',
        UP: 'fc',
        DOWN: 'd2',
        LEFT: 'fc',
        RIGHT: 'e1',
    },
    'd2': {
        ZONENAME: "West Corridor North",
        DESCRIPTION: 'This hallway is brick with a dirt floor, and is lit with two light bulbs.\nYou can continue to NORTH or SOUTH along the hallway. There is also a chamber to the WEST ',
        RETURNED: False,
        SOLVE: False,
        LOCKED: True,
        ZONE: '2',
        UP: 'd1',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'fc',
    },
    'd3': {
        ZONENAME: "West Corridor South",
        DESCRIPTION: 'A dark room only lit by fireflies captured in a jar.\nThe hallway continues to the NORTH and the SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '2',
        UP: 'd2',
        DOWN: 'd4',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    'd4': {
        ZONENAME: "Intersection 1",
        DESCRIPTION: 'An intersection of two hallways: There is a banner with the words "ARKOS" hanging from the ceiling.\nThe hallway continues to your WEST and EAST. Another hallway begins to your NORTH.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '2',
        UP: 'd3',
        DOWN: 'fc',
        LEFT: 'c4',
        RIGHT: 'e4',
    },
    'e1': {
        ZONENAME: "North Corridor",
        DESCRIPTION: 'The room is lit by a small assortment of candles. Doors loom in the WEST and EAST. ',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '3',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: 'd1',
        RIGHT: 'f1',
    },
    'e4': {
        ZONENAME: "Main Hallway East",
        DESCRIPTION: 'This room is full of trash. \nAs you wade through, You find doors to the WEST, EAST, and SOUTH ',
        RETURNED: False,
        SOLVE: False,
        LOCKED: True,
        ZONE: '2',
        UP: 'fc',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: 'f4',
    },
    'e5': {
        ZONENAME: "South Chamber",
        DESCRIPTION: 'A bright room with a bunch of bookcases stacked against the back wall. \nYou can exit the room by going back the way you came: to the NORTH.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: 'e4',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    'f1': {
        ZONENAME: "Corner Room Northeast",
        DESCRIPTION: 'This corridor is ominous. The dirt pathway is littered with something that looks like wolf scat. \nDoors to the WEST and SOUTH.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '3',
        UP: 'fc',
        DOWN: 'f2',
        LEFT: 'e1',
        RIGHT: 'fc',
    },
    'f2': {
        ZONENAME: "East Corridor North",
        DESCRIPTION: 'The hallway is dark. It is lit by a light-up Eiffel Tower keychain that is suspended from the ceiling.\nAmid the shadows, you sight doors to your NORTH, EAST, SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '4',
        UP: 'f1',
        DOWN: 'f3',
        LEFT: 'fc',
        RIGHT: 'g2',
    },
    'f3': {
        ZONENAME: "East Corridor South",
        DESCRIPTION: 'This corridor is ominous. The dirt pathway is littered with something that looks like wolf scat. \nDoors on the NORTH and SOUTH.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '3',
        UP: 'f2',
        DOWN: 'f4',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    'f4': {
        ZONENAME: "Corner Room Southeast",
        DESCRIPTION: 'This room is cold and gloomy. The air seems stale. \nDoors to your NORTH and EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '3',
        UP: 'f3',
        DOWN: 'fc',
        LEFT: 'e4',
        RIGHT: 'fc',
    },
    'g2': {
        ZONENAME: "Transition 1",
        DESCRIPTION: 'The stunning brightness of the room burns your eyes as you squint into the light. \nThere is a room to the WEST and EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '4',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: 'f2',
        RIGHT: 'h2',
    },
    'h1': {
        ZONENAME: "Stairwell: Level 1",
        DESCRIPTION: 'Stairwell: This stainless steel stairwell is brightly lit by an outside source. \nTo ascend, type NORTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: '2a2',
        DOWN: 'h2',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    'h2': {
        ZONENAME: "Transition 2",
        DESCRIPTION: 'The dusty floor now contains some footprints. Has someone else been here before? \nDoors to '
                     'your WEST, NORTH, and SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '4',
        UP: 'h1',
        DOWN: 'h3',
        LEFT: 'g2',
        RIGHT: 'fc',
    },
    'h3': {
        ZONENAME: "East Chamber",
        DESCRIPTION: 'This chamber is larger than all the previous rooms. A firefly darts around the room. \nYou can go back the way you came by going back NORTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: 'h2',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2a2': {
        ZONENAME: "Stairwell Level 2",
        DESCRIPTION: 'The top of the stairwell. There appears to be a second floor here. \nA door resides to your EAST. To return to the bottom level, go SOUTH',
        RETURNED: False,
        SOLVE: False,
        ZONE: '0',
        UP: 'fc',
        DOWN: 'h1',
        LEFT: 'fc',
        RIGHT: '2b2',
    },
    '2b2': {
        ZONENAME: "Hall West",
        DESCRIPTION: 'A transistor mural can be seen on the ceiling. A faint light emanates from the Southwest. \nYou see a stairwell to your WEST, a small door to your NORTH, and a continuation of the hall to your EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '4',
        UP: '2b1',
        DOWN: 'fc',
        LEFT: '2a2',
        RIGHT: '2c2',
    },
    '2b1': {
        ZONENAME: "North Chamber",
        DESCRIPTION: 'The room is cramped and dingy. It seems like something was here before... \nYou can return back to the hall by going SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: 'fc',
        DOWN: '2b2',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2c2': {
        ZONENAME: "Hall Main",
        DESCRIPTION: 'This hall is well-lit by a lava lamp. \nThe hall extends to the WEST and EAST. There is a small tunnel to the SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: 'fc',
        DOWN: '2c3',
        LEFT: '2b2',
        RIGHT: '2d2',
    },
    '2c3': {
        ZONENAME: "Tunnel North",
        DESCRIPTION: 'This tunnel is slightly cramped and is suddenly dark. A single candle lights the wall. \nYou can continue along the tunnel by going NORTH or SOUTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: '2c2',
        DOWN: '2c4',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2c4': {
        ZONENAME: "Tunnel South",
        DESCRIPTION: 'This section of the tunnel is dim. There is a banner with the words "ARKOS" hanging from the ceiling. \nA battered door resides to the SOUTH. Or, you can go NORTH back up the tunnel.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: '2c3',
        DOWN: '2c5',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2c5': {
        ZONENAME: "Opal Toal",
        DESCRIPTION: 'The room ends here. Return the way you came by going NORTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: '2c4',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2d2': {
        ZONENAME: "Hall East",
        DESCRIPTION: 'Hall East: The end of the hall. \nThere is a door to your SOUTH. You can go back down the hall by going WEST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: True,
        ZONE: '5',
        UP: 'fc',
        DOWN: '2d3',
        LEFT: '2c2',
        RIGHT: 'fc',
    },
    '2d3': {
        ZONENAME: "Opal",
        DESCRIPTION: 'This room is clean and well kept. \nReturn to the Hall by going NORTH. A wooden door resides to the SOUTH and there is a room to your EAST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '0',
        UP: '2d2',
        DOWN: '2d4',
        LEFT: 'fc',
        RIGHT: '2e3',
    },
    '2d4': {
        ZONENAME: "Roomy",
        DESCRIPTION: 'A Transition room. You hear a growl in the distance. A sharp light pierces from the Southeast. \nTo enter the final hallway, go SOUTH. To return to the previous room, go NORTH',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: '2d3',
        DOWN: '2d5',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
    '2d5': {
        ZONENAME: "Final Hallway West",
        DESCRIPTION: 'You begin to hear to rumblings of something to the west. Shadows loom ominously. Heavy clanking is heard.\nYou can go NORTH to return, or proceed EAST down the hall.',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '5',
        UP: '2d4',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: '2e5',
    },
    '2e3': {
        ZONENAME: "???Room???",
        DESCRIPTION: 'The room is pitch black. You feel disoriented. \nReturn by going WEST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '6',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: '2d3',
        RIGHT: 'fc',
    },
    '2e5': {
        ZONENAME: "Final Hall Main",
        DESCRIPTION: 'The sounds are getting louder.  The light is coming from an unidentified source.\nReturn to the darkness by going WEST, or continue toward the light by going EAST ',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '6',
        UP: 'fc',
        DOWN: 'fc',
        LEFT: '2d5',
        RIGHT: '2f5',
    },
    '2f5': {
        ZONENAME: "Final Hall East",
        DESCRIPTION: 'You are disoriented. It is very bright. \nA door denoting "Exit" is to the NORTH. You can also return down the hallway to the WEST',
        RETURNED: False,
        SOLVE: False,
        LOCKED: True,
        ZONE: '6',
        UP: '2f4',
        DOWN: 'fc',
        LEFT: '2e5',
        RIGHT: 'fc',
    },
    '2f4': {
        ZONENAME: "Final Room",
        DESCRIPTION: 'The End. You can see the glowing exit sign above a staircase. A giant sphere of gas surrounds the room. \nThe boss stands menacingly in the middle of the room. Once you beat it, go NORTH to escape up the staircase!',
        RETURNED: False,
        SOLVE: False,
        LOCKED: False,
        ZONE: '7',
        UP: 'dub',
        DOWN: 'fc',
        LEFT: 'fc',
        RIGHT: 'fc',
    },
}

#
# class Item:
#     def __init__(self, name, price, stock, note):
#         self.name = name
#         self.price = price
#         self.stock = stock
#         self.note = note
#
#     def updateStock(self, stock):
#         self.stock = stock
#
#     def buyFromStock(self):
#         if self.stock == 0:
#             # raise not item exception
#             pass
#         self.stock -= 1
#
#
# class VendingMachine:
#     def __init__(self):
#         self.amount = 0
#         self.items = []
#
#     def addItem(self, item):
#         self.items.append(item)
#
#     def showItems(self):
#         for item in self.items:
#             if item.stock == 0:
#                 self.items.remove(item)
#         print(str("Name:") + "\t\t\t" + str("Price:") + "\t\t\t" + str("Stock:") + "\t\t\t" + str("Note:"))
#         print('**********************************************************************************')
#         for item in self.items:
#             if item.name == 'Bullet' and (int(item.stock) >= 10):
#                 print(str(item.name) + ":" + "\t\t\t" + str(item.price) + " coin" + "\t\t\t" + str(
#                     item.stock) + " left!" + "\t\t" + str(item.note))
#             elif item.name == 'Bullet' and (int(item.stock) < 10):
#                 print(str(item.name) + ":" + "\t\t\t" + str(item.price) + " coin" + "\t\t\t" + str(
#                     item.stock) + " left!" + "\t\t\t" + str(item.note))
#
#             elif (5 <= (len(item.name)) < 7) and (len(str(item.price)) <= 1):
#                 print(str(item.name) + ":" + "\t\t\t" + str(item.price) + " coins" + "\t\t\t" + str(
#                     item.stock) + " left!" + "\t\t\t" + str(item.note))
#             elif (5 <= (len(item.name)) < 7) and (len(str(item.price)) >= 2):
#                 print(str(item.name) + ":" + "\t\t\t" + str(item.price) + " coins" + "\t\t" + str(
#                     item.stock) + " left!" + "\t\t\t" + str(item.note))
#             elif item.name == 'Rifle':
#                 print(str(item.name) + ":" + "\t\t\t" + str(item.price) + " coins" + "\t" + str(
#                     item.stock) + " left!" + "\t\t\t" + str(item.note))
#             elif len(item.name) >= 7:
#                 print(str(item.name) + ":" + "\t\t" + str(item.price) + " coins" + "\t\t\t" + str(
#                     item.stock) + " left!" + "\t\t\t" + str(item.note))
#         print('**********************************************************************************')
#
#     def buyItem(self, item):
#         global mainwdamage
#         self.amount = myPlayer.inventory.count(coin)
#         if self.amount < item.price:
#             print('--------------------------------------------------')
#             print('You do not have enough coins!')
#             print('--------------------------------------------------')
#         else:
#             self.amount -= item.price
#
#             item.buyFromStock()
#             if (item.name.lower() == 'sniper' or 'pistol' or 'rifle' or 'sword' or 'bullet' or 'potion' or 'baguette'):
#                 print('You bought a ' + item.name + "!")
#             elif item.name.lower() == 'elixir':
#                 print('You bought a pot of ' + item.name + "!")
#             else:
#                 print("this failed")
#             if (item.name.lower() == 'sniper'):
#                 fifteencost()
#                 print('--------------------------------------------------')
#                 currentmands()
#                 addsniper()
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'sword'):
#                 fivecost()
#                 print('--------------------------------------------------')
#                 currentmands()
#                 addsword()
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'pistol'):
#                 fivecost()
#                 twocost()
#                 print('--------------------------------------------------')
#                 currentmands()
#                 addpistol()
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'rifle'):
#                 tencost()
#                 print('--------------------------------------------------')
#                 currentmands()
#                 addrifle()
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'bullet'):
#                 onecost()
#                 myPlayer.inventory.append(bullet)
#                 print("You now have " + str(myPlayer.inventory.count(bullet)) + " bullet(s)!")
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'potion'):
#                 twocost()
#                 myPlayer.inventory.append(potion)
#                 print("You now have " + str(myPlayer.inventory.count(potion)) + " potions(s)!")
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'baguette'):
#                 threecost()
#                 print("You ate a Baguette! (Main Damage: +2)\n")
#                 mainwdamage += 2
#                 currentmands()
#                 print('--------------------------------------------------')
#             elif (item.name.lower() == 'elixir'):
#                 fivecost()
#                 print('''You drank the pot of Elixir! ( +25 Health and +25 HP )''')
#                 myPlayer.health += 25
#                 myPlayer.orighealth += 25
#                 effects = ['invigorated', 'energized',
#                            'rejuvenated',
#                            'revitalized', "strengthened"]
#                 rand_effects = random.randrange(0, len(effects))
#                 print("\nYou feel " + effects[rand_effects] + "! ")
#                 print("Your New Health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")")
#                 print('--------------------------------------------------')
#             print('Coins remaining: ' + str(self.amount) + ' coin(s)')
#             print('--------------------------------------------------')
#
#     def containsItem(self, wanted):
#         returnn = False
#         for item in self.items:
#             if item.name.lower() == wanted:
#                 returnn = True
#                 break
#         return returnn
#
#     def getItem(self, wanted):
#         returnn = None
#         for item in self.items:
#             if item.name.lower() == wanted:
#                 returnn = item
#                 break
#         return returnn
#
#         print('Thank you, have a nice day!\n')


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold")
        # self.attributes('-fullscreen',True)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # self.h1 = 200
        # self.h2 = 540
        self.frames = {}

        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["Play"] = Play(parent=container, controller=self, controller1=self)
        self.frames["Help"] = Help(parent=container, controller=self)
        # self.frames["Glossary"] = Play(parent=container, controller=self,controller2=self)
        self.frames["Credits"] = Credits(parent=container, controller=self)
        self.frames["Victory"] = Victory(parent=container, controller=self)
        self.frames["Death"] = Death(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Play"].grid(row=0, column=0, sticky="nsew")
        self.frames["Help"].grid(row=0, column=0, sticky="nsew")
        # self.frames["Glossary"].grid(row=0, column=0, sticky="nsew")
        self.frames["Credits"].grid(row=0, column=0, sticky="nsew")
        self.frames["Death"].grid(row=0, column=0, sticky="nsew")
        self.frames["Victory"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.s = tk.Canvas(self, background='gray', width= 1440)
        self.s.create_rectangle(0, 740, 1440, 770)
        self.s.pack()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='LightBlue1')
        self.controller = controller
        # self.w1 = 734
        # self.w2 = 694
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        label = tk.Label(self, text="The Abandoned Building RPG", font = tkfont.Font(family='Helvetica', size=40, weight="bold"), bg='LightBlue1')
        label.grid(row=0, column=0, sticky='ns')

        Button1 = tk.Button(self, text="Play", width=30,
                            command=lambda: controller.show_frame("Play"))
        Button2 = tk.Button(self, text="Help", width=30,
                            command=lambda: controller.show_frame("Help"))
        Button3 = tk.Button(self, width=30, text="Glossary")
        Button4 = tk.Button(self, text="Credits", width=30,
                            command=lambda: controller.show_frame("Credits"))
        # Button5 = tk.Button(self, text="Quit", width=30,
        #                     command=lambda: sys.exit())
        Button6 = tk.Button(self, text="Victory",
                            command=lambda: controller.show_frame("Quit"))
        Button1.grid(row=1, sticky='ns')
        Button2.grid(row=2, sticky='ns')
        Button3.grid(row=3, sticky='ns')
        Button4.grid(row=4, sticky='ns')
        # Button5.grid(row=5, sticky='ns')


mx = 0
sx = 0
sy = 0
my = 0


class Play(tk.Frame):

    def __init__(self, parent, controller, controller1):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.shared_data = {
            "Code #1": tk.StringVar(),
            "Code #2": tk.StringVar(),
            "Code #3": tk.StringVar(),
        }
        self.controller = controller
        self.controller1 = controller1
        self.number = tk.IntVar()
        self.slowvar = tk.IntVar()
        self.attackvar = tk.IntVar()
        self.vendvar = tk.IntVar()
        self.codevar = tk.IntVar()
        # self.attackvar = tk.IntVar()
        myPlayer.main = weapons[6]
        myPlayer.secondary = weapons[7]
        # self.grid_rowconfigure(0, weight=67)
        # self.grid_rowconfigure(1, weight=23)
        # self.grid_columnconfigure(0, weight=74)
        # self.grid_columnconfigure(1, weight=70)

        self.swframe = tk.Frame(self, background="orange")
        self.swframe.grid(row=1, column=0)
        # self.swframe.grid_propagate(0)
        container1 = tk.Frame(self.swframe, background="orange")
        container1.pack()

        self.nwframe = tk.Frame(self, background='blue')
        self.nwframe.grid(row=0, column=0)
        # self.nwframe.grid_propagate(0)
        self.neframe = tk.Frame(self, background='red')
        self.neframe.grid(row=0, column=1)
        mapcontainer = tk.Frame(self.neframe, background="orange")
        mapcontainer.pack()
        self.seframe = tk.Frame(self, background='black')
        self.seframe.grid(row=1, column=1)
        # self.grid_columnconfigure(0, weight=740)
        # self.grid_columnconfigure(1, weight=700)
        # self.grid_rowconfigure(0, weight=550)
        # self.grid_rowconfigure(1, weight=230)
        # self.seframe.grid_propagate(0)

        tabframe = tk.Frame(self.nwframe, width=740, height=30)
        stframe = tk.Frame(self.nwframe, width=740, height=510)

        tabframe.grid(row=0, column=0)
        stframe.grid(row=1, column=0)

        upperwhitespace = tk.Label(tabframe,
                                   text='The Abandoned Building', font=controller.title_font,
                                   bg='LightBlue1', fg='black')
        upperwhitespace.place(x=0, y=0, relwidth=1, relheight=1)

        self.text_area = st.ScrolledText(stframe, font=("Times New Roman", 15))
        self.text_area.place(x=0, y=0, relwidth=1, relheight=1)

        framep0 = tk.Frame(self.seframe, background='blue', height=50, width=520)
        framep0.grid(row=1, column=0)
        framep1 = tk.Frame(self.seframe, background='blue', height=30, width=520)
        framep1.grid(row=2, column=0)
        framep2 = tk.Frame(self.seframe, background='blue', height=20, width=520)
        framep2.grid(row=3, column=0)
        framep3 = tk.Frame(self.seframe, background='blue', height=20, width=520)
        framep3.grid(row=4, column=0)
        framep4 = tk.Frame(self.seframe, background='blue', height=20, width=520)
        framep4.grid(row=5, column=0)
        framep5 = tk.Frame(self.seframe, background='blue', height=30, width=520)
        framep5.grid(row=6, column=0)
        framep6 = tk.Frame(self.seframe, background='blue', height=10, width=520)
        framep6.grid(row=7, column=0)
        framep7 = tk.Frame(self.seframe, background='white', height=20, width=520)
        framep7.grid(row=8, column=0)

        frame1 = tk.Frame(self.seframe, background="LightBlue1", height=200, width=180)
        frame1.grid(row=1, column=1, rowspan=8)

        # self.frame2 = tk.Frame(self.seframe, background="LightBlue1")
        # self.frame2.grid(row=1,column=1,ipady=83,ipadx=2)
        def varupdate():
            # print("yo")
            Lab1.configure(text="Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")")
            Lab2.configure(text="You have " + str(myPlayer.inventory.count(coin)) + " coin(s)")
            Lab3.configure(text="You have " + str(myPlayer.inventory.count(potion)) + " potion(s)")
            Lab4.configure(text="You have " + str(myPlayer.inventory.count(bullet)) + " bullet(s)")
            Lab5.configure(text="Main Weapon: {name}; damage: {damage}".format(name=myPlayer.main['name'],
                                                                               damage=myPlayer.main['damage']))
            Lab6.configure(text="Secondary Weapon: {name}; damage: {damage}".format(name=myPlayer.secondary['name'],
                                                                                    damage=myPlayer.secondary[
                                                                                        'damage']))
            self.seframe.after(500, varupdate)

        Lab0 = tk.Label(framep0,
                        text="Inventory:", font=controller.title_font)
        Lab0.place(x=0, y=0, relwidth=1, relheight=1)
        Lab1 = tk.Label(framep1, text="Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")")
        Lab1.place(x=0, y=0, relwidth=1, relheight=1)
        Lab2 = tk.Label(framep2,
                        text="You have " + str(myPlayer.inventory.count(coin)) + " coin(s)")
        Lab2.place(x=0, y=0, relwidth=1, relheight=1)
        Lab3 = tk.Label(framep3,
                        text="You have " + str(myPlayer.inventory.count(potion)) + " potion(s)")
        Lab3.place(x=0, y=0, relwidth=1, relheight=1)
        Lab4 = tk.Label(framep4,
                        text="You have " + str(myPlayer.inventory.count(bullet)) + " bullet(s)")
        Lab4.place(x=0, y=0, relwidth=1, relheight=1)
        Lab5 = tk.Label(framep5,
                        text="Main Weapon: {name}; damage: {damage}".format(name=myPlayer.main['name'],
                                                                            damage=myPlayer.main['damage']))
        Lab5.place(x=0, y=0, relwidth=1, relheight=1)
        Lab6 = tk.Label(framep6,
                        text="Secondary Weapon: {name}; damage: {damage}".format(name=myPlayer.secondary['name'],
                                                                                 damage=myPlayer.secondary['damage']))
        Lab6.place(x=0, y=0, relwidth=1, relheight=1)
        button = tk.Button(frame1, text='Help')
        button.place(x=0, y=0, relwidth=1, relheight=1)
        self.seframe.after(500, varupdate)

        # self.map()
        # leftwhitespace = tk.Label(self.neframe,
        #                           text='Instructions: You are the Green square. \nThe Gold square indicates a room of interest. The Blue square marks the staircase',
        #                           bg='LightBlue1', fg='black', height=3, width=76)
        # leftwhitespace.pack(side='bottom')
        self.mapframes = {}
        self.mapframes["Map 1"] = Map1(parent=mapcontainer, controller2=self)
        self.mapframes["Map 2"] = Map2(parent=mapcontainer, controller2=self)
        self.mapframes["Map 1"].grid(row=0, column=0, sticky="nsew")
        self.mapframes["Map 2"].grid(row=0, column=0, sticky="nsew")

        self.show_frame2("Map 1")

        self.frames1 = {}
        self.frames1["Proceed"] = Proceed(parent=container1, controller1=self)
        self.frames1["Move"] = Move(parent=container1, controller1=self)
        self.frames1["PickUp"] = PickUp(parent=container1, controller1=self)
        self.frames1["Attack"] = Attack(parent=container1, controller1=self)
        # self.frames1["Vending"] = Vending(parent=container1, controller1=self)
        # self.frames1["Code"] = Code(parent=container1, controller1=self)
        # self.frames["Glossary"] = Play(parent=container, controller=self,controller2=self)
        # self.frames["Credits"] = Help(parent=container, controller=self)
        self.frames1["Proceed"].grid(row=0, column=0, sticky="nsew")
        self.frames1["Move"].grid(row=0, column=0, sticky="nsew")
        self.frames1["PickUp"].grid(row=0, column=0, sticky="nsew")
        self.frames1["Attack"].grid(row=0, column=0, sticky="nsew")
        # self.frames1["Vending"].grid(row=0, column=0, sticky="nsew")
        # self.frames1["Code"].grid(row=0, column=0, sticky="nsew")
        # self.frames["Glossary"].grid(row=0, column=0, sticky="nsew")
        # self.frames["Credits"].grid(row=0, column=0, sticky="nsew")
        self.show_frame1("Proceed")

        self.scrolltobottom()
        # self.RPGfont = tkfont.Font(family='Helvetica', size=20, weight="bold")
        # tk.Label(self.nwframe, text='The Abandoned Building (RPG)', font=self.RPGfont).pack(padx=10)
        # tk.Label(self.neframe, text='Main pageNE', width=68, height=30, bg='green').pack()

        # tk.Label(self.seframe, text='Main pageSE').pack()

        # Buttonn = tk.Button(self.seframe, text="Go to the start page",
        #                       command=lambda: controller.show_frame("StartPage"))
        # Buttonn.pack()
        # tk.Label(self.swframe, text='Main pageSW').pack()
        # tk.Button(self.nwframe, text='Go to Page 1',
        #           command=self.make_page_1).pack()

    def text(self, qwerty):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.INSERT, qwerty)
        self.text_area.configure(state='disabled')
        #print(qwerty)
        #print("texty")

    def intro_text(self):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.INSERT, zonemap[myPlayer.location][ZONENAME] + "\n")
        self.text_area.configure(state='disabled')
        self.print_location('a5')

    def show_frame1(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames1[page_name]
        frame.tkraise()

    def show_frame2(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.mapframes[page_name]
        frame.tkraise()

    # def get_page(self, page_class):
    #     return self.frames1[page_class]
    def scrolltobottom(self):
        self.text_area.see("end")
        self.nwframe.after(1000, self.scrolltobottom)

    def movement_handler(self, destination, whattodo):
        global map, mx, my
        randlist.clear()
        for j in range(300):
            randlist.append(random.randint(1, 100))
        myPlayer.location = destination
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.INSERT,
                              "===========================================================================\nYou went " + whattodo.upper() + " and entered the " +
                              zonemap[myPlayer.location][ZONENAME] + ".\n")
        self.text_area.configure(state='disabled')
        self.print_location(destination)
        if zonemap[myPlayer.location][RETURNED] is False:
            #print("weapongot")
            self.weapongot()
            #
            # print(zonemap[myPlayer.location][RETURNED])
            self.freething()

            # self.freething(self)
            self.enemiesgot()
            self.battle()

            # if myPlayer.location in ['c2', 'e5', 'h3', '2d3']:
            #     if randlist[112] <= 100:
            #         pass
            #         # self.codegot()
            #     elif 75 <= randlist[112] <= 100:
            #         if donecodes == True:
            #             pass
            #         #     self.vend()
            #         # # self.codegot()
            #         # self.vend()
            #     else:
            #         nothingtxt = ['It seems like there used to be machines here!',
            #                       'Lines on the floor mark a place by the wall where a heavy object used to be.',
            #                       'Chipped coins litter the floor, were they used for something?',
            #                       'A broken power socket lies against the back wall.',
            #                       'Shards of metal and frayed wires cover the ground']
            #         rand_nothing = random.randrange(0, len(nothingtxt))
            #         print("----------------------------------------")
            #         print(nothingtxt[rand_nothing] + "\nSomething used to be here...")
            # elif myPlayer.location in ['2c5']:
            #     # self.codegot()
            #     # self.vend()
            #     pass
            if myPlayer.location in ['2f4']:
                # self.codegot()
                print("nonefornow")

        else:
            cameback = ['It seems like you have been in this room before.', 'This room seems awfully familiar.',
                        'Have you been here before?']
            rand_cameback = random.randrange(0, len(cameback))
            self.text("\n" + cameback[rand_cameback]+"\n")

    def move_up(self):
        global my, sy
        zonemap[myPlayer.location][RETURNED] = True
        destination = zonemap[myPlayer.location][UP]
        if destination == 'fc':
            self.text_area.configure(state='normal')
            self.text_area.insert(tk.INSERT,
                                  "You tried going NORTH, but came face to face with a wall.\n")
            self.text_area.configure(state='disabled')
        elif destination == 'dub':
            self.text_area.configure(state='normal')
            self.text_area.insert(tk.INSERT,
                                  "----------------------------------------\n")
            self.after(2000,self.text("You ascend the staircase and reach the roof. \nYou look out over the edge at the barren wasteland"))
            self.text_area.insert(tk.INSERT, "\n----------------------------------------\n")
            self.text_area.configure(state='disabled')
            self.victory()
        elif destination == '2a2':
            #print('map2')
            self.show_frame2("Map 2")
            self.movement_handler(destination, whattodo='NORTH')
        elif (zonemap[destination][ZONE] in ['1', '2', '3']) or (destination in ['c2' , 'd1' , 'e5' , 'f2' , 'g2' ,'h1' , 'h2' ,'h3']):
            my -= 1
            self.movement_handler(destination, whattodo='NORTH')
        else:
            sy -= 1
            self.movement_handler(destination, whattodo='NORTH')

    def move_down(self):
        global my, sy
        zonemap[myPlayer.location][RETURNED] = True
        destination = zonemap[myPlayer.location][DOWN]
        whattodo = 'SOUTH'
        if destination == 'fc':
            self.text_area.configure(state='normal')
            self.text_area.insert(tk.INSERT,
                                  "You tried going " + str(whattodo) + ", but came face to face with a wall.\n")
            self.text_area.configure(state='disabled')
        elif destination == 'h1':
            #print('map1')
            self.show_frame2("Map 1")
            self.movement_handler(destination, whattodo='SOUTH')
        elif (zonemap[destination][ZONE] in ['1', '2', '3']) or (destination in ['c2' , 'd1' , 'e5' , 'f2' , 'g2' ,'h1' , 'h2' ,'h3']):
            my += 1
            self.movement_handler(destination, whattodo='SOUTH')
        else:
            sy += 1
            self.movement_handler(destination, whattodo='SOUTH')

    def move_left(self):
        global mx, sx
        zonemap[myPlayer.location][RETURNED] = True
        destination = zonemap[myPlayer.location][LEFT]
        whattodo = 'WEST'
        if destination == 'fc':
            self.text_area.configure(state='normal')
            self.text_area.insert(tk.INSERT,
                                  "You tried going " + str(whattodo) + ", but came face to face with a wall.\n")
            self.text_area.configure(state='disabled')
        elif (zonemap[destination][ZONE] in ['1', '2', '3']) or (destination in ['c2' , 'd1' , 'e5' , 'f2' , 'g2' ,'h1' , 'h2' ,'h3']):
            mx -= 1
            self.movement_handler(destination, whattodo)
        else:
            sx -= 1
            self.movement_handler(destination, whattodo)

    def move_right(self):
        global mx, sx
        zonemap[myPlayer.location][RETURNED] = True
        destination = zonemap[myPlayer.location][RIGHT]
        whattodo = 'EAST'
        if destination == 'fc':
            self.text_area.insert(tk.INSERT,
                                  "You tried going " + str(whattodo) + ", but came face to face with a wall.\n")
        elif (zonemap[destination][ZONE] in ['1', '2', '3']) or (destination in ['c2' , 'd1' , 'e5' , 'f2' , 'g2' ,'h1' , 'h2' ,'h3']):

            mx += 1
            self.movement_handler(destination, whattodo)
        else:
            sx += 1
            self.movement_handler(destination, whattodo)

    def m(self):
        num = self.number.get()
        myPlayer.main = weapons[num]
        self.text_area.configure(state='normal', font=("Times New Roman", 15))
        self.text_area.insert(tk.INSERT, "You equipped the " + myPlayer.main['name'] + " into your Main weapon slot.\n")
        self.text_area.insert(tk.INSERT, "----------------------------------------\n")
        self.text_area.configure(state='disabled', font=("Times New Roman", 15))
        self.number.set(0)
        self.slowvar.set(0)

    def s(self):
        num = self.number.get()
        myPlayer.secondary = weapons[num]
        self.text_area.configure(state='normal', font=("Times New Roman", 15))
        self.text_area.insert(tk.INSERT,
                              "You equipped the " + myPlayer.secondary['name'] + " into your Secondary weapon slot.\n")
        self.text_area.insert(tk.INSERT, "----------------------------------------\n")
        self.text_area.configure(state='disabled', font=("Times New Roman", 15))
        self.number.set(0)
        self.slowvar.set(0)

    def d(self):
        num = self.number.get()
        self.text_area.configure(state='normal', font=("Times New Roman", 15))
        self.text_area.insert(tk.INSERT, "You dropped the " + weapons[num]['name'] + ".\n")
        self.text_area.insert(tk.INSERT, "----------------------------------------\n")
        self.text_area.configure(state='disabled', font=("Times New Roman", 15))
        self.number.set(0)
        self.slowvar.set(0)

    def freething(self):
        #print("free thing")
        if zonemap[myPlayer.location][ZONE] in ['1', '2', '3']:
            if randlist[8] <= 33:
                myPlayer.main['damage'] += 2
                self.text_area.configure(state='normal')
                self.text_area.insert(tk.INSERT, "-----\n")
                self.text_area.insert(tk.INSERT,
                                      "A bottle of " + item[5]['name'] + " appears out of thin air.\n")
                self.text_area.insert(tk.INSERT, "You chug the entire bottle.\nYour " + myPlayer.main[
                    'name'] + " now deals " + str(
                    myPlayer.main['damage']) + " damage!\n")
                self.text_area.insert(tk.INSERT, "----------------------------------------\n")
                self.text_area.configure(state='disabled')

        elif zonemap[myPlayer.location][ZONE] in ['4', '5', '6']:
            if randlist[9] <= 25:
                myPlayer.main['damage'] += 2
                self.text_area.configure(state='normal')
                self.text_area.insert(tk.INSERT,
                                      "A " + item[5]['name'] + " appears out of thin air.\n")
                self.text_area.insert(tk.INSERT, "You chug the entire bottle.\nYour " + myPlayer.main[
                    'name'] + " now deals " + str(
                    myPlayer.main['damage']) + " damage!\n")
                self.text_area.insert(tk.INSERT, "----------------------------------------\n")
                self.text_area.configure(state='disabled')
        elif zonemap[myPlayer.location][ZONE] in ['0']:
            if randlist[70] <= 75:
                myPlayer.inventory.append(coin)
                self.text_area.configure(state='normal')
                self.text_area.insert(tk.INSERT, "You found a coin!\n")
                self.text_area.insert(tk.INSERT, "----------------------------------------\n")
                self.text_area.configure(state='disabled')

            elif randlist[70] > 75:
                myPlayer.inventory.append(bullet)
                self.text_area.configure(state='normal')
                self.text_area.insert(tk.INSERT, "You found a bullet!\n")
                self.text_area.insert(tk.INSERT, "----------------------------------------\n")
                self.text_area.configure(state='disabled')

    def enemiesgot(self):
        global currentenemy
        #print("one enem")
        if zonemap[myPlayer.location][ZONE] == '0':
            currentenemy = None
        elif zonemap[myPlayer.location][ZONE] == '1':
            if randlist[20] <= 99:
                currentenemy = enemy1
                self.restore()
            else:
                currentenemy = None

        elif zonemap[myPlayer.location][ZONE] == '2':
            if randlist[21] <= 20:
                currentenemy = enemy2
                self.restore()
            elif randlist[22] <= 40:
                currentenemy = enemy1
                self.restore()
            else:
                currentenemy = None

        elif (zonemap[myPlayer.location][ZONE] == '3'):
            if randlist[23] <= 20:
                currentenemy = enemy3
                self.restore()

            elif randlist[24] <= 40:
                currentenemy = enemy2
                self.restore()

            elif randlist[25] <= 60:
                currentenemy = enemy1
                self.restore()
            else:
                currentenemy = None

        elif (zonemap[myPlayer.location][ZONE] == '4'):
            if randlist[26] <= 10:
                currentenemy = enemy4
                self.restore()

            if randlist[27] <= 30:
                currentenemy = enemy3
                self.restore()

            if randlist[28] <= 50:
                currentenemy = enemy2
                self.restore()
            else:
                currentenemy = None

        elif (zonemap[myPlayer.location][ZONE] == '5'):
            if randlist[30] <= 20:
                currentenemy = enemy4
                self.restore()

            elif randlist[31] <= 40:
                currentenemy = enemy3
                self.restore()

            elif randlist[32] <= 80:
                currentenemy = enemy2
                self.restore()
            else:
                currentenemy = None

        elif zonemap[myPlayer.location][ZONE] == '6':
            if randlist[34] <= 50:
                currentenemy = enemy4
                self.restore()

            elif randlist[35] <= 80:
                currentenemy = enemy3
                self.restore()
            else:
                currentenemy = None

        elif zonemap[myPlayer.location][ZONE] == '7':
            currentenemy = enemy5
            self.restore()

    def print_location(self, destination):
        # works but test
        # locale = tk.Label(self.nwframe, text=destination, borderwidth=4, padx=2, pady=2)
        # locale.pack()
        if myPlayer.location in ['f2', 'g2', 'h2', 'c2', 'e5', 'h3', 'h1']:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "" + '| ' + myPlayer.location.upper() + ' |')
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "\n" + zonemap[myPlayer.location][DESCRIPTION] + "\n")
            # self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))

        elif myPlayer.location in ['2b2', '2a2', '2c5', '2d3']:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT, "" + ('*' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "" + '|  ' + myPlayer.location.upper() + '  |')
            self.text_area.insert(tk.INSERT, "" + ('*' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "\n" + zonemap[myPlayer.location][DESCRIPTION] + "\n")
            # self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))

        elif zonemap[myPlayer.location][ZONE] in ['1', '2', '3']:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "" + '| ' + myPlayer.location.upper() + ' |')
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "\n" + zonemap[myPlayer.location][DESCRIPTION] + "\n")
            # self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))

        elif zonemap[myPlayer.location][ZONE] in ['5', '6', '7']:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "" + '|  ' + myPlayer.location.upper() + '  |')
            self.text_area.insert(tk.INSERT, "" + ('**' * (len(myPlayer.location))))
            self.text_area.insert(tk.INSERT, "\n" + zonemap[myPlayer.location][DESCRIPTION] + "\n")
            # self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))

    def examine(self):
        randlist.clear()
        for j in range(300):
            randlist.append(random.randint(1, 100))

        if zonemap[myPlayer.location][SOLVE]:
            self.text_area.configure(state='normal')
            self.text_area.insert(tk.INSERT, "You have examined this room already!\n")
            self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
            self.text_area.configure(state='disabled')
        else:
            if zonemap[myPlayer.location][SOLVE] is False:
                self.text_area.configure(state='normal')
                wheres = ['hiding in the corner of the room', 'on the dirt floor',
                          'which magically appeared in your pocket',
                          'under the light source', "that was hidden in a crack in the wall"]
                rand_index = random.randrange(0, len(wheres))
                rand_indexx = random.randrange(0, len(wheres))
                rand_indexxx = random.randrange(0, len(wheres))

                written = ['written', 'scrawled', 'scratched', 'carved']
                rand_index4 = random.randrange(0, len(written))
                posters = ['Cloudy with a Chance of Monsters', 'Are you sure this place is abandoned?',
                           'I forgot. -Lisa Birgit Holst',
                           'uvsviarl si oedc het!', 'C.D TheoryOE', 'N.A.A; B.E.A',
                           'dashdot dashdashdash dashdash dashdashdash!', 'NAG A RAM: Lisa Birgit Holst?']
                rand_index2 = random.randrange(0, len(posters))
                fonting = ['muddled', 'hypnotized', 'rushed', 'panicked', 'confused', 'chaotic', 'angry']
                rand_index3 = random.randrange(0, len(fonting))
                self.text_area.insert(tk.INSERT, "Examining the room...\n")
                if randlist[1] <= 75:
                    self.text_area.insert(tk.INSERT,
                                          "Someone " + written[rand_index4] + " " + posters[rand_index2] + " in a " +
                                          fonting[
                                              rand_index3] + " fashion on the wall\n")
                if randlist[45] <= 20:
                    myPlayer.inventory.append(coin)
                    myPlayer.inventory.append(coin)
                    self.text_area.insert(tk.INSERT, "You found two coins " + wheres[rand_index] + "!\n")
                elif randlist[2] <= 35:
                    myPlayer.inventory.append(coin)
                    self.text_area.insert(tk.INSERT, "You found a coin " + wheres[rand_indexx] + ".\n")
                if randlist[47] <= 5:
                    myPlayer.inventory.append(bullet)
                    myPlayer.inventory.append(bullet)
                    self.text_area.insert(tk.INSERT, "You found two bullets " + wheres[rand_indexx] + ".\n")
                elif randlist[4] <= 15:
                    myPlayer.inventory.append(bullet)
                    self.text_area.insert(tk.INSERT, "You found a bullet " + wheres[rand_index] + ".\n")
                if randlist[13] <= 35:
                    myPlayer.inventory.append(potion)
                    self.text_area.insert(tk.INSERT, "You found a potion " + wheres[rand_indexxx] + ".\n")
                if randlist[1] > 75 and randlist[45] > 20 and randlist[2] > 35 and randlist[47] > 5 and randlist[
                    4] > 15 and randlist[13] > 25:
                    self.text_area.insert(tk.INSERT, "You found nothing. This room is empty.\n")
                self.text_area.insert(tk.INSERT, '--------------------------------------------------\n')
                zonemap[myPlayer.location][SOLVE] = True
                self.text_area.configure(state='disabled')

    # def chanceforshotmain(self):
    #     # global enemturn, youmiss

    def vend(self):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.INSERT,
                              "\nWelcome to Lisa Birgit Holst's Vending Machine!\n--------------------------------------------------------\n")
        self.text_area.insert(tk.INSERT,
                              'Items available: \n**********************************************************************************\n')
        self.text_area.configure(state='disabled')
        # machine = VendingMachine()
        # bulhow = random.randint(1, 10)
        # pothow = random.randint(1, 4)
        # elixhow = random.randint(1, 2)
        # htwoohow = random.randint(1, 3)
        # item8 = Item('Sniper', 15, 1, "75% hit rate: " + weapons[5]['description'] + "(" + str(weapons[5]['damage']) + " damage) ")
        # item7 = Item('Rifle', 10, 1, "75% hit rate: " + weapons[4]['description']+ " (" + str(weapons[4]['damage']) + " damage) ")
        # item6 = Item('Pistol', 7, 1, "75% hit rate: " + weapons[3]['description'] + " (" + str(weapons[3]['damage']) + " damage)")
        # item5 = Item('Sword', 5, 1, weapons[2]['description'] + " (" + str(weapons[2]['damage']) + " damage) ")
        # item4 = Item('Elixir', 5, elixhow, weapons[4]['description'])
        # item3 = Item('H2O', 3, htwoohow, weapons[5]['description'])
        # item2 = Item('Potion', 2, pothow, weapons[1]['description'])
        # item1 = Item('Bullet', 1, bulhow, weapons[3]['description'])
        # if myPlayer.location in ['c2', 'e5', 'h3']:
        #     if randlist[34] <= 15:
        #         machine.addItem(item1)
        #     if randlist[35] <= 25:
        #         machine.addItem(item2)
        #     if randlist[36] <= 50:
        #         machine.addItem(item3)
        #     if randlist[37] <= 75:
        #         machine.addItem(item4)
        #     if randlist[40] <= 25:
        #         machine.addItem(item5)
        #     if randlist[39] <= 50:
        #         machine.addItem(item6)
        #     machine.addItem(item8)
        #     machine.addItem(item9)
        #
        # elif myPlayer.location in ['2c5', '2d3']:
        #     if randlist[34] <= 25:
        #         machine.addItem(item8)
        #     elif randlist[34] > 25:
        #         machine.addItem(item7)
        #     if randlist[35] <= 25:
        #         machine.addItem(item6)
        #     elif randlist[35] > 25:
        #         machine.addItem(item5)
        #     scramble = [item1,item2,item3, item4]
        #     pick = random.sample(scramble,2)
        #     machine.addItem(pick[1])
        #     machine.addItem(pick[2])
        #
        # self.show_frame1("Vending")

        # continueToBuy = True
        # while continueToBuy == True:
        #     machine.showItems()
        #     print(
        #         "Select item for purchase? Type the name of the item you want to purchase or type 'i' for inventory, alternatively, type 'n' to exit.\n(-You have " + str(
        #             myPlayer.inventory.count(coin)) + " coin(s)-)")
        #     selected = input('> ')
        #     if machine.containsItem(selected.lower()):
        #         item = machine.getItem(selected.lower())
        #         machine.buyItem(item)
        #
        #
        #     elif selected.lower() == 'n':
        #         continueToBuy = False
        #         print("You left the vending machine")
        #     else:
        #         print('--------------------------------------------------')
        #         print('Item not available. Please select another item.')
        #         print('--------------------------------------------------')
        #         # clear
        #         continue

    def restore(self):
        currentenemy.health = currentenemy.orighealth

    def weapongot(self):
        global adddagger, addsword, addpistol, addrifle, addsniper
        wherew = [' sits in the middle of the room on a pedestal', ' glints in the corner of the room',
                  ' lies on the dusty floor', ' sits atop a table in the room']
        rand_index3 = random.randrange(0, len(wherew))
        if (zonemap[myPlayer.location][ZONE] == '1'):
            if randlist[7] <= 10:
                self.find(2)
                self.wait_variable(self.slowvar)
                # addsword()
            elif (randlist[6] <= 33):
                self.find(1)
                self.wait_variable(self.slowvar)
        elif (zonemap[myPlayer.location][ZONE] == '2'):
            if randlist[7] <= 10:
                self.find(2)
                self.wait_variable(self.slowvar)
            elif randlist[6] <= 33:
                self.find(1)
                self.wait_variable(self.slowvar)
        elif (zonemap[myPlayer.location][ZONE] == '3'):
            if randlist[8] <= 10:
                self.find(3)
                self.wait_variable(self.slowvar)
            elif randlist[7] <= 25:
                self.find(2)
                self.wait_variable(self.slowvar)
            elif randlist[6] <= 50:
                self.find(1)
                self.wait_variable(self.slowvar)
        elif (zonemap[myPlayer.location][ZONE] == '4'):
            if randlist[9] <= 10:
                self.find(4)
                self.wait_variable(self.slowvar)
            elif randlist[8] <= 20:
                self.find(3)
                self.wait_variable(self.slowvar)
            elif randlist[7] <= 50:
                self.find(2)
                self.wait_variable(self.slowvar)
        elif (zonemap[myPlayer.location][ZONE] == '5'):
            if randlist[10] <= 10:
                self.find(5)
                self.wait_variable(self.slowvar)
            elif randlist[9] <= 20:
                self.find(4)
                self.wait_variable(self.slowvar)
            elif randlist[8] <= 33:
                self.find(3)
                self.wait_variable(self.slowvar)
            elif randlist[7] <= 50:
                self.find(2)
                self.wait_variable(self.slowvar)
        elif (zonemap[myPlayer.location][ZONE] == '6'):
            if randlist[10] <= 20:
                self.find(5)
                self.wait_variable(self.slowvar)
            elif randlist[9] <= 30:
                self.find(4)
                self.wait_variable(self.slowvar)
            elif randlist[8] <= 50:
                self.find(3)
                self.wait_variable(self.slowvar)

    def main(self):
        global enemturn, youmiss
        if not enemturn:
            #print('not turn')
            # randlistten.clear()
            # for o in range(150):
            #     randlistten.append(random.randint(1, 100))
            # if (myPlayer.main[0] == "Pistol" or myPlayer.main[0] == "Rifle" or myPlayer.main[0] == "Sniper") and (
            #         myPlayer.inventory.count(bullet) >= 1):
            #     if randlistten[35] <= 25:
            #         print("You attempted to " + str(myPlayer.main[2]) + " the " + currentenemy.name)
            #         howumiss = ['you missed', 'your gun jammed', 'the bullets were faulty',
            #                     'you were not strong enough to pull back the trigger',
            #                     'the enemy distracted you by making funny faces', 'your finger slipped']
            #         rand_howumiss = random.randrange(0, len(howumiss))
            #         print("but " + howumiss[rand_howumiss] + "!\n")
            #         myPlayer.inventory.remove(bullet)
            #         enemturn = True
            #         youmiss = True
            #     else:
            #         enemturn = False
            #         youmiss = False
            # elif (myPlayer.main[0] == "Pistol" or myPlayer.main[0] == "Rifle" or myPlayer.main[0] == "Sniper") and (
            #         myPlayer.inventory.count(bullet) < 1):
            #     print("You can't shoot using your " + myPlayer.main[0] + "!\nYou don't have any bullets!\n")
            #     enemturn = True
            #     youmiss = True
            if youmiss is False:
                myPlayer.base_damage = myPlayer.main['damage']
                myPlayer.attack(currentenemy)
                self.text_area.configure(state='normal', font=("Times New Roman", 15))
                self.text_area.insert(tk.INSERT,
                                      "You " + str(
                                          myPlayer.main['action']) + " the " + currentenemy.name + "!" + " ( -" + str(
                                          myPlayer.base_damage) + " )\n")
                self.text_area.insert(tk.INSERT, "Opponent health: (" + str(currentenemy.health) + " / " + str(
                    currentenemy.orighealth) + ")\n\n")
                self.text_area.configure(state='disabled', font=("Times New Roman", 15))
                if myPlayer.main['name'] == ['Sniper', 'Rifle', 'Pistol']:
                    myPlayer.inventory.remove(bullet)
                enemturn = True
                self.attackvar.set(0)

    def secondary(self):
        global enemturn, youmiss
        if not enemturn:
            randlistten.clear()
            for u in range(150):
                randlistten.append(random.randint(1, 100))

            self.text_area.configure(state='normal', font=("Times New Roman", 15))

            if (myPlayer.secondary['name'] == ["Pistol", "Rifle", "Sniper"]) and (
                    myPlayer.inventory.count(bullet) >= 1):
                if randlistten[135] <= 25:
                    self.text_area.insert(tk.INSERT, "You attempted to " + str(
                        myPlayer.secondary['action']) + " the " + currentenemy.name + "\n")

                    howumiss = ['you missed', 'your gun jammed', 'the bullets were faulty',
                                'you were not strong enough to pull back the trigger',
                                'the enemy distracted you by making funny faces', 'your finger slipped']
                    rand_howumiss = random.randrange(0, len(howumiss))
                    self.text_area.insert(tk.INSERT, "but " + howumiss[rand_howumiss] + "!\n")
                    myPlayer.inventory.remove(bullet)
                    enemturn = True
                    youmiss = True
                else:
                    enemturn = False
                    youmiss = False
            elif myPlayer.secondary['name'] == ['Sniper', 'Pistol', 'Rifle'] and (myPlayer.inventory.count(bullet) < 1):
                self.text_area.insert(tk.INSERT, "You can't shoot using your " + myPlayer.secondary[
                    'name'] + "!\n You don't have any bullets!\n")
                enemturn = True
                youmiss = True
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            if youmiss is False:
                myPlayer.base_damage = myPlayer.secondary['damage']
                myPlayer.attack(currentenemy)
                self.text_area.configure(state='normal', font=("Times New Roman", 15))
                self.text_area.insert(tk.INSERT,
                                      "You " + str(myPlayer.secondary[
                                                       'action']) + " the " + currentenemy.name + "!" + " ( -" + str(
                                          myPlayer.base_damage) + " )\n")
                self.text_area.insert(tk.INSERT, "Opponent health: (" + str(currentenemy.health) + " / " + str(
                    currentenemy.orighealth) + ")\n\n")
                self.text_area.configure(state='disabled', font=("Times New Roman", 15))
                if myPlayer.secondary['name'] == ['Sniper', 'Rifle', 'Pistol']:
                    myPlayer.inventory.remove(bullet)
                enemturn = True
                self.attackvar.set(0)

    def potion(self):
        self.text_area.configure(state='normal', font=("Times New Roman", 15))
        if (myPlayer.inventory.count(potion) >= 1):
            if (myPlayer.orighealth - myPlayer.health) <= 50:
                difhealth = (myPlayer.orighealth - myPlayer.health)
                myPlayer.health = myPlayer.orighealth
                self.text_area.insert(tk.INSERT,
                                      "( +" + str(difhealth) + " ) You've healed " + str(
                                          difhealth) + " health! \nYour health: (" + str(myPlayer.health) + " / " + str(
                                          myPlayer.orighealth) + ")\n")

                myPlayer.inventory.remove(potion)
                self.text_area.insert(tk.INSERT,
                                      "You have " + str(myPlayer.inventory.count(potion)) + " potion(s) left\n")
                self.text_area.insert(tk.INSERT,
                                      "-------------------------\n")
            elif (myPlayer.orighealth - myPlayer.health) >= 50:
                myPlayer.health += 50
                self.text_area.insert(tk.INSERT,
                                      "( +50 )\nYour new health: (" + str(myPlayer.health) + " / " + str(
                                          myPlayer.orighealth) + ")\n")
                myPlayer.inventory.remove(potion)
                self.text_area.insert(tk.INSERT,
                                      "You have " + str(myPlayer.inventory.count(potion)) + " potion(s) left\n")
                self.text_area.insert(tk.INSERT,
                                      "-------------------------\n")
        elif (myPlayer.inventory.count(potion) < 1):
            self.text_area.insert(tk.INSERT,
                                  "You have no potions!\n")
            self.text_area.insert(tk.INSERT,
                                  "-------------------------\n")

        self.text_area.configure(state='disabled', font=("Times New Roman", 15))

    def battle(self):
        global enemturn, youmiss, mainwdamage, secwdamage, currentenemy
        #print("run battle")
        if currentenemy is None:
            #print(("none"))
            pass
        else:
            #print(("Fight time"))
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT,
                                  "===========================================================================\n")
            self.text_area.insert(tk.INSERT, "A " + currentenemy.name + " appeared!\n")
            self.text_area.insert(tk.INSERT, "You: (" + str(myPlayer.health) + " / " + str(
                myPlayer.orighealth) + ") face off against a " + str(currentenemy.name) + ": (" + str(
                currentenemy.health) + " / " + str(currentenemy.orighealth) + ")!\n")
            self.text_area.insert(tk.INSERT, "-------------------------\n")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))

            self.show_frame1("Attack")
            self.fight()

    def fight(self):
        global currentenemy, enemturn, youmiss
        rand1 = random_number(8)
        youmiss = False
        # print("Main Weapon: " + str(myPlayer.main[0]) + " ; damage: " + str(mainwdamage))
        # print("Secondary Weapon: " + str(myPlayer.secondary[0]) + " ; damage: " + str(secwdamage))
        # if (myPlayer.main[0] == "Pistol" or myPlayer.main[0] == "Rifle" or myPlayer.main[0] == "Sniper" or
        #         myPlayer.secondary[0] == "Pistol" or myPlayer.secondary[0] == "Rifle" or myPlayer.secondary[
        #             0] == "Sniper"):
        #     print("\nYou have " + str(myPlayer.inventory.count(bullet)) + " bullet(s).")
        # print("Type M to use the main weapon, Type S to use the secondary weapon, or Type P to use a potion")
        # mors = input("> ")
        # yesmors = ['m', 's', 'p']
        # while mors.lower() not in yesmors:
        #     print("Unknown action, try again")
        #     mors = input("> ")
        #     print("-------------------------")
        # if mors.lower() == 'm' and enemturn is False:
        #     chanceforshotmain()
        #     if youmiss is False and enemturn is False:
        #         myPlayer.base_damage = mainwdamage
        #         myPlayer.attack(currentenemy)
        #         print("You " + str(myPlayer.main[1]) + " the " + currentenemy.name + "!" + " ( -" + str(
        #             myPlayer.base_damage) + " )")
        #         print(
        #             "Opponent health: (" + str(currentenemy.health) + " / " + str(
        #                 currentenemy.orighealth) + ")\n")
        #         if myPlayer.main[0] == "Pistol" or myPlayer.main[0] == "Rifle" or myPlayer.main[0] == "Sniper":
        #             myPlayer.inventory.remove(bullet)
        #         enemturn = True
        # elif mors.lower() == 's' and enemturn is False:
        #     chanceforshotsec()
        #     if youmiss is False and enemturn is False:
        #         myPlayer.base_damage = secwdamage
        #         myPlayer.attack(currentenemy)
        #         print("You " + str(myPlayer.secondary[1]) + " the " + currentenemy.name + "!" + " ( -" + str(
        #             myPlayer.base_damage) + " )")
        #         print(
        #             "Opponent health: (" + str(currentenemy.health) + " / " + str(
        #                 currentenemy.orighealth) + ")\n")
        #         if (myPlayer.secondary[0] == "Pistol" or myPlayer.secondary[0] == "Rifle" or myPlayer.secondary[
        #             0] == "Sniper"):
        #             myPlayer.inventory.remove(bullet)
        #         enemturn = True
        # elif mors.lower() == 'p' and enemturn is False:
        #     if (myPlayer.inventory.count(potion) >= 1):
        #         if (myPlayer.orighealth - myPlayer.health) <= 50:
        #             difhealth = (myPlayer.orighealth - myPlayer.health)
        #             myPlayer.health = myPlayer.orighealth
        #             print("( +" + str(difhealth) + " ) You've healed " + str(
        #                 difhealth) + " health! \nYour health: (" + str(myPlayer.health) + " / " + str(
        #                 myPlayer.orighealth) + ")")
        #             myPlayer.inventory.remove(potion)
        #             print("You have " + str(myPlayer.inventory.count(potion)) + " potion(s) left")
        #             print("-------------------------")
        #         elif (myPlayer.orighealth - myPlayer.health) >= 50:
        #             myPlayer.health += 50
        #             print("( +50 )\nYour new health: (" + str(myPlayer.health) + " / " + str(
        #                 myPlayer.orighealth) + ")")
        #             myPlayer.inventory.remove(potion)
        #             print("You have " + str(myPlayer.inventory.count(potion)) + " potion(s) left")
        #             print("-------------------------")
        #     elif (myPlayer.inventory.count(potion) < 1):
        #         print("You have no potions!")
        #         print("-------------------------")
        self.wait_variable(self.attackvar)
        if currentenemy.health <= 0:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT, "You killed the " + currentenemy.name + "!\n")
            self.text_area.insert(tk.INSERT, "-------------------------\n")

            if (randlist[30] >= 75) and (zonemap[myPlayer.location][ZONE] in ['4', '5', '6', '7']):
                myPlayer.inventory.append(potion)
                myPlayer.inventory.append(potion)
                self.text_area.insert(tk.INSERT, "You got 2 potions from beating the " + currentenemy.name + "!\n")
            if (randlist[30] <= 25) and (zonemap[myPlayer.location][ZONE] in ['4', '5', '6', '7']):
                myPlayer.inventory.append(potion)
                self.text_area.insert(tk.INSERT, "You got a potion from beating the " + currentenemy.name + "!\n")
            if (randlist[145] <= 50) and (zonemap[myPlayer.location][ZONE] in ['1', '2', '3']):
                myPlayer.inventory.append(potion)
                self.text_area.insert(tk.INSERT, "You got a potion from beating the " + currentenemy.name + "!\n")
            if 25 < randlist[31] <= 50:
                myPlayer.inventory.append(bullet)
                self.text_area.insert(tk.INSERT, "You got a bullet from beating the " + currentenemy.name + "!\n")
            if randlist[31] <= 25:
                myPlayer.inventory.append(coin)
                self.text_area.insert(tk.INSERT, "You got a coin from beating the " + currentenemy.name + "!\n")
            if randlist[39] <= 50:
                self.text_area.insert(tk.INSERT, "\nThe " + currentenemy.name + " dropped a pot of Elixir!\n")
                myPlayer.health += 25
                myPlayer.orighealth += 25
                effects = ['invigorated', 'energized',
                           'rejuvenated',
                           'revitalized', "strengthened"]
                rand_effects = random.randrange(0, len(effects))
                self.text_area.insert(tk.INSERT, "You feel " + effects[rand_effects] + "!\n")
                self.text_area.insert(tk.INSERT, "Your New Health: (" + str(myPlayer.health) + " / " + str(
                    myPlayer.orighealth) + ")\n\n")
            if (randlist[39] > 50) and randlist[31] > 50:
                if 25 < randlist[30] < 75 and (zonemap[myPlayer.location][ZONE] in ['4', '5', '6', '7']):

                    self.text_area.insert(tk.INSERT, "The " + currentenemy.name + " did not drop anything!\n")

                elif (randlist[145] > 50) and (zonemap[myPlayer.location][ZONE] in ['1', '2', '3']):
                    self.text_area.insert(tk.INSERT, "The " + currentenemy.name + " did not drop anything!\n")
            currentenemy = None
            enemturn = False
            #print("stop fighting")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            #print('config')
            self.show_frame1("Move")
            #print('move')
        elif enemturn is True and rand1 <= 4:
            currentenemy.base_damage = currentenemy.orig_damage
            currentenemy.attack(myPlayer)
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT,
                                  "The " + str(currentenemy.name) + " " + str(
                                      currentenemy.basicmove) + " you!" + " ( -" + str(
                                      currentenemy.base_damage) + " )\n")
            self.text_area.insert(tk.INSERT,
                                  "Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + "\n")
            self.text_area.insert(tk.INSERT, "-------------------------\n")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            if myPlayer.health <= 0:
                self.death()
            enemturn = False
            self.fight()
        elif enemturn is True and rand1 == 5:
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT,
                                  "The " + str(currentenemy.name) + " attempted to " + str(
                                      currentenemy.failspecialmove) + " you!\nbut it missed!\n")
            self.text_area.insert(tk.INSERT, "-------------------------\n")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            enemturn = False
            self.fight()
        elif enemturn is True and rand1 >= 6:
            currentenemy.base_damage = currentenemy.special_damage
            currentenemy.attack(myPlayer)
            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT,
                                  "The " + str(currentenemy.name) + " " + str(
                                      currentenemy.specialmove) + " you!" + " ( -" + str(
                                      currentenemy.base_damage) + " )\n")
            self.text_area.insert(tk.INSERT,
                                  "Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")\n")
            self.text_area.insert(tk.INSERT, "-------------------------\n")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            if myPlayer.health <= 0:
                self.death()
            enemturn = False
            self.fight()

    def death(self):
        if myPlayer.health <= 0:
            deathway = ['devoured', 'obliterated',
                        'destroyed', "defeated", 'killed', 'annihilated']
            rand_deathway = random.randrange(0, len(deathway))
            # switch

            self.text_area.configure(state='normal', font=("Times New Roman", 15))
            self.text_area.insert(tk.INSERT,
                                  str(myPlayer.location) + ": Here lies the bones of " + myPlayer.name + ".\n")
            self.text_area.insert(tk.INSERT,
                                  "You were " + deathway[rand_deathway] + " by a " + str(currentenemy.name) + ".\n")
            self.text_area.insert(tk.INSERT, "Rerun the program to play again.\n")
            self.text_area.insert(tk.INSERT,
                                  "=================================================================================\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n================================================================================\n")
            self.text_area.configure(state='disabled', font=("Times New Roman", 15))
            print("You died")
        # self.after(5000,self.controller.show_frame("Death"))
            #     #time.sleep(20)

    def find(self, number):

        wherew = [' sits in the middle of the room on a pedestal', ' glints in the corner of the room',
                  ' lies on the dusty floor', ' sits atop a table in the room']
        rand_index3 = random.randrange(0, len(wherew))
        self.text_area.configure(state='normal', font=("Times New Roman", 15))
        self.text_area.insert(tk.INSERT, "--------------------------------------------------\n")
        self.text_area.insert(tk.INSERT, "A " + weapons[number]['name'] + wherew[rand_index3] + ".\n")
        self.text_area.insert(tk.INSERT, "You pick up the " + weapons[number]['name'] + ": (" + str(
            weapons[number]['damage']) + ").\n")
        self.text_area.configure(state='disabled', font=("Times New Roman", 15))
        self.show_frame1("PickUp")
        self.number.set(number)
        #print("number is set")
        #print(number)
        # now a definition that can get called back when m or s is passed

    def codegot(self):
        global currentenemy, gotten0, gotten1, gotten2, donecodes, numcodes, tries
        numcodes = 3
        tries = round((randlist[159] / 20)) + 2
        if donecodes == True:
            self.text("-------------------------")
            self.text("You see a computer with a dark screen.")
            self.text("You have already solved all the riddles!")
            self.text("-------------------------")
            if myPlayer.location in ['2f4']:
                self.text("-------------------------")
                # time.sleep(2)
                self.text("You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
                # time.sleep(2)
            donecodes = True
        elif donecodes == False:
            gocode = True
            # time.sleep(2)
            self.text("===========================================================================\n")
            self.text(
                "A computer with a sticker 'Lisa Birgit Holst' sits in front of you. There is " + str(
                    numcodes) + " entry field(s) and a keyboard to type with.")
            self.text("\nSmall Reward: What is the code?")
            self.text("Medium Reward: What city are you in?")
            self.text("Jackpot: This is a ___ _____")
            self.text("\n--------------------------------------------------")

            while gocode:
                if tries == 0:
                    self.text("The screen turns black. You have no more attempts!")
                    ##time.sleep(2)
                    if myPlayer.location in ['2f4']:
                        self.text("-------------------------")
                        # time.sleep(2)
                        self.text(
                            "You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
                        # time.sleep(2)
                    break
                self.text("What is the code? (" + str(
                    tries) + " attempt(s) remaining!). Type 'i' to check inventory and 'n' to exit.\nThere are " + (
                                  str(numcodes) + " riddles left to solve!"))
                if gotten0 == False:
                    return Code.entry1.get() and self.shared_data["Code #1"]
                    self.text('The code is "arkos"!')
                    speech89 = '''Dispensing the Small Reward....'''
                    for character in speech89:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        # time.sleep(0.05)
                    if randlist[79] <= 33:
                        myPlayer.inventory.append(potion)
                        self.text("\nYou got a potion!")
                        self.text("-------------------------")
                        # time.sleep(1)
                    elif 33 < randlist[79] < 66:
                        myPlayer.inventory.append(coin)
                        self.text("\nYou got a coin!")
                        self.text("-------------------------")
                        # time.sleep(1)
                    # elif randlist[79] >= 66:
                    #     #time.sleep(2)
                    #     print("\nUh oh.")
                    #     #time.sleep(2)
                    #     if randlist[88] <= 33:
                    #         currentenemy = enemy1
                    #         self.restore()
                    #
                    #         print("-------------------------")
                    #     elif 33 < randlist[88] <= 66:
                    #         currentenemy = enemy2
                    #         self.restore()
                    #         self.battle()
                    #
                    #         print("-------------------------")
                    #     elif randlist[88] > 66:
                    #         currentenemy = enemy3
                    #         restore()
                    #         battle()
                    #
                    #         print("-------------------------")
                    gotten0 = True
                    numcodes -= 1
                    tries -= 1
                elif yes.lower() == yesno[1] and gotten1 == False:
                    self.text('You are in "Paris"!')
                    speech89 = '''Dispensing the Medium Reward....'''
                    for character in speech89:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        # time.sleep(0.05)
                    if randlist[78] <= 50:
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(potion)
                        self.text("\nYou got a potion and a coin!")
                    elif randlist[78] >= 50:
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(coin)
                        self.text("\nYou got two coins!")
                    self.text("-------------------------")
                    # time.sleep(1)
                    gotten1 = True
                    numcodes -= 1
                    tries -= 1
                elif yes.lower() == yesno[2] and gotten2 == False:
                    self.text('You are right! This is a "big troll"!')
                    speech89 = '''Dispensing the JACKPOT!....'''
                    for character in speech89:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        # time.sleep(0.05)
                    if randlist[79] <= 50:
                        myPlayer.inventory.append(bullet)
                        myPlayer.inventory.append(bullet)
                        myPlayer.inventory.append(bullet)
                        myPlayer.inventory.append(bullet)
                        myPlayer.inventory.append(bullet)
                        self.text("\nYou got 5 bullets!")
                    elif randlist[79] > 50:
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(coin)
                        myPlayer.inventory.append(coin)
                        self.text("\nYou got 5 coins!")
                    self.text("-------------------------")
                    # time.sleep(1)
                    gotten2 = True
                    numcodes -= 1
                    tries -= 1
                elif yes.lower() == 'n':
                    self.text("The Computer disappears .....")
                    if myPlayer.location in ['2f4']:
                        self.text("-------------------------")
                        # time.sleep(2)
                        self.text(
                            "You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
                        # time.sleep(2)
                    gocode = False
                elif yes.lower() in yesno:
                    self.text('You have already received a reward for the code "' + str(yes) + '"!')
                    self.text("-------------------------")
                    # time.sleep(1)
                else:
                    self.text("That code is incorrect!")
                    self.text("-------------------------")
                    # time.sleep(1)
                    tries -= 1
                if (gotten0 is True and gotten1 is True and gotten2 is True):
                    # time.sleep(2)
                    self.text("You have solved all the riddles! ")
                    self.text("The computer turns into a coin!")
                    myPlayer.inventory.append(coin)
                    # time.sleep(2)
                    if myPlayer.location in ['2f4']:
                        self.text("-------------------------")
                        # time.sleep(2)
                        self.text(
                            "You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
                        # time.sleep(2)
                    donecodes = True
                    gocode = False
    def victory(self):
        self.after(5000, self.controller.show_frame("Victory"))

    # def codegot(self):
    #     global currentenemy, gotten0, gotten1, gotten2, donecodes, numcodes, tries
    #
    #     tries = round((randlist[159] / 20)) + 2
    #     if donecodes == True:
    #         # time.sleep(2)
    #         print("-------------------------")
    #         print("You see a computer with a dark screen.")
    #         # time.sleep(1)
    #         print("You have already solved all the riddles!")
    #         print("-------------------------")
    #         # time.sleep(2)
    #         if myPlayer.location in ['2f4']:
    #             print("-------------------------")
    #             # time.sleep(2)
    #             print("You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
    #             # time.sleep(2)
    #         donecodes = True
    #     elif donecodes == False:
    #         gocode = True
    #         # time.sleep(2)
    #         print("===========================================================================\n")
    #         print(
    #             "A computer with a sticker 'Lisa Birgit Holst' sits in front of you. There is " + str(
    #                 numcodes) + " entry field(s) and a keyboard to type with.")
    #         print("\nSmall Reward: What is the code?")
    #         print("Medium Reward: What city are you in?")
    #         print("Jackpot: This is a ___ _____")
    #         print("\n--------------------------------------------------")
    #
    #         while gocode:
    #             if tries == 0:
    #                 print("The screen turns black. You have no more attempts!")
    #                 # time.sleep(2)
    #                 if myPlayer.location in ['2f4']:
    #                     print("-------------------------")
    #                     # time.sleep(2)
    #                     print("You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
    #                     # time.sleep(2)
    #                 break
    #             print("What is the code? (" + str(
    #                 tries) + " attempt(s) remaining!). Type 'i' to check inventory and 'n' to exit.\nThere are " + (
    #                           str(numcodes) + " riddles left to solve!"))
    #             yes = input(">")
    #             if yes.lower() == yesno[0] and gotten0 == False:
    #                 print('The code is "arkos"!')
    #                 speech89 = '''Dispensing the Small Reward....'''
    #                 for character in speech89:
    #                     sys.stdout.write(character)
    #                     sys.stdout.flush()
    #                     # time.sleep(0.05)
    #                 if randlist[79] <= 33:
    #                     myPlayer.inventory.append(potion)
    #                     print("\nYou got a potion!")
    #                     print("-------------------------")
    #                     # time.sleep(1)
    #                 elif 33 < randlist[79] < 66:
    #                     myPlayer.inventory.append(coin)
    #                     print("\nYou got a coin!")
    #                     print("-------------------------")
    #                     # time.sleep(1)
    #                 elif randlist[79] >= 66:
    #                     # time.sleep(2)
    #                     print("\nUh oh.")
    #                     # time.sleep(2)
    #                     if randlist[88] <= 33:
    #                         currentenemy = enemy1
    #                         self.restore()
    #                         self.battle()
    #
    #                         print("-------------------------")
    #                     elif 33 < randlist[88] <= 66:
    #                         currentenemy = enemy2
    #                         self.restore()
    #                         self.battle()
    #
    #                         print("-------------------------")
    #                     elif randlist[88] > 66:
    #                         currentenemy = enemy3
    #                         self.restore()
    #                         self.battle()
    #
    #                         print("-------------------------")
    #                 gotten0 = True
    #                 numcodes -= 1
    #                 tries -= 1
    #             elif yes.lower() == yesno[1] and gotten1 == False:
    #                 print('You are in "Paris"!')
    #                 speech89 = '''Dispensing the Medium Reward....'''
    #                 for character in speech89:
    #                     sys.stdout.write(character)
    #                     sys.stdout.flush()
    #                     # time.sleep(0.05)
    #                 if randlist[78] <= 50:
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(potion)
    #                     print("\nYou got a potion and a coin!")
    #                 elif randlist[78] >= 50:
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(coin)
    #                     print("\nYou got two coins!")
    #                 print("-------------------------")
    #                 # time.sleep(1)
    #                 gotten1 = True
    #                 numcodes -= 1
    #                 tries -= 1
    #             elif yes.lower() == yesno[2] and gotten2 == False:
    #                 print('You are right! This is a "big troll"!')
    #                 speech89 = '''Dispensing the JACKPOT!....'''
    #                 for character in speech89:
    #                     sys.stdout.write(character)
    #                     sys.stdout.flush()
    #                     # time.sleep(0.05)
    #                 if randlist[79] <= 50:
    #                     myPlayer.inventory.append(bullet)
    #                     myPlayer.inventory.append(bullet)
    #                     myPlayer.inventory.append(bullet)
    #                     myPlayer.inventory.append(bullet)
    #                     myPlayer.inventory.append(bullet)
    #                     print("\nYou got 5 bullets!")
    #                 elif randlist[79] > 50:
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(coin)
    #                     myPlayer.inventory.append(coin)
    #                     print("\nYou got 5 coins!")
    #                 print("-------------------------")
    #                 # time.sleep(1)
    #                 gotten2 = True
    #                 numcodes -= 1
    #                 tries -= 1
    #             elif yes.lower() == 'n':
    #                 print("The Computer disappears .....")
    #                 if myPlayer.location in ['2f4']:
    #                     print("-------------------------")
    #                     # time.sleep(2)
    #                     print("You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
    #                     # time.sleep(2)
    #                 gocode = False
    #             elif yes.lower() in yesno:
    #                 print('You have already received a reward for the code "' + str(yes) + '"!')
    #                 print("-------------------------")
    #                 # time.sleep(1)
    #             else:
    #                 print("That code is incorrect!")
    #                 print("-------------------------")
    #                 # time.sleep(1)
    #                 tries -= 1
    #             if (gotten0 is True and gotten1 is True and gotten2 is True):
    #                 # time.sleep(2)
    #                 print("You have solved all the riddles! ")
    #                 print("The computer turns into a coin!")
    #                 myPlayer.inventory.append(coin)
    #                 # time.sleep(2)
    #                 if myPlayer.location in ['2f4']:
    #                     print("-------------------------")
    #                     # time.sleep(2)
    #                     print("You step over the toppled boss. You spy a staircase. Type NORTH to ascend it.")
    #                     # time.sleep(2)
    #                 donecodes = True
    #                 gocode = False


class Map1(tk.Frame):
    # root.attributes('-fullscreen', True)
    # height = self.neframe.height
    # getting screen's width in pixels
    # width = root.winfo_screenwidth()
    # print(width)
    def __init__(self, parent, controller2):
        tk.Frame.__init__(self, parent)
        self.controller2 = controller2
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.SIZE = 675
        self.AXIS = 6.75

        mx = 0
        my = 0

        self.map1frame = tk.Frame(self, width=700, height=40)
        self.canvasFrame = tk.Frame(self, width=700, height=450, padx=10, bg='black')
        self.descriptionframe = tk.Frame(self, width=700, height=50)

        self.map1frame.grid(row=0, column=0)
        self.canvasFrame.grid(row=1, column=0)
        self.descriptionframe.grid(row=2, column=0)

        self.map1label = tk.Label(self.map1frame,
                                  text='Map 1', bg='green', fg='black', font=controller2.title_font)
        self.map1label.place(x=0, y=0, relwidth=1, relheight=1)
        self.canfram = tk.Frame(self.canvasFrame)
        self.canfram.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas = tk.Canvas(self.canfram)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.descriptionlabel = tk.Label(self.descriptionframe,
                                         text='Instructions: You are the Green square. \nThe Gold square indicates a room of interest. The Blue square marks the staircase',
                                         bg='LightBlue1', fg='black')
        self.descriptionlabel.place(x=0, y=0, relwidth=1, relheight=1)

        i = 0
        while i <= self.SIZE:
            self.canvas.create_line(0, i, self.SIZE, i)
            self.canvas.create_line(i, 0, i, self.SIZE - 225)

            i += 75

        colormap = ["green", "black", "blue", "gray", "yellow"]

        # black squares/border
        self.squares(3, 4, 2, 3, 'black')
        self.squares(4, 2, 1, 1, 'black')
        self.squares(4, 4, 1, 1, 'black')
        self.squares(5, 6, 2, 1, 'black')
        self.squares(9, 6, 3, 1, 'black')
        self.squares(9, 5, 2, 1, 'black')
        self.squares(8, 4, 1, 1, 'black')
        self.squares(8, 2, 1, 1, 'black')
        self.squares(6, 4, 1, 2, 'black')
        self.squares(6, 6, 1, 1, colormap[4])
        self.squares(9, 4, 1, 1, colormap[4])

        self.squares(4, 3, 1, 1, colormap[4])

        self.squares(9, 2, 1, 1, colormap[2])
        # self.squares(8.625, 1.625, 0.25, 0.25, 'yellow')
        self.canvas.create_polygon(617.5, 122.5, 637.5, 102.5, 657.5, 122.5, fill='#000000')
        cl = self.canvas.create_rectangle(75 + (mx * 75), 375 + (my * 75), 150 + (mx * 75), 450 + (75 * my),
                                          fill='#228B22')
        # cl = squares(2 + mx, 6 + my, 1, 1, 'green')

        # if now1 is False:
        #     cl = canvas.create_rectangle(100 + (mx * 100), 500 + (my * 100), 200 + (mx * 100), 600 + (100 * my),
        #                                  fill='#228B22')
        # elif now1 is True:
        #     cl = canvas.create_rectangle(100 + (sx * 100) + (mx * 100), 500 + (sy * 100) + (my * 100),
        #                                  200 + (sx * 100) + (mx * 100), 600 + (sy * 100) + (100 * my), fill='#228B22')
        # top and bottom labels :(
        self.key(2, 1, "A")
        self.key(3, 1, "B")
        self.key(4, 1, "C")
        self.key(5, 1, "D")
        self.key(6, 1, "E")
        self.key(7, 1, "F")
        self.key(8, 1, "G")
        self.key(9, 1, "H")

        self.key(1, 2, "1")
        self.key(1, 3, "2")
        self.key(1, 4, "3")
        self.key(1, 5, "4")
        self.key(1, 6, "5")

        # canvasn = Canvas(frame1, width=300, height=600)
        # canvasn.pack(side="right")
        # canvasn.create_text(150, 300,
        #                     text="The Map:\n\nHow to Interpret:\n\nYou are unable to\n go on the black squares\n\nWhite squares show areas\n that are accessible \n\nThe Blue square marks \n a staircase \n\nThe Green square denotes \n where you are now. ",
        #                     font=('Times', 20), fill='#000000', justify='center')
        def update():
            global mx, my
            if mx != 0 or my != 0:
                # print(mx, my)
                self.canvas.move(cl, (75 * mx), (75 * my))
                mx = 0
                my = 0
            self.after(500, update)

        self.after(1000, update)

    # define title for window

    # PARAMETERS

    def squares(self, x, y, bigx, bigy, color):
        pos = [0.75 * x * self.SIZE / self.AXIS, 0.75 * y * self.SIZE / self.AXIS]
        pas = [0.75 * x * self.SIZE / self.AXIS - 100 * 0.75 * bigx,
               0.75 * y * self.SIZE / self.AXIS - 100 * 0.75 * bigy]

        pawn_colors = {'gray': '#999999', 'blue': '#6495ED', 'black': '#000000', 'green': '#228B22',
                       'yellow': '#FFD343'}
        self.canvas.create_rectangle(pas, pos, fill=pawn_colors[color])

    def key(self, x, y, letter):
        pos = [(0.75 * x - 0.5 * 0.75) * self.SIZE / self.AXIS, (0.75 * y - 0.5 * 0.75) * self.SIZE / self.AXIS]

        pawn_colors = {'gray': '#999999', 'blue': '#6495ED', 'black': '#000000'}

        self.canvas.create_text(pos, text=letter, font=('Times', 30), fill='#000000')

    # frame1.minsize(SIZE, SIZE-225)
    # frame1.maxsize(SIZE,SIZE-225)
    # map_button = Button(frame1, text="Show Map")
    # map_button.pack()
    #
    # def run():
    #     global z
    #     z = random.randint(0,1000)
    #
    # b = Button(frame1, text="Smth", command=run)
    # b.pack()
    # def name():
    #     player_name = txtentered
    #     myPlayer.name = player_name
    #     grabtxt( '''Here begins the journey of ''' + str(player_name) + ".\n")
    #     root.wait_variable(proceed)
    #     grabtxt("###############################\n    The Abandoned Building     \n###############################")
    #     grabtxt('''You can't get out. Be on the lookout for clues. "Escape if you can"..... \n''')
    #     grabtxt(
    #         '''\nRemember, type a "direction" to move in that direction, type "e" to examine \nType "i" to check inventory, type 'map' to see the map and type "p" to use a potion''')
    #     weaponadd(fists)
    #     secondaryadd(none)


class Map2(tk.Frame):
    def __init__(self, parent, controller2):
        tk.Frame.__init__(self, parent)
        self.controller2 = controller2
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.SIZE = 525
        self.AXIS = 5.25

        sx = 0
        sy = 0

        self.map1frame = tk.Frame(self, width=700, height=40)
        self.canvasFrame = tk.Frame(self, width=700, height=450, padx=85, bg='black')
        self.descriptionframe = tk.Frame(self, width=700, height=50)

        self.map1frame.grid(row=0, column=0)
        self.canvasFrame.grid(row=1, column=0)
        self.descriptionframe.grid(row=2, column=0)

        self.map1label = tk.Label(self.map1frame,
                                  text='Map 2', bg='green', fg='black', font=controller2.title_font)
        self.map1label.place(x=0, y=0, relwidth=1, relheight=1)
        self.canfram = tk.Frame(self.canvasFrame)
        self.canfram.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas = tk.Canvas(self.canfram)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.descriptionlabel = tk.Label(self.descriptionframe,
                                         text='Instructions: You are at the location of the Green square. The Gold square indicates a room of interest. \nThe Blue square marks a staircase. The Pink square marks the end',
                                         bg='LightBlue1', fg='black')
        self.descriptionlabel.place(x=0, y=0, relwidth=1, relheight=1)

        i = 0
        while i <= self.SIZE:
            self.canvas.create_line(0, i, self.SIZE, i)
            self.canvas.create_line(i, 0, i, self.SIZE - 75)

            i += 75

        colormap = ["green", "black", "blue", "gray", "yellow", "pink"]

        # black squares/border

        self.squares(3, 6, 2, 3, 'black')

        self.squares(7, 2, 4, 1, 'black')
        self.squares(7, 3, 2, 1, 'black')
        self.squares(6, 5, 1, 1, 'black')
        self.squares(7, 4, 1, 1, 'black')
        self.squares(2, 2, 1, 1, 'black')

        # the end square
        self.squares(7, 5, 1, 1, 'pink')

        # the blue squares
        self.squares(2, 3, 1, 1, colormap[2])
        # the yellow self.squares
        self.squares(4, 6, 1, 1, colormap[4])
        self.squares(5, 4, 1, 1, colormap[4])
        # the Arrows
        self.canvas.create_polygon(92.5, 177.5, 112.5, 197.5, 132.5, 177.5, fill='#000000')
        self.canvas.create_polygon(467.5, 347.5, 487.5, 327.5, 507.5, 347.5, fill='#000000')
        cl2 = self.canvas.create_rectangle(75 + (sx * 75), 150 + (sy * 75), 150 + (sx * 75), 225 + (75 * sy),
                                           fill='#228B22')
        #     # cl = squares(2 + mx, 6 + my, 1, 1, 'green')
        #
        #     # if now1 is False:
        #     #     cl = canvas.create_rectangle(100 + (mx * 100), 500 + (my * 100), 200 + (mx * 100), 600 + (100 * my),
        #     #                                  fill='#228B22')
        #     # elif now1 is True:
        #     #     cl = canvas.create_rectangle(100 + (sx * 100) + (mx * 100), 500 + (sy * 100) + (my * 100),
        #     #                                  200 + (sx * 100) + (mx * 100), 600 + (sy * 100) + (100 * my), fill='#228B22')
        #     # top and bottom labels :(
        #
        self.canvas.create_line(300, 225, 300, 450,width=4)
        self.key(2, 1, "A")
        self.key(3, 1, "B")
        self.key(4, 1, "C")
        self.key(5, 1, "D")
        self.key(6, 1, "E")
        self.key(7, 1, "F")
        # self.key(8,1, "G")
        # self.key(9,1, "H")

        self.key(1, 2, "1")
        self.key(1, 3, "2")
        self.key(1, 4, "3")
        self.key(1, 5, "4")
        self.key(1, 6, "5")

        def update():
            global sx, sy
            if sx != 0 or sy != 0:
                # print(sx, sy)
                self.canvas.move(cl2, (75 * sx), (75 * sy))
                sx = 0
                sy = 0
            self.after(500, update)

        self.after(1000, update)

    # define title for window

    # PARAMETERS

    def squares(self, x, y, bigx, bigy, color):
        pos = [0.75 * x * self.SIZE / self.AXIS, 0.75 * y * self.SIZE / self.AXIS]
        pas = [0.75 * x * self.SIZE / self.AXIS - 100 * 0.75 * bigx,
               0.75 * y * self.SIZE / self.AXIS - 100 * 0.75 * bigy]

        pawn_colors = {'gray': '#999999', 'blue': '#6495ED', 'black': '#000000', 'green': '#228B22',
                       'yellow': '#FFD343', 'pink': '#FFC0CB'}
        self.canvas.create_rectangle(pas, pos, fill=pawn_colors[color])

    def key(self, x, y, letter):
        pos = [(0.75 * x - 0.5 * 0.75) * self.SIZE / self.AXIS, (0.75 * y - 0.5 * 0.75) * self.SIZE / self.AXIS]

        pawn_colors = {'gray': '#999999', 'blue': '#6495ED', 'black': '#000000'}

        self.canvas.create_text(pos, text=letter, font=('Times', 30), fill='#000000')

    #
    #     while i < SIZE:
    #         canvas.create_line(0, i - 200, SIZE - 200, i - 200)
    #         canvas.create_line(i - 100, 0, i - 100, SIZE - 300)
    #
    #         i += SIZE / AXIS
    #
    # def squares(x, y, bigx, bigy, color):
    #     pos = [x * SIZE / AXIS, y * SIZE / AXIS]
    #     pas = [x * SIZE / AXIS - 100 * bigx, y * SIZE / AXIS - 100 * bigy]
    #
    #     pawn_colors = {'gray': '#999999', 'blue': '#6495ED', 'black': '#000000', 'green': '#228B22',
    #                    'red': '#FF0000',
    #                    'yellow': '#FFD343', 'pink': '#FFC0CB'}
    #     canvas.create_rectangle(pas, pos, fill=pawn_colors[color])
    #
    # def key(x, y, letter):
    #     pos = [(x - 0.5) * SIZE / AXIS, (y - 0.5) * SIZE / AXIS]
    #     canvas.create_text(pos, text=letter, font=('Times', 30), fill='#000000')
    #
    # # root = tk.Tk()
    # root.title("Map 2")
    # # root.minsize(SIZE - 200, SIZE - 300)
    # canvas = tk.Canvas(root, width=SIZE - 200, height=SIZE - 305)
    # canvas.pack(side="left")
    # draw_board()
    #
    # colormap = ["green", "black", "blue", "red", "gray", "yellow", "pink"]
    #
    # # black squares/
    #
    # squares(3, 6, 2, 3, 'black')
    #
    # squares(7, 2, 4, 1, 'black')
    # squares(7, 3, 2, 1, 'black')
    # squares(6, 5, 1, 1, 'black')
    # squares(7, 4, 1, 1, 'black')
    # squares(2, 2, 1, 1, 'black')
    #
    # # the end square
    # canvas.create_polygon(600, 500, 600, 400, 700, 400, fill='#FFC0CB')
    # canvas.create_polygon(600, 500, 700, 500, 700, 400, fill='#FFD343')
    #
    # # the blue squares
    # squares(2, 3, 1, 1, colormap[2])
    # # the yellow squares
    # squares(4, 6, 1, 1, colormap[5])
    # squares(5, 4, 1, 1, colormap[5])
    # # the Arrows
    # canvas.create_polygon(125, 237.5, 150, 262.5, 175, 237.5, fill='#000000')
    # canvas.create_polygon(625, 462.5, 650, 437.5, 675, 462.5, fill='#000000')
    #
    # # moving green square denoting location
    # # squares(2 + mx, 3 + my, 1, 1, colormap[0])
    # if now1 is False:
    #     cl = canvas.create_rectangle(100 + (mx * 100), 200 + (my * 100), 200 + (mx * 100), 300 + (100 * my), fill='#228B22')
    # elif now1:
    #     cl = canvas.create_rectangle(100 +(sx*100) + (mx * 100), 200 + (sy*100)+ (my * 100), 200 + (sx*100)+ (mx * 100), 300 + (sy*100) + (100 * my), fill='#228B22')
    #
    # # squares(2, 2, 'gray')
    # # top and bottom labels :(
    #
    # self.key(2, 1, "A")
    # self.key(3, 1, "B")
    # self.key(4, 1, "C")
    # self.key(5, 1, "D")
    # self.key(6, 1, "E")
    # self.key(7, 1, "F")
    # # self.key(8,1, "G")
    # # self.key(9,1, "H")
    #
    # self.key(1, 2, "1")
    # self.key(1, 3, "2")
    # self.key(1, 4, "3")
    # self.key(1, 5, "4")
    # self.key(1, 6, "5")

    # self.neframe.after(500,update)


# sub frames in Play
class Proceed(tk.Frame):
    def __init__(self, parent, controller1):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller1
        self.frame1 = tk.Frame(self, background="LightBlue1", width=740, height=20)
        self.frame1.grid(row=0)
        self.frame2 = tk.Frame(self, background="LightBlue1", width=740, height=180)
        self.frame2.grid(row=1)
        self.controller1.text_area.configure(state='normal')
        self.controller1.text_area.insert(tk.INSERT,
                                          "====================================================================================\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n====================================================================================\nYou awaken in a dark room. You are holding a map of your surroundings. (On the right of the screen) \nYou also find a crumpled note in your pocket: 'Find your way out if you can. Lookout for special codes.'\nClick 'Proceed' to continue.\n")
        self.controller1.text_area.insert(tk.INSERT, "--------------------------------------------------\n")
        self.controller1.text_area.configure(state='disabled')

        label = tk.Label(self.frame1, text="Click to Proceed", font=controller1.title_font, background="LightBlue1")
        label.place(x=0, y=0, relwidth=1, relheight=1)
        Button = tk.Button(self.frame2, text="Proceed",
                           command=lambda: [self.controller1.intro_text(), self.controller1.show_frame1("Move")])
        Button.place(x=0, y=0, relwidth=1, relheight=1)


class Move(tk.Frame):

    def __init__(self, parent, controller1):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller1

        self.framep = tk.Frame(self, background='blue', width=740, height=40)
        self.framep.grid(row=0, column=0, columnspan=2)
        self.frame1 = tk.Frame(self, background="LightBlue1", width=500, height=160, padx=62, pady=5)
        self.frame1.grid(row=1, column=0)
        self.frame2 = tk.Frame(self, background="LightBlue1", width=240, height=160, padx=30, pady=50)
        self.frame2.grid(row=1, column=1)

        self.framep0 = tk.Frame(self.frame1, background='blue', height=50, width=125)
        self.framep0.grid(row=0, column=1)
        self.framep1 = tk.Frame(self.frame1, background='blue', height=50, width=125)
        self.framep1.grid(row=2, column=1)
        self.framep2 = tk.Frame(self.frame1, background='blue', height=50, width=125)
        self.framep2.grid(row=1, column=0)
        self.framep3 = tk.Frame(self.frame1, background='blue', height=50, width=125)
        self.framep3.grid(row=1, column=2)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        # label = tk.Label(self, text="This is page 2", font=controller1.title_font)
        # label.pack(side="top", fill="x", pady=10)
        upperwhitespace1 = tk.Label(self.framep,
                                    text='What would you like to do now? Click an Arrow Key to go in that direction, or click "Examine" to examine the room',
                                    bg='LightBlue1', fg='black')
        upperwhitespace1.place(x=0, y=0, relwidth=1, relheight=1)

        # whitespace1 = tk.Label(self.frame1, text='', bg='LightBlue1', fg='black', height=5, width=4)
        # whitespace1.pack(side='left')
        self.img = tk.PhotoImage()  # zero size image

        Up = tk.Button(self.framep0, text='North', command=lambda: self.controller1.move_up())
        Up.place(x=0, y=0, relwidth=1, relheight=1)

        down = tk.Button(self.framep1, text='South', command=lambda: self.controller1.move_down())
        down.place(x=0, y=0, relwidth=1, relheight=1)

        left = tk.Button(self.framep2, text='West', command=lambda: self.controller1.move_left())
        left.place(x=0, y=0, relwidth=1, relheight=1)

        right = tk.Button(self.framep3, text='East', command=lambda: self.controller1.move_right())
        right.place(x=0, y=0, relwidth=1, relheight=1)

        # whitespace2 = tk.Label(self.frame2, text='', bg='LightBlue1', fg='black', height=5, width=12)
        # whitespace2.pack(side='left')

        examine = tk.Button(self.frame2, text='Examine Room', command=lambda: self.controller1.examine())

        examine.place(x=0, y=0, relwidth=1, relheight=1)

        # whitespace3 = tk.Label(self.frame2, text='', bg='LightBlue1', fg='black', height=5, width=4)
        # whitespace3.pack(side='left')
        # Button = tk.Button(self, text="Pickup",
        #                    command=lambda: controller1.show_frame("PickUp"))
        # Button.pack()


class PickUp(tk.Frame):
    #print('ard')

    def __init__(self, parent, controller1):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller1

        self.framep = tk.Frame(self, background='LightBlue1', pady=10)
        self.framep.pack(side='left')
        upperwhitespace1 = tk.Label(self.framep,
                                    text='What do you want to do with the weapon? Stash it in Main(M), Secondary(S), or Drop it(D)?',
                                    bg='LightBlue1', fg='black', height=3, width=74)
        upperwhitespace1.grid(row=0, column=0, columnspan=7)

        whitespace1 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=5)
        whitespace1.grid(row=1, column=0)

        whitespace2 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=10)
        whitespace2.grid(row=1, column=2)

        whitespace3 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=10)
        whitespace3.grid(row=1, column=4)

        whitespace4 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=5)
        whitespace4.grid(row=1, column=6)

        upperwhitespace2 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=2, width=74)
        upperwhitespace2.grid(row=2, column=0, columnspan=7)
        main = tk.Button(self.framep, text='Main', height=5, width=16,
                         command=lambda: [self.controller1.m(), self.controller1.show_frame1("Move")])
        main.grid(row=1, column=1)
        secondary = tk.Button(self.framep, text='Secondary', height=5, width=16,
                              command=lambda: [self.controller1.s(), self.controller1.show_frame1("Move")])
        secondary.grid(row=1, column=3)
        drop = tk.Button(self.framep, text='Drop', height=5, width=16,
                         command=lambda: [self.controller1.d(), self.controller1.show_frame1("Move")])
        drop.grid(row=1, column=5)
        # label = tk.Label(self, text="This is page 2", controller1.title_font=font)
        # label.pack(side="top", fill="x", pady=10)
        # Button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: self.controller1.show_frame("Attack"))
        # Button.pack()


class Attack(tk.Frame):

    def __init__(self, parent, controller1):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller1

        self.framep = tk.Frame(self, background='LightBlue1', pady=10)
        self.framep.pack(side='left')
        upperwhitespace1 = tk.Label(self.framep,
                                    text='What do you want to do? Attack with your Main(M), Secondary(S), or use a Potion(P)?',
                                    bg='LightBlue1', fg='black', height=3, width=74)
        upperwhitespace1.grid(row=0, column=0, columnspan=7)

        whitespace1 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=5)
        whitespace1.grid(row=1, column=0)

        whitespace2 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=10)
        whitespace2.grid(row=1, column=2)

        whitespace3 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=10)
        whitespace3.grid(row=1, column=4)

        whitespace4 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=5, width=5)
        whitespace4.grid(row=1, column=6)

        upperwhitespace2 = tk.Label(self.framep, text='', bg='LightBlue1', fg='black', height=2, width=74)
        upperwhitespace2.grid(row=2, column=0, columnspan=7)
        main = tk.Button(self.framep, text='Main', height=5, width=16,
                         command=lambda: [self.controller1.main()])
        main.grid(row=1, column=1)
        secondary = tk.Button(self.framep, text='Secondary', height=5, width=16,
                              command=lambda: [self.controller1.secondary()])
        secondary.grid(row=1, column=3)
        potion = tk.Button(self.framep, text='Potion', height=5, width=16,
                           command=lambda: [self.controller1.potion()])
        potion.grid(row=1, column=5)


class Vending(tk.Frame):

    def __init__(self, parent, controller1):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller1
        # self.wait_variable(self.controller1.vendvar)
        # print("omega")
        #
        # self.controller1.text.after(2000,"Hello, world")

    # self.parent
    # Play.text.text_area.configure(state='normal')
    # self.text_area.insert(tk.INSERT,
    #                       "\nWelcome to Lisa Birgit Holst's Vending Machine!\n--------------------------------------------------------\n")
    # self.text_area.insert(tk.INSERT,
    #                       'Items available: \n**********************************************************************************\n')
    # self.text_area.configure(state='disabled')
    #

    #
    # framep0 = tk.Frame(self.seframe, background='blue', height=50, width=520)
    # framep0.grid(row=1, column=0)
    # framep1 = tk.Frame(self.seframe, background='blue', height=30, width=520)
    # framep1.grid(row=2, column=0)
    # framep2 = tk.Frame(self.seframe, background='blue', height=20, width=520)
    # framep2.grid(row=3, column=0)
    # framep3 = tk.Frame(self.seframe, background='blue', height=20, width=520)
    # framep3.grid(row=4, column=0)
    # Lab0 = tk.Label(framep0,
    #                 text="Inventory:")
    # Lab0.place(x=0, y=0, relwidth=1, relheight=1)
    # Lab1 = tk.Label(framep1, text="Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")")
    # Lab1.place(x=0, y=0, relwidth=1, relheight=1)
    # Lab2 = tk.Label(framep2,
    #                 text="You have " + str(myPlayer.inventory.count(coin)) + " coin(s)")
    # Lab2.place(x=0, y=0, relwidth=1, relheight=1)
    # Lab3 = tk.Label(framep3,
    #                 text="You have " + str(myPlayer.inventory.count(potion)) + " potion(s)")
    # Lab3.place(x=0, y=0, relwidth=1, relheight=1)
    # Lab4 = tk.Label(framep4,
    #                 text="You have " + str(myPlayer.inventory.count(bullet)) + " bullet(s)")
    # Lab4.place(x=0, y=0, relwidth=1, relheight=1)
    #
    #


class Code(tk.Frame):

    def __init__(self, parent, controller1, entry1):
        tk.Frame.__init__(self, parent)
        self.entry1 = tk.Entry(self)
        self.controller1 = controller1
        self.label = tk.Label(self, text="This is page 2", font=controller1.title_font)
        self.label.pack(side="top", fill="x", pady=10)
        self.input = ""
        # username = self.controller1.shared_data["username"].get()
        self.entry1.pack()
        # Button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller1.show_frame("Move"))
        # Button.pack()


class Victory(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="You win", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        Button.pack()


class Death(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.framep = tk.Frame(self, background='blue')
        self.framep.pack()
        label = tk.Label(self, text="You Died. Press the Red X and rerun the program to play again",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Lab1 = tk.Label(self.framep,
                        text="Inventory:", font=controller.title_font)
        Lab1.pack(side='bottom')
        Lab1 = tk.Label(self.framep,
                        text="Your health: (" + str(myPlayer.health) + " / " + str(myPlayer.orighealth) + ")")
        Lab1.pack(side='top')
        Lab2 = tk.Label(self.framep,
                        text="You have " + str(myPlayer.inventory.count(coin)) + " coin(s)")
        Lab2.pack(side='top')
        Lab3 = tk.Label(self.framep,
                        text="You have " + str(myPlayer.inventory.count(potion)) + " potion(s)")
        Lab3.pack(side='top')
        Lab4 = tk.Label(self.framep,
                        text="You have " + str(myPlayer.inventory.count(bullet)) + " bullet(s)")
        Lab4.pack(side='top')
        Lab5 = tk.Label(self.framep,
                        text="Main Weapon: {name}; damage: {damage}".format(name=myPlayer.main['name'],
                                                                            damage=myPlayer.main['damage']))
        Lab5.pack(side='top')
        Lab6 = tk.Label(self.framep,
                        text="Secondary Weapon: {name}; damage: {damage}".format(name=myPlayer.secondary['name'],
                                                                                 damage=myPlayer.secondary['damage']))
        Lab6.pack(side='top')
        # zonemap[RETURNED] = False
        # myPlayer.main.clear()
        # myPlayer.secondary.clear()
        # myPlayer.inventory.clear()
        # Button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # Button.pack()


class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        Button.pack()


# class Glossary(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         tk.Button = tk.Button(self, text="Go to the start page",
#                               command=lambda: controller.show_frame("StartPage"))
#         tk.Button.pack()


class Credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        Button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.minsize(1440, 770)
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    print(width, height)
    # for x in range(0:width):
    #     r = tk.Label(self, text=width)
    #     r.()
    app.title("The Abandoned Building (RPG)")
    app.mainloop()