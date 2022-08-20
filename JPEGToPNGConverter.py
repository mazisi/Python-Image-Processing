import sys
import  os
from PIL import Image

#Grab all pics in images folder..loop through ..and convert them to PNGs

#check if new folder exists..if not create it...
if not os.path.exists('new_images'):
    os.makedirs('new_images')
for file_name in os.listdir('images'):     #Loop through images and convert to png
    img = Image.open('images/'+file_name)
    clean_file_name = os.path.splitext(file_name)[0]  #remove .jpg extension in filenames
    img.save('new_images/'+clean_file_name+'.png', 'png')


