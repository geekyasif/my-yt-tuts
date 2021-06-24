# pip install qrcode
# pip install pillow

import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# to create qrcode
img = qrcode.make("https://geekyasif.github.io/")
img.save('geeky.png')

# to read qrcode
d = decode(Image.open('geeky.png'))
print(d[0].data.decode('ascii'))