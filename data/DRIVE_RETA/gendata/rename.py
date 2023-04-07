#: I.D.
#: Rename data from: original/ to successive positive integers, following their files name

import os
import sys
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    originalSourcePath = curPath+"/../original/source/"
    newSourcePathTrain = curPath+"/../source/"+width+"x"+height+"/train/"
    newSourcePathTest = curPath+"/../source/"+width+"x"+height+"/test/"

    originalTargetAVPath = curPath+"/../original/targetAV/"
    newTargetVesselsPathTrain = curPath+"/../targetVessels/"+width+"x"+height+"/train/"
    newTargetVesselsPathTest = curPath+"/../targetVessels/"+width+"x"+height+"/test/"
    newTargetVeinsPathTrain = curPath+"/../targetVeins/"+width+"x"+height+"/train/"
    newTargetVeinsPathTest = curPath+"/../targetVeins/"+width+"x"+height+"/test/"
    newTargetArteriesPathTrain = curPath+"/../targetArteries/"+width+"x"+height+"/train/"
    newTargetArteriesPathTest = curPath+"/../targetArteries/"+width+"x"+height+"/test/"

    for originalPath, trainPath, testPath in [
    (originalSourcePath,newSourcePathTrain,newSourcePathTest), \
    (originalTargetAVPath,newTargetVesselsPathTrain,newTargetVesselsPathTest), \
    # (originalTargetAVPath,newTargetVeinsPathTrain,newTargetVeinsPathTest), \
    # (originalTargetAVPath,newTargetArteriesPathTrain,newTargetArteriesPathTest)
    ]:
        for image in os.listdir(originalPath):
            name, ext = image.split(".")
            ext = "."+ext.lower()
            if "vessel" in name:
                nb, _, _ = name.split("_")
            else:
                nb, _ = name.split("_")
            newName = nb+ext
            if int(nb) <= 8:
                subprocess.run(["cp", originalPath+image, testPath+newName])
                print("In /test/: ", nb)
            else:
                subprocess.run(["cp", originalPath+image, trainPath+newName])

if __name__ == '__main__':
    main(sys.argv)
