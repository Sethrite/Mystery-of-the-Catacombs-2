
# Name: Ned Hammatt
# Date: October 25th, 2024
# Description: Room Adventure with a GUI

from tkinter import Tk
from game2 import Game
# from playsound import playsound

window = Tk()
window.title("Room Adventure Reloaded")
game = Game(window)
game.play()
window.mainloop()

