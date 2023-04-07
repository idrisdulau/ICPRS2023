#: I.D.
#: normalize the groundtruth for veins and arteries subsets

import os
import sys
import cv2
import numpy
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()

    targetVeinsPathTest = curPath+"/../targetVeins/"+width+"x"+height+"/test/"
    targetVeinsPathTrain = curPath+"/../targetVeins/"+width+"x"+height+"/train/"  

    targetArteriesPathTest = curPath+"/../targetArteries/"+width+"x"+height+"/test/"
    targetArteriesPathTrain = curPath+"/../targetArteries/"+width+"x"+height+"/train/"  

    newExt = ".tif"

    for path in [targetVeinsPathTest, targetVeinsPathTrain]:
        for item in os.listdir(path):
            name, oldExt = item.split(".")
            if oldExt == "png":
                output = cv2.imread(path+item, cv2.IMREAD_UNCHANGED)  
                blue, green, red = cv2.split(output)
                output = blue
                output = numpy.where(output==0, numpy.zeros(output.shape), numpy.ones(output.shape)*255)
                output = output.astype(numpy.uint8)   
                cv2.imwrite(path+name+newExt, output)
                subprocess.run(["rm", path+item])

    for path in [targetArteriesPathTest, targetArteriesPathTrain]:
        for item in os.listdir(path):
            name, oldExt = item.split(".")
            if oldExt == "png":
                output = cv2.imread(path+item, cv2.IMREAD_UNCHANGED)  
                blue, green, red = cv2.split(output)
                output = red
                output = numpy.where(output==0, numpy.zeros(output.shape), numpy.ones(output.shape)*255)
                output = output.astype(numpy.uint8)   
                cv2.imwrite(path+name+newExt, output)
                subprocess.run(["rm", path+item])

if __name__ == '__main__':
    main(sys.argv)
