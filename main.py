# Name: Mark Masenda
# Date: 10/25/2024
# Description: Room Adventure with a GUI

from tkinter import Tk
from game import Game

window = Tk()
window.title("Mystery of the Catacombs 2")
game = Game(window)
game.play()
game.mainloop()