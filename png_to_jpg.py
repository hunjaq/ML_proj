from PIL import Image
import os

#cleanup?

dir = os.listdir('king-png')
for i,file in enumerate(dir):
    im = Image.open(f"king-png/king-{i+1}.png")
    rgb_im = im.convert('RGB')
    rgb_im.save(f'king-resize/king-{i+1}.jpg')
