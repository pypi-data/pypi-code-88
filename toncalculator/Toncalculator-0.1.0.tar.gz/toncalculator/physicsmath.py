from math import cos, radians, sqrt

# Motion


def speed(s, t):
    return s/t


def velocity(s=None, t=None, a=None, u=None):
    if s != None and t != None:
        return s/t
    elif u != None and a != None and t != None:
        return u+a*t
    elif a != None and u != None and s != None:
        return sqrt(u**2+2*a*s)
    elif u != None and a != None and t != None:
        return u+1/2*a*t


def acceleration(v=None, u=None, t=None, s=None):
    if v != None and u != None and t != None:
        if v > u:
            return (v-u)/t
        elif u > v:
            return (u-v)/t
    elif u != None and v != None and s != None:
        return (u**2+v**2)/2*s


class Laws_Of_Falling_Bodies:
    def __init__(self, v=None, u=None, t=None, h=None):
        self.v = v
        self.u = u
        self.t = t
        self.h = h
        self.g = 9.806

    def velocity(self):
        if self.t != None:
            return self.u+self.g*self.t
        elif self.u != None and self.h != None:
            return sqrt(self.u**2+2*self.g*self.h)

    def height(self):
        if self.u != None and self.t != None:
            return self.u*self.t + 1/2*self.g*self.t**2
        elif self.v != None and self.u != None:
            return (self.u**2+self.v**2)/2*self.g
        elif self.u == 0 and self.v:
            return (self.v**2)/2*self.g
        elif self.v == 0 and self.u:
            return (self.u**2)/2*self.g

# Force


def monentum(m, v):
    return m*v


def force(m, a):
    return m*a

# Work, Power and Energy


def work(F=None, s=None, x=None, thita=None):
    if F != None and s != None:
        return F*s
    elif F != None and x != None and thita != None:
        return F*x*cos(radians(thita))


def kinatienargy(m, v):
    return 1/2*m*v**2


def power(W, t):
    return W/t


def pressure(F, A):
    return F/A
