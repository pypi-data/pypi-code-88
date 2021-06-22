
"""
Find the coordinates for verteces of a TF coil, in a 2D profile on the XZ plane
Run some checks for data validation
The main function find_points() takes 3 positional arguments for the TF coil parameters,
and takes two additional boolean arguments that are defaulted to False.
test argument set to True prints to console the list which it returns
line type argument sets the returned list to be populated by elements for MixedShape() function in the Paramak module
"""

from _pytest.python_api import raises


def find_points(lower_inner_coordinates,mid_point_coordinates,thickness,test=False,line_type=False):
    """

    lower_inner_coordinates must be a 2 element tuple
    mid_point_coordinates must be a 2 elemenet tuple
    thickness must be a float or an int
    test=True will print the returned coordinates to console
    line_type=True will return a 3 element tuple with line types for mixed shape paramak functions

    """

    ### Check if input values are what they meant to be ###
    if tup_check(lower_inner_coordinates) == False or tup_check(mid_point_coordinates) == False:
        raise TypeError("Invalid input - Coordinates must be a tuple")

    elif (thick_check(thickness)) == False:
        raise TypeError("Invalid input - Thickness must be a number")
        
    elif len(lower_inner_coordinates) != 2 or len(mid_point_coordinates) != 2:
        raise ValueError("The input tuples are too long or too short, they must be 2 element long")

    elif lower_inner_coordinates[0] > mid_point_coordinates[0]:
        raise ValueError("The middle point's x-coordinate must be larger than the lower inner point's x-coordinate")

    else:
        lower_x, lower_z = lower_inner_coordinates
        mid_x, mid_z = mid_point_coordinates

        ### redifine values to be floats to make it look consistent 
        lower_x,lower_z, mid_x, mid_z, thickness = float(lower_x),float(lower_z), float(mid_x),float(mid_z), float(thickness)

        ### Define differences to avoid miss claculation due to signs
        base_length = mid_x - lower_x
        height = abs(mid_z - lower_z) * 2
        
        ### 10 points/tuples are returned from the initial 2 coordinates and thickness value
        p1 = (lower_x,lower_z)
        p2 = (p1[0]+base_length,p1[1])
        p3 = (p2[0],p2[1]+height)
        p4 = (p1[0],p1[1]+height)
        p5 = (p4[0],p4[1]+thickness)
        p6 = (p3[0],p4[1]+thickness)
        p7 = (p3[0]+thickness,p3[1])
        p8 = (p2[0]+thickness,p2[1])
        p9 = (p2[0],p2[1]-thickness)
        p10 = (lower_x,lower_z-thickness)

        ### The inner curvature is scales as a function of the base length of the coil and its thickness as long as the thickness does not exceed the base length

        if thickness/base_length >= 1:
            # if the thickness/base length ratio is larger or equal to 1
            # it takes 10% of the thickness as the inner curve radius 
            # this to avoid having coordinates before the previous or at the same spot as Paramak cannot compute it
            inner_curve_radius = thickness*0.1
            outter_curve_radius = thickness*1.1
        else:
            outter_curve_radius = (1 + (thickness/base_length))*thickness
            inner_curve_radius = (thickness**2) / base_length 

        ### New subroutines to calculate inner and outter curve mid-points, x and y displacement from existing points
        # long shift does a sin(45)*radius of curvature amount of shift
        # short shift does a (1-sin(45))*radius of curvature amount of shift
        def shift_long(radius):
            """ 
            radius is the radius of curvature
            """
            return (2**0.5)*0.5*radius
            
        def shift_short(radius):
            """ 
            radius is the radius of curvature
            """
            return (2-(2**0.5))*0.5*radius
        

        p11 = (p2[0]-inner_curve_radius, p2[1])
        p12 = (p11[0]+shift_long(inner_curve_radius),p11[1]+shift_short(inner_curve_radius))
        p13 = (p2[0],p2[1]+inner_curve_radius)
        p14 = (p3[0],p3[1]-inner_curve_radius)
        p15 = (p14[0]-shift_short(inner_curve_radius),p14[1]+shift_long(inner_curve_radius))
        p16 = (p3[0]-inner_curve_radius, p3[1])
        p17 = (p6[0]-inner_curve_radius, p6[1])
        p18 = (p17[0]+shift_long(outter_curve_radius), p17[1]-shift_short(outter_curve_radius))
        p19 = (p14[0]+thickness,p14[1])
        p20 = (p8[0],p8[1]+inner_curve_radius)
        p21 = (p18[0], p20[1]-shift_long(outter_curve_radius))
        p22 = (p11[0], p11[1]-thickness)


        #print(inner_curve_radius,base_length,thickness,outter_curve_radius)
        ### List holding the points that are being returned by the function
        #points = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
        points = [p1,p11,p12,p13,p14,p15,p16,p4,p5,p17,p18,p19,p20,p21,p22,p10]
        tri_points = []
        lines = ["straight"] + ['circle']*2 + ['straight'] + ['circle']*2 + ['straight']*3 + ['circle']*2 + ['straight'] + ['circle']*2 + ['straight']*2

        for i in range(len(points)):
            tri_points.append(points[i] + (lines[i],))


        if test == True:
            print(points,'\n',tri_points)

        if line_type == True:   
            return tri_points
        elif line_type == False:
            return points

def tup_check(tup):
    check = type(tup) == tuple
    #print(check)
    return check

def thick_check(thickness):
    check = type(thickness) == float or type(thickness) == int
    #print(check)
    return check

find_points((50,0), (100,100), 20, test=True, line_type=True)