#: I.D.
#: Resize data stored in source and target subfolders, normalize the groundtruth

import os
import sys
import cv2
import numpy
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    newSourcePathTrain = curPath+"/../source/"+width+"x"+height+"/train/"
    newSourcePathTest = curPath+"/../source/"+width+"x"+height+"/test/"

    newTargetPathTrain = curPath+"/../targetVessels/"+width+"x"+height+"/train/"
    newTargetPathTest = curPath+"/../targetVessels/"+width+"x"+height+"/test/"

    for path in [newSourcePathTrain, newSourcePathTest]:
        for item in os.listdir(path):
            img = cv2.imread(path+item, cv2.IMREAD_UNCHANGED)   
            output = cv2.resize(img, (int(width), int(height)))
            output = output.astype(numpy.uint8)   
            cv2.imwrite(path+item, output)

    for path in [newTargetPathTrain, newTargetPathTest]:
        for item in os.listdir(path):
            gt = cv2.imread(path+item, cv2.IMREAD_UNCHANGED)  
            output = cv2.resize(gt, (int(width), int(height)), cv2.INTER_LINEAR)
            output = numpy.where(output==0, numpy.zeros(output.shape), numpy.ones(output.shape)*255)
            output = output.astype(numpy.uint8)   
            cv2.imwrite(path+item, output)

if __name__ == '__main__':
    main(sys.argv)
