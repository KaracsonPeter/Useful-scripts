import os
from PIL import Image


def resize_images(source_dir, output_dir, size_x, size_y):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through each image file in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file is an image
        if filename.endswith((".png", ".jpg", ".jpeg")):
            # Open the image
            image_path = os.path.join(source_dir, filename)
            img = Image.open(image_path)

            # Resize the image
            img_resized = img.resize((size_x, size_y))

            # Save the resized image to the output directory
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)

            print(f"Processed: {filename}")


if __name__ == "__main__":
    """
    Resize image by distorting them.
    """
    input_file = 'input'
    output_folder = "output"

    resize_images(input_file, output_folder, 512, 512)
