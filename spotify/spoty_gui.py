import pathlib

import yaml
import tkinter as tk
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
l15.grid(row=row, column=5, sticky=W, pady=2)

l16 = Label(master, text="Key 3")
l16.grid(row=row, column=7, sticky=W, pady=2)

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
l51 = Label(master, text="Play next music by pressing")
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

# 6th row: Specify forwarding of music --------------------------------------------------------
row = 5
l61 = Label(master, text="Stop / Start music by pressing")
l61.grid(row=row, column=0, sticky=W, pady=2)

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

# 7th row: Specify forwarding of music --------------------------------------------------------
row = 6
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

# 8th row: Specify forwarding of music --------------------------------------------------------
row = 7
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

# 9th row: Specify forwarding of music --------------------------------------------------------
row = 8
l91 = Label(master, text="Add current music to playlist named")
l91.grid(row=row, column=0, sticky=W, pady=2)

e92 = Entry(master)  # Playlist name
e92.grid(row=row, column=1, sticky=W, pady=2)

l93 = Label(master, text="by pressing")
l93.grid(row=row, column=2, sticky=W, pady=2)

e94 = Entry(master)  # Key 1
e94.grid(row=row, column=3, sticky=W, pady=2)

l95 = Label(master, text="+")
l95.grid(row=row, column=4, sticky=W, pady=2)

e96 = Entry(master)  # Key 2
e96.grid(row=row, column=5, sticky=W, pady=2)

l97 = Label(master, text="+")
l97.grid(row=row, column=6, sticky=W, pady=2)

e98 = Entry(master)  # Key 3
e98.grid(row=row, column=7, sticky=W, pady=2)


# 10th row: Modification lock --------------------------------------------------------
all_entry = {
    "e22": e22, "e24": e24, "e26": e26, "e28": e28,
    "e32": e32, "e34": e34, "e36": e36, "e38": e38,
    "e44": e44, "e46": e46, "e48": e48,
    "e54": e54, "e56": e56, "e58": e58,
    "e64": e64, "e66": e66, "e68": e68,
    "e72": e72, "e74": e74, "e76": e76, "e78": e78,
    "e82": e82, "e84": e84, "e86": e86, "e88": e88,
    "e92": e92, "e94": e94, "e96": e96, "e98": e98,
}
all_entry_request_dict = dict()
if pathlib.Path('settings.yaml').is_file():
    # Read settings
    with open('settings.yaml', 'r') as f:
        all_entry_request_dict = yaml.load(f, Loader=yaml.SafeLoader)

    # Load settings
    for entry_name, content in all_entry_request_dict.items():
        eval(f"{entry_name}.insert(0, '{content}')")


def get_var_name(var):
    for name, value in locals().items():
        if value is var:
            return name


def checkbox_callback():
    if check_var.get() == 1:
        for name, entry in all_entry.items():
            entry.config(state="enabled")
    else:
        for name, entry in all_entry.items():
            entry.config(state="disabled")
            all_entry_request_dict[name] = entry.get()
        with open('settings.yaml', 'w') as outfile:
            yaml.dump(all_entry_request_dict, outfile, default_flow_style=False)


row = 9
check_var = tk.IntVar()
c101 = Checkbutton(
    master,
    text="Check this for edit; Uncheck for verifying edit",
    variable=check_var,
    command=checkbox_callback
)
c101.grid(row=row, column=0, sticky=W, columnspan=2)

l103 = Label(master, text="Last pressed key combination")
l103.grid(row=row, column=2, sticky=W, pady=2)

e104 = Entry(master)  # Key 1
e104.grid(row=row, column=3, sticky=W, pady=2)
e104.config(state="disabled")

e106 = Entry(master)  # Key 2
e106.grid(row=row, column=5, sticky=W, pady=2)
e106.config(state="disabled")

e108 = Entry(master)  # Key 3
e108.grid(row=row, column=7, sticky=W, pady=2)
e108.config(state="disabled")


def set_entry_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)
    return True
