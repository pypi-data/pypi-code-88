'''Generator and Discriminator for GAN.'''
import torch
import torch.nn.functional as F
import torch.nn as nn

#Generator for the GAN
class Generator(nn.Module):
    '''Generator Module for GAN.'''
    def __init__(self , normalization = None):
        super(Generator , self).__init__()

        # downsampling layers
        self.d1 = ConvolutionBlock(1 , 64 ,
                                   normalization = normalization ,
                                   kernel_size = 4 ,
                                   stride = 1 ,
                                   padding = 0 ,
                                   dropout = None
                                   )
        self.d2 = ConvolutionBlock(64, 128,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        self.d3 = ConvolutionBlock(128, 256,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        self.d4 = ConvolutionBlock(256, 512,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        self.d5 = ConvolutionBlock(512, 512,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        # upsampling layers
        self.u1 = TransposeConvolutionBlock(512 ,512 ,
                                            normalization=normalization,
                                            kernel_size=4,
                                            stride=2,
                                            padding=1,
                                            dropout=None
                                            )
        self.u2 = TransposeConvolutionBlock(1024, 256,
                                            normalization=normalization,
                                            kernel_size=4,
                                            stride=2,
                                            padding=1,
                                            dropout=None
                                            )
        self.u3 = TransposeConvolutionBlock(512, 128,
                                            normalization=normalization,
                                            kernel_size=4,
                                            stride=2,
                                            padding=1,
                                            dropout=None
                                            )
        self.u4 = TransposeConvolutionBlock(256, 64,
                                            normalization=normalization,
                                            kernel_size=4,
                                            stride=2,
                                            padding=1,
                                            dropout=None
                                            )

        self.final_layer = ConvolutionBlock(128 , 2 ,
                                            normalization = None,
                                            kernel_size=1,
                                            stride=1,
                                            padding=0,
                                            dropout=None,
                                            activation_function=nn.Tanh()
                                            )

    def forward(self , x):
        '''Forward Method for Generator.'''
        x = F.interpolate(x, size=(35,35),mode='bilinear',align_corners=True)
        # print(f'Initial: {x.shape}')
        # downsampling layers
        d1 = self.d1(x)
        d2 = self.d2(d1)
        d3 = self.d3(d2)
        d4 = self.d4(d3)
        d5 = self.d5(d4)
        # print(f'Shape d1: {d1.shape}')
        # print(f'Shape d2: {d2.shape}')
        # print(f'Shape d3: {d3.shape}')
        # print(f'Shape d4: {d4.shape}')
        # print(f'Shape d5: {d5.shape}')

        # upsampling layers with U Net Structure
        u1 = self.u1(d5,d4)
        u2 = self.u2(u1,d3)
        u3 = self.u3(u2,d2)
        u4 = self.u4(u3,d1)

        # print(f'Shape u1: {u1.shape}')
        # print(f'Shape u2: {u2.shape}')
        # print(f'Shape u3: {u3.shape}')
        # print(f'Shape u4: {u4.shape}')

        final = self.final_layer(u4)
        # print(f'Final: {final.shape}')
        return final


# Discriminator Module for GAN
class Discriminator(nn.Module):
    '''Discriminator Module for GAN.'''
    def __init__(self,
                 normalization=None):
        super(Discriminator , self).__init__()

        # downsampling layers
        # similar to Donsampling in Generator
        self.d1 = ConvolutionBlock(3, 64,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=1,
                                   padding=0,
                                   dropout=None
                                   )
        self.d2 = ConvolutionBlock(64, 128,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        self.d3 = ConvolutionBlock(128, 256,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )
        self.d4 = ConvolutionBlock(256, 512,
                                   normalization=normalization,
                                   kernel_size=4,
                                   stride=2,
                                   padding=1,
                                   dropout=None
                                   )

        self.final_layer = ConvolutionBlock(512,1,
                                            normalization=None,
                                            kernel_size=4,
                                            stride=1,
                                            padding=0,
                                            dropout=None,
                                            activation_function=nn.Sigmoid()
                                            )
    def forward(self,x):
        '''Forward method for Discriminator Module.'''
        x = F.interpolate(x,size=(35,35), mode='bilinear', align_corners=True)
        d1 = self.d1(x)
        d2 = self.d2(d1)
        d3 = self.d3(d2)
        d4 = self.d4(d3)

        # print(f'Shape d1: {d1.shape}')
        # print(f'Shape d2: {d2.shape}')
        # print(f'Shape d3: {d3.shape}')
        # print(f'Shape d4: {d4.shape}')

        final_out = self.final_layer(d4)
        # print(f'Final intial: {final_out.shape}')
        final_out = final_out.view(x.size()[0],-1)
        # print(f'Final final: {final_out.shape}')
        return final_out



# Convolution Layer Block for Downsampling Operation
class ConvolutionBlock(nn.Module):
    '''Class for Convolution Blocks for Downsampling.'''
    def __init__(self , input_channel , output_channel ,
                 normalization = None,
                 kernel_size  = 4,
                 stride  = 2,
                 padding  = 1,
                 dropout  = None,
                 activation_function = nn.ReLU() ):
        super(ConvolutionBlock ,  self).__init__()
        model_layers = []

        # Appending the Main Convolution Layer
        model_layers.append(
            nn.Conv2d(input_channel , output_channel ,
                      kernel_size = kernel_size ,
                      stride = stride ,
                      padding = padding)
        )

        #Applying Normalization Layer
        if normalization is not None:
            if normalization == 'Batch':
                model_layers.append(
                    nn.BatchNorm2d(output_channel)
                )
            elif normalization == 'Instance':
                model_layers.append(
                    nn.InstanceNorm2d(output_channel)
                )
        # Appending Activation Function given in the input
        model_layers.append(activation_function)

        # If Dropout is applicable
        if dropout is not None:
            model_layers.append(
                nn.Dropout(dropout)
            )
        # Making the Sequential Model
        model = nn.Sequential(*model_layers)
        self.model = model

    def forward(self , x):
        '''Forward Operation for Convolution Layer'''
        return self.model(x)

# Transpose Convolution block for Upsampling Operation
class TransposeConvolutionBlock(nn.Module):
    '''Transpose Convolution Block for Upsampling Architecture.'''
    def __init__(self, input_channel, output_channel,
                 normalization=None,
                 kernel_size=4,
                 stride=2,
                 padding=1,
                 dropout=None,
                 activation_function=nn.ReLU()):
        super(TransposeConvolutionBlock , self).__init__()
        model_layers = []

        # Adding the Transpose Convolution Layer
        model_layers.append(
            nn.ConvTranspose2d(input_channel , output_channel ,
                               kernel_size = kernel_size ,
                               stride = stride ,
                               padding = padding)
        )

        # adding normalization
        if normalization is not None:
            if normalization == 'Batch':
                model_layers.append(
                    nn.BatchNorm2d(output_channel)
                )
            elif normalization == 'Instance':
                model_layers.append(
                    nn.InstanceNorm2d(output_channel)
                )

        # adding activation function for the layer
        model_layers.append(
            activation_function
        )

        # adding dropout
        if dropout is not None:
            model_layers.append(
                nn.Dropout(dropout)
            )

        # creating the sequential model
        model = nn.Sequential(*model_layers)
        self.model = model

    def forward(self , x1 , skip_input):
        '''Forward Method for the input.'''
        x = self.model(x1)
        return torch.cat((x , skip_input) , 1)

# # Testing
# if __name__=='__main__':
#     gen = Discriminator()
#     sample_input = torch.zeros((1,1,32,32))
#     print(sample_input.shape)
#     print(gen)
#     print(gen(sample_input))







