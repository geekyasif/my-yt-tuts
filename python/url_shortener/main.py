# pip install pyshorteners

import pyshorteners

url = "https://thecompetitiveprogrammer.com/hackerrank-offer-internship-opportunity-for-students-as-software-engineer-intern/"
short = pyshorteners.Shortener()

shorted_url = short.tinyurl.short(url)
print(shorted_url)