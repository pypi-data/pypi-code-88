'''Configuration file for ColourGAN.'''

class ColourGANConfig:
    initial_weights_generator = None
    initial_weights_discriminator = None

    generator_normalization = 'batch'
    discriminator_normalization = 'batch'

    base_lr_generator = 3e-4
    base_lr_discriminator = 6e-5

    lr_decay = 0.1
    lr_decay_steps = 6e4

    l1_weight = 0.99

    data_path = ''
    output_path = 'output'
    training_stats_file = 'training_logs.txt'
    checkpoint_frequency = 5
    batch_size = 32
    num_workers = 4
    epochs = 100
    smoothing = 0.9

def get_cfg():
    return ColourGANConfig()