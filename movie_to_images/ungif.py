import imageio
import os


def gif_to_png(input_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the GIF file
    gif = imageio.get_reader(input_file)

    # Iterate over each frame in the GIF
    for i, frame in enumerate(gif):
        # Generate the output file name
        output_file = os.path.join(output_folder, f"frame_{i}.png")
        
        # Save the frame as a PNG file
        imageio.imwrite(output_file, frame)


if __name__ == "__main__":
    # Path to the input GIF file
    gif_file_name = 'dogs_are_barking.gif'
    input_file = f"C:/path/to/your/gif/file/{gif_file_name}"
    output_folder = "../output"

    # Convert GIF to PNG
    gif_to_png(input_file, output_folder)
