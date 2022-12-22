#!C:\Users\rosenwild\anaconda3\python.exe
text = "Михайленко!"
s = ''

from PIL import Image, ImageDraw, ImageFont
import numpy as np

myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1", size, "black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ', '#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
s = "\n".join(strings)

print("Content-type: text/html\n")
print("<html><head>\n")
print("</head><body>")

print('<pre>' + s + '</pre>')

print("</body></html>")