#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
# PNG (400, 300) RGB
im.thumbnail((1024, 728))
im.save('thumb.jpg', 'JPEG')

help(Image)