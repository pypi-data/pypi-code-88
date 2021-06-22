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

class CoefficientMatrix:
    def __init__(self, data):
        self.ROWS = [Row(d) for d in data]
        self.NUM_ROWS = len(data)
        self.NUM_COLS = len(data[0]) # assuming all rows same length (todo exception handling)

    def ref(self):
        """ Perform row ops to convert matrix to row-echelon form """

        # sort rows by pivot position
        self._sort_rows()

        # loop through rows until last row is reached or next row does not have valid pivot position
        current_row = 0
        while current_row < self.NUM_ROWS - 1 and self.ROWS[current_row].update_pivot_pos() < self.NUM_COLS:
            # call zeros below on current row
            self._zeros_below(current_row)
            # sort rows by pivot position
            self._sort_rows()
            # increment current row
            current_row += 1

        # update pivot position of last row
        self.ROWS[self.NUM_ROWS-1].update_pivot_pos()

        return

    def rref(self):
        """ Perform row ops to convert matrix to reduced row-echelon form """

        # first get to row-echelon form
        self.ref()

        # starting with the last row, loop backward to find the last row that is not all zeros
        current_row = self.NUM_ROWS - 1
        while self.ROWS[current_row].get_all_zero():
            current_row -= 1

        # for current_row --> 1 (incl.): zeros above
        while current_row > 0:
            #todo reduce current_row so leading coefficient is 1
            self.ROWS[current_row].reduce()
            # zeros above
            self._zeros_above(current_row)
            # decrement current_row
            current_row -= 1

        #todo reduce row 0 so leading coefficient is 1
        self.ROWS[0].reduce()

        return

    def _zeros_above(self, row_num):
        """ Perform row ops to get zeros above the leading coefficient of the given row number """

        # get the relevant pivot position and pivot value
        pivot_pos = self.ROWS[row_num].get_pivot_pos()
        pivot_value = self.ROWS[row_num].get_value(pivot_pos)

        # loop through the rows ABOVE row_num
        for i in range(row_num):
            # calculate the appropriate scalar
            # current_scalar = -1 * self.ROWS[i].get_value(pivot_pos) / pivot_value
            current_scalar = Fraction(-1 * self.ROWS[i].get_value(pivot_pos), pivot_value)
            # scale and replace scalar, row_num, i
            self._scale_and_replace(current_scalar, row_num, i)

        return

    def _zeros_below(self, row_num):
        """ hopefully this will replace _zeros_below. still in progress right now """

        # get the relevant pivot position and pivot value
        pivot_pos = self.ROWS[row_num].get_pivot_pos()
        pivot_value = self.ROWS[row_num].get_value(pivot_pos)

        # loop through the rows below row_num
        for i in range(row_num+1, self.NUM_ROWS):
            # calculate the appropriate scalar and store as a Fraction object
            current_scalar = Fraction(-1 * self.ROWS[i].get_value(pivot_pos), pivot_value)
            # scale and replace scalar, row_num, i
            self._scale_and_replace(current_scalar, row_num, i)

        return

    def _scale_and_replace(self, scalar, row_a, row_b):
        """ Add a scalar multiple of row_a to row_b. row_a does not change, row_b does change. """

        # loop through each column
        for i in range(self.NUM_COLS):
            # calculate new value of the current column of row_b
            v = scalar * self.ROWS[row_a].get_value(i) + self.ROWS[row_b].get_value(i)
            # set new value
            self.ROWS[row_b].set_value(i, v)

        return

    def _sort_rows(self):
        """
        sort rows by pivot_pos
        note: pivot_pos can be in range 0-->self.NUM_COLS (inclusive)
        """

        # first, update pivot_pos for each row
        for row in self.ROWS:
            row.update_pivot_pos()

        # insertion sort
        #todo use more efficient sorting algorithm (counting sort?)
        for i in range(1, self.NUM_ROWS):
            current_row = self.ROWS[i]
            current_row_pivot_pos = current_row.get_pivot_pos()
            j = i - 1
            while j >= 0 and self.ROWS[j].get_pivot_pos() > current_row_pivot_pos:
                self.ROWS[j+1] = self.ROWS[j]
                j -= 1
            self.ROWS[j+1] = current_row

        return

    def print_matrix(self):
        """ neatly format and print matrix so columns are even """

        # loop through rows to find the max value length
        max_val_length = 0
        for row in self.ROWS:
            r_max_length = row.max_value_length()
            if r_max_length > max_val_length:
                max_val_length = r_max_length

        # loop through rows to print
        for row in self.ROWS:
            row.print_row(max_val_length)


    #* GETTERS
    def get_num_rows(self):
        return self.NUM_ROWS
    def get_num_cols(self):
        return self.NUM_COLS
    def get_rows(self):
        return self.ROWS
    def get_row(self, r):
        return self.ROWS[r] #todo move this into a try block