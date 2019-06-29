import os
from PIL import Image
from glob import glob


"""
Example tree file convert:

  NAME_FOLDER
    + B
      - file.tif
      - file.tif
    + C
      - file.tif
      - file.tif
    + D
"""

NAME_FOLDER = "file_tiff" # change name folder here


dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + NAME_FOLDER
os.chdir(dir_path)

for folder in os.listdir():
  fileConvert = dir_path + "/" + folder
  os.chdir(fileConvert)

  for name in glob('*.tif'):
    im = Image.open(name)
    name = str(name).rstrip(".tif")

    im.save(name + '.jpg', 'JPEG') # save file to .jpg

    os.remove(rm) # remove file tif old in folder

    print(">> convert done: ", name)


print("Conversion from tif to jpg completed!")