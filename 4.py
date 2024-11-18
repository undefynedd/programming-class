# my idea is you have a mask image file, (less than #800000 is black) and it uses an input string to generate a yes!

from PIL import Image
import numpy as np

rawmask = Image.open('./images/horse.png')
rawmask = rawmask.resize((rawmask.size[0], 2*rawmask.size[1]//5))
rawmask = rawmask.convert('1')

mask = np.array(rawmask)

print(mask.shape)

pattern = input('tell me what u wanna use as ur thingy')
step = 0

cat = ''

for x in range(rawmask.size[1]):
    for y in range(rawmask.size[0]):
        if mask[x,y]:
            cat += pattern[step] 
            step += 1
            if step == len(pattern):
                step = 0
        else:
            cat += ' '
    cat += "\n"

print(cat)

#mask = rawmask.tobitmap()
#print(mask)

