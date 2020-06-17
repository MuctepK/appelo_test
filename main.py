import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
for file in os.listdir('source-images'):
    img = Image.open('source-images/'+file)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 50)
    author = file[:file.find('.jpg')]
    name, surname = author.split('-')
    name, surname = name.title(), surname.title()
    text = "©{} {}".format(name, surname)
    text_w, text_h = draw.textsize(text, font)
    draw.text((width-text_w-20, height-text_h-20), text, (255, 255, 255), font=font)
    img.save('output-images/'+file)