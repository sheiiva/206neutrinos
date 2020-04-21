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


class Neutrinos():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self.tmp = 0
        # self.n = int(argv[1])
        # self.a = int(argv[2])
        # self.h = int(argv[3])
        # self.sd = int(argv[4])

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

        value = 0

        print("\tNumber of values:   {}".format(value))

    def computestdeviation(self):

        """
        Compute standard deviation and print the result.
        """

        value = 0
        print("\tStandard deviation: {:.2f}".format(value))

    def computeAmean(self):

        """
        Compute arithmetic mean and print the result.
        """

        value = 0
        print("\tArithmetic mean:    {:.2f}".format(value))

    def computerootsquare(self):

        """
        Compute Root mean square and print the result.
        """

        value = 0
        print("\tRoot mean square:   {:.2f}".format(value))

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
            self.computeAmean()
            self.computerootsquare()
            self.computeHmean()
            print()

        return 0