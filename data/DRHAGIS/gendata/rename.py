#: I.D.
#: Rename data from: original/ to successive positive integers.

import os
import sys
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    originalDatasetSourcePath = curPath+"/../original/source/"
    originalDatasetTargetPath = curPath+"/../original/targetVessels/"

    newSourcePathTrain = curPath+"/../source/"+width+"x"+height+"/train/"
    newSourcePathTest = curPath+"/../source/"+width+"x"+height+"/test/"

    newTargetPathTrain = curPath+"/../targetVessels/"+width+"x"+height+"/train/"
    newTargetPathTest = curPath+"/../targetVessels/"+width+"x"+height+"/test/"

    for originalPath, trainPath, testPath in [(originalDatasetSourcePath,newSourcePathTrain,newSourcePathTest), (originalDatasetTargetPath,newTargetPathTrain,newTargetPathTest)]:
        for image in os.listdir(originalPath):
            name, ext = image.split(".")
            ext = "."+ext.lower()
            if "_" in name:
                nb, _, _ = name.split("_")
            else:
                nb = name
            newName = str(nb)+ext
            if int(nb) <= 8:
                subprocess.run(["cp", originalPath+image, testPath+newName])
            else:
                subprocess.run(["cp", originalPath+image, trainPath+newName])

if __name__ == '__main__':
    main(sys.argv)
