# Name: Mark Masenda
# Date: 10/25/2024
# Description: Room Adventure with a GUI

from tkinter import Tk
from game import Game

window = Tk()
window.title("Room Adventure Reloaded")
game = Game(window)
game.play()
game.mainloop()