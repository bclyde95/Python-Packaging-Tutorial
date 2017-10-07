""" Command line tool """

import sys
#import printcsv from example package to access the printcsv function
from example import printcsv

def main():
    """
    Take in a csv file as input and use the example
    package to perform the printpairs function
    """
    if len(sys.argv) != 2:
        exit("usage: ./sample file.csv")
    prints = printcsv.Prints(sys.argv[1])
    prints.printpairs()
