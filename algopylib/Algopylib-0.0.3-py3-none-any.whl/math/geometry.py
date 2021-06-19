import math

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        Finds distance between two given points

        Parameters:
                x1, y1 : The x and y coordinates of first point
                x2, y2 : The x and y coordinates of second point

        Returns:
                Distance upto two decimal places.
        """
        distance = math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )
        return round(distance,2)


def is_collinear(x1: float, y1: float , x2: float, y2: float, x3: float, y3: float) -> bool:
        """
        Finds whether given three points are collinear.

        Parameters:
                x1, y1 : The x and y coordinates of first point
                x2, y2 : The x and y coordinates of second point
                x3, y3 : The x and y coordinates of third point

        Returns:
                True if the points are collinear, otherwise False
        """
        a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if a==0:
                return True
        else:
                return False


def eqn_of_line(x1: float, y1: float, x2: float, y2: float) -> str:
        """
        Finds equation of a line passing through two given points.

        Parameters:
                x1, y1 : The x and y coordinates of first point
                x2, y2 : The x and y coordinates of second point

        Returns:
                Equation of the line as a string.
        """
        a = y2 - y1
        b = x1 - x2
        c = a*(x1) + b*(y1)

        if b<0:
                s=( f"{a}x - {abs(b)}y = {c}")
        else:
                s=( f"{a}x  + {b}y = {c}")
        return s

def is_inside_circle(circle_x: float, circle_y: float, rad: float, x: float, y: float) -> bool:
        """
        Finds if a given point lies on or inside the circle, or outside the circle.

        Parameters:
                circle_x, circle_y : Coordinates of center of circle
                rad: radius of circle
                x, y : Coordinates of test point

        Returns:
                True if the point lies on or inside the circle, False if outside the circle.
        """
        d = (x - circle_x) * (x - circle_x) +(y - circle_y) * (y - circle_y) 
        if d<= rad*rad:
                return True
        else:
                return False
                

def area_triangle(side1: float, side2: float, side3: float) -> float:
        """
        Calculates area of triangle using Heron's Formula when the length of 3 sides are known.
        
        Parameters:
                side1, side2, side3 : Lengths of three sides of the triangle.
        
        Returns:
                Area of the triangle upto two decimal values.
        """
        if side1 < 0 or side2 < 0 or side3 < 0:
                raise ValueError("Length of side can only be a non-negative value")

        elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
                raise ValueError("Given three sides do not form a triangle")

        semi_per = (side1 + side2 + side3) / 2
        area = math.sqrt((semi_per) * (semi_per - side1) * (semi_per - side2) * (semi_per - side3) )
        return round(area , 2)

