from PIL import Image
import os

def convert_to_webp(input_image_path, output_image_path):
    try:
        # Open the input image file
        img = Image.open(input_image_path)

        # Convert and save the image in WebP format
        img.save(output_image_path, format="webp")
        print(f"Conversion successful: {output_image_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Keep the space in the folder name if that's the actual folder name
    input_image = "C:\\Users\\Admin\\Desktop\\ds departme nt\\ali.jpg"
    
    # Path to save the WebP image
    output_image = "C:\\Users\\Admin\\Desktop\\ds departme nt\\ali.webp"

    # Convert the image
    convert_to_webp(input_image, output_image)
