import random
import time
#THE BATTLE BOT GAME: BY ETHAN LAM 6/24/20
Tankyselected = False
Dandsyselected = False
Mixxyselected = False
# orig1 = 125.0
# orig2 = 80.0
# orig3 = 100.0
# centerprint("message".center())
# s = "hiad"
# s.center(40)

def centerprint(string):
    print(string.center(120))
def centerinput(string):
    inputt = input(string.center(120))
    return(inputt)

def random_number(max_int):
    rand = random.randint(1, max_int)

    return (rand)
# def add_spaces(num):
#
#
#     my_spaces = ""
#     for x in range(0, num):
#         my_spaces += " "
#     return my_spaces
#
# def centerprint_centered(string):
#
#     length = len(string)
#     spaces_to_add = int((125 - length)/2)
#     centerprint_this = add_spaces(spaces_to_add) + string
#     centerprint(centerprint_this)
#
class battlebot:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.base_armor = 10.0
        self.base_damage = 10.0
        self.speed = 10.0

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def attack(self, opponent):
        robotBaseDamage = self.base_damage
        opponentBaseArmor = opponent.base_armor
        damage_dealt = robotBaseDamage - (opponentBaseArmor / 10)
        opponent.take_damage(damage_dealt)

    def detect_speed(self, opponent):
        if self.speed > opponent.speed:
            gofirst = True
        elif self.speed < opponent.speed:
            gofirst = False
        else:
            gofirst = False #gofirst = random.randint(0, 1)
        return gofirst
    # def is_alive(self):
    #         if(self.health) <= 0:
    #             return False
    #         else:
    #             return True

class Tanky(battlebot):
    def __init__(self, name):
        self.name = name
        self.orighealth = 125.0
        self.health = 125.0
        self.base_armor = 50.0
        self.base_damage = 20.0
        self.base_orig_damage = 20.0
        self.base_special_damage = 35.0
        self.speed = 1
        self.basicmove = "Fat Punch"
        self.specialmove = "Heavy Slam"
        self.description = "I am a slow-moving destroyer! I may not do the most damage but I can withstand anything!"

    def get_stats(self):
        centerprint(self.name)
        centerprint("Health: " + str(self.health))
        centerprint("Armor: " + str(self.base_armor))
        centerprint("Basic Attack: " + str(self.base_damage))
        centerprint("Special Attack: " + str(self.base_special_damage))
        centerprint("Speed: " + str(self.speed))
        centerprint("Description: " + str(self.description))


class DandSy(battlebot):
    def __init__(self, name):
        self.name = name
        self.orighealth = 80.0
        self.health = 80.0
        self.base_armor = 5.0
        self.base_damage = 25.0
        self.base_orig_damage = 22.5
        self.base_special_damage = 42.5
        self.speed = 3
        self.basicmove = "Quick Slash"
        self.specialmove = "Slice Attack"
        self.description = "I am a speedy attacker! I will output high amounts of damage but I may be a little fragile!"

    def get_stats(self):
        centerprint(self.name)
        centerprint("Health: " + str(self.health))
        centerprint("Armor: " + str(self.base_armor))
        centerprint("Basic Attack: " + str(self.base_damage))
        centerprint("Special Attack: " + str(self.base_special_damage))
        centerprint("Speed: " + str(self.speed))
        centerprint("Description: " + str(self.description))


class Mixxy(battlebot):
    def __init__(self, name):
        self.name = name
        self.orighealth = 100.0
        self.health = 100.0
        self.base_armor = 10.0
        x = random.randint(1,5) + 20.0
        y = random.randint(1,5) + 35.0

        self.base_damage = x
        self.base_orig_damage = x
        self.base_special_damage = y
        self.speed = 2
        self.basicmove = "Cross Chop"
        self.specialmove = "Focus Blast"
        self.description = "I am a balanced monster! I'm so good that a randomizer was put into my brain my attacks!"

    def get_stats(self):
        centerprint(self.name)
        centerprint("Health: " + str(self.health))
        centerprint("Armor: " + str(self.base_armor))
        centerprint("Basic Attack: " + str(self.base_damage))
        centerprint("Special Attack: " + str(self.base_special_damage))
        centerprint("Speed: " + str(self.speed))
        centerprint("Description: " + str(self.description))
    # def randomizer(self):

# centerprint("sdrpf)t(")
# print(centerinput("are yuu dumb"))


Bot2 = DandSy("DandSy")
botuno = battlebot("Botthebot")
Bot3 = Mixxy("Mixxy")
Bot1 = Tanky("Tanky")

