#: I.D.
#: Rename data from: original/ to successive positive integers.
#: Each image is stored as it follows, if name%3==0: hypertension, if name%3==1: diabetic retinopathy, if name%3==2: glaucoma

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

    originalTargetAVPath = curPath+"/../original/targetAV/"
    newTargetVeinsPathTrain = curPath+"/../targetVeins/"+width+"x"+height+"/train/"
    newTargetVeinsPathTest = curPath+"/../targetVeins/"+width+"x"+height+"/test/"
    newTargetArteriesPathTrain = curPath+"/../targetArteries/"+width+"x"+height+"/train/"
    newTargetArteriesPathTest = curPath+"/../targetArteries/"+width+"x"+height+"/test/"

    print("Following the rule: if name%3==0: hypertension, if name%3==1: diabetic retinopathy, if name%3==2: glaucoma")
    for originalPath, trainPath, testPath in [
    (originalSourcePath,newSourcePathTrain,newSourcePathTest), \
    (originalTargetVesselsPath,newTargetVesselsPathTrain,newTargetVesselsPathTest), \
    # (originalTargetAVPath,newTargetVeinsPathTrain,newTargetVeinsPathTest), \
    # (originalTargetAVPath,newTargetArteriesPathTrain,newTargetArteriesPathTest)
    ]:
        for image in os.listdir(originalPath):
            name, ext = image.split(".")
            ext = "."+ext.lower()
            if "AVmanual" in name:
                nb,pat,_ = name.split("_")
            else:
                nb,pat = name.split("_")
            if pat == "h":
                newNb = 3*int(nb)-0
            if pat == "g":
                newNb = 3*int(nb)-1
            if pat == "dr":
                newNb = 3*int(nb)-2
            newName = str(newNb)+ext
            if int(newNb) <= 9:
                subprocess.run(["cp", originalPath+image, testPath+newName])
                print("In /test/: ",nb, pat, "=>", newNb)
            else:
                subprocess.run(["cp", originalPath+image, trainPath+newName])

if __name__ == '__main__':
    main(sys.argv)
