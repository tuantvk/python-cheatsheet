from PIL import Image
from glob import glob

basewidth = 800

for p in glob("*.png"):
  print(p)
  img = Image.open(p)
  wpercent = (basewidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
  img.save(p) 