Bot5 = DandSy("DandSy")
Bot6 = Mixxy("Mixxy")
Bot4 = Tanky("Tanky")
# centerprint(Tanky.get_stats(Bot3))
abot = Bot1
personbot = Bot1
screen = 0
correct = True
next = False
selected = False
choosebot = random_number(3)
personturn = False
second = "N"
first = "N"
while correct and next == False:
    centerprint("----------******----------******  Battle Bots  ******----------******----------")
    # centerprint("It is the year 2106, and Artificial Intelligence rules the world")
    # centerprint("In the hot musty attic of your house, you find an old gaming console")
    # centerprint("You decide to check it out")
    # centerprint("In the game, You are given the opportunity to work with one of the 3 bots against a bot controlled by Artificial Intelligence (AI)")
    # centerprint("If you beat the opposing AI bot, you would be wired some money, which your family could really use")
    # centerprint("This is the game. Good Luck")
    centerprint("You can choose between three different bots to face off against the AI")
    first = centerinput("Type R for rules, Type C to see the 3 classes of bots, Type T for tips, or Type B to battle the bots against the AI\n")
    if (str(first) == "R" or str(first) == "r"):
        centerprint("Rules:")
        centerprint("Choose one of three bots to battle with!")
        centerprint("To see the classes of the bots, go back to the menu and type C")
        centerprint("In battle, Type A to use the basic attack or Type S to use the special attack")
        centerprint("The basic attack is guaranteed to hit every time, but the special has a 50% chance of missing!")
        centerinput("Type any key to go back to the menu\n")
    elif (screen == 0 and str(first) == "C") or (screen == 0 and str(first) == "c"):
        Bot1.get_stats()
        centerprint("\n")
        Bot2.get_stats()
        centerprint("\n")
        Bot3.get_stats()
        centerprint("\n")
        centerinput("Type any key to go back to the menu\n")
    elif (screen == 0 and str(first) == "T") or (screen == 0 and str(first) == "t"):
        centerprint("Use Speed to your advantage! Faster bots like the Dandsy will be able to go first!")
        centerprint("The Mixxy will have randomized damage! Its basic attack and special attack damage will be different each time you play!")
        centerprint("Remember to keep checking your health to make sure your bot doesn't die!")
        centerprint("The AI can use all 3 bots as well!\n")
        centerinput("Type any key to go back to the menu\n")

    elif screen == 0 and str(first) == "B" or str(first) == "b":
        centerprint("Entering the Battling Area: (I hope you read the rules!")
        centerprint("Choose your bot!")
        second = centerinput("Type 1 for Tanky, Type 2 for Dandsy, and Type 3 for Mixxy\n")
        next = True
if correct and next == True:
    if screen == 0 and str(second) == "1":
        Tankyselected = True
        centerprint("Tanky selected!")
        centerprint(
            "-----------------------------------------------------------------------------------------------------------------")
        selected = True
    elif screen == 0 and str(second) == "2":
        centerprint("Dandsy selected!")
        centerprint(
            "-----------------------------------------------------------------------------------------------------------------")
        selected = True
        Dandsyselected = True
    elif screen == 0 and str(second) == "3":
        centerprint("Mixxy selected!")
        centerprint("-----------------------------------------------------------------------------------------------------------------")
        selected = True
        Mixxyselected = True

if(Mixxyselected == True):
    personbot = Bot3
if(Dandsyselected == True):
    personbot = Bot2
if (Tankyselected == True):
    personbot = Bot1

if(choosebot == 1):
    abot = Bot4
elif(choosebot == 2):
    abot = Bot5
elif(choosebot == 3):
    abot = Bot6
