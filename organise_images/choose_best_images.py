import os
import shutil
import keyboard
import pathlib

import tkinter

from PIL import Image, ImageTk


class ImageViewer:
    def __init__(self, master, image_files, destination_folder):
        self.master = master
        self.image_files = image_files
        self.destination_folder = destination_folder
        self.current_index = 0

        self.image_label = tkinter.Label(master)
        self.image_label.pack()

        self.display_image()

        self.master.bind("<Right>", self.copy_image)
        self.master.bind("<Left>", self.next_image)

    def display_image(self):
        image = Image.open(self.image_files[self.current_index])

        width, height = image.size
        scale_factor = 1
        image = image.resize((width // scale_factor, height // scale_factor))

        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def copy_image(self, event):
        shutil.copy(self.image_files[self.current_index], self.destination_folder)
        print(f"Image '{self.image_files[self.current_index].name}' copied to '{self.destination_folder}'")
        self.next_image(None)

    def next_image(self, event):
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.display_image()


def get_image_files(directory: pathlib.Path):
    return [file for file in directory.iterdir() if file.suffix.lower() in ['.png', '.jpg']]


if __name__ == "__main__":
    # ˇˇˇ CONFIGURE YOUR VARIABLES HERE ˇˇˇ
    # Location, from where you wanna see your images:
    directory = pathlib.Path('C:/move/pictures/7dtd')
    # Location, where you wanna save copy your favourite ones:
    destination_folder = pathlib.Path('C:/move/pictures/7dtd/_essence')
    # The following number shall exclude the first 'N' images (You might use it to pick up where you left off)
    exclude_first = 10
    # ^^^ CONFIGURE YOUR VARIABLES HERE ^^^

    image_files = get_image_files(directory)
    if len(image_files) > exclude_first:
        image_files = image_files[exclude_first:]
    else:
        print(f'Could not continue from image {exclude_first}. There is not enough picture in the designated folder.')

    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    app = ImageViewer(root, image_files, destination_folder)
    root.mainloop()
