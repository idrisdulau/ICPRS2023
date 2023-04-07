#: I.D.
#: Create folders and subfolders to store custom data that will be generated from: original/

import os
import sys
import subprocess

def main(argv):
    width, height = argv[1:3]

    curPath = os.getcwd()
    source = curPath+"/../source/"
    target = curPath+"/../targetVessels/"
    size = width+"x"+height+"/"
    test = "test/"
    train = "train/"

    subprocess.run(["mkdir", "-p", source+size+train])
    subprocess.run(["mkdir", "-p", source+size+test])
    
    subprocess.run(["mkdir", "-p", target+size+train])
    subprocess.run(["mkdir", "-p", target+size+test])

if __name__ == '__main__':
    main(sys.argv)
