from fractions import Fraction

class Row:
    def __init__(self, data):
        self.DATA = data
        self.all_zero = False # default value, updated if necessary when pivot pos is updated
        self.pivot_pos = len(self.DATA) # default value, updated immediately
        self.update_pivot_pos()

    def update_pivot_pos(self):
        """ Update and return pivot position """

        # find the first nonzero value in row
        i = 0
        while i < len(self.DATA) and self.DATA[i] == 0:
            i += 1

        # if i is less than len(data) there is a pivot; otherwise, the row is all zero
        if i < len(self.DATA):
            self.pivot_pos = i
        else:
            self.pivot_pos = len(self.DATA)
            self.all_zero = True

        return self.pivot_pos

    def reduce(self):
        """ Reduce values so the leading coefficient is 1 """

        # if all zeros, there is no leading coefficient so simply return
        if self.all_zero:
            return

        # get value of leading coefficient
        v = self.DATA[self.pivot_pos]

        # loop through self.DATA and put each entry over the denominator v
        self.DATA = [Fraction(x, v) for x in self.DATA]

        return

    def print_row(self, value_length, spacing=3):
        """ print row according to the given value_length and spacing arguments """

        # loop through the list of values
        for v in self.DATA:
            # print v with no linebreak or spaces
            print(v, end='')
            # calculate num spaces for this column break
            num_spaces = spacing + value_length - len(str(v))
            # print spaces with no linebreaks
            for _ in range(num_spaces):
                print(" ", end='')

        # line break for end of row
        print()

    def max_value_length(self):
        value_lengths = [len(str(d)) for d in self.DATA]
        return max(value_lengths)

    
    #* GETTERS
    def get_pivot_pos(self):
        return self.pivot_pos
    def get_all_zero(self):
        return self.all_zero
    def get_length(self):
        return len(self.DATA)
    def get_data(self):
        return self.DATA
    def get_value(self, index):
        return self.DATA[index]

    #* SETTERS
    def set_value(self, index, value):
        self.DATA[index] = value
        return