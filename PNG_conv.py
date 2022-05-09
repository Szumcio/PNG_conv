import os
import errno
from PIL import Image

input_file = './input_folder'
out_file = './output_folder'
watermark_file = './watermark_file'


if not os.path.exists(input_file):
    try:
        os.makedirs(input_file)
    except OSError as e:
                if e.errno != errno.EEXIST:
            raise

if not os.path.exists(out_file):
    try:
        os.makedirs(out_file)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

if not os.path.exists(watermark_file):
    try:
        os.makedirs(watermark_file)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

for filename in os.listdir(input_file):
    current_img = Image.open(input_file + '/' + filename)
    current_img.save(out_file + '/' + os.path.splitext(filename)[0] + '.png', 'PNG')
