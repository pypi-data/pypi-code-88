from random import randint
from time import time
import numpy as np
import matplotlib.pyplot as plt

class TimeTest:
    """This class serves as time testing method for a set of functions that
    iterate over a numerical ('int', 'float') array. Said array can either be
    specified or randomly generated. Since some functions might mutate its
    structure, the 'list' data type is preferred for usage.
    """
    def __init__(self, *functions, data: list = []):
        self.Data = self.dataCheck(data)
        
        # ITM required due to position mixing if 'set(...)' is used instead.
        self.Functions = []
        for function in functions:
            self.Functions.append(function) if function not in self.Functions else None
        
        self.Averages = {function: 0 for function in functions}
        self.LTStatistics = {function: [] for function in self.Functions}

    def tester(
            self,
            maxlen = 1000,
            iterations = 1000,
            minval = -100000,
            maxval = 100000,
            verbose = False
        ):
        """Tests the execution time for each function over an increasing array.

        Arguments:
        ----------
        - 'maxlen': the maximum allowed length of the array (if any default
        array is provided, this is set to the length of said array).
        - 'iterations': the amount of iterations performed over the array.
        - 'minval': minimum randomly generated value for the array (if no
        default one is specified).
        - 'maxval': maximum randomly generated value for the array (if no
        default one is specified).
        - 'verbose': determines whether or not a textual representation of the
        iteration process should be displayed or not.
        """
        # Variable definition:
        size, self.Sizes = (len(self.Data), [len(self.Data) for slot in range(iterations)]) if self.DefaultData else (0, [])
        array = self.Data

        # Main iteration cycle (iterations + generated array size increment):
        for iteration_cycle in range(iterations):
            if not self.DefaultData:
                size += int(maxlen / iterations)
                self.Sizes.append(size)
                array = [randint(minval, maxval) for element in range(size)]

            # Short-Term Statistics data collection:
            STStatistics = {function: 0 for function in self.Functions}

            # Execution of each function over given array:
            for function in self.Functions:
                tstart = time()
                function(array)
                tend = time()
                
                STStatistics[function] = tend - tstart
                self.LTStatistics[function].append(tend - tstart)

            # Short-Term Statistics display:
            if verbose:
                strOut = f'Short-Term Statistics for iteration cycle {iteration_cycle + 1} of {iterations}: '.ljust(80, '-') + '\n' + f' Array size: {size}'.rjust(80, '-') + '\n'
                for function in STStatistics:
                    strOut += f"\tTime: {format(STStatistics[function], '.8f')}s\tFunction: {function.__name__}\n"
                print(strOut)

        # Averages (average for each function) data treatment:
        for function in self.Functions:
            self.Averages[function] = sum(self.LTStatistics[function]) / len(self.LTStatistics[function])

        # Averages display:
        if verbose:
            strOut = f'Long-Term Statistics for total {iterations} cycles: '.ljust(80, '-') + '\n' + f' Maximum array size: {size}'.rjust(80, '-') + '\n'
            for function in self.LTStatistics:
                strOut += f"\tAverage: {format(self.Averages[function], '.8f')}s\tFunction: {function.__name__}\n"
            print(strOut)

    def performance(self, function1, function2, verbose = False):
        """Represents a performance comparison between two functions. A 2-tuple
        is returned, containing the performance of function 1 over function 2
        and vice versa.
        """
        if function1 not in self.Averages:
            print(f'[Comparison Error] Function {function1} has not been defined yet.',)
            return
        elif function2 not in self.Averages:
            print(f'[Comparison Error] Function {function2} has not been defined yet.')
            return
        elif self.Averages[function1] == 0:
            print(f'[Comparison Error] Function {function1} has not been tested yet.')
            return
        elif self.Averages[function2] == 0:
            print(f'[Comparison Error] Function {function2} has not been tested yet.')
            return

        f1overf2 = 1 / (self.Averages[function1] / self.Averages[function2])
        f2overf1 = 1 / (self.Averages[function2] / self.Averages[function1])

        if verbose:
            print('Performance comparison: '.ljust(80, '-') + '\n' +\
                  f"\tperformance({function1.__name__}) = {format(f1overf2, '.5f')} * performance({function2.__name__})\n" +\
                  f"\tperformance({function2.__name__}) = {format(f2overf1, '.5f')} * performance({function1.__name__})\n")

        return f1overf2, f2overf1

    def compare(self, *functions):
        """Graphically displays each function's tested data.

        If any number of functions is provided, they are compared, yet if no
        functions are provided, all functions contained in the instance are
        compared.
        """
        functions = self.Functions if len(functions) == 0 else functions
        validFunctions = []
        for function in functions:
            if function not in self.LTStatistics:
                print(f'[Comparison Error] Function {function} has not been defined yet.',)
            elif self.LTStatistics[function] == []:
                print(f'[Comparison Error] Function {function} has not been tested yet.')
            else:
                validFunctions.append(function)

        xAxis = self.Sizes
        for function in validFunctions:
            yAxis = self.LTStatistics[function]
            plt.plot(xAxis, yAxis)
        plt.title(f"{' vs. '.join([function.__name__ for function in validFunctions])}")
        plt.xlabel('Array size')
        plt.ylabel('Time')
        plt.show()

    def addFunction(self, function):
        """Adds a function to the instance."""
        if function not in self.Functions:
            self.Functions.append(function)
            self.Averages[function] = 0
            self.LTStatistics[function] = []

    def removeFunction(self, function):
        """Removes a function from the instance."""
        self.Functions.remove(function)
        del self.Averages[function]
        del self.LTStatistics[function]

    def dataCheck(self, data):
        """Checks if provided data array meets specified requirements."""
        self.DefaultData = False if len(data) == 0 else True
        for item in data:
            if type(item) not in [int, float]:
                print("The provided data array can only contain 'int' or 'float' objects.\nSwitching to random generation array.")
                self.DefaultData = False
                data.clear()
        return data

    def __repr__(self):
        return f"'TimeTest' object with functions {', '.join([str(function) for function in self.Functions])}."
