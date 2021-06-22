"""Application that opens ANA files
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
from glob import glob
import sklearn.mixture
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
import re


"""
    List of methods available
    
    xml2hdf()
        converts scalar_data xml files to a more efficient hdf file
    
    spec_map()
        takes experiment png and adds boxes where the measurements were taken.
        Saves to new file
        
    read()
        imports all hdf data scalar_data files
    
    parameters()
        imports measurement info including: original NID filename,
        spot number, spring constant, deflection sensitivity, map size (um),
        map size (pixels), data points, ramp length, ramp speed, and max force
        
    stats(spots)
        calculates general statistics of the data
            spot (integer) or aggregated spots (list)
        
    channelData(spots, channel, direction, fill_empty=False)
        returns data for a specific
            spot (integer) or spots aggregated (list),
            channel (string: 'E-Modul', 'Minimum', etc.),
            direction (bool: backward=True), and
            fill_empty=False (bool: fills missing data with NaN)
    
    spotData(spots)
        returns data all data for a specific
            spot (integer) or spots (list)

    image(spot, channel, direction, lim=None, scale=None, label=None, cmap=cm.afmhot, kwargs)
        plots a force-volume map of the data from a specific
            spot (integer),
            channel (string: 'E-Modul', 'Minimum', etc.),
            direction (bool: backward=True),
            lim=None (float: limit the data)
            scale=None (float: scale the data)
            label=None (string: the label (i.e. unit) of the colorbar)
            cmap=cm.afmhot (pyplot colormap: the colormap to use)
            kwargs (extra keyed arguments that are passed on to pyplot)

    hist(spots, channel, direction, lim=None, scale=None, label=None, cmap=cm.afmhot, kwargs)
        plots a histogram of the data from specific
            spot (integer) or spots aggregated (list),
            channel (string: 'E-Modul', 'Minimum', etc.),
            direction (bool: backward=True),
            lim=None (float: limit the data)
            scale=None (float: scale the data)
            label=None (string: the label (i.e. unit) of the x axis)
            cmap=cm.afmhot (pyplot colormap: the colormap to use)
            kwargs (extra keyed arguments that are passed on to pyplot)
            
    gaussianMix(spots, channel, direction, number=1, lim=None, scale=None)
        tries to identify different populations in a data set using gaussian mixture
        algorithm and returns means and weights of mixture.  Works okay, need
        to add ability to input first guesses
            spot (integer) or spots aggregated (list),
            channel (string: 'E-Modul', 'Minimum', etc.),
            direction (bool: backward=True),
            number=1 (integer: number of populations)
            lim=None (float: limit the data)
            scale=None (float: scale the data)
