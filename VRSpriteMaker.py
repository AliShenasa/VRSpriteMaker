#!/usr/bin/env python
# coding: utf-8

import argparse
from PIL import Image, ImageDraw

def create_parser():
    """Creates the parser object 

    Returns:
        args: object storing all of the arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--spatialperiod', '--sp', '-p',
                        type=int, action='store',
                        help='number of stripes')
    parser.add_argument('--resolution','-r',
                        type=str, action='store',
                        help='resolution of sprite')
    parser.add_argument('--stripecolor','-s',
                        default="0,0,255",
                        type=str, action='store',
                        help='rgb of the strip')
    parser.add_argument('--bgcolor','-b',
                        default="50,50,50",
                        type=str, action='store',
                        help='rgb of the background')
    parser.add_argument('--outfile','-o',
                        type=str, action='store',
                        help='file to save image to')

    return parser.parse_args()


def create_image(spatial_period=60, 
                 width=400, height=300,  
                 stripe_color=(0,0,255), 
                 bg_color=(50,50,50)):
    """Creates an image with alternating stripes

    Args:
        spatial_period (int, optional): Amount of 360 view a light and dark stripe occupy. Defaults to 60. 
        width (int, optional): Width of image. Defaults to 400.
        height (int, optional): Height of image. Defaults to 300.
        stripe_color (tuple, optional): Color of light stripe. Defaults to (0,0,255).
        bg_color (tuple, optional): Color of dark stripe. Defaults to (50,50,50).

    Returns:
        ~PIL.Image.Image: image
    """

    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    stripe_count = int(360/spatial_period)
    stripe_width = int(spatial_period/2 * (width/360))

    for i in range(0, stripe_count):
        draw.rectangle([(i*width/stripe_count, 0),
                        (i*width/stripe_count+stripe_width, height)],
                        fill=stripe_color)
    return img

if __name__ == "__main__":

    # Create parser
    args = create_parser()

    # Read in arguments
    spatial_period = args.spatialperiod
    resolution = args.resolution.split(',')
    width = int(resolution[0])
    height = int(resolution[1])
    stripe_color = tuple([int(item) for item in args.stripecolor.split(',')])
    bg_color = tuple([int(item) for item in args.bgcolor.split(',')])
    outfile = args.outfile if args.outfile is not None else "sprite.png"

    # Create image
    img = create_image(spatial_period, width, height, stripe_color, bg_color)
    img.save(outfile)
