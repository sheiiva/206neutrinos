############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#        Project : 206neutrinos_2019       #
#                                          #
############################################


from sys import argv
from math import sqrt
import statistics


class Neutrinos():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self.n = int(argv[1])
        self.a = int(argv[2])
        self.h = int(argv[3])
        self.sd = int(argv[4])

    def getValue(self):

        """
        Get input and look for interruption command.
        """

        try:
            ret = input("Enter next value: ")
            retint = int(ret)
        except OSError:
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

        self.n += 1
        
        print("\tNumber of values:   {}".format(self.n))

    def computestdeviation(self):

        """
        Compute standard deviation and print the result.
        """

        value = 0
        print("\tStandard deviation: {:.2f}".format(value))

    def computeAmean(self, value):

        """
        Compute arithmetic mean and print the result.
        """

        self.a = ((self.a * (self.n - 1)) + value) / self.n
        print("\tArithmetic mean:    {:.2f}".format(self.a))
        
    def computerootsquare(self, value):

        """
        Compute Root mean square and print the result.
        """

        tmp = (pow(self.sd, 2) + pow(self.a, 2)) * self.n
        square = sqrt(tmp + pow(value, 2)) / self.n
        print("\tRoot mean square:   {:.2f}".format(square))

    def computeHmean(self):

        """
        Compute Harmonic mean and print the result.
        """

        value = 0
        print("\tHarmonic mean:      {:.2f}".format(value))


    def run(self):

        """
        Run computations and process output printing.
        """

        while (1):
            value = self.getValue()
            self.computeValuesNbr()
            self.computestdeviation()
            self.computeAmean(value)
            self.computerootsquare(value)
            self.computeHmean()
            print()

        return 0
