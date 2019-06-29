import requests
import os

HOST = 'http://0.0.0.0:8000/' # Server
PATH_FILE = '/user/file.png' # Path file

 
def send_data_to_server(image_path, temperature = ''):
         
  image_filename = os.path.basename(image_path)

  multipart_form_data = {
    'image': (image_filename, open(image_path, 'rb')),
    'temperature': ('', str(temperature)),
  }
 
  response = requests.post(HOST, files=multipart_form_data)
  print(response.json())


send_data_to_server(PATH_FILE)