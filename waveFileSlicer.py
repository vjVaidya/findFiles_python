__author__ = 'vaidvj'
""" To slice waveFiles which are greater than 10seconds long """
""" Input : 'topWavDir', name of the directory to be searched """

import os
""""import a method to find the file and then slice a single file"""

class wavFileSlicer():

    def process(self):
        topWavDirName = "wavFiles"
        topWavDir = os.path.join(os.path.dirname(__file__), topWavDirName)
        """ find .wav Files in the given directory """
        wavFileLabels, wavClassLabels = wavFileFinder.findWavFileRecursive(self, topWavDir)
        print (len(wavFileLabels))
        for currWaveFileNumber, currWavFile in enumerate(wavFileLabels):
            # split the file name
			filenameParts = currWavFile.split(".")
            # rename the file
			filenameParts[0] = filenameParts[0] + "_new"
            outWavFile = ".".join(filenameParts)
            """ the slicewaveFile will slice the file with respect to the inputs in 
			the command below where the time is usually denoted in milliseconds 
			meaning start time is 10ms and end time is 10 secs """
			sliceWavFile.slice(currWavFile, outWavFile, 10, 10000 )

        pass


if __name__ == "__main__":
    c = wavFileSlicer()
    c.process()



