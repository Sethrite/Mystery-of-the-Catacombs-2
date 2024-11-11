from tkinter import (
    # Widgets
    Frame, Label, Text, PhotoImage, Entry,
    
    # Constants
    X, Y, BOTH,
    BOTTOM, RIGHT, LEFT,
    DISABLED, NORMAL, END,

    # Additional Stuff for Typehints
    Tk
)

import os
from room2 import Room



class Game(Frame):

    # Some constants for the game
    EXIT_ACTIONS = ["exit", "quit", "q", "bye"]

    # Some statuses
    STATUS_DEFAULT = "I don't understand. Try verb noun. Valid verbs are go, look, take."
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid exit."
    STATUS_ROOM_CHANGE = "Room Changed."
    STATUS_GRABBED = "Item Grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that item."

    #Game Dimensions
    WIDTH = 800
    HEIGHT = 600


    def __init__(self, parent: Tk):
        """
        The Game Class.
        
        parent: Tk - a Tk object representing the window the game runs in
        """

        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

    def setup_game(self):
        
        # create rooms
        r1 = Room("Room 1", os.path.join("images2","room1.PNG"))
        r2 = Room("Room 2", os.path.join("images2","room2.PNG"))
        r3 = Room("Room 3", os.path.join("images2","room3.PNG"))
        r4 = Room("Room 4", os.path.join("images2","room4.PNG"))
        r5 = Room("Room 5", os.path.join("images2","room5.PNG"))
        r6 = Room("Room 6", os.path.join("images2","room6.PNG"))
        r7 = Room("Room 7", os.path.join("images2","room7.PNG"))
        r8 = Room("Room 8", os.path.join("images2","room8.PNG"))
        r9 = Room("Room 9", os.path.join("images2","room9.PNG"))
        r10 = Room("Room 10", os.path.join("images2","room10.PNG"))
        r11 = Room("Room 11", os.path.join("images2","room11.PNG"))
        r12 = Room("Room 12", os.path.join("images2","room12.PNG"))
        r13 = Room("Room 13", os.path.join("images2","room13.PNG"))
        
        # create exits to rooms
    
    # add exits to room 1
        r1.add_exit("east", r2) # -> to the east of room 1 is room 2
        r1.add_exit("south", r3)# -> to the east of room 1 is room 3
        # add grabbables to room 1
        # add items to room 1
        r1.add_item("chair", "The chair is made of mahogany and a ghost is sitting on it.")
        """r1.add_item("death (temporary, to test death effect)", " ")"""
        r1.add_item("table", "The table is made of very brittle birch. A key rests on it. You pick it up.\n\nA key was added to your inventory.")
        
        
        # add exits to room 2
        r2.add_exit("west", r1)# -> to the west of room 2 is room 1
        r2.add_exit("south", r4)# -> to the south of room 2 is room 4
        # add items to room 2
        r2.add_item("rug", "It is an egyptian rug, you see it slightly hovering above the ground. Under it you discover a stair way leading north!")
        r2.add_item("fireplace", "You pull the lever next to the fireplace. A doorway appears to the east!")
        
        
        # add exits to room 3
        r3.add_exit("north", r1)# -> to the north of room 3 is room 1
        r3.add_exit("west", r10)# -> to the west of room 3 is room 10
        r3.add_exit("south", r11)# -> to the north of room 3 is room 11
        # add grabbables to room 3
        r3.add_grabbable("statue")
        # add items to room 3
        r3.add_item("spell_book", "You open the book to Chapter 7. (How to Create a Sleeping Potion) the ingredients requried are: A Rat Heart, Water-Filled Flask, and a Serapias Herb.")
        r3.add_item("statue", "The statue depicts a woman in a long dress, with angel wings. It is covering its face.")
        r3.add_item("desk", "The desk is dusty and withered. The statue and spell book are resting on it.")
        
        
        # add exits to room 4
        r4.add_exit("north", r2)# -> to the north of room 4 is room 2
        r4.add_exit("south", r12)# -> to the south of room 4 is room 12
        # add grabbables to room 4
        r4.add_grabbable("flask")
        # add items to room 4
        r4.add_item("stone_table", "Yep, that is a indeed a stone table. The brewing stand and flask are resting on it.")
        r4.add_item("brewing_stand", "You see the brewing stand on top of the stone table. It looks like it could prove useful.")
        r4.add_item("flask", "The glass flask is on the stone table, filled with water. It is in mint condition.")

        # add exits to room 5
        r5.add_exit("north", r6) # -> to the north of room 5 is room 6
        # add grabbables to room 5
        # No grabbables
        # add items to room 5
        r5.add_item("casket","You see a diamond ring next to the wrapped body. You found an artifact!\n\nA diamond ring was added to your inventory.")
        r5.add_item("painting","The artwork depicts a long lost land, with the an ancient scroll positioned at the center.")
        r5.add_item("cobwebs","")
        
        # add exits to room 6
        r6.add_exit("west", r2) # -> to the west of room 6 is room 2
        # add grabbables to room 6
        r6.add_grabbable("coin")
        # add items to room 6
        r6.add_item("armor","You see armor lying on the floor and there are remanents of human ash on it.")
        r6.add_item("pressure_plate","")
        r6.add_item("coin","The coin has the face of the dead king and is worth a wooping $5.")
        r6.add_item("door", "You try to open the door, but you need a code. The door leads to the prince's room.")
        # add exits to room 7
        r7.add_exit("south", r2) # -> to the south of room 7 is room 2
        # add grabbables to room 7
        r7.add_grabbable("serapias_herb")
        r7.add_grabbable("rat")
        # add items to room 7
        r7.add_item("rat", "In the corner you see the carcas of a rat from long ago and for some reason it did not decompose.")
        r7.add_item("serapias_herb", "You find it   ide a wooden barrel. The plant's smell makes you drowsy.")
        r7.add_item("cabinet", "You move the cabinet and discover a secret door to the west. You notice it has a keyhole.")
        
        # add exits to room 8
        r8.add_exit("east", r7) # -> to the east of room 8 is room 7
        # add grabbables to room 8
        r8.add_grabbable("gems")
        r8.add_grabbable("gold")
        r8.add_grabbable("jewelry")
        r8.add_grabbable("priceless_painting")
        # add items to room 8
        r8.add_item("gold", "You see a stack of gold on the floor, it looks very appealing.\n\nYou hear a voice say 'You should take some.'")
        r8.add_item("jewelry", "You see a stack of jewelry on the floor, it looks really appealing.\n\nYou hear a voice say 'You should take some'.")
        r8.add_item("gems", "The gems glisten on the floor of the room, it looks extremely appealing.\n\nYou hear a voice say 'You should take some.'")
        r8.add_item("priceless_painting", "The painting displays a starry night above a dark blue city, the painting would look perfect on your wall.\n\nYou hear a voice say 'You should take it.'")
        r8.add_item("ruby_goblet", "You see a golden goblet with a ruby gem ingrained upon it. You found an artifact!\n\nA ruby goblet was added to your inventory.")
        
        # add exits to room 9
        r9.add_exit("south", r10) # -> to the south of room 9 is room 10
        # add grabbables to room 9
        # No grabbable
        # add items to room 9
        r9.add_item("casket", "You see a the king's crown next to the mummified body. You found an artifact!\n\nThe king's crown was added to your inventory.")
        r9.add_item("crack", "")
        r9.add_item("scroll", "You pick up the scroll and it has some ancient language written on it. You do not understand what it says.")
        
        # add exits to room 10
        r10.add_exit("north", r9) # -> to the north of room 10 is room 9
        r10.add_exit("east", r3)# -> to the east of room 10 is room 3
        # add grabbables to room 10
        # No grabbable
        # add items to room 10
        r10.add_item("guard", "You see the eteranl guard. His title 'Blood-Red Commander Igris'. \n\nHe stares at you menacingly and yells 'LEAVE AT ONCE OR ELSE!'")
        
        # add exits to room 11
        r11.add_exit("north", r3) # -> to the north of room 11 is room 3
        # add grabbables to room 11
        r11.add_grabbable("code")
        # add items to room 11
        r11.add_item("shovel", "You see a code for a door attached to the shovel's head.\n\nA code was added to your inventory.")
        r11.add_item("pickaxe", "The pickaxe is is missing its shaft. It is unusable.")
        r11.add_item("sword", "The sword is rusted and shattered. It is unsuitable for combat")
        r11.add_item("shield", "The shield is burnt and split in half. It is out of commission.")
        
        # add exits to room 12
        r12.add_exit("north", r4) # -> to the north of room 12 is room 4
        r12.add_exit("south", r12)# -> to the south of room 12 is room 4
        # add grabbables to room 12
        # No grabbables
        # add items to room 12
        r12.add_item("locked_gate", "In the door you see three spaces for three objects. The spaces for the artifacts seem relatively small.")
        
        # add exits to room 13
        # No Exits
        # add grabbables to room 13
        # No grabbables
        # add items to room 13

            # set room 1 as the current room at the beginning of the game
        self.current_room = r1


    def setup_gui(self):

        # the input element (bottom of the window)
        self.player_input = Entry(self, bg = "white", fg ="black")
        self.player_input.bind("<Return>", self.process_input)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # the image element (left side)
        img = None
        img_width = Game.WIDTH // 2
        self.image_container = Label(self, width =img_width, image=img)
        self.image_container.image = img
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False)


        # the info area (right side)
        text_container_width = Game.WIDTH // 2
        text_container = Frame(self, width=text_container_width)

        self.text = Text(text_container, bg="lightgrey", fg="black",state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

    def set_image(self):
        if self.current_room == None:
            img = PhotoImage(file="images/skull.gif")
        else:
            img = PhotoImage(file=self.current_room.image)
        
        self.image_container.config(image=img)
        self.image_container.image = img
        
    def set_status(self, status: str):
        self.text.config(state=NORMAL) # make the text editable
        self.text.delete(1.0, END)

        if self.current_room == None:
            self.text.insert(END, Game.STATUS_DEAD)
        else:
            content = f"{self.current_room}\n"
            content += f"You are carrying: {self.inventory}\n\n"
            content += status
            self.text.insert(END, content)
        
        self.text.config(state=DISABLED)    

    def clear_entry(self):
        self.player_input.delete(0, END)
            
    def handle_go(self, destination):
        status = Game.STATUS_BAD_EXIT
        if destination in self.current_room.exits: # exits is a dictionary, we're checking the keys
            self.current_room = self.current_room.exits[destination]
            status = Game.STATUS_ROOM_CHANGE

        self.set_status(status)
        self.set_image()

    def handle_look(self, item):
        status = Game.STATUS_BAD_ITEM
        if item in self.current_room.items:
            status = self.current_room.items[item]
        self.set_status(status)

    def handle_take(self, grabbable):
        status = Game.STATUS_BAD_GRABBABLE
        if grabbable in self.current_room.grabbables: # this is just a list, not a dict
            self.inventory.append(grabbable)
            self.current_room.deleta_grabbable(grabbable)
            status = Game.STATUS_GRABBED
        self.set_status(status)
    
    def handle_default(self):
        self.set_status(Game.STATUS_DEFAULT)
        self.clear_entry()

    def play(self):
        self.setup_game()
        self.setup_gui()
        self.set_image()
        self.set_status("")

    def process_input(self, event):
        action = self.player_input.get()
        action = action.lower()


        if action in Game.EXIT_ACTIONS:
            exit()

        if self.current_room == None:
            self.clear_entry()
            return
        
        words = action.split() # creates a list, default splits at space

        if len(words) != 2:
            self.handle_default()
            return
        
        verb = words[0]
        noun = words[1]

        match verb:
            case "go":self.handle_go(noun)
            case "look":self.handle_look(noun)
            case "take":self.handle_take(noun)
        
        self.clear_entry()
        


