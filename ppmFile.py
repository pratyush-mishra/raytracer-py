
import os

# The format of a PPM file (Portable Pixel Map) is like - 
# P3
# <width of image> <height of image>
# 255 (for max colour)
# rgb triplets

#Image

image_width:int = 255
image_height:int = 255

#Render
with open('hello_world.ppm', 'w') as f:
    f.write("P3\n{image_width} {image_height}\n255\n".format(image_width=image_width, image_height=image_height))

    for j in range(image_height):
        for i in range(image_width):
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0.0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            f.write("{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib))