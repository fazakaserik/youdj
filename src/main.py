from win32api import GetSystemMetrics
import tkinter as tk
from tkinter import Grid, ttk
import time

from youTubePlayer import YouTubePlayer

# Get screen resolution
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# Constraints
player_height = 0.65
fader_resoltuion = 10

class Mixer:
  def __init__(self, width=800, height=600, x_pos=0, y_pos=0):
    self.root = tk.Tk()
    # Configure the root window
    self.root.title("YouDJ Mixer")
    self.root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    self.root.resizable(False, False)
    self.root.protocol("WM_DELETE_WINDOW", self.close_windows)

    Grid.rowconfigure(self.root, 0, weight=1)
    Grid.rowconfigure(self.root, 1, weight=1)
    Grid.columnconfigure(self.root, 0, weight=1)
    Grid.columnconfigure(self.root, 1, weight=5)
    Grid.columnconfigure(self.root, 2, weight=1)

    # Volume fader
    self.fader = ttk.Scale(
      self.root, 
      from_=0, 
      to=100,
      value=0,
      orient=tk.HORIZONTAL,
      length=screen_width*0.5
      )
    self.fader.grid(row=0, column=1)
    self.fader.bind("<ButtonRelease-1>", self.fader_event_handler)

    # Fader controllers
    self.fader_left_arrow = ttk.Button(
      text="<"
      )
    self.fader_left_arrow.grid(row=0, column=0, sticky="nsew")
    self.fader_left_arrow.bind(
      "<Button-1>", 
      lambda event: self.set_fader_value(self.fader.get()-fader_resoltuion)
      )

    self.fader_right_arrow = ttk.Button(
      text=">"
      )
    self.fader_right_arrow.grid(row=0, column=2, sticky="nsew")
    self.fader_right_arrow.bind(
      "<Button-1>",
      lambda event: self.set_fader_value(self.fader.get()+fader_resoltuion)
      )

    self.label = tk.Label(self.root, text="42%")
    self.label.grid(row=1, column=1, sticky="ew")

    # Set default volume
    self.set_fader_value(0)

    self.root.mainloop()

  def fader_event_handler(self, event):
    self.set_fader_value(int(self.fader.get()))

  def set_fader_value(self, value):
    value = max(0, min(100, value))
    player1.set_volume(100-value)
    player2.set_volume(value)
    self.fader.set(value)
    self.label.config(text="{}%".format(value))

  def close_windows(self):
    self.root.destroy()
    player1.close_browser()
    player2.close_browser()

if __name__ == "__main__":
    
  # Set up windows
  player1 = YouTubePlayer(
      width=screen_width/2, 
      height=screen_height * player_height, 
      x_pos=0, 
      y_pos=0)

  player2 = YouTubePlayer(
      width=screen_width/2, 
      height=screen_height * player_height, 
      x_pos=screen_width/2, 
      y_pos=0)

  mixer = Mixer(
      width=screen_width, 
      height=int(screen_height*(1-player_height)),
      x_pos=0,
      y_pos=int(screen_height*player_height)
      )