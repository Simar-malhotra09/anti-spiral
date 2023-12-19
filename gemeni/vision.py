import base64
from PIL import Image
import os
from collections import OrderedDict

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




'''
use vision for image and q_input and clean image_input 
use pro for everything else

'''

model_pro_vision = genai.GenerativeModel('gemini-pro-vision')

chat = model_pro_vision.start_chat(history=[])

prompt = "Can you extract all the the main text in the image, whateves in the window of the image "


response = model_pro_vision.generate_content([prompt, img], stream=True)


response = chat.send_message([prompt, img], stream=True)
response.resolve()
#rint(response.text)


for message in chat.history:
  print(f'**{message.role}**: {message.parts[0].text}')

'''
message_dict = OrderedDict()
for message in chat.history:
    message_dict[message['parts'][0]['text']] = {'role': message.role, 'text': message.parts[0].text}

# Print the message dictionary
for text, data in message_dict.items():
    print(f'**{data["role"]}**: {data["text"]}')'''