__author__ = 'im_g'

import pickle
import numpy as np


pkl_file = open('featMat.pkl', 'rb')
featMat = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('X.pkl', 'rb')
X = pickle.load(pkl_file)
pkl_file.close()

