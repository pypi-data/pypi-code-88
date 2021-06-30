from .Distribution import Distribution


class General(Distribution):
    """ General distribution class for calculating mode and median

    Attributes:
            mode (float/int) representing the mode value of the distribution
            median (float/int/str) representing the standard deviation of the distribution
    """

    def __init__(self, mode, median):
        self.mode = mode
        self.median = median

    def mode(self):
        """Function to calculate the mode of the data set.

        Args: 
                None

        Returns: 
                float / int / string(no mode): mode of the data set

        """
        counts = dict()
        data_list = self.data

        for data in data_list:
            data = str(data)
            counts[data] = counts.get(data, 0) + 1

        mode = [int(k) for k, v in counts.items()
                if v == max(list(counts.values()))]

        if len(mode) == len(data_list):
            self.mode = "No mode found"
        else:
            self.mode = mode[0]

        return self.mode

    def median(self):
        """Function to calculate the median of the data set.

        Args: 
                None

        Returns: 
                float / int: median of the data set

        """
        data_list = self.data
        data_list.sort()

        if len(data_list) % 2 == 0:
            median_one = data_list[len(data_list)//2]
            median_two = data_list[len(data_list)//2 - 1]
            self.median = (median_one + median_two)/2
        else:
            self.median = data_list[len(data_list)//2]

        return self.median
