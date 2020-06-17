import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ImageParser:
    def __init__(self, file):
        self.file = file
        self.img = Image.open('source-images/' + file)
        self.draw = ImageDraw.Draw(self.img)
        self.width, self.height = self.img.size
        self.save_dir = 'output-images'
        self.font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 50)

    def get_text(self):
        author = self.file[:file.find('.jpg')]
        name, surname = author.split('-')
        name, surname = name.title(), surname.title()
        self.text = "©{} {}".format(name, surname)
        self.text_w, self.text_h = self.draw.textsize(self.text, self.font)

    def set_text_and_save(self):
        self.draw.text((self.width - self.text_w - 20, self.height - self.text_h - 20),
                       self.text, (255, 255, 255), font=self.font)
        self.img.save("{}/{}".format(self.save_dir, self.file))


for file in os.listdir('source-images'):
    if file.endswith('.jpg'):
        img = ImageParser(file)
        img.get_text()
        img.set_text_and_save()



