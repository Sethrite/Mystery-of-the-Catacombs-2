from RADeath import death
from time import sleep
import sys

######################################################################
#                                                                    #
#       Title: Mystery of the Catacombs                              #
#       By Mark Masenda and Zachary Palacios                         #
#                                                                    #
######################################################################

# the blueprint for a room
class Room:
# the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits: list = value
        
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations: list = value
        
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items: list = value
        
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions: list = value
        
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables: list = value
    
    
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
    # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
        
        
    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    def addItem(self, item, desc = " "):
    # append the item and exit to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
        
        
    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item, desc = " "):
    # append the item to the list
        self._grabbables.append(item)
        
        
    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
    # remove the item from the list
        self._grabbables.remove(item)
    
    global border
        
    # returns a string description of the room
    def __str__(self):
    # first, the room name
        s = f"You are in {self.name}\n"
        # next, the items in the room
        s += "\nYou see: \n"

        for item in self.items:
            s += "\t"+ item + "\n"

        # next, the exits from the room
        s += "\n\nExits: \n"
        for exit in self.exits:
            s += "\t" + exit + " "
        s += "\n"
        return s


######################################################################
# creates the rooms
def createRooms():
    # r1 through r13 are the 13 rooms in the catacomb
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r13)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7
    global r8
    global r9
    global r10
    global r11
    global r12
    global r13

    # create the rooms and give them meaningful names
    r1 = Room("The Start")
    r2 = Room("The Crematorium")
    r3 = Room("The Library")
    r4 = Room("The Brewing Room")
    r5 = Room("The Prince's Tomb")
    r6 = Room("The Empty Guard Room")
    r7 = Room("The Food Storage")
    r8 = Room("The Treasure Room")
    r9 = Room("The King's Tomb")
    r10 = Room("The Guard Room")
    r11 = Room("The Equipment Room")
    r12 = Room("The Gate")
    r13 = Room("Outside")
    
    # add exits to room 1
    r1.addExit("East", r2) # -> to the east of room 1 is room 2
    r1.addExit("South", r3)# -> to the east of room 1 is room 3
    # add grabbables to room 1
    # add items to room 1
    r1.addItem("Chair", "The chair is made of mahogany and a ghost is sitting on it.")
    """r1.addItem("death (temporary, to test death effect)", " ")"""
    r1.addItem("Table", "The table is made of very brittle birch. A key rests on it. You pick it up.\n\n\t\t\tA key was added to your inventory.")
    
    
    # add exits to room 2
    r2.addExit("West", r1)# -> to the west of room 2 is room 1
    r2.addExit("South", r4)# -> to the south of room 2 is room 4
    # add items to room 2
    r2.addItem("Rug", "It is an egyptian rug, you see it slightly hovering above the ground. Under it you discover a stair way leading north!")
    r2.addItem("Fireplace", "You pull the lever next to the fireplace. A doorway appears to the east!")
    
    
    # add exits to room 3
    r3.addExit("North", r1)# -> to the north of room 3 is room 1
    r3.addExit("West", r10)# -> to the west of room 3 is room 10
    r3.addExit("South", r11)# -> to the north of room 3 is room 11
    # add grabbables to room 3
    r3.addGrabbable("statue")
    # add items to room 3
    r3.addItem("Spell Book", "You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb.")
    r3.addItem("Statue", "The statue depicts a woman in a long dress, with angel wings. It is covering its face.")
    r3.addItem("Desk", "The desk is dusty and withered. The statue and spell book are resting on it.")
    
    
    # add exits to room 4
    r4.addExit("North", r2)# -> to the north of room 4 is room 2
    r4.addExit("South", r12)# -> to the south of room 4 is room 12
    # add grabbables to room 4
    r4.addGrabbable("flask")
    # add items to room 4
    r4.addItem("Stone Table", "Yep, that is a indeed a stone table. The brewing stand and flask are resting on it.")
    r4.addItem("Brewing Stand", "You see the brewing stand on top of the stone table. It looks like it could prove useful.")
    r4.addItem("Flask", "The glass flask is on the stone table, filled with water. It is in mint condition.")

    # add exits to room 5
    r5.addExit("North", r6) # -> to the north of room 5 is room 6
    # add grabbables to room 5
    # No grabbables
    # add items to room 5
    r5.addItem("Casket","You see a diamond ring next to the wrapped body. You found an artifact!\n\n\t\t\tA diamond ring was added to your inventory.")
    r5.addItem("Painting","The artwork depicts a long lost land, with the an ancient scroll positioned at the center.")
    r5.addItem("Cobwebs","")
    
    # add exits to room 6
    r6.addExit("West", r2) # -> to the west of room 6 is room 2
    # add grabbables to room 6
    r6.addGrabbable("coin")
    # add items to room 6
    r6.addItem("Armor","You see armor lying on the floor and there are remanents of human ash on it.")
    r6.addItem("Pressure Plate","")
    r6.addItem("Coin","The coin has the face of the dead king and is worth a wooping $5.")
    r6.addItem("Door", "You try to open the door, but you need a code. The door leads to the prince's room.")
    # add exits to room 7
    r7.addExit("South", r2) # -> to the south of room 7 is room 2
    # add grabbables to room 7
    r7.addGrabbable("Serapias Herb")
    r7.addGrabbable("Rat")
    # add items to room 7
    r7.addItem("Rat", "In the corner you see the carcas of a rat from long ago and for some reason it did not decompose.")
    r7.addItem("Serapias Herb", "You find it inside a wooden barrel. The plant's smell makes you drowsy.")
    r7.addItem("Cabinet", "You move the cabinet and discover a secret door to the west. You notice it has a keyhole.")
    
    # add exits to room 8
    r8.addExit("East", r7) # -> to the east of room 8 is room 7
    # add grabbables to room 8
    r8.addGrabbable("gems")
    r8.addGrabbable("gold")
    r8.addGrabbable("jewelry")
    r8.addGrabbable("priceless_painting")
    # add items to room 8
    r8.addItem("Gold", "You see a stack of gold on the floor, it looks very appealing.\n\nYou hear a voice say 'You should take some.'")
    r8.addItem("Jewelry", "You see a stack of jewelry on the floor, it looks really appealing.\n\nYou hear a voice say 'You should take some'.")
    r8.addItem("Gems", "The gems glisten on the floor of the room, it looks extremely appealing.\n\nYou hear a voice say 'You should take some.'")
    r8.addItem("Priceless Painting", "The painting displays a starry night above a dark blue city, the painting would look perfect on your wall.\n\nYou hear a voice say 'You should take it.'")
    r8.addItem("Ruby Goblet", "You see a golden goblet with a ruby gem ingrained upon it. You found an artifact!\n\n\t\t\tA ruby goblet was added to your inventory.")
    
    # add exits to room 9
    r9.addExit("South", r10) # -> to the south of room 9 is room 10
    # add grabbables to room 9
    # No grabbable
    # add items to room 9
    r9.addItem("Casket", "You see a the king's crown next to the mummified body. You found an artifact!\n\n\t\t\tThe king's crown was added to your inventory.")
    r9.addItem("Crack", "")
    r9.addItem("Scroll", "You pick up the scroll and it has some ancient language written on it. You do not understand what it says.")
    
    # add exits to room 10
    r10.addExit("North", r9) # -> to the north of room 10 is room 9
    r10.addExit("East", r3)# -> to the east of room 10 is room 3
    # add grabbables to room 10
    # No grabbable
    # add items to room 10
    r10.addItem("Guard", "You see the eteranl guard. His title 'Blood-Red Commander Igris'. \n\nHe stares at you menacingly and yells 'LEAVE AT ONCE OR ELSE!'")
    
    # add exits to room 11
    r11.addExit("North", r3) # -> to the north of room 11 is room 3
    # add grabbables to room 11
    r11.addGrabbable("code")
    # add items to room 11
    r11.addItem("Shovel", "You see a code for a door attached to the shovel's head.\n\n\t\t\tA code was added to your inventory.")
    r11.addItem("Pickaxe", "The pickaxe is missing its shaft. It is unusable.")
    r11.addItem("Sword", "The sword is rusted and shattered. It is unsuitable for combat")
    r11.addItem("Shield", "The shield is burnt and split in half. It is out of commission.")
    
    # add exits to room 12
    r12.addExit("North", r4) # -> to the north of room 12 is room 4
    #r12.addExit("south", r12)# -> to the south of room 12 is room 4
    # add grabbables to room 12
    # No grabbables
    # add items to room 12
    r12.addItem("Locked Gate", "In the door you see three spaces for three objects. The spaces for the artifacts seem relatively small.")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
    
