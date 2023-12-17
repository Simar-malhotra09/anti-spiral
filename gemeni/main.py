import base64
from PIL import Image
import os
import google.generativeai as genai


#genai.configure(api_key='')




max_bytes = 4194304  
'''4,194,304 bytes'''

def get_image_size_bytes(file_path):
    """
    Get the size of an image file in bytes.

    Args:
        file_path (str): input file

    Returns:
        int: The size of the image file in bytes.
    """
    image_size_bytes = os.path.getsize(file_path)
    return image_size_bytes

def compress_image(file_path):
    """
    Compress an image and save it as a JPEG file.

    Args:
        file_path (str)
    Returns:
        compressed file_path (str)
    """
    try:
        # Open the image and get its size
        img = Image.open(file_path)
        print(f"Image format: {img.format}")
        image_size_bytes = get_image_size_bytes(file_path)

        # Convert the image to RGB mode (removing alpha channel), compress, and save it
        img = img.convert("RGB")
        img.save("compressed_image.jpg", "JPEG", optimize=True, quality=80)
        compressed_file_path = "compressed_image.jpg"
        print("Image saved successfully")

        # Compare the sizes of the original and compressed images
        compressed_image_size_bytes = get_image_size_bytes("compressed_image.jpg")
        print(f"Original Image size: {image_size_bytes} bytes")
        print(f"Compressed Image size: {compressed_image_size_bytes} bytes")

        return compressed_file_path
    except Exception as e:
        print(f"An error occurred while compressing the image: {e}")

def check_compression_eligibility(file_path):
    """
    Check if an image file exceeds the maximum allowed size for compression,
    and compress it if necessary.

    Args:
        file_path (str): The path to the input image file.
    
    """
    try:
        if get_image_size_bytes(file_path) > max_bytes:
            compress_image(file_path)
        else:
            print("Image size is within the acceptable range.")
            return file_path

    except Exception as e:
        print(f"An error occurred: {e}")




img = Image.open(check_compression_eligibility('./convergence.png'))





model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["In the context of the text in this image, can you explain what convergence is and how the author references it? ", img], stream=True)
response.resolve()
print(response.text)
