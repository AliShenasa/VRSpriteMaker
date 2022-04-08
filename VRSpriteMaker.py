#!/usr/bin/env python
# coding: utf-8

from PIL import Image, ImageDraw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--stripecount','-n', type=int, action='store', help='number of stripes')
parser.add_argument('--resolution','-r', type=str, action='store', help='resolution of sprite')
parser.add_argument('--stripewidth','-w', type=int, action='store', help='width of stripe')
parser.add_argument('--stripecolor','-s', type=str, action='store', help='rgb of the strip')
parser.add_argument('--backgroundcolor','-b', type=str, action='store', help='rgb of the background')

args = parser.parse_args()

stripecount = (args.stripecount if args.stripecount != None else 5)
resolution = (args.resolution.split(',') if args.resolution != None else ["400","300"])
width = int(resolution[0])
height = int(resolution[1])

if(args.stripecolor != None):
    stripecolor = tuple([int(item) for item in args.stripecolor.split(',')])
else:
    stripecolor = (0,0,255) #blue

if(args.backgroundcolor != None):
    backgroundcolor = tuple([int(item) for item in args.backgroundcolor.split(',')])
else:
    backgroundcolor = (50,50,50) #gray

stripewidth = (args.stripewidth if args.stripewidth != None else 10)


img = Image.new('RGB', (width, height), color=backgroundcolor)
draw = ImageDraw.Draw(img)

for i in range(0, stripecount):
    draw.rectangle([(i*width/stripecount, 0),
                    (i*width/stripecount+stripewidth, height)],
                    fill=stripecolor)

img.save('sprite.png')