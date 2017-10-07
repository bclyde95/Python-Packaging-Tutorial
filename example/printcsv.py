""" Prints the contents of a csv """

import csv

class Prints():
    """ Reads and prints a csv file """
    def __init__(self, csvfile):
        """ opens, reads, and stores the contents of a csv file """
        self.data = []
        self.csvfile = csvfile
        infile = open(csvfile, 'r')
        reader = csv.reader(infile)
        for row in reader:
            self.data.append((row[0], row[1]))

        infile.close()

    def printpairs(self):
        """ prints tuples of the data """
        for data in self.data:
            print(data)
