import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from PIL import Image


#size of the output png file
width=800
height=500

#magic numbers to adjust the aspectratio of the figure and the origin of the cropping
originX=161
originY=78
sizeX=12.88
sizeY=6.48
################

def Idp_to_png(inputfile,IntMax):

    z=np.genfromtxt(inputfile,delimiter=",")

    print("input file: %s"%(inputfile))
    print("The upper limit for the color plot (intensity map): %s"%(IntMax))

    fig=plt.figure(figsize=(sizeX,sizeY))
    ax=fig.add_subplot(111)
    mappable=ax.pcolor(z,cmap='jet',vmin=0,vmax=IntMax)
    fig.colorbar(mappable,ax=ax)
    ax.set_xlabel('d')
    ax.set_ylabel('p')

    outputfile=inputfile.replace('csv','png')

    fig.savefig(outputfile)
    print("output file: %s"%(outputfile))

    im = Image.open(outputfile)
    im_crop = im.crop((originX, originY, originX+width, originY+height))
    im_crop.save(outputfile)

if __name__=='__main__':
    if (len(sys.argv)==3):
        if(os.path.isfile(sys.argv[1])):
            if(sys.argv[2].isdigit()):
                Idp_to_png(sys.argv[1],sys.argv[2])
            else:
                print("usage: python Idp_plot.py [input csv filename] [intensity maximum]")                
                print("2nd argument must be a number.")                
        else:
            print("%s does not exist. "%(sys.argv[1]))
    else:
        print("usage: python Idp_plot.py [input csv filename] [intensity maximum]")