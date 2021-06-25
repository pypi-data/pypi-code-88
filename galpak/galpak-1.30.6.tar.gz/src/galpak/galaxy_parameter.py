# coding=utf-8


class GalaxyParameter(property):
    """
    A parameter of a galaxy model.
    This is deep voodoo. The base class of this (property) is a python trick to allow us to define
    custom accessors (fget) and mutators (fset) for each property created with it.
    We simply use it to fetch the corresponding value in the ndarray, by numerical index.
    This allows us named/documented/autocompleted access to the galaxy parameters, instead of
    accessing them only through the numerical index, numpy-like, which is boring/annoying to memorize.
    You still can access the data through numerical indices if you want.
    Win-win ! Except for the maintenance of the particular piece of code.

    - name (string) : a name, for access (MUST be the same as the name in `GalaxyParameters.names`.)
    - key (int) : the position in the the ndarray of this parameter
    - short (string) : a shorter name, for compact display
    - doc (string) : some documentation that will appear to the enduser.
    - unit (string) : the unit, if any
    - precision (string) : the precision to use during string casting, as used by `string.format()`.
    """
    def __init__(self, name, key, short=None, doc=None, unit=None, format='3.2f'):
        self.name = name
        self.key = key
        self.unit = unit
        self.format = format
        if unit is not None:
            doc += " (%s)" % unit
        if short is not None:
            self.short = short
        else:
            self.short = name

        super(GalaxyParameter, self).__init__(fget=lambda selfie: selfie[key],
                                              fset=lambda selfie, value: selfie.__setitem__(key, value),
                                              doc=doc)
        # The above doc= is insufficient to set the docstring?! This takes care of it.
        self.__doc__ = doc