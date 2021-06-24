"""Test of an upstrim-generated file: deserialze and plot all its items"""
import sys, argparse
from glob import glob
import numpy as np
import msgpack
import msgpack_numpy
msgpack_numpy.patch()
import time, pyqtgraph as pg

#__version__ = 'v04 2021-06-03'# DateTime axis
__version__ = 'v05 2021-06-12'# Unix style pathname pattern expansion

#````````````````````````````Helper methods```````````````````````````````````
def decompress(arg):
    return

class DateAxis(pg.AxisItem):
    """Time scale for plot"""
    def tickStrings(self, values, scale, spacing):
        strns = []
        if len(values) == 0: 
            return ''
        rng = max(values)-min(values)
        #if rng < 120:
        #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
        if rng < 3600*24:
            string = '%H:%M:%S'
        elif rng >= 3600*24 and rng < 3600*24*30:
            string = '%d'
        elif rng >= 3600*24*30 and rng < 3600*24*30*24:
            string = '%b'
        elif rng >=3600*24*30*24:
            string = '%Y'
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')
        return strns
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#````````````````````````````Deserialize files````````````````````````````````
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-k', '--keys', help=('Items to plot. '
'String of 1-letter keys of the parameter map e.g. 1357'))
parser.add_argument('files', nargs='*', default='apstrim.aps', help=\
'Input files, Unix style pathname pattern expansion allowed e.g: pi0_2021*.aps')
pargs = parser.parse_args()
print(f'pargs: {pargs}')
print(f'files: {pargs.files}')

for file in pargs.files:
    print(f'Processing {file}')
    f = open(file,'rb')
    book = msgpack.Unpacker(f)
    
    nSections = 0
    nParagraphs = 0
    for section in book:
        #if nSections > 100:  break
        nSections += 1
        if nSections == 1:# skip info section 
            print(f'file info: {section}')
            compression = section.get('compression')
            if compression is None:
                continue
            if compression != 'None':
                module = __import__(compression)
                decompress = module.decompress
            continue
        if nSections == 2:# section: parameters
            par2key = section['parameters']
            key2par = {value[0]:key for key,value in par2key.items()}
            print(f'parameter map: {key2par}')
            ykeys = list(key2par.keys())
            nkeys = len(ykeys)
            x,y = [],[]
            for i in range(nkeys):
                x.append([])
                y.append([])
            continue
    
        # data sections
        #print(f'dsec: {section}')
        try:
            if compression != 'None':
                decompressed = decompress(section)
                section = msgpack.unpackb(decompressed)
            sectionDatetime, paragraphs = section
        except Exception as e:
            print(f'WARNING: wrong section {nSections}: {str(section)[:75]}...')
            continue
        nParagraphs += len(paragraphs)
        for timestamp,parkeys in paragraphs:
            for i,ykey in enumerate(ykeys):
                if ykey in parkeys:
                    #print(f'ik: {i,ykey}, {parkeys}')
                    x[i].append(timestamp)
                    try:    
                        v = parkeys[ykey][0]
                    except:
                        v = parkeys[ykey]
                    y[i].append(v)
    #print(f'xy: {list(zip(x[0],y[0]))}')
    print(f'Deserialized from {file}: {nSections} sections, {nParagraphs} paragraphs')
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
#```````````````````````````` Plot objects````````````````````````````````````
win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(800,600)
win.setWindowTitle('pyqtgraph example: Plotting')

plot = win.addPlot(title="apstrim plot",
    axisItems={'bottom':DateAxis(orientation='bottom')})
plot.getViewBox().setMouseMode(pg.ViewBox.RectMode)

for i in range(len(ykeys)):
    if pargs.keys is not None and str(i) not in pargs.keys:
        continue
    try:
        plot.plot(x[i],y[i])#,pen=(255,0,0))#, pen=None, symbol='o')
    except Exception as e:
        print(f'WARNING: plotting is not supported for item {i}: {e}')
pg.mkQApp().exec_()
