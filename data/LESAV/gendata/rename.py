#: I.D.
#: Rename data from: original/ to positive integers

import os
import sys
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    originalSourcePath = curPath+"/../original/source/"
    newSourcePathTrain = curPath+"/../source/"+width+"x"+height+"/train/"
    newSourcePathTest = curPath+"/../source/"+width+"x"+height+"/test/"

    originalTargetVesselsPath = curPath+"/../original/targetVessels/"
    newTargetVesselsPathTrain = curPath+"/../targetVessels/"+width+"x"+height+"/train/"
    newTargetVesselsPathTest = curPath+"/../targetVessels/"+width+"x"+height+"/test/"

    # originalTargetVeinsPath = curPath+"/../original/targetVeins/"
    # newTargetVeinsPathTrain = curPath+"/../targetVeins/"+width+"x"+height+"/train/"
    # newTargetVeinsPathTest = curPath+"/../targetVeins/"+width+"x"+height+"/test/"

    # originalTargetArteriesPath = curPath+"/../original/targetArteries/"
    # newTargetArteriesPathTrain = curPath+"/../targetArteries/"+width+"x"+height+"/train/"
    # newTargetArteriesPathTest = curPath+"/../targetArteries/"+width+"x"+height+"/test/"

    for originalPath, trainPath, testPath in [
    (originalSourcePath,newSourcePathTrain,newSourcePathTest), \
    (originalTargetVesselsPath,newTargetVesselsPathTrain,newTargetVesselsPathTest), \
    # (originalTargetVeinsPath,newTargetVeinsPathTrain,newTargetVeinsPathTest), \
    # (originalTargetArteriesPath,newTargetArteriesPathTrain,newTargetArteriesPathTest)
    ]:
        for image in os.listdir(originalPath):
            name, ext = image.split(".")
            if int(name) <= 37:
                subprocess.run(["cp", originalPath+image, testPath+image])
            else:
                subprocess.run(["cp", originalPath+image, trainPath+image])

if __name__ == '__main__':
    main(sys.argv)
