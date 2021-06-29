import math, cmath, re, argparse

class QuadraticError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'QuadraticError: {} are not real & real_roots is True'.format(self.message)
        else:
            return 'QuadraticError has been raised'


class QuadRoots(object):
    # object goes into *args below
    def __init__(self, *args):
        self.root1 = None
        self.root2 = None
        self.abc = None
        self.real_roots = None

    def io(self):
        """ Provide a way to take in and parse user input for the three different
        coefficients of a quadratic equation, a,b, and c. Also, allow user to specify
        whether or not the roots are real or imaginary so that determining the results
        can be simplified.

        Args:
            N/A
        Returns:
            N/A
        Raises:
            N/A
        """

        parser = argparse.ArgumentParser(description='quad. eq inputs')

        parser.add_argument('floats', type=float, help='3 numbers', nargs=3)
        parser.add_argument('real_roots', type=str, help='roots real True/False?',nargs=1)

        args = parser.parse_args()
        self.abc = args.floats

        self.real_roots = args.real_roots

        if self.real_roots[0].upper() == 'TRUE' or self.real_roots[0].upper() == 'T':
            self.real_roots = True
        else:
            self.real_roots = False

    def solve(self):
        """ Provide a way to take in and parse user input for the three different
        coefficients of a quadratic equation, a,b, and c. Also, allow user to specify
        whether or not the roots are real or imaginary so that determining the results
        can be simplified.

        Args:
            N/A
        Returns:
            :obj:`tuple`: list of 2 roots of the quadratic equation, either real or complex
        Raises:
            :obj:`ValueError`: if `a` is 0
            :obj:`QuadraticError`: if 'real_roots' is true, yet the actual roots are complex
        """

        # ax^2 + bx + c = 0

        a, b, c = self.abc[0], self.abc[1], self.abc[2]

        if a == 0:
            raise ValueError('a must be non-zero')

        if self.real_roots==False:

            self.root1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            self.root2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

            r1 = str(self.root1)
            r2 = str(self.root2)

            if re.findall("0j", r1) or re.findall("0j", r2):
                print('real_roots == False but roots are not imaginary')
                return ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),\
                        (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

            return (r1, r1)

        elif self.real_roots==True:
            self.root1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            self.root2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            r1 = str(self.root1)
            r2 = str(self.root2)

            if re.findall("0j", r1) or re.findall("0j", r2):
                return ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),\
                        (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))

            if isinstance(self.root1, complex) and isinstance(self.root2, complex):
                raise QuadraticError(self.root1, self.root2)

            else:

                return (self.root1, self.root2)

        return (self.root1, self.root2)


if __name__ == "__main__":
    qr = QuadRoots()
    qr.io()
    print(qr.solve())

