from PIL import Image
import os
from collections import OrderedDict 
from collections import defaultdict
import csv


def get_text_between_rows(file_path, start_row_num, end_row_num):
    extracted_text = []
    
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row_number, row in enumerate(csv_reader, start=1):
            if start_row_num <= row_number <= end_row_num:
                extracted_text.append(' '.join(row))
    
    return '\n'.join(extracted_text)

def format_csv(file_path):
    resume_list= []
    edu_row_num = 0
    work_row_num = 0
    skills_row_num = 0
    projects_row_num = 0

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row_number, row in enumerate(csv_reader, start=1):
            if 'Education' in row:
                edu_row_num = row_number
            elif 'Work Experience' in row:
                work_row_num = row_number
            elif 'Skills' in row:
                skills_row_num = row_number
            elif 'Projects' in row:
                projects_row_num = row_number

    edu_text = get_text_between_rows(file_path, edu_row_num, work_row_num)
    
    return edu_text


        

def write_to_csv(file_path, data):
    """
    Write data to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        header (list): A list containing the column names (header) for the CSV.
        data (list of lists): A list of lists containing the data to be written.
    """
    try:
        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        print(f"Data written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


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


