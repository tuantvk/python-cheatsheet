# import send_data_to_server from uploadImage in folder upload
from uploadImage import send_data_to_server
from glob import glob

all_file = glob('*.png') # get all file .png in folder

for index, item in enumerate(all_file):
  send_data_to_server(item)