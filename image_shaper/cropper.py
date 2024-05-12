import os
from PIL import Image


def cut_edges(source_dir, output_dir, cut_top, cut_bot, cut_right, cut_left):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith(".png"):
            image_path = os.path.join(source_dir, filename)
            img = Image.open(image_path)

            width, height = img.size
            img_cropped = img.crop((cut_left, cut_top, width - cut_right, height - cut_bot))

            output_path = os.path.join(output_dir, filename)
            img_cropped.save(output_path)

            print(f"Processed: {filename}")


if __name__ == "__main__":
    """
    Cut the edges of every image can be found in "source_dir" and saves the cut images to "output_dir".
    """
    source_dir = "input"
    output_dir = "cropped"

    cut_edges(source_dir, output_dir,
              cut_top=0,
              cut_bot=0,
              cut_right=200,
              cut_left=200
              )
