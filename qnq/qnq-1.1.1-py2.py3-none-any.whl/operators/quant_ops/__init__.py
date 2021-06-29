from .activation import *
from .convolution import *
from .dropout import *
from .linear import *
from .normalization import *
from .padding import *
from .pooling import *
from .recurrent import *
from .sparse import *
from .torchfunc import *
from .transformer import *
from .vision import *
from .complex import *
from .quant_base import *

qnq_switch = {
    **activation_switch,
    **convolution_switch,
    **dropout_switch,
    **linear_switch,
    **normalization_switch,
    **padding_switch,
    **pooling_switch,
    **recurrent_switch,
    **sparse_switch,
    **torchfunc_switch,
    **transformer_switch,
    **vision_switch
}