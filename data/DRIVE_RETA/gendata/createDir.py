#: I.D.
#: Create folders and subfolders to store custom data that will be generated from: original/

import os
import sys
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    source = curPath+"/../source/"
    targetVessels = curPath+"/../targetVessels/"
    targetVeins = curPath+"/../targetVeins/"
    targetArteries = curPath+"/../targetArteries/"
    size = width+"x"+height+"/"
    test = "test/"
    train = "train/"

    subprocess.run(["mkdir", "-p", source+size+train])
    subprocess.run(["mkdir", "-p", source+size+test])
    
    subprocess.run(["mkdir", "-p", targetVessels+size+train])
    subprocess.run(["mkdir", "-p", targetVessels+size+test])

    # subprocess.run(["mkdir", "-p", targetVeins+size+train])
    # subprocess.run(["mkdir", "-p", targetVeins+size+test])

    # subprocess.run(["mkdir", "-p", targetArteries+size+train])
    # subprocess.run(["mkdir", "-p", targetArteries+size+test])

if __name__ == '__main__':
    main(sys.argv)