Admin = "OFF"  
    
######################################################################
# START THE GAME!!!

Duplicate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def STARTGAME():
    createRooms() # add the rooms to the game
    global currentRoom
    global Duplicate
    Duplicate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    currentRoom = r1
    attempt = 0
    Artifact = 0
    guardStatus = "awake"
    inventory = [] # nothing in inventory...yet
    previousRoom = "The Start"

    while (True):

        # play forever (well, at least until the player dies or asks to quit)

        # set the status so the player has situational awareness
        # the status has room and inventory information

        status = f"{middle} {currentRoom}\n\nYou are carrying: {inventory}\n"
 
        # display the status

        print(f"\n{border}\n{border}")
        for stats in status:
            sleep(0.005)
            sys.stdout.write(stats)
            sys.stdout.flush()


        if (Duplicate[21] > 0):
            if (previous == currentRoom.name):
                print(f"\n{middle} You are {prevExit} of {previousRoom}")
            else:
                print(f"\n{middle} You are {prevExit} of {previous}")
                previousRoom = previous
                previous = currentRoom.name

        if (Duplicate[22] < 1):
            if (currentRoom.name == "The Crematorium" or currentRoom.name == "The Library"):
                print(f"\n{middle} You are {prevExit} of {previousRoom}")
                previous = currentRoom.name
                Duplicate[21] += 1
                Duplicate[22] += 1
        print(f"{border}\n{border}")
        
    
            

        Duplicate[23] = 0
        # prompt for player input
        # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, and take
        # valid nouns depend on the verb

        Question = "\nWhat would you like to do? ('look', 'take', or 'go')\n\n> "

        for desc in Question:
            sleep(0.005)
            sys.stdout.write(desc)
            sys.stdout.flush()

        action = input()
        # set the user's input to lowercase to make it easier to compare
        # the verb and noun to known values
        action = action.lower()
        
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)

        Quit = {
            "quit": "quit",
            "leave": "quit",
            "bye": "bye",
            "exit": "exit"
        }

        if (Quit.get(action)):
            exit()
        # set a default response
        response = "\t\t\t\t\tERROR\n\nYou have provided either an invalid location or item. Valid verbs are go, look, and take"
        # split the user input into words (words are separated by spaces)
        words = action.split()
        # the game only understands two word inputs

        command = {         # Dictionary for all commands
            "go": "go",
            "look": "look",
            "looked": "look",
            "take": "take",
            "took": "take",
            "get": "take",
            "got": "take"
        }
        
        items = {           # Dictionary for all key words that will cause actions
            "r1": "r1",
            "r2": "r2",
            "r3": "r3",
            "r4": "r4",
            "r5": "r5",
            "r6": "r6",
            "r7": "r7", 
            "r8": "r8",
            "r9": "r9",
            "r10": "r10",
            "r11": "r11",
            "r12": "r12",
            "r13": "r13",
            "east": "east",
            "west": "west",
            "north": "north",
            "south": "south",
            "chair": "chair",
            "table": "table",
            "key": "key",
            "rug": "rug",
            "fireplace": "fireplace",
            "fire": "fireplace",
            "fire place": "fireplace",
            "spellbook": "spell",
            "spell": "spell",
            "spell book": "spell",
            "book": "spell",
            "statue": "statue",
            "desk": "desk",
            "stone table": "stone_table",
            "stone": "stone_table",
            "stonetable": "stone_table",
            "brewing stand": "brewing_stand",
            "brewing": "brewing_stand",
            "flask": "flask",
            "water flask": "flask",
            "water": "flask",
            "waterflask": "flask",
            "casket": "casket",
            "painting": "painting",
            "cobwebs": "cobwebs",
            "cobweb": "cobwebs",
            "armor": "armor",
            "pressure": "pressure_plate",
            "pressure plate": "pressure_plate",
            "coin": "coin",
            "door": "door",
            "rat": "rat",
            "serapias": "serapias",
            "serapias herb": "serapias",
            "herb": "serapias",
            "serapiasherb": "serapias",
            "cabinet": "cabinet",
            "gold": "gold",
            "jewelry": "jewelry",
            "gems": "gems",
            "gem": "gems",
            "priceless": "priceless_painting",
            "priceless painting": "priceless_painting",
            "painting": "priceless_painting",
            "pricelesspainting": "priceless_painting",
            "ruby goblet": "ruby_goblet",
            "ruby": "ruby_goblet",
            "goblet": "ruby_goblet",
            "crack": "crack",
            "scroll": "scroll",
            "guard": "guard",
            "code": "code",
            "shovel": "shovel",
            "pickaxe": "pickaxe",
            "sword": "sword",
            "shield": "shield",
            "locked gate": "locked_gate",
            "locked": "locked_gate",
            "lock": "locked_gate",
            "gate": "locked_gate",
            "diamond": "diamond",
            "king": "king",
            "scroll": "scroll",
        }

        # isolate the verb and noun
        verb = " "
        noun = " "

        for i in words:
            if command.get(i):
                verb = i
                break
        
        if verb == " ":
            Duplicate[23] += 1      # Will skip all actions and give error message directly about not finding correct verb

        for j in words:
            if items.get(j):
                noun = j
                break

        if noun == " ":
            Duplicate[23] += 1      # Will skip all actions and give error message directly about not finding correct noun

        # the verb is: go

        match verb:
            case "go":
                # set a default response
                response = "Invalid exit."
                # check for valid exits in the current room
                for i in range(len(currentRoom.exits)):
                    # a valid exit is found
                    noun = noun.title()
                    if (noun == currentRoom.exits[i]):
                        # change the current room to the one that is
                        # associated with the specified exit
                        currentRoom = currentRoom.exitLocations[i]
                        prevExit = noun
                        # set the response (success)
                        response = "Room Changed."
                        # no need to check any more exits
                        break
                
        # the verb is: look
            case "look":
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                for i in range(len(currentRoom.items)):
                    noun = noun.title()
                    if (noun == currentRoom.items[i]):
                        # set the response to the item's description
                        response = currentRoom.itemDescriptions[i]
                        # no need to check any more items
                        break
            # the verb is: take
            case "take":
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current room
                for grabbable in currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's
                        # inventory
                        inventory.append(grabbable)
                        # remove the grabbable item from the room
                        currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = f"Item grabbed. {grabbable} was added to your inventory"
                        # no need to check any more grabbable items
                        break


                                    # Special Interactions:


        
        
            #  *** ADD LOOK SLEEPING POTION FUNCTIONALITY ***

        noun = noun.lower() 

        match verb, noun:

            case "look", "guard":       # Eternal Guard interaction
                if (Duplicate[12] < 1):
                    for x in inventory:
                        if (x == "Sleeping Potion"):
                            response = "You used the sleeping potion on the guard. The guard's armor immediately falls to the ground. The king's Tomb is now available north!\n"
                            inventory.remove("sleeping_potion")
                            guardStatus = "asleep"
                            Duplicate[12] += 1             
                else:
                    response = "You see the pile of armor on the floor, lifeless and cold. North leads to the king's Tomb"


            case "look", "rug":     # Rug Interaction
                if (currentRoom.name == "The Crematorium"):
                    if (Duplicate[0] < 1):
                        r2.addExit("North", r7)# -> to the west of room 2 is room 7
                        Duplicate[0] += 1
                    else:
                        response = "The egyptian rug stopped floating. It lost its power after you touched it."


            case "look", "fireplace" | "fire":       # Fireplace Interaction
                    if (currentRoom.name == "The Crematorium"):
                        if (Duplicate[1] < 1):      
                            r2.addExit("East", r6)# -> to the east of room 2 is room 6
                            Duplicate[1] += 1
                        else:
                            response = "The fireplace is cold and empty. All that remains are ash and dust."

            case "look", "spell":
                if (Duplicate[2] < 1):
                    inventory.append("Spell Book")
                    response = "You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb\n\n\t\t\tA Spell Book was added to your inventory."
                    currentRoom.items.remove("Spell Book")
                    currentRoom.itemDescriptions.remove("You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb.")
                    Duplicate[2] += 1
                else:
                    response = "You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb"

            case "take", "spell" | "book":
                if (Duplicate[29] < 1):
                    if (Duplicate[2] < 1):
                        inventory.append("Spell Book")
                        response = "You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb\n\n\t\t\tA Spell Book was added to your inventory."
                        currentRoom.items.remove("Spell Book")
                        currentRoom.itemDescriptions.remove("You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are:\n\t\t\tA Rat Heart, Water-Filled Flask, and a Serapias Herb.")
                        Duplicate[2] += 1
                        Duplicate[29] += 1
    
                    
                

            case "look", "desk":        # Desk Interaction after Spell Book is taken
                if (currentRoom.name == "The Library"):
                    if (Duplicate[2] > 0):      # Checks if the spell book is taken
                        response = "The desk is dusty and withered. The statue is resting on it."


            case "look", "brewing" | "stand":
                for y in inventory:
                    if (y == "Spell Book"):
                        item = 0
                        for x in inventory:
                            if (x == "Rat"):
                                item += 1
                            if (x == "Serapias Herb"):
                                item += 1
                            if (x == "Flask"):
                                item += 1
                        if (item == 3):
                                response = "You have made a sleeping potion! A Sleeping Potion was added to your inventory."
                                inventory.append("Sleeping Potion")
                                inventory.remove("Rat")
                                inventory.remove("Serapias Herb")
                                inventory.remove("flask")
                                inventory.remove("Spell Book")
                                Duplicate[30] += 1
                        else:
                            response = f"You have {item}/3 ingredients required to make the sleeping potion."

            case "look", "Sleeping" | "Potion":
                if (Duplicate[30] > 0):
                    response = "The Sleeping Potion shines with a mysterious purple shade, it seems strong enough to put a hundered men to sleep"



            case "look", "table":       # Table ---> Key Interaction

                if (Duplicate[3] < 1):  # Prevents the player from duplicating the items after already looking at the table
                    inventory.append("Key")
                    Duplicate[3] += 1
                else:
                    response = "The table is made of very brittle birch."


            case "look", "Key":         # Key inventory statement

                if (Duplicate[3] > 0):
                    response = "The golden key is wierdly shaped. It glistens in your hand."
                

            case "look", "shovel":      # Shovel Interaction

                if (Duplicate[11] < 1):
                    inventory.append("code")
                    Duplicate[11] += 1
                else:
                    response = "The shovel is cracked. It is useless."
                

            case "look", "cabinet":     # Cabinet ---> Door Interaction
                if (Duplicate[4] < 1):
                    r7.addItem("Door", "The door is very old and rusted. Through the keyhole you see something glistening.")
                    Duplicate[4] += 1
                else:
                    response = "The wooden cabinet is empty. You are disappointed."

            
            

            case "look", "door":        # Food Storage door interaction

                if (currentRoom.name == "The Food Storage"):       # Checks if the player is in the Food Storage
                    if (Duplicate[10] < 1):     # Prevents the player from reciving same response after using the key
                        for z in inventory:
                            if (z == "Key"):
                                r7.addExit("West", r8) # -> to the west of room 7 is room 8
                                inventory.remove("Key")
                                response = "You use the key on the door and reveal a room to the west!"
                                Duplicate[10] += 1
                    else:
                        response = "The door is very old and rusted."
            
            case "look", "casket":      # Casket Interaction --> Prince

                if (currentRoom.name == "The Prince's Tomb"):      # Checks if the player is in the Prince's Tomb
                    if (Duplicate[7] < 1):      # Prevents the player from duplicating the diamond ring
                        inventory.append("Diamond Ring")
                        Duplicate[7] += 1
                        Artifact += 1
                    else:
                        response = "All that is left is the prince's mummified body"


                else:       # Casket Interaction --> King

                    if (currentRoom.name == "The King's Tomb"):        # Checks if the player is in the King's Tomb
                        if (Duplicate[8] < 1):      # Prevents the player from duplicating the King's Crown
                            inventory.append("King Crown")
                            Duplicate[8] += 1
                            Artifact += 1
                        else:
                            response = "All that is left is the king's mummified body"


                            # Equipment Room Interactions: Take functions


            case "take", "sword":

                if (currentRoom.name == "The Equipment Room"):
                    response = "The sword is rusted and shattered. It is unsuitable for combat"
            

            case "take", "shield":
                
                if (currentRoom.name == "The Equipment Room"):
                    response = "The shield is burnt and split in half. It is out of commission."
                

            case "take", "pickaxe":

                if (currentRoom.name == "The Equipment Room"):
                    response = "The pickaxe is missing its shaft. It is unusable."
            

            case "take", "pickaxe":

                if (currentRoom.name == "The Equipment Room"):
                    response = "The pickaxe is missing its shaft. It is unusable."


            case "take", "shovel":

                if (currentRoom.name == "The Equipment Room"):
                    if (Duplicate[11] < 1):
                        response = "The shaft is missing. Unfortunately it is not usable. However, you notice something on its head."
                    else:
                        response = "The shovel is cracked. It is useless."


                            # Treasure Room Interactions: Look functions

            case "look", "gold":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[24] > 0):
                        response = "After taking the gold you feel a little guilty. But, it still looks very appealing."
            

            case "look", "jewelry":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[25] > 0):
                        response = "After taking the jewelry you feel a little guilty. But, it still looks really appealing."
            

            case "look", "gems":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[26] > 0):
                        response = "After taking the gems you feel a little guilty. But, it still looks extremely appealing."


            case "look", "priceless" | "painting":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[27] > 0):
                        response = "After taking the priceless_painting you feel a little guilty. But, it still would look perfect on your wall."


                            # Treasure Room Interactions: Take functions


            case "take", "gold":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[24] < 1):
                        currentRoom.items.remove("gold")
                        currentRoom.itemDescriptions.remove("You see a stack of gold on the floor, it looks very appealing.\n\nYou hear a voice say 'You should take some.'")
                        Duplicate[24] += 1
            

            case "take", "jewelry":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[25] < 1):
                        currentRoom.items.remove("jewelry")
                        currentRoom.itemDescriptions.remove("You see a stack of jewelry on the floor, it looks really appealing.\n\nYou hear a voice say 'You should take some'.")
                        Duplicate[25] += 1


            case "take", "gems":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[26] < 1):
                        currentRoom.items.remove("gems")
                        currentRoom.itemDescriptions.remove("The gems glisten on the floor of the room, it looks extremely appealing.\n\nYou hear a voice say 'You should take some.'")
                        Duplicate[26] += 1


            case "take", "priceless" | "painting":

                if (currentRoom.name == "The Treasure Room"):
                    if (Duplicate[27] < 1):
                        currentRoom.items.remove("Priceless Painting")
                        currentRoom.itemDescriptions.remove("The painting displays a starry night above a dark blue city, the painting would look perfect on your wall.\n\nYou hear a voice say 'You should take it.'")
                        Duplicate[27] += 1
                        
                            # Artifact Interactions

            case "look", "ruby" | "goblet":     # Ruby Goblet Interaction
                if (Duplicate[17] < 1):
                    inventory.append("Ruby Goblet")
                    currentRoom.items.remove("Ruby Goblet")
                    currentRoom.itemDescriptions.remove("You see a golden goblet with a ruby gem ingrained upon it. You found an artifact!\n\nA ruby goblet was added to your inventory.")
                    Duplicate[17] += 1
                    Artifact += 1
                else:
                    response = f"You hold the golden goblet ingrained with a ruby proudly. You have {Artifact}/3 of the artifacts."

            case "look", "diamond" | "ring":        # Diamond Ring Interaction
                if (Duplicate[7] > 0):
                    response = f"You proudly place the diamond ring on your finger. You have {Artifact}/3 of the artifacts."

            case "look", "king" | "crown":      # King Crown Interaction
                if (Duplicate[8] > 0):
                    response = f"You wear the king's crown on your head with pride. You have {Artifact}/3 of the artifacts."

                    



                                                # Continue the rest of the match case statments BELOW


            case "take", "flask":       # Flask Interaction

                if (currentRoom.name == "The Brewing Room"):
                    if (Duplicate[13] < 1):
                        currentRoom.items.remove("flask")
                        currentRoom.itemDescriptions.remove("The glass flask is on the stone table, filled with water. It is in mint condition.")
                        Duplicate[13] += 1


            case "look", "flask":

                if (currentRoom.name == "The Brewing Room"):
                    if (Duplicate[13] > 0):
                        response = "The flask is made out of glass and filled with water."
                

            case "look", "stone" | "table":

                if (currentRoom.name == "The Brewing Room"):
                    if (Duplicate[13] > 0):
                        response = "Yep, that is a indeed a stone table. The brewing stand is resting on it."


            case "take", "rat":     # Rat Interaction

                if (Duplicate[14] < 1):
                    currentRoom.items.remove("Rat")
                    currentRoom.itemDescriptions.remove("In the corner you see the carcas of a rat from long ago and for some reason it did not decompose.")
                    Duplicate[14] += 1


            case "look", "rat":

                if (Duplicate[14] > 0):
                    response = "You hold the rats heart, and for some reason it has a faint beat."

            
            case "take", "coin":        # Coin Interaction

                if (Duplicate[5] < 1):
                    currentRoom.items.remove("coin")
                    currentRoom.itemDescriptions.remove("The coin has the face of the dead king and is worth a wooping $5.")
                    Duplicate[5] += 1

            case "look", "coin":

                if (Duplicate[5] > 0):
                    response = "You put the coin in between your teeth and bite it. It's real gold!"

            
            case "take", "serapias" | "herb":       # Herb Interaction
                
                if (Duplicate[15] < 1):
                    currentRoom.items.remove("Serapias Herb")
                    currentRoom.itemDescriptions.remove("You find it inside a wooden barrel. The plant's smell makes you drowsy.")
                    Duplicate[15] += 1


            case "look", "serapias" | "herb":
                if (Duplicate[15] > 0):
                    response = "You hold the serapias herb. You have small signs of nausea and drowsiness."

        # Code-INVENTORY Interaction

            case "look", "code":
                if (Duplicate[11] > 0):
                    response = "The code seems special. It has 5 ancient symbols on it in different colors."

            case "look", "scroll":      # Scroll Interaction
                if (Duplicate[9] < 1):
                    inventory.append("king_scroll")
                    Duplicate[9] += 1
                    currentRoom.items.remove("scroll")
                else:
                    response == "It has some ancient language written on it. You do not understand what it says."

            case "look", "king" | "scroll":
                if (Duplicate[9] > 0):
                    response = f"It has an ancient language written on it. The symbols on the scroll remind you of something."
 

                                        # Gate Interaction: (All 3 artifacts required to reveal the exit south to win game)

            case "look", "locked" | "gate":
                if (Duplicate[7] > 0 or Duplicate[8] > 0 or Duplicate[17] > 0):
                    if (Duplicate[18] < 1):
                        items = 0
                        for b in inventory:
                            if (b == "King Crown"):
                                items += 1
                            if (b == "Ruby Goblet"):
                                items += 1
                            if (b == "Diamond Ring"):
                                items += 1
                        if (items == 3):
                            r12.addExit("South", r13)
                            response = "You have placed down all the artifacts and the door is now open. Make your escape!"
                            inventory.remove("King Crown")
                            inventory.remove("Diamond Ring")
                            inventory.remove("Ruby Goblet")
                            Duplicate[18] += 1
                        else:
                            response = f"In the door you see three spaces for three objects. The spaces for the artifacts seem relatively small.\n\nYou have {items}/3 artifacts required to make the offering."
                    else:
                        response = "You placed down all the artifacts and the door is now open. Make your escape!"
            

                                        # Code and Prince Interaction: (Code required for way south from empty guard room to be revealed)

            case "look", "door":
                if (Duplicate[16] < 1):
                    if (currentRoom.name == "The Empty Guard Room"):
                        for a in inventory:
                            if (a == "code"):
                                response = "You use the code on the door and reveal a room to the south!"
                                r6.addExit("South", r5) # -> to the south of room 6 is room 5
                                inventory.remove("code")
                                Duplicate[16] += 1
                else:
                    response = "The door is now open, south leads to the prince's room."



                                        # EXTRA IDEAS FOR CONTENT, MAYBE AFTER END OF GAME


            # Make a contine game option (potentially)

            # Secret Death Interaction: (If player gets all 5 different deaths in the game)

            # Secret Ghost Interaction: (If all 3 items are collected and the player inspects the chair again the ghost is the king and he talks to the player)

            # Secret Prince's Knight Interaction: (If the player takes the jewelry and the ancient coin and brings it to the sword in the equipment room)

            # Secret Queen Interaction: (If the player collects the king's scroll and priceless painting, and brings it to the old painting in the prince's room)

            # I also want to add a percentage complete of the game, like if the player gets all the easter egss they get 100%. But, if they just beat the game the straight forward route they get 75% complete.




            # if the current room is None, then the player is dead




                                    # All Deaths:

                """
                if (verb == "look" and noun == "death"):
                    print(border)
                    print("\n\n\t\tYou looked death in the face, well what did you expect...\n\n")
                    print(border)
                    sleep(5)
                    currentRoom = None
                """
            
                                    # Eternal Guard Death

            case "go", "north":
                if (currentRoom.name == "The King's Tomb"):
                    if (guardStatus == "awake"):
                        attempt += 1
                        if (attempt > 1):
                            print(border)
                            print("\n\n\t\tYou have disregarded my warnings and now you will pay the consequences.\n\n")
                            print(border)
                            sleep(6)
                            currentRoom = None
                        else:
                            response = "Heed my warning little one, I will protect my king for as long as my spirit remains. Next time you test me, I will extinguish your soul!"
                            prevExit = "west"
                            currentRoom = r10
                    else:
                        response = "Room Changed."
                        currentRoom = r9
                
            
                                    # Pressure Plate Death

            case "look", "pressure" | "plate":
                print(border)
                print("\n\nYou step on the pressure plate and the door closes, while the ceiling begins to decend. All you can do is wait as impending doom approaches.\n\n")
                print(border)
                sleep(6)
                Duplicate[20] += 1
                currentRoom = None  
        
                                    

            case "look", "cobwebs" | "cobweb":      # Cobweb Death
                print(border)
                print("\n\nYou tug on the cobweb and suddenly a giant spider appears. You freeze in terror as the spider crawls toward you.\n\n")
                print(border)
                sleep(6)
                currentRoom = None


            case "look", "crack":       # Crack Death
                print(border)
                print("\n\nYou put your hand through the crack. The wall begins to open up and suddently holes surround you.\n\n\tYou are impaled by poison darts leaving you incompacitated on the floor.\n\n")
                print(border)
                sleep(6)
                currentRoom = None
                

        # Death by Greed


        if (currentRoom == None):
            pass
        else:
            if (currentRoom.name == "The Treasure Room"):
                item = 0
                for treasure in inventory:
                    if (treasure == "gold"):
                        item += 1
                    if (treasure == "jewelry"):
                        item += 1
                    if (treasure == "priceless_painting"):
                        item += 1
                    if (treasure == "gems"):
                        item += 1
                if (item > 3):
                    print(border)
                    print("\n\nYou begin to sink into the floor. You hear a voice, 'There is no greater disaster than greed. Your greediness has become your downfall.'\n\n")
                    print(border)
                    sleep(6)
                    currentRoom = None

        # Death Sequence

        if (currentRoom == None):
            status = "\t\tYou are Dead"

        # Death Message
        if (currentRoom == None):
            print(f"\n{status}\n")
            death()
            print(f"\n{border}\n")
            sleep(2)
            print("\n\n\t\tGame Over\n\n")
            sleep(1)
            print(f"\t{CharName}")
            sleep(1)
            print("\tYou cannot give up just yet...\n\n")
            sleep(2)
            STARTGAME()

        # Admin Controls
        if (Duplicate[23] < 1):
            if (Admin == "ON"):
                if (verb == "go" and noun == "r1"):
                    currentRoom = r1
                    response = "Room Changed."
                if (verb == "go" and noun == "r2"):
                    currentRoom = r2
                    response = "Room Changed."
                if (verb == "go" and noun == "r3"):
                    currentRoom = r3
                    response = "Room Changed."
                if (verb == "go" and noun == "r4"):
                    currentRoom = r4
                    response = "Room Changed."
                if (verb == "go" and noun == "r5"):
                    currentRoom = r5
                    response = "Room Changed."
                if (verb == "go" and noun == "r6"):
                    currentRoom = r6
                    response = "Room Changed."
                if (verb == "go" and noun == "r7"):
                    currentRoom = r7
                    response = "Room Changed."
                if (verb == "go" and noun == "r8"):
                    currentRoom = r8
                    response = "Room Changed."
                if (verb == "go" and noun == "r9"):
                    currentRoom = r9
                    response = "Room Changed."
                if (verb == "go" and noun == "r10"):
                    currentRoom = r10
                    response = "Room Changed."
                if (verb == "go" and noun == "r11"):
                    currentRoom = r11
                    response = "Room Changed."
                if (verb == "go" and noun == "r12"):
                    currentRoom = r12
                    response = "Room Changed."
                if (verb == "go" and noun == "r13"):
                    currentRoom = r13
                    response = "Room Changed."
        
        # WIN GAME MESSAGE
        if (currentRoom.name == "Outside"):
            Duplicate[19] += 1
            return

        # display the response

        print(f"\n\n\n\t\t\t{response}\n\n")
        if (response == "Room Changed."):
            sleep(0.3)
        else:
            print(f"{border}\n")
            input("\t\tPress ENTER to continue: ")


