"""
Filter class and subclasses
"""
# Standard library modules
import math as m
import warnings
from scipy._lib.doccer import extend_notes_in_docstring

# Non-standard modules
# import obspy.core.inventory.response as obspy_response


class Filter(object):
    """
    Filter superclass
    """
    def __init__(self, type="PolesZeros", offset=0):
        """
        Constructor
        """
        self.type = type
        self.offset = offset
        
    @staticmethod
    def dynamic_class_constructor(attributes_dict, channel_modif={}, selected_config={}, stage_id="-1"):
        """
        Creates an appropriate Filter subclass from an attributes_dict
        stage_id is stage_name if it exists
        """
        
        if attributes_dict == None:
            raise TypeError("No attributes in filter")
        
        if "type" not in attributes_dict:
            raise TypeError('No "type" specified for filter in stage #{stage_id}')
        else:
            filter_type = attributes_dict.get_configured_element('type', 
                                                           channel_modif, 
                                                           selected_config, 
                                                           None)
            if filter_type == 'PolesZeros':
                obj = PolesZeros.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'FIR':
                obj = FIR.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'Coefficients':
                obj = Coefficients.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'ResponseList':
                obj = ResponseList.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'AD_CONVERSION':
                obj = AD_Conversion.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'ANALOG':
                obj = Analog.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            elif filter_type == 'DIGITAL':
                obj = Digital.dynamic_class_constructor(filter_type, attributes_dict, selected_config, stage_id)
            else:
                raise TypeError(f'Unknown Filter type: "{filter_type}" in stage #{stage_id}')
                
        return obj
    
        
