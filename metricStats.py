import os
import cv2
import tqdm
import math
import numpy
import statistics

def metrics(pred,gt):
    with numpy.errstate(divide='ignore', invalid='ignore'):
        conf = pred/gt
        TP = numpy.sum(conf == 1).item()
        FP = numpy.sum(conf == float('inf')).item()
        TN = numpy.sum(numpy.isnan(conf)).item()
        FN = numpy.sum(conf == 0).item()
        assert TP+TN+FP+FN == 1024*1024
        DICE = 2*TP/(2*TP+FP+FN)
    return TP, DICE

def getCC(pred):
    numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(pred.astype(numpy.uint8), connectivity=8)
    sortedSequences = sorted([s[cv2.CC_STAT_AREA] for s in stats[1:]], reverse=True)
    lastRemove = numpy.copy(pred)
    lastRemove[labels == numpy.argmin(stats[1:, cv2.CC_STAT_AREA]) + 1] = 0
    THLD = sortedSequences[-1]/sortedSequences[0]
    return numLabels-1, THLD, lastRemove

def isMultipleCC(pred):
    numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(pred.astype(numpy.uint8), connectivity=8)
    return numLabels > 1
    
for DB in tqdm.tqdm(["CHASEDB1","DRHAGIS","DRIVE_RETA","HRF","IOSTAR","LESAV"]):
    for gpu in tqdm.tqdm(["0","1","2"]):
        predPath = os.getcwd()+"/pred/"+DB+"/"+gpu+"/"
        gtPath = os.getcwd()+"/data/"+DB+"/targetVessels/1024x1024/all/"

        print(DB,"- pred: "+gpu)

        stackPREDMetricsList = []
        stackCC1MetricsList = []
        stackDICEMetricsList = []

        for images in os.listdir(predPath):
            name,ext = images.split(".") 
            pred = cv2.imread(predPath+name+".png", cv2.IMREAD_UNCHANGED)
            gt = cv2.imread(gtPath+name+".tif", cv2.IMREAD_UNCHANGED)
            gt = numpy.where(gt==0, 0, 1)
            pred = numpy.where(pred==0, 0, 1)

            imageMetricsList = []
            while isMultipleCC(pred):
                TP, DICE = metrics(pred,gt)
                CC, THLD, pred = getCC(pred)
                imageMetricsList.append((TP, DICE, CC, THLD))

            stackPREDMetricsList.append((imageMetricsList[0][0], imageMetricsList[0][1], imageMetricsList[0][2], imageMetricsList[0][3]))
            stackCC1MetricsList.append((imageMetricsList[-1][0], imageMetricsList[-1][1], imageMetricsList[-1][2], imageMetricsList[-1][3]))

            # # Get the best threshold(CC & THLD) based on the best Dice (known data)
            for (TP,DICE,CC,THLD) in imageMetricsList:
                curTP, bestDICE, curCC, curTHLD = max(imageMetricsList, key=lambda x: x[1])
            stackDICEMetricsList.append((curTP, bestDICE, curCC, curTHLD))

            # Get the corresponding Dice based on a defined threshold (unknown data)
            # tmpTuple = filter(lambda x: x[3] >= 0.0103, imageMetricsList)
            # curTP, curDICE, curCC, maxTHLD = min(tmpTuple, key=lambda x: x[3])
            # stackDICEMetricsList.append((curTP, curDICE, curCC, maxTHLD))


        TPMeanPRED = round(statistics.mean([TP for TP,DICE,CC,THLD in stackPREDMetricsList]))
        DICEMeanPRED = round(statistics.mean([DICE for TP,DICE,CC,THLD in stackPREDMetricsList]),3)
        CCMeanPRED = round(statistics.mean([CC for TP,DICE,CC,THLD in stackPREDMetricsList]))
        THLDMeanPRED = round(statistics.mean([THLD for TP,DICE,CC,THLD in stackPREDMetricsList]),4)

        TPMeanDICE = round(statistics.mean([TP for TP,DICE,CC,THLD in stackDICEMetricsList]))
        DICEMeanDICE = round(statistics.mean([DICE for TP,DICE,CC,THLD in stackDICEMetricsList]),3)
        CCMeanDICE = round(statistics.mean([CC for TP,DICE,CC,THLD in stackDICEMetricsList]))
        THLDMeanDICE = round(statistics.mean([THLD for TP,DICE,CC,THLD in stackDICEMetricsList]),4)

        TPMeanCC1 = round(statistics.mean([TP for TP,DICE,CC,THLD in stackCC1MetricsList]))
        DICEMeanCC1 = round(statistics.mean([DICE for TP,DICE,CC,THLD in stackCC1MetricsList]),3)
        CCMeanCC1 = round(statistics.mean([CC for TP,DICE,CC,THLD in stackCC1MetricsList]))
        THLDMeanCC1 = round(statistics.mean([THLD for TP,DICE,CC,THLD in stackCC1MetricsList]),4)

        print("TP    | KB(%)| DICE  | CC | THLD ")
        print(TPMeanPRED,"|","100%","|",DICEMeanPRED,"|",CCMeanPRED,"|",THLDMeanPRED)
        print(TPMeanDICE,"| ",str(math.floor(100*(TPMeanDICE-TPMeanCC1)/(TPMeanPRED-TPMeanCC1)))+"%","|",DICEMeanDICE,"|",CCMeanDICE,"|",THLDMeanDICE)
        print(TPMeanCC1,"|","  0%","|",DICEMeanCC1,"| ",CCMeanCC1,"|",THLDMeanCC1)
        print()