border = "=" * 120
middle = " " * 35
textSpeed = 0.005
TitleScreen = "\n\n\t\tMystery of the Catacombs\n\n\t\t    New Game\n\n\t\t    Exit Game\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Ver 1.2\n"

def MainMenu():
    print(border), print(border)
    for Subtitles in TitleScreen:
        sleep(textSpeed)
        sys.stdout.write(Subtitles)
        sys.stdout.flush()
    print(border), print(border)
    sleep(0.3)
    choice()

def choice():
    Choice = input("Choose an option above: ")

    New = {
        "New Game": "new",
        "new game": "new",
        "new": "new"
    }

    Exit = {
        "Exit Game": "exit",
        "exit game": "exit",
        "Exit": "exit",
        "exit": "exit",
        "quit": "exit",
        "Quit": "exit"
    }
    AdminOptions = {
        "skip": "skip",
        "Skip": "skip"
    }


    if (New.get(Choice) == "new"):
        pass
    elif (Exit.get(Choice) == "exit"):
        return quit()
    elif (AdminOptions.get(Choice) == "skip"):
        global Admin
        Admin = "ON"
        STARTGAME()
    else:
        print("\n\nThe phrase you have provided is not supported. Try again.\n\n")
        choice()

def instruction():
    print(f"\n{border}")
    print("\nThere are 3 commands in the game: 'GO', 'LOOK', and 'TAKE'. \n\n\t\t\t'Go' is used to navigate to different rooms.\n\n\t\t\t'Look' is used to interact with objects in those rooms.\n\n\t\t\t'Take' is used to add items to your inventory.")
    print("\n\n\t\t\t'Look' at items in your inventory to see their descriptions.")
    print("\n\n\nTo quit the game use the keywords 'quit', 'exit', or 'bye'\n")
    print(f"{border}\n")
    input("\t\tPress ENTER to continue: ")

CharName = "Zachary"

MainMenu()

if (Duplicate[19] < 1):
    print(f"\n{border}")
    CharName = input("\nPlease input your character name: ")
    print(f"\n{border}\n")

    Intro = f"\t{CharName}, you wake up on the floor of a long forgotten King's tomb, your only goal is to escape.\n\t  Find the three precious artifacts hidden in the tomb to leave through the 12th room.\n\t\t\t\t\tGood Luck!\n\n"
    for char in Intro:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
        if (char == "!"):
            sleep(0.5)
        if (char == "."):
            sleep(0.5)
    print(f"{border}\n")
    input("\t\tPress ENTER to continue: ")

    instruction()

    STARTGAME()


End = f"\n\nYou have escaped the catacomb and reached the outside world. \n\n\t\t{CharName}, Well Done!\n\n"

print(border)
for chara in End:
    sleep(0.04)
    sys.stdout.write(chara)
    sys.stdout.flush()
    if (chara == "!"):
        sleep(0.5)
    if (chara == "."):
        sleep(0.5)
print(border)
quit()