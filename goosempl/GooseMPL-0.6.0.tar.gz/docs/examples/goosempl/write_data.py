import h5py
import numpy as np
import matplotlib.pyplot as plt
import GooseMPL as gplt

x = np.arange(10)
y = np.arange(10)

with h5py.File('write_data.hdf5', 'w') as data:

    fig, axes = plt.subplots(ncols=2)

    h = axes[0].plot(x, y, c='r', marker='o')
    gplt.write_data(data, '/plot', h)

    gplt.restore_data(data, '/plot', axis=axes[1])

    plt.savefig('write_data.svg')
    plt.close()

