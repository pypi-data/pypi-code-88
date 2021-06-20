from oap.core import imagefile, number_of_buffers
import numpy as np
import pickle
from oap.bnp import Loading, progress, Runtime
from matplotlib import pyplot as plt


def load_imagefile(filename):
    loading = Loading("Loading Imagefile", mode="bar", runtime=True).start()
    with open(filename, "rb") as file:
        image_file = pickle.load(file)
    loading.stop("Imagefile loaded successfully! - ")
    return image_file


class Imagefile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.arrays = []
        self.particles = imagefile(self.filepath, arrays=self.arrays, poisson=True, principal=True,
                                   truncated=True, components=False, stdout=True)
        """
        self.library = {}
        runtime = Runtime().start()
        for i, arr in enumerate(self.arrays):
            progress(i, self.particles, prefix="Init Hashtable ")
            self.library[str(arr.second)+"_"+str(arr.number)] = i
        runtime.stop()

        self.n_buffers = number_of_buffers(self.filepath)
        """


    def __len__(self):
        return self.particles

    """
    def search(self):

        from oap.deep import f1
        from tensorflow.keras.models import load_model

        model_c = load_model("weights/final_column_mc_pre14_e11_acc0.98_fs0.98.hdf5", custom_objects={'f1': f1})
        model_r = load_model("weights/final_rosette_mc_pre06_e05_acc0.97_fs0.97.hdf5", custom_objects={'f1': f1})

        buffer_batch_size = 500
        model_c.predict(np.zeros(shape=(1, 64, 64, 1)))

        runtime = Runtime().start()

        for i in range(0, self.n_buffers + buffer_batch_size, buffer_batch_size):   # ToDo
            progress(i, self.n_buffers, "Searching particle types ")
            tensor = []
            output = []
            batch_size = imagefile(self.filepath, tensor=tensor, output=output,
                                   includebuffers=[b for b in range(i, i+buffer_batch_size, 1)],
                                   monochromatic=True, new_xbary=31, new_ybary=31,
                                   xsizes=[(5, 64)], ysizes=[(5, 64)], stdout=False)
            if batch_size != 0:
                batch = np.array(tensor)
                batch = np.reshape(batch, newshape=(batch_size, 64, 64, 1))

                prediction = model_c.predict(batch)
                for j, p in enumerate(prediction):
                    index = self.library[str(output[j][0])+"_"+str(output[j][1])]
                    self.arrays[index].column = p[0]

                prediction = model_r.predict(batch)
                for j, p in enumerate(prediction):
                    index = self.library[str(output[j][0])+"_"+str(output[j][1])]
                    self.arrays[index].rosette = p[0]
        print()
        runtime.stop()
    """
    def search_old(self):

        from oap.deep import f1
        from tensorflow.keras.models import load_model

        model_c = load_model("weights/final_column_mc_pre14_e11_acc0.98_fs0.98.hdf5", custom_objects={'f1': f1})
        model_r = load_model("weights/final_rosette_mc_pre06_e05_acc0.97_fs0.97.hdf5", custom_objects={'f1': f1})
        model_c.predict(np.zeros(shape=(1, 64, 64, 1)))

        tmp = self.get_particles(size=(75, 960))

        runtime = Runtime().start()
        buffer = 16384
        for i in range((len(tmp) // buffer) + 1):
            progress(i, (len(tmp) // buffer) + 1, "Searching particle types ")


            arrays = tmp[i * buffer:i * buffer + buffer]

            batch = []
            for arr in arrays:
                batch.append(arr.tensor())

            batch = np.reshape(batch, (len(arrays), 64, 64, 1))
            pred_c = model_c.predict(batch)
            pred_r = model_r.predict(batch)

            for p, arr in zip(pred_c, arrays):
                arr.column = p[0]
            for p, arr in zip(pred_r, arrays):
                arr.rosette = p[0]
        runtime.stop()

    def save(self, filename):
        loading = Loading("Saving Imagefile", mode="bar", runtime=True).start()
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        loading.stop("Imagefile saved! - ")

    def get_particles(self, timespan=None, size=None, c_th=None, r_th=None, hit_ratio=None, alpha=None,
                      aspect_ratio=None):

        timespan = (0, 86400) if timespan is None else timespan
        size = (0, 960) if size is None else size
        aspect_ratio = (0, 18446744073709551615) if aspect_ratio is None else aspect_ratio
        alpha = (-360, 360) if alpha is None else alpha
        c_th = (-1, 1) if c_th is None else c_th
        r_th = (-1, 1) if r_th is None else r_th
        hit_ratio = (-1, 100) if hit_ratio is None else hit_ratio

        particles = []
        for array in self.arrays:
            if timespan[0] <= array.second <= timespan[1] \
                    and size[0] <= array.area_ratio() <= size[1] \
                    and aspect_ratio[0] <= array.aspect_ratio <= aspect_ratio[1] \
                    and alpha[0] <= array.alpha <= alpha[1] \
                    and c_th[0] <= array.column <= c_th[1] \
                    and r_th[0] <= array.rosette <= r_th[1] \
                    and hit_ratio[0] <= array.hit_ratio <= hit_ratio[1]:
                particles.append(array)
        return particles

    def init_plot(self, figures):
        self.figures = figures
        self.plot_iterator = 0
        self.fig, self.axes = plt.subplots(self.figures)

    def plot(self, timespan=None, size=None, c_th=None, r_th=None, hit_ratio=None, alpha=None, aspect_ratio=None,
             color="b", log=False, iterate=True, label=None, legend=False, grid=False,
             ylabel="Anzahl Partikel", xlabel=None, timeshift=0, title=None):

        timespan = (0, 86400) if timespan is None else timespan
        size = (0, 960) if size is None else size
        aspect_ratio = (0, 18446744073709551615) if aspect_ratio is None else aspect_ratio
        alpha = (-360, 360) if alpha is None else alpha
        c_th = (-1, 1) if c_th is None else c_th
        r_th = (-1, 1) if r_th is None else r_th
        hit_ratio = (-1, 100) if hit_ratio is None else hit_ratio

        number_per_second = {}
        for i in range(self.arrays[0].second+timeshift, self.arrays[-1].second+timeshift):
            number_per_second[i] = 0

        for array in self.arrays:
            if timespan[0] <= array.second+timeshift <= timespan[1] \
                    and size[0] <= array.area_ratio() <= size[1] \
                    and aspect_ratio[0] <= array.aspect_ratio <= aspect_ratio[1] \
                    and alpha[0] <= array.alpha <= alpha[1] \
                    and c_th[0] <= array.column <= c_th[1] \
                    and r_th[0] <= array.rosette <= r_th[1] \
                    and hit_ratio[0] <= array.hit_ratio <= hit_ratio[1]:
                if array.second+timeshift in number_per_second.keys():
                    number_per_second[array.second+timeshift] += 1

        y, x = zip(*sorted(number_per_second.items()))

        if title is not None:
            self.axes[self.plot_iterator].title.set_text(title)
        self.axes[self.plot_iterator].plot(y, x, c=color, linewidth=1, label=label)
        self.axes[self.plot_iterator].set_ylabel(ylabel)
        if xlabel is not None:
            self.axes[self.plot_iterator].set_xlabel(xlabel)
        if grid:
            self.axes[self.plot_iterator].grid()
        if legend:
            self.axes[self.plot_iterator].legend()
        if log:
            self.axes[self.plot_iterator].set_yscale("log")
        if iterate:
            self.plot_iterator += 1
        if self.plot_iterator == self.figures:
            plt.show()


if __name__ == "__main__":
    file_path = "../__data/Nixe/mlcirrus_nixe/Imagefile_1CIP Grayscale_20140327151147"
    # file_path = "../__data/Nixe/NIXECAPS_CIP-Bilder_ML-CIRRUS/20140322083727/Imagefile_1CIP Grayscale_20140322083727"
    tmp = Imagefile(file_path)
    tmp.search()
