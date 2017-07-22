__author__ = 'vaidvj'

import os, time
from findFile import findFilesRecursive


class fileNameSplitter():
    def __init__(self):
        topWavDirName = "AFP8K"
        self.topWavDir = os.path.join(os.path.dirname(__file__), topWavDirName)

    def process(self, fileName):
        self.wavFileLabels, self.wavClassLabels = findFilesRecursive(self,self.topWavDir)
        for currWavfile, fileName in enumerate(self.wavFileLabels):
            # compute the Modulation Feature matrix
            print ("FileName", fileName)
            # new_name = os.path.splitext(os.path.basename(currWavfile))[0]
            newName = fileName.split("\\")[-1]
            newName1 = newName.split("-")[-3]

        pass

if __name__ == "__main__":
    c = fileNameSplitter()
    featureMatrix = c.process(fileName= "rollercoaster.wav")