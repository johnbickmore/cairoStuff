#!/users/jgrey/anaconda/bin/python

import sys
import time
import math
import cairo
import draw_routines

#constants
N = 12
X = pow(2,N)
Y = pow(2,N)
imgPath = "./imgs/"
imgName = "initialTest"
currentTime = time.gmtime()
#format the name of the image to be saved thusly:
saveString = "%s%s_%s-%s-%s_%s-%s.png" % (imgPath,
                                          imgName,
                                          currentTime.tm_min,
                                          currentTime.tm_hour,
                                          currentTime.tm_mday,
                                          currentTime.tm_mon,
                                          currentTime.tm_year)

#get the type of drawing to do from the command line argument:
if len(sys.argv) > 1:
    drawRoutineName = sys.argv[1]
else:
    drawRoutineName = "circles"

#setup
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, X,Y)
ctx = cairo.Context(surface)
ctx.scale(X,Y)
    
#Drawing:
draw_routines.draw(ctx,drawRoutineName)
    
#write to file:
print('Saving')
surface.write_to_png (saveString)
