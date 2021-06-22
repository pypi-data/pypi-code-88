#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2020 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External libraries
import numpy as np
# Internal libraries
from miscnn import Preprocessor
from miscnn.neural_network.data_generator import DataGenerator

#-----------------------------------------------------#
#        Estimate Voxel Spacing for Resampling        #
#-----------------------------------------------------#
""" Function for automatic drawing loss/metric vs epochs figures between training and
    testing data set. The plots will be saved in the provided evaluation directory.

Args:
    data_io (Data_IO):                      Data IO class instance which handles all I/O operations according to the user
                                            defined interface.
    input_size (tuple of integer):          Input shape. Recommended to use desired patch shape.
    ratio (float):                          Ratio between input size and resampled median image size.
"""
def estimate_resampling(data_io, input_size, ratio=0.125):


    # Compute optimal median image size
    opt_is = np.prod(input_size) / ratio

    # Converge to optimal spacing
    threshold = 10
    print(m_is_shape)
    print(m_is_shape.shape)
    print(np.mean(m_is_shape, axis=0)[0:-1])
    # c_is = np.prod(m_is_shape)
    # while(np.abs(c_is - opt_is) > threshold):
    #     print(c_is, opt_is)
    #
    # print(m_vs)
    # print(m_is)
    # print(opt_is)
        # sample_data[index].append(tuple(class_freq))
        #
    # # Create and configure the Preprocessor class
    # pp = Preprocessor(data_io, data_aug=None, batch_size=1, subfunctions=None,
    #                   prepare_subfunctions=False, prepare_batches=False,
    #                   analysis="fullimage")

def _compute_data(data_io):
    # Obtain sample list
    sample_list = data_io.get_indiceslist()

    # Collect information from the dataset
    m_vs = []
    m_is = []
    for index in sample_list[0:3]:
        # Sample loading
        sample = data_io.sample_loader(index, load_seg=False)
        # Obtain information
        vs = sample.get_extended_data()["spacing"]
        shape = sample.img_data.shape
        # Store in cache
        m_vs.append(vs)
        m_is.append(shape)
    # Convert information to NumPy
    m_vs = np.array(m_vs)
    m_is_shape = np.array(m_is)
