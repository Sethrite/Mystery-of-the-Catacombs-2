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
from room import Room
import os

class Game(Frame):

    # Some constants for the game
    EXIT_ACTIONS = ["exit", "quit", "q", "bye"]

    # Some statuses
    STATUS_DEFAULT = "I don't understand.. Try verb noun. Valid verbs are go, look, take."
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid exit."
    STATUS_ROOM_CHANGE = "Room Changed."
    STATUS_GRABBED = "Item Grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."

    # option: have a Status class within the Game class
    # class Status:
    #     Default = ""
    #     DEAD = ""

    # Game Dimensions
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
        r1 = Room("Room 1", os.path.join("images","room1.PNG"))
        r2 = Room("Room 2", os.path.join("images","room2.PNG"))
        r3 = Room("Room 3", os.path.join("images","room3.PNG"))
        r4 = Room("Room 4", os.path.join("images","room4.PNG"))
        
        # create exits to rooms

        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("west", r3)
        r4.add_exit("north", r2)
        r4.add_exit("south", None)


        # add items to rooms

        r1.add_item("chair", "Its made of baked beans in a grocery bag, there is a key in the bag")
        r1.add_item("tv", "Its playing Spongebob")

        r2.add_item("knife", "Its rusted.")
        r2.add_item("tv", "It's also playing Spongebob, but a different episode")

        r3.add_item("sponge", "Its just a sponge")
        r3.add_item("bob", "Its a guy named bob.")

        r4.add_item("squidward", "He's playing the clarinet.")
        r4.add_item("patrick", "He's playing the mayonnaise")

        # add grabbables to rooms
        r1.add_grabbable("key")
        r2.add_grabbable("knife")
        r3.add_grabbable("sponge")
        r4.add_grabbable("clarinet")

        # set the starting room for the game

        self.current_room = r1

    def setup_gui(self):

        # the input element (bottom of the window)
        self.player_input = Entry(self, bg="white", fg="black")
        self.player_input.bind("<Return>", self.process_input)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # the image element (left side)
        img = None
        img_width = Game.WIDTH // 2
        self.image_container = Label(
            self,
            width=img_width,
            image=img,
        )
        self.image_container.image = img
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False)

        # the info area (right side)
        text_container_width = Game.WIDTH // 2
        text_container = Frame(self, width=text_container_width)

        self.text = Text(
            text_container,
            bg="lightgrey",
            fg="black",
            state=DISABLED
        )
        self.text.pack(fill=Y, expand=1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

    def set_image(self):
        if self.current_room == None:
            img = PhotoImage(file="image/skull.gif")
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
            self.current_room.delete_grabbable(grabbable)
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
            case "go": self.handle_go(noun)
            case "look": self.handle_look(noun)
            case "take": self.handle_take(noun)
        
        self.clear_entry()