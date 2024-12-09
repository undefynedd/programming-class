# my idea is you have a mask image file, (less than #800000 is black) and it uses an input string to generate a yes!

from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join
files = [f for f in listdir('./images/') if isfile(join('./images/', f))]

filelist=''
filenum=1

for file in files:
    filelist += str(filenum) + ". " + file + "\n"
    filenum += 1

try:
    maskfile = files[int(input('Choose an image:\n' + filelist)) - 1]
except:
    maskfile = files[int(input('Type a number: ')) - 1]


rawmask = Image.open('./images/' + maskfile)
width = int(input("size: "))
rawmask = rawmask.resize((width, 2 * (width * rawmask.size[1])//(5 * rawmask.size[0])))
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