"""


class ANA():
    def __init__(self, directory):
        self.directory = directory
        self._filelist()
        if not self.files:
            print('scalar_data files not in HDF format.  Run xml2hdf to convert.')
            
        self.parameters()

    def spec_map(self):
        tree = ET.parse(self.directory + '//spec_maps')
        root = tree.getroot()

        maps = root.findall('element')

        im = Image.open(self.directory + '//experiment.png')
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial", 16)
        sz = 10

        for i, m in enumerate(maps):
            cx = int(m.find('center_x_on_image').text)
            cy = int(m.find('center_y_on_image').text)

            draw.rectangle([cx - sz, cy - sz, cx + sz, cy + sz], fill='orange')

            w, h = draw.textsize(str(i + 1))
            draw.text((cx - w/2, cy - h/2), str(i + 1), font=font, anchor='SE')

        im.save(self.directory + '//exp_loc.png')
        self.spec_image = im

    def parameters(self):
        tree = ET.parse(self.directory + '//spec_maps')
        root = tree.getroot()

        maps = root.findall('element')

        sz = []
        dP = []
        xStart = []
        xEnd = []
        maxF = []
        rampL = []
        rampS = []
        for m in maps:
            sz.append(int(m.find('spec_map_').find('x_point_count').text))
            xStart.append(float(m.find('spec_map_').find('x_start').text))
            xEnd.append(float(m.find('spec_map_').find('x_end').text))
            dP.append(int(m.find('forward_').find('datapoints_').text))
            rampL.append(float(m.find('forward_').find('ramp_length_').text))
            rampS.append(float(m.find('forward_').find('ramp_speed_').text))
            maxF.append(float(m.find('forward_').find('maximum_force_').text))

        tree = ET.parse(self.directory + '//measurement')
        root = tree.getroot()

        maps = root.findall('measurement')

        filename = [x.text for x in root.find('spec_nid_files_').findall('element')]
        springK = [float(x.text) for x in root.find('spring_constants_').findall('element')]
        deflection = [float(x.text) * 1e9/10 for x in root.find('deflection_sensitivities_').findall('element')]

        mapSz = (np.array(xEnd) - np.array(xStart)) * 1e6
        
        spots = np.arange(len(filename)) + 1

        self.param = pd.DataFrame(data={'FileName': filename,
                                        'Spot': spots,
                                        'SpringConstant': springK,
                                        'DeflSens': deflection,
                                        'MapSize': mapSz,
                                        'MapPixSize': sz,
                                        'DataPoints': dP,
                                        'RampLength': rampL,
                                        'RampSpeed': rampS,
                                        'MaxForce': maxF})

    def read(self, index=[]):

        data_list = []
        file_list = []
        
        if not isinstance(index, list):
            print('File index must be list')
            return
            
        idx = np.arange(len(self.files))

        if not index:
            index = idx
        
        idx = [i for i in index if i in idx]
        if len(idx) == 1:
            idx = (idx[0],)
    
        for i in idx:
            df = pd.read_hdf(self.files[i])
            
            data_list.append(df)
            file_list.append(self.files[i])
        file_list = np.array([f.split('\\') for f in file_list])
        spot_num = [int(f[:-3].split('_')[2]) + 1 for f in file_list[:, -1]]

        self.data = pd.DataFrame(data={'Experiment': file_list[:, 0],
                                       'Files': file_list[:, 1],
                                       'Spot': spot_num,
                                       'Data': data_list})

    def stats(self, spots):
        d = self.spotData(spots)
                        
        return d.groupby(['Channel', 'Backward']).Value.describe()

    def xml2hdf(self):
        f1 = glob(self.directory + '//scalar*')
        f2 = glob(self.directory + '//scalar*.h5')
        
        files = [f for f in f1 if f not in f2]
        
        for f in files:
            tree = ET.parse(f)
            root = tree.getroot()
            
            name = []
            line = []
            value = []
            backward = []
            for element in root[0].findall('element'):
                line.append(int(element.find('line_').text))
                name.append(element.find('calc_name_').text)
                value.append(float(element.find('value_').text))
                backward.append(int(element.find('p_').text))
                
            df = pd.DataFrame({'Line': line,
                               'Channel': name,
                               'Value': value,
                               'Backward': backward})

            df.to_hdf(f + '.h5', key='df')

    def channelData(self, spots, channel, backward, fill_empty=False):
        d = self.spotData(spots)
        dd = d[(d['Channel'] == channel) & (d['Backward'] == backward)]
        if fill_empty:
            sz = self.param.MapPixSize[spots - 1]
        
            ar = np.zeros(sz * sz) * np.nan
            ar[dd.Line.values] = dd.Value.values
            dd = pd.DataFrame({'Value': ar})
        return dd
    
    def spotData(self, spots):
        if isinstance(spots, list):
            if len(spots) > 1:
                spots = self.data.Spot.isin(spots)
                d = pd.concat([x for x in self.data[spots].Data], axis=0)
            else:
                spots = self.data.Spot.isin(spots)
                d = self.data[spots]
        else:
            spots = self.data.Spot.isin([spots])
            d = self.data[spots].Data.iloc[0]
        return d

    def image(self, spot, channel, backward,
              lim=None, scale=None, label=None, cmap=cm.afmhot,
              **kwargs):

        if isinstance(spot, list):
            print('Can only show map of one spot at a time')
            return

        ar = self.channelData(spot, channel, backward, fill_empty=True).Value.values

        if scale:
            ar /= scale
        
        if not label:
            label = ''

        sz = self.param.MapPixSize[spot - 1]
        ar = ar.reshape((sz, sz)).copy()
        ar[::2] = np.fliplr(ar[::2])
        
        ar = np.fliplr(ar)

        mSize = self.param.MapSize[spot - 1]
        plt.imshow(ar, origin='bottomleft', extent=(0, mSize, 0, mSize), cmap=cmap, **kwargs)
        if lim:
            plt.clim(vmax=lim)
        plt.xlabel(r'[$\mu$m]')
        plt.ylabel(r'[$\mu$m]')
        plt.title(channel)
        cbar = plt.colorbar()
        cbar.set_label(label, rotation=-90, va="bottom")
        return ar

    def hist(self, spots, channel, backward,
             lim=None, scale=None, label=None, cmap=cm.afmhot,
             **kwargs):

        dd = self.channelData(spots, channel, backward).Value.dropna().values
        if scale:
            dd /= scale

        if not lim:
            lim = max(dd)

        if not label:
            label = ''
        histtype = dict(histtype="step", linewidth=1, edgecolor='k')
        n, bins, patches = plt.hist(dd[dd <= lim], **kwargs)

        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        col = bin_centers - min(bin_centers)
        col /= max(col)

        for c, p in zip(col, patches):
            plt.setp(p, 'facecolor', cmap(c))

        plt.hist(dd[dd <= lim], **histtype, **kwargs)
        plt.title(channel)
        plt.xlabel(label)
        plt.ylabel('Counts')
        return n, bin_centers

    def gaussianMix(self, spots, channel, backward, number=1, lim=None, scale=None, **kwargs):
        gmm = sklearn.mixture.GaussianMixture(n_components=number, covariance_type='diag', **kwargs)
        d = self.channelData(spots, channel, backward).Value.values
        if scale:
            d /= scale

        if lim:
            d = d[d < lim]

        r = gmm.fit(d[:, np.newaxis])
        m = r.means_.flatten()
        w = r.weights_.flatten()
        # c = r.covariances_.flatten()
        fits = pd.DataFrame({'mean': m, 'weight': w})
        fits = fits.sort_values('mean').reindex()
        return fits

    def _filelist(self):
        self.files = glob(self.directory + '\\scalar*.h5')
        self.files.sort(key=self._natural_keys)
    
    # sorts list numerically
    def _atoi(self, text):
        return int(text) if text.isdigit() else text
    
    def _natural_keys(self, text):
        return [self._atoi(c) for c in re.split(r'(\d+)', text)]


if __name__ == "__main__":
    from matplotlib import cm
    directory = r'test'
    ana = ANA(directory)
    
    ana.read()

    ana.image(1, 'E-Modul', True, scale=1e9, lim=3, label='[GPa]', cmap=cm.afmhot)
    plt.show()
    ana.hist(1, 'E-Modul', True, scale=1e9, lim=3, label='[GPa]', bins=128)
    plt.show()

    r = ana.gaussianMix(1, 'E-Modul', True, 3, lim=3, scale=1e9)
    print(r)
