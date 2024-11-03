# import tkinter module
from tkinter import *
from tkinter.ttk import *

master = Tk()

# First row: column explanation --------------------------------------------------------
row = 0
l11 = Label(master, text="Key bounds for Spotify background helper")
l11.grid(row=row, column=0, sticky=W, pady=2)

l14 = Label(master, text="Key 1")
l14.grid(row=row, column=3, sticky=W, pady=2)

l15 = Label(master, text="Key 2")
l15.grid(row=row, column=4, sticky=W, pady=2)

l16 = Label(master, text="Key 3")
l16.grid(row=row, column=5, sticky=W, pady=2)

# Second row: Specify forwarding of music --------------------------------------------------------
row = 1
l21 = Label(master, text="Forward music by")
l21.grid(row=row, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e22 = Entry(master)
e22.grid(row=row, column=1, sticky=W, pady=2)

l23 = Label(master, text="seconds by pressing")
l23.grid(row=row, column=2, sticky=W, pady=2)

e24 = Entry(master)  # Key 1
e24.grid(row=row, column=3, sticky=W, pady=2)

l25 = Label(master, text="+")
l25.grid(row=row, column=4, sticky=W, pady=2)

e26 = Entry(master)  # Key 2
e26.grid(row=row, column=5, sticky=W, pady=2)

l27 = Label(master, text="+")
l27.grid(row=row, column=6, sticky=W, pady=2)

e28 = Entry(master)  # Key 3
e28.grid(row=row, column=7, sticky=W, pady=2)

# 3nd row: Specify forwarding of music --------------------------------------------------------
row = 2
l31 = Label(master, text="Backward music by")
l31.grid(row=row, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e32 = Entry(master)
e32.grid(row=row, column=1, sticky=W, pady=2)

l33 = Label(master, text="seconds by pressing")
l33.grid(row=row, column=2, sticky=W, pady=2)

e34 = Entry(master)  # Key 1
e34.grid(row=row, column=3, sticky=W, pady=2)

l35 = Label(master, text="+")
l35.grid(row=row, column=4, sticky=W, pady=2)

e36 = Entry(master)  # Key 2
e36.grid(row=row, column=5, sticky=W, pady=2)

l37 = Label(master, text="+")
l37.grid(row=row, column=6, sticky=W, pady=2)

e38 = Entry(master)  # Key 3
e38.grid(row=row, column=7, sticky=W, pady=2)

# 4th row: Specify forwarding of music --------------------------------------------------------
row = 3
l41 = Label(master, text="Play previous music by pressing")
l41.grid(row=row, column=0, sticky=W, pady=2)

e44 = Entry(master)  # Key 1
e44.grid(row=row, column=3, sticky=W, pady=2)

l45 = Label(master, text="+")
l45.grid(row=row, column=4, sticky=W, pady=2)

e46 = Entry(master)  # Key 2
e46.grid(row=row, column=5, sticky=W, pady=2)

l47 = Label(master, text="+")
l47.grid(row=row, column=6, sticky=W, pady=2)

e48 = Entry(master)  # Key 3
e48.grid(row=row, column=7, sticky=W, pady=2)

# 5th row: Specify forwarding of music --------------------------------------------------------
row = 4
l41 = Label(master, text="Play next music by pressing")
l41.grid(row=row, column=0, sticky=W, pady=2)

e44 = Entry(master)  # Key 1
e44.grid(row=row, column=3, sticky=W, pady=2)

l45 = Label(master, text="+")
l45.grid(row=row, column=4, sticky=W, pady=2)

e46 = Entry(master)  # Key 2
e46.grid(row=row, column=5, sticky=W, pady=2)

l47 = Label(master, text="+")
l47.grid(row=row, column=6, sticky=W, pady=2)

e48 = Entry(master)  # Key 3
e48.grid(row=row, column=7, sticky=W, pady=2)

# 6th row: Specify forwarding of music --------------------------------------------------------
row = 5
l51 = Label(master, text="Stop / Start music by pressing")
l51.grid(row=row, column=0, sticky=W, pady=2)

e54 = Entry(master)  # Key 1
e54.grid(row=row, column=3, sticky=W, pady=2)

l55 = Label(master, text="+")
l55.grid(row=row, column=4, sticky=W, pady=2)

e56 = Entry(master)  # Key 2
e56.grid(row=row, column=5, sticky=W, pady=2)

l57 = Label(master, text="+")
l57.grid(row=row, column=6, sticky=W, pady=2)

e58 = Entry(master)  # Key 3
e58.grid(row=row, column=7, sticky=W, pady=2)

# 7th row: Specify forwarding of music --------------------------------------------------------
row = 6
l61 = Label(master, text="Add current music to playlist named")
l61.grid(row=row, column=0, sticky=W, pady=2)

e62 = Entry(master)  # Playlist name
e62.grid(row=row, column=1, sticky=W, pady=2)

l63 = Label(master, text="by pressing")
l63.grid(row=row, column=2, sticky=W, pady=2)

e64 = Entry(master)  # Key 1
e64.grid(row=row, column=3, sticky=W, pady=2)

l65 = Label(master, text="+")
l65.grid(row=row, column=4, sticky=W, pady=2)

e66 = Entry(master)  # Key 2
e66.grid(row=row, column=5, sticky=W, pady=2)

l67 = Label(master, text="+")
l67.grid(row=row, column=6, sticky=W, pady=2)

e68 = Entry(master)  # Key 3
e68.grid(row=row, column=7, sticky=W, pady=2)

# 8th row: Specify forwarding of music --------------------------------------------------------
row = 7
l71 = Label(master, text="Add current music to playlist named")
l71.grid(row=row, column=0, sticky=W, pady=2)

e72 = Entry(master)  # Playlist name
e72.grid(row=row, column=1, sticky=W, pady=2)

l73 = Label(master, text="by pressing")
l73.grid(row=row, column=2, sticky=W, pady=2)

e74 = Entry(master)  # Key 1
e74.grid(row=row, column=3, sticky=W, pady=2)

l75 = Label(master, text="+")
l75.grid(row=row, column=4, sticky=W, pady=2)

e76 = Entry(master)  # Key 2
e76.grid(row=row, column=5, sticky=W, pady=2)

l77 = Label(master, text="+")
l77.grid(row=row, column=6, sticky=W, pady=2)

e78 = Entry(master)  # Key 3
e78.grid(row=row, column=7, sticky=W, pady=2)

# 9th row: Specify forwarding of music --------------------------------------------------------
row = 8
l81 = Label(master, text="Add current music to playlist named")
l81.grid(row=row, column=0, sticky=W, pady=2)

e82 = Entry(master)  # Playlist name
e82.grid(row=row, column=1, sticky=W, pady=2)

l83 = Label(master, text="by pressing")
l83.grid(row=row, column=2, sticky=W, pady=2)

e84 = Entry(master)  # Key 1
e84.grid(row=row, column=3, sticky=W, pady=2)

l85 = Label(master, text="+")
l85.grid(row=row, column=4, sticky=W, pady=2)

e86 = Entry(master)  # Key 2
e86.grid(row=row, column=5, sticky=W, pady=2)

l87 = Label(master, text="+")
l87.grid(row=row, column=6, sticky=W, pady=2)

e88 = Entry(master)  # Key 3
e88.grid(row=row, column=7, sticky=W, pady=2)

# 10th row: Modification lock --------------------------------------------------------
row = 9
c91 = Checkbutton(master, text="Enable Settings Modification")
c91.grid(row=row, column=0, sticky=W, columnspan=2)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()
