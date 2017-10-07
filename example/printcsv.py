""" Prints the contents of a csv """

import csv
import sys

class Prints():
    """ Reads and prints a csv file """
    def __init__(self, csvfile):
        """ opens, reads, and stores the contents of a csv file """
        self.data = []
        self.csvfile = csvfile
        infile = open(csvfile, 'r')
        reader = csv.reader(infile)
        for r in reader:
            self.data.append((r[0], r[1]))

        infile.close()

    def printpairs(self):
        """ prints tuples of the data """
        for d in self.data:
            print(d)
