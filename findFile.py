__author__ = 'vaidvj'
""" function to find .txt files existing in the directory """

import os
import pandas as pd

class featureMatrix():
    def __init__(self):
        self.topWavDirName = "J_lists"
        self.topWavDir = os.path.join(os.path.dirname(__file__), self.topWavDirName)

# function to find a given type of file existing in the directory
    def findFilesRecursive(self,directory):
        fileLabels = []
        dir_id = []
        noDirsContainingFile = 0
        for dirpath, dirnames, files in os.walk(directory):
            foundFile = False
            for name in files:
                # check for last name ending in .File
                if name.lower().endswith(".txt"):
                    foundFile = True
                    # Save to results string instead of printing
                    fullFilePath = os.path.abspath(os.path.join(dirpath, name))
                    fileLabels .append(fullFilePath)
                    # classLabels.append(dirpath.split("\\")[-1]) # split the string:get folder and the file name

            if foundFile:
            # update the list of file names
                dir_id.append(noDirsContainingFile)
                noDirsContainingFile = noDirsContainingFile + 1
        #
        df = pd.DataFrame(fileLabels)
        df.to_csv('FilefileLabels.csv', index=True, header=True, sep=';')


        return fileLabels

    def process(self):
        self.FileLabels= self.findFilesRecursive(self.topWavDir)

        return self.FileLabels

if __name__ == "__main__":
    c = featureMatrix()
    c.process()