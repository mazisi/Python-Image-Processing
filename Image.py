import img as img
from PIL import Image, ImageFilter
def image():
    img  = Image.open('images/msesh.jpg')
    #print(img.size)#get image
    #print(img.size)  #get image size
    #print(img.format)  # get image format
    #print(img.mode)  # get image coloring e.g rgb
    #img.show()  # display image with default image viewer
    print(dir(img))

#apply image filters
def filterimage():
    img = Image.open('images/msesh.jpg')
    filtered_image = img.filter(ImageFilter.BLUR)
    #Availabkle options are: SMOOTH_MORE,SMOOTH,BLUR,CONTOUR,DETAIL,EDGE_ENHANCE,EDGE_ENHANCE_MORE,EMBOSS,FIND_EDGES,SHARPEN,SMOOTH
    #See docs: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html#module-PIL.ImageFilter
    #filtered_image.save("blur.png","png")

    #convert image to different formats eg ..apply grey scale
    # filtered_image.convert("L")
    # filtered_image.save("greyed.png", "png")

    # rotate image
    #rotate_image = filtered_image.rotate(90)
    #rotate_image.save("rotated.png", "png")
    # resize image
    resize_image = filtered_image.resize((300,300))#resized fn accepts a tuple
    resize_image.save("resized.png", "png")

    #crop image
    region = (100, 100, 400, 400)
    crop_image = filtered_image.crop(region)
    crop_image.save("cropped.png", "png")

def compressImage():
    img = Image.open('images/_3mb_image.jpg')
    img.thumbnail((400,400))#thumbnail tries to keep aspect ratio..as compared to resize()..(400 * 400) are max ranges
    img.save('compressed_image.png')


#image()
# filterimage()
#compressImage()