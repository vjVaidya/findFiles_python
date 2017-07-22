__author__ = 'vjVaidya'
""" download a specific file/any number of files from a given url """

from urllib import request
import requests
from bs4 import BeautifulSoup
import time, os

class downloadFileFunc():
    def __init__(self):
        self.url_for_download = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
        self.url_for_searching = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
        self.noOfPages = 2

    def downloadFunc(self, url__for_storage):
        output = request.urlopen(url__for_storage) # use the link to store the output
        csvFile = output.read()#store the output in to a csv format
        csvFile_string = str(csvFile)# to make sure the data stored is in a string
        """ the extracted csvFile will contain data that is stored in a single line """
        lines = csvFile_string.split("\n")#to break the data and organize using the next line \n
        destination_url = r'dFile.csv' #rawstring using 'r' because we deal with file pass but in this case url's
        fx = open(destination_url, "w") # function to write data into a file
        fx.seek(0, 0)  #read the file from the beginning
        for line in lines: #loop through the string
            fx.write(line)
        fx.close() # close the file object
        return

    def crawlerFunc(self, url_for_searching, noOfPages):
        while noOfPages < 2:
            url_for_searching = url_for_searching + str(noOfPages)
            resultFile = requests.get(url_for_searching)
            textFromFile = source_code.text
            soup = BeautifulSoup(resultFile)

        return

    def process(self):
        self.downloadFunc(self.url_for_download)
        self.crawlerFunc(self.url_for_searching)
        return

if __name__ == "__main__":
    c = downloadFileFunc()
    c.process()