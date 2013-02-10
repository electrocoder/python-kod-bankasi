#! /usr/bin/env python

# directory_image_gif2png.py
#
# Klasorun icerisindeki tum gif formatındaki resimleri png olarak kaydeder.


import os
import Image

for i in os.listdir(os.getcwd()):
    if i.split(".")[1] == "gif":
        im = Image.open(i)
        im.save((i.split(".")[0]).lower() + ".png")
        print i + " -> " + (i.split(".")[0]).lower() + ".png ok"
