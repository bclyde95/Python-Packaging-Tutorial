""" Acts as the interface between user and program """

import sys
from printcsv import Prints

def main():
    """ 
    Takes in a command line argument and uses the 
    Prints class to printpairs 
    """
    if len(sys.argv) != 2:
        exit("usage: ./sample file.csv")
    prints = Prints(sys.argv[1])
    prints.printpairs()

if __name__ == "__main__":
    main()