# if(personbot.speed >= abot.speed) or (personbot.speed == abot.speed):
#         personturn = True
# if(abot.speed >= personbot.speed):
#         abotturn = True
centerprint("Battle!")
centerprint("Your " + str(personbot.name) + " (" + str(personbot.health) + "/" + str(personbot.orighealth) + ") squares off against the AI's " + str(abot.name) +  " (" + str(abot.health) + "/" + str(abot.orighealth) + ") !\n")
while correct and next == True and selected == True:
    amrand = random_number(2)
    amsprand = random_number(2)
    if(personbot.detect_speed(abot) == True):
        third = centerinput("Type A to use the basic move and Type S to use the special move\n")
        if(str(third) == "A" or str(third) == "a"):
            personbot.base_damage = personbot.base_orig_damage
            personbot.attack(abot)
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.basicmove))
            centerprint("Opponent health:  " + str(abot.health) + "/" + str(abot.orighealth) + "\n")
        elif (str(third) == "S" and amsprand == 1) or (str(third) == "s" and amsprand == 1):
            personbot.base_damage = personbot.base_special_damage
            personbot.attack(abot)
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.specialmove))
            centerprint("Opponent health:  " + str(abot.health) + "/" + str(abot.orighealth) + "\n")
        elif (str(third) == "S" and amsprand == 2) or (str(third) == "s" and amsprand == 2):
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.specialmove))
            centerprint("but it missed! \n")
        if (abot.health <= 0):
            centerprint("You destroyed the AI bot!")
            centerprint("Congratulations on destroying the AI! Please click the green arrow on the top left of the run console under the run button to battle again.\n\n")
            centerprint("-----------------------------------------------------------------------------------------------------------------")
            correct = False
            break
        if (amrand == 1):
            abot.base_damage = abot.base_orig_damage
            abot.attack(personbot)
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.basicmove))
            centerprint("Your health:  " + str(personbot.health) + "/" + str(personbot.orighealth) + "\n")
        elif (amrand == 2 and amsprand == 2):
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.specialmove))
            centerprint("but it missed! \n")
        elif (amrand == 2 and amsprand == 1):
            abot.base_damage = abot.base_special_damage
            abot.attack(personbot)
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.specialmove))
            centerprint("Your health:  " + str(personbot.health) + "/" + str(personbot.orighealth) + "\n")
        if (personbot.health <= 0):
            centerprint("Your bot was destroyed.")
            centerprint("Thank you for giving the AI some more experience. Please click the green arrow on the top left of the run console under the run button to battle again.\n\n")
            centerprint("-----------------------------------------------------------------------------------------------------------------")
            correct = False


    elif(personbot.detect_speed(abot) == False):
        if (amrand == 1):
            abot.base_damage = abot.base_orig_damage
            abot.attack(personbot)
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.basicmove))
            centerprint("Your health:  " + str(personbot.health) + "/" + str(personbot.orighealth) + "\n")
        elif (amrand == 2 and amsprand == 2):
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.specialmove))
            centerprint("but it missed! \n")
        elif (amrand == 2 and amsprand == 1):
            abot.base_damage = abot.base_special_damage
            abot.attack(personbot)
            centerprint("The AI's " + str(abot.name) + " used " + str(abot.specialmove))
            centerprint("Your health:  " + str(personbot.health) + "/" + str(personbot.orighealth) + "\n")
        if (personbot.health <= 0):
            centerprint("Your bot was destroyed.")
            centerprint("Thank you for giving the AI some more experience. Please click the green arrow on the top left of the run console under the run button to battle again.\n")
            centerprint("-----------------------------------------------------------------------------------------------------------------")
            correct = False
            break
        third = centerinput("Type A to use the basic move and Type S to use the special move\n")
        if (str(third) == "A" or str(third) == "a"):
            personbot.base_damage = personbot.base_orig_damage
            personbot.attack(abot)
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.basicmove))
            centerprint("Opponent health:  " + str(abot.health) + "/" + str(abot.orighealth) + "\n")
        elif (str(third) == "S" and amsprand == 1) or (str(third) == "s" and amsprand == 1):
            personbot.base_damage = personbot.base_special_damage
            personbot.attack(abot)
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.specialmove))
            centerprint("Opponent health:  " + str(abot.health) + "/" + str(abot.orighealth) + "\n")
        elif (str(third) == "S" and amsprand == 2) or (str(third) == "s" and amsprand == 2):
            centerprint("Your " + str(personbot.name) + " used " + str(personbot.specialmove))
            centerprint("but it missed! \n")
        if (abot.health <= 0):
            centerprint("You destroyed the AI bot!")
            centerprint("Congratulations on destroying the AI! Please click the green arrow on the top left of the run console under the run button to battle again.\n")
            centerprint("-----------------------------------------------------------------------------------------------------------------")
            correct = False
            time.sleep(0.5)

    # if(personbot.speed > abot.speed):
    #    centerprint(abot.name + "used" abot.move )

# arand = random.randint(1,3)
# abot.move = random.randint(1,2)
#     if abot.move == 1:
#         abot.bas
# if arand == 1:
#     bot = Bot1("Tanky")


# centerprint(Bot3.name)
# Bot1.attack(Bot3)
# centerprint(Bot2.base_damage)
# attack(Bot3)

# bot = Bot3("Tanky")