class PolesZeros(Filter):
    """
    PolesZeros Filter
    """
    def __init__(self, filter_type, transfer_function_type='LAPLACE (RADIANS/SECOND)', 
                 poles=[], zeros=[],
                 normalization_frequency=1., 
                 normalization_factor=None,
                 offset=0,
                 stage_id=-1):
        """
        poles and zeros should be lists of complex numbers
        """
        if transfer_function_type not in ['LAPLACE (RADIANS/SECOND)','LAPLACE (HERTZ)','DIGITAL (Z-TRANSFORM)']:
            raise TypeError(f'Illegal transfer_function_type in PolesZeros: "{transfer_function_type}" in stage #{stage_id}')
            
        self.transfer_function_type = transfer_function_type
        self.poles = poles
        self.zeros = zeros
        
        self.normalization_frequency = normalization_frequency
        if normalization_frequency and normalization_factor:
            self.normalization_factor = normalization_factor
        elif filter_type != 'ANALOG':     #norm frequency doesn't make sense in analog      
            self.normalization_factor = self.calc_normalization_factor(stage_id)
        else:
            self.normalization_factor = 1.0

        super().__init__(filter_type, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create PolesZeros instance from an attributes_dict
        """
        obj = cls(filter_type,
                attributes_dict.get_configured_element('transfer_function_type', 
                                                  channel_modif, 
                                                  selected_config, 
                                                  'LAPLACE (RADIANS/SECOND)'),
                [(float(x[0]) + 1j*float(x[1])) for x in attributes_dict.get_configured_element('poles',
                                                         channel_modif, 
                                                         selected_config, 
                                                         [])],
                [(float(x[0]) + 1j*float(x[1])) for x in attributes_dict.get_configured_element('zeros',
                                                         channel_modif, 
                                                         selected_config,
                                                         [])],
                attributes_dict.get_configured_element('normalization_frequency', 
                                                 channel_modif, 
                                                 selected_config, 
                                                 1.),
                attributes_dict.get_configured_element('normalization_factor', 
                                                 channel_modif, 
                                                 selected_config, 
                                                 None),
                attributes_dict.get_configured_element('offset', 
                                                 channel_modif, 
                                                 selected_config,
                                                 0),
                stage_id
              )
        return obj

    def __repr__(self):
        """
        String representation of object
        """
        s = f'          PolesZeros(Poles={self.poles}, Zeros={self.zeros}, '
        s += f'Normalization Frequency={self.normalization_frequency:g}, '
        s += f'Normalization Factor={self.normalization_factor:g})'
        return s

    def calc_normalization_factor(self, stage_id=-1, debug=False):
        """
        Calculate the normalization factor for give poles-zeros

        The norm factor A0 is calculated such that
                           sequence_product_over_n(s - zero_n)
                A0 * abs(------------------------------------------) === 1
                           sequence_product_over_m(s - pole_m)
        for s_f=i*2pi*f if the transfer function is in radians
                i*f     if the transfer function is in Hertz
        """
        if not self.normalization_frequency:
            raise ValueError(f'No normalization frequency for PZ filter in stage #{stage_id}')

        A0 = 1.0 + (1j * 0.0)
        if self.transfer_function_type == "LAPLACE (HERTZ)":
            s = 1j * self.normalization_frequency
        elif self.transfer_function_type == "LAPLACE (RADIANS/SECOND)":
            s = 1j * 2 * m.pi * self.normalization_frequency
        else:
            print("Don't know how to calculate normalization factor "
                  "for z-transform poles and zeros!") #Warning msg
            return None
        for p in self.poles:
            A0 *= (s - p)
        for z in self.zeros:
            A0 /= (s - z)

        if debug:
            print("poles={}, zeros={}, s={:g}, A0={:g}".format(
                self.poles, self.zeros, s, A0))

        A0 = abs(A0)
        return A0


class FIR(Filter):
    """
    FIR Filter
    """
    def __init__(self, filter_type, symmetry, coefficients, coefficient_divisor, offset=0, stage_id=-1):
        
        self.symmetry = symmetry
        if symmetry not in ['ODD', 'EVEN', 'NONE']:
            raise TypeError(f'Illegal FIR symmetry: "{symmetry} in stage #{stage_id}"')
        
        #Validate coefficients
        sum_coeff = 0
        coeff_cnt = 0
        for coeff in coefficients:
            sum_coeff += coeff
            coeff_cnt += 1
        
        sum_coeff /= coefficient_divisor
        sum_coeff = round(sum_coeff, 2) #check up to two decimal places  
        if sum_coeff != 1 and sum_coeff != 0: #the last conditional means there is at least one coeff
            warnings.warn(f'Coefficient sum "{sum_coeff}" not equal to one, \
            num. coefficient: "{coeff_cnt}", in stage #{stage_id}')
        
        self.coefficients = coefficients
        self.coefficient_divisor = coefficient_divisor
        
        super().__init__(filter_type, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create FIR instance from an attributes_dict
        """
        
        offset = attributes_dict.get_configured_element('offset', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   0)
        if not offset:
            raise TypeError(f'No offset in FIR filter')
        
        obj = cls(filter_type,
                  attributes_dict.get_configured_element('symmetry', 
                                                   channel_modif, 
                                                   selected_config,
                                                   None), #Default will cause an error in init
                  attributes_dict.get_configured_element('coefficients', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   []),
                  attributes_dict.get_configured_element('coefficient_divisor', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   1.),
                  offset)
        
        return obj

    def __repr__(self):
        """
        String representation of object
        """
        s = f'          FIR("Symmetry={self.symmetry}",'
        s += f' Coefficients={self.coefficients}, Divisor={self.coefficient_divisor})'
        return s


class Coefficients(Filter):
    """
    Coefficients Filter
    """
    def __init__(self, filter_type, transfer_function_type, numerator_coefficients,
                 denominator_coefficients, offset=0):
        if transfer_function_type not in ["ANALOG (RADIANS/SECOND)",
                                          "ANALOG (HERTZ)",
                                          "DIGITAL"]:
            raise TypeError('Illegal transfer function type: "{transfer_function_type}" in stage #{stage_id}')

        self.transfer_function_type = transfer_function_type
        self.numerator_coefficients = numerator_coefficients
        self.denominator_coefficients = denominator_coefficients
        
        super().__init__(filter_type, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create Coefficients instance from an attributes_dict
        """
        obj = cls(filter_type, 
                  attributes_dict.get_configured_element('transfer_function_type', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   'DIGITAL'),
                  attributes_dict.get_configured_element('numerator_coefficients', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   []),
                  attributes_dict.get_configured_element('denominator_coefficients', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   []),
                  attributes_dict.get_configured_element('offset', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   0)
                  )
        return obj

    def __repr__(self):
        s = f'          Coefficients("Transfer Function Type={self.transfer_function_type}", '
        s += f'Numerator={self.numerator_coefficients}, '
        s += f'Denominator={self.denominator_coefficients})'
        return s


class ResponseList(Filter):
    """
    ResponseList Filter
    """
    def __init__(self, filter_type, response_list, offset=0):
        self.response_list = response_list
        
        super().__init__(filter_type, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create Response List instance from an attributes_dict
        """
        obj = cls(filter_type, 
                  attributes_dict.get_configured_element('elements', channel_modif, selected_config, []), 
                  attributes_dict.get_configured_element('offset', channel_modif, selected_config, 0))
        
        return obj

    def __repr__(self):
        return f'          ResponseList("{self.response_list}")'


class Analog(PolesZeros):
    """
    Analog Filter (Flat PolesZeros filter)
    """
    def __init__(self, filter_type, offset=0): 
        
        self.poles = []
        self.zeros = []
        self.normalization_frequency = 0.
        self.normalization_factor = None
        
        super().__init__(filter_type, "LAPLACE (RADIANS/SECOND)", 
                         self.poles, self.zeros, self.normalization_frequency, self.normalization_factor, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}):
        """
        Create Analog instance from an attributes_dict
        """
        obj = cls(filter_type, attributes_dict.get_configured_element('offset', 
                                                                channel_modif, 
                                                                selected_config, 
                                                                0))
        return obj

    def __repr__(self):
        return '          Analog()'


class Digital(Coefficients):
    """
    Digital Filter (Flat Coefficients filter)
    """
    def __init__(self, filter_type, offset=0):
        self.transfer_function_type = 'DIGITAL'
        self.numerator_coefficients = [1.0]
        self.denominator_coefficients = []

        super().__init__(filter_type, "DIGITAL", self.numerator_coefficients, self.denominator_coefficients, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create Digital instance from an attributes_dict
        """
        obj = cls(filter_type, attributes_dict.get_configured_element('offset', 
                                                                channel_modif, 
                                                                selected_config, 
                                                                0))
        return obj

    def __repr__(self):
        return '          Digital()'


class AD_Conversion(Coefficients):
    """
    AD_Conversion Filter (Flat Coefficients filter)
    """
    def __init__(self, filter_type, input_full_scale, output_full_scale, offset=0):
        self.transfer_function_type = 'DIGITAL'
        self.numerator_coefficients = [1.0]
        self.denominator_coefficients = []
        self.input_full_scale = input_full_scale
        self.output_full_scale = output_full_scale
        
        super().__init__(filter_type, "DIGITAL", 
                         self.numerator_coefficients, self.denominator_coefficients, offset)

    @classmethod
    def dynamic_class_constructor(cls, filter_type, attributes_dict, channel_modif={}, selected_config={}, stage_id=-1):
        """
        Create AD_Conversion instance from an attributes_dict
        """
        obj = cls(filter_type, 
                  attributes_dict.get_configured_element('input_full_scale', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   None),
                  attributes_dict.get_configured_element('output_full_scale', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   None), 
                  attributes_dict.get_configured_element('offset', 
                                                   channel_modif, 
                                                   selected_config, 
                                                   0))
        return obj

    def __repr__(self):
        s = f'          AD_Conversion(Input Full Scale={self.input_full_scale:g}, '
        s += f'Output Full Scale={self.output_full_scale})'
        return s
