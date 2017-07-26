__author__ = 'vjVaidya'
""" download a specific file/any number of files from a given url """

from PIL import Image as pil

foo = pil.open("path\\to\\image.jpg")
print (foo.size) #get the size of the image
foo = foo.resize((160,300),pil.ANTIALIAS) # downsize the image with an ANTIALIAS filter (gives the highest quality)
foo.save("path\\to\\save\\image_scaled.jpg",quality=95) # The saved downsized image size is 24.8kb
foo.save("path\\to\\save\\image_scaled_opt.jpg",optimize=True,quality=95) # The saved downsized image size is 22.9kb