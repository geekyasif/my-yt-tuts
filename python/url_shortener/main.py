# pip install pyshorteners

import pyshorteners

url = "https://www.youtube.com/watch?v=4XPwdX60tDg"
short = pyshorteners.Shortener()

shorted_url = short.tinyurl.short(url)
print(shorted_url)