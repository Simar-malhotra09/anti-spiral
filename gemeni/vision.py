from PIL import Image
import os
import csv
from helper import check_compression_eligibility, write_to_csv, format_csv

import google.generativeai as genai


#genai.configure(api_key='')




if __name__ == "__main__":

    img = Image.open(check_compression_eligibility('./resume.png'))




    '''
    use vision for image and q_input and clean image_input 
    use pro for everything else

    '''

    model_pro_vision = genai.GenerativeModel('gemini-pro-vision')

    chat = model_pro_vision.start_chat(history=[])

    prompt = """
    Given this resume, please extract all the relevant information put into distinct sections with clearly numbered headings:

    1. Contact Information (this shoud include the name and/or email, linkedin, github)
    2. Education (this shoud include the name of the university, and/or place , relevant courses etc)
    3. Work Experience (Any research should be included)
    4. Skills
    5. Additional Information
    6. Projects

    This format will make it easy for me to review and post-process each section individually. 
    """


'''    response = model_pro_vision.generate_content([prompt, img], stream=True)
    response = chat.send_message([prompt, img], stream=True)
    response.resolve()
    #print(response.text)
    response_text= response.text
'

    data_to_write = [[img, response_text]]
    file_path = "resume.csv"  
    write_to_csv(file_path, data_to_write);'''
file_path = "resume.csv"  
dicta = format_csv(file_path)
print(dicta)




 #   for message in chat.history:
  #      print(f'**{message.role}**: {message.parts[0].text}')

'''
    message_dict = OrderedDict()
    for message in chat.history:
        message_dict[message['parts'][0]['text']] = {'role': message.role, 'text': message.parts[0].text}

    # Print the message dictionary
    for text, data in message_dict.items():
        print(f'**{data["role"]}**: {data["text"]}')'''