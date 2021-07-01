import PIL
from PIL import Image
from tkinter.filedialog import *

width = 300
height = 300

image = askopenfilename()

img = Image.open(image)
img = img.resize((width, height),PIL.Image.ANTIALIAS)
img.save("resize_image.jpg")