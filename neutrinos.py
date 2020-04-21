############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#        Project : 206neutrinos_2019       #
#                                          #
############################################

import numpy as np
from sys import argv
from math import sqrt
import statistics


class Neutrinos():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._n = int(argv[1])
        self._a = int(argv[2])
        self._h = int(argv[3])
        self._sd = int(argv[4])
        self._oldSd = 0
        self._oldA= 0
        self._square = 0

    def getValue(self):

        """
        Get input and look for interruption command.
        """

        try:
            ret = input("Enter next value: ")
            retint = int(ret)
        except KeyboardInterrupt:
            exit(0)
        except ValueError:
            if (ret == "END"):
                exit(0)
            else:
                print("Wrong value.")
                exit(84)
        else:
            return retint

    def computeValuesNbr(self):

        """
        Compute number of values and print the result.
        """

        self._n += 1
        
        print("\tNumber of values:   {}".format(self._n))


    def computestdeviation(self, inputNb):

        """
        Compute standard deviation and print the result.
        """

        self._oldSd = self._sd
        rootMeanSquare = ((self._sd**2) + (self._a**2)) * (self._n-1)
        self._sd = np.sqrt(
           (rootMeanSquare + (inputNb**2)) / self._n
           - ((((self._a * (self._n-1)) + inputNb) / self._n)**2)
        )

        print("\tStandard deviation: {:.2f}".format(self._sd))

    def computeAmean(self, value):

        """
        Compute arithmetic mean and print the result.
        """

        self._oldA = self._a
        self._a = ((self._a * (self._n - 1)) + value) / self._n

        print("\tArithmetic mean:    {:.2f}".format(self._a))
        
    def computerootsquare(self, value):

        """
        Compute Root mean square and print the result.
        """

        tmp = (pow(self._oldSd, 2) + pow(self._oldA, 2)) * (self._n - 1)
        self._square = sqrt((tmp + pow(value, 2)) / self._n)

        print("\tRoot mean square:   {:.2f}".format(self._square))

    def computeHmean(self, inputNb):

        """
        Compute Harmonic mean and print the result.
        """
        
        self._h = self._n /((1 / inputNb) + ((self._n - 1) / self._h))

        print("\tHarmonic mean:      {:.2f}".format(self._h))


    def run(self):

        """
        Run computations and process output printing.
        """

        while (1):
            value = self.getValue()
            self.computeValuesNbr()
            self.computestdeviation(value)
            self.computeAmean(value)
            self.computerootsquare(value)
            self.computeHmean(value)
            print()

        return 0
