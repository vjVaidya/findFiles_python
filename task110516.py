__author__ = 'vaidvj'

import time, pickle, pandas as pd
import csv
from pylab import *
from scipy import *
from sklearn import datasets
import sklearn.cross_validation as cv
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
from sklearn.linear_model import SGDClassifier

class exploratoryAnalysis():
    def __init__(self):
        print ("Exploratory Data Analysis and Prediction Model")
    def readData(self, dataSet):
        self.dataSet = dataSet


    def process(self):
        reader = csv.reader(open("day", "rb"), delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row)

if __name__ == "__main__":

    c = exploratoryAnalysis()
    c.process()