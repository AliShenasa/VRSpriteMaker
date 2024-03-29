# VRSpriteMaker

VRSpriteMaker will produce a png to use as a sprite for Unity VR project.
You can run it from a python file or a python notebook

## Setup

Setup anaconda environment:

```conda create -n VRSpriteMaker python=3```

```conda activate VRSpriteMaker```

```pip install Pillow```

### VRSpriteMaker.py setup
Input parameters using flags:

--spatialperiod OR --sp or -p to specify the spatialperiod. Default: 60

--resolution OR -r to specify the resolution. Default: 400, 300

--stripecolor OR -s to specify the color of the stripe in rgb. Default: 0,0,255 aka blue

--backgroundcolor OR -b to specify the color of the background in rgb. Default: 50,50,50 aka gray

--outfile OR -o to specify the filename to save the image as. Default: sprite.png
Include the filename extension so the script knows what format to save the image in.

Program will output a png in the directory it was run in.

Example usage:

```python VRSpriteMaker.py --sp 60 -r 400,300 -s 0,0,255 -b 50,50,50 -o sprite_60deg.png```

### VRSpriteMaker.ipynb setup
Open jupyter notebook:

```jupyter notebook```

There you can modify the parameters and run the file to produce a png.
