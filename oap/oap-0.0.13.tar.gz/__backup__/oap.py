# --- Imports and Options ---------------------------------------------------------------

import random as rnd



from binascii import hexlify


from scipy.stats.stats import pearsonr


import BitsAndPieces as bnp








# --- Globals ---------------------------------------------------------------------------





# --- Output or Export Methods ----------------------------------------------------------















# --- Import Methods --------------------------------------------------------------------


def read_oap_file(fname,
                  type="array",
                  dtype="int64",
                  headersize=1,
                  onecolor=False,
                  color=MONOSC_SHADOWLEVEL,
                  grayscale=[0.0, 0.25, 0.5, 0.75]):
    """
    Reads an OAP binary image file and returns an optical array
    as string, list or numpy array.
    """
    with open(fname, "rb") as f:
        # Binary particle header.
        header = f.read(headersize)
        byte = f.read(1)


        # If onecolor is True, this method ignores the different grayscale
        # level and sets every shadow pixel to the monoscale shadow level.
        #
        # CAUTION: This is not the same as the monoscale output!
        # The first shadow level still exists.
        if onecolor:
            colors = [0, color, color, color]
        else:
            colors = [0, 1, 2, 3]

        if type.upper() == "STRING":
            img_string = ""
            while byte:
                byte = int(hexlify(byte), 16)
                if   byte == 0: img_string += str(colors[0])
                elif byte == 1: img_string += str(colors[1])
                elif byte == 2: img_string += str(colors[2])
                elif byte == 3: img_string += str(colors[3])
                else:           img_string += str(int(byte))
                byte = f.read(1)
            f.close()
            return img_string, header

        elif type.upper() == "LIST":
            img_list = []
            while byte:
                byte = int(hexlify(byte), 16)
                if   byte == 0: img_list.append(colors[0])
                elif byte == 1: img_list.append(colors[1])
                elif byte == 2: img_list.append(colors[2])
                elif byte == 3: img_list.append(colors[3])
                else:           img_list.append(int(byte))
                byte = f.read(1)
            f.close()
            return img_list, header

        elif type.upper() == "ARRAY" and dtype.upper() == "INT64":
            file_size = os.stat(fname).st_size - headersize
            img_array = np.zeros(file_size, dtype="int64")
            i = 0
            while byte:
                byte = int(hexlify(byte), 16)
                if   byte == 0: img_array[i] = colors[0]
                elif byte == 1: img_array[i] = colors[1]
                elif byte == 2: img_array[i] = colors[2]
                elif byte == 3: img_array[i] = colors[3]
                else:           img_array[i] = int(byte)
                byte = f.read(1)
                i += 1
            f.close()
            return img_array, header

        elif type.upper() == "ARRAY" and dtype.upper() == "FLOAT32":
            file_size = os.stat(fname).st_size - headersize
            img_array = np.zeros(file_size, dtype="float32")
            i = 0
            while byte:
                byte = int(hexlify(byte), 16)
                if   byte == 0: img_array[i] = grayscale[0]
                elif byte == 1: img_array[i] = grayscale[1]
                elif byte == 2: img_array[i] = grayscale[2]
                elif byte == 3: img_array[i] = grayscale[3]
                else:           img_array[i] = float(byte)
                byte = f.read(1)
                i += 1
            f.close()
            return img_array, header




def header_to_logits(header, headersize=1, classes=4):
    """
    Translates an OAP particle header into a numpy array.
    """
    if headersize == 1 and classes == 4:
        logits = np.zeros(classes, dtype="float32")

        if   header[0] == 's': logits[0] = 1.0
        elif header[0] == 'n': logits[1] = 1.0
        elif header[0] == 'b': logits[2] = 1.0
        elif header[0] == 'u': logits[3] = 1.0
        elif header[0] == 'o': logits[3] = 1.0
        elif header[0] == 't': logits[3] = 1.0
        else:                  logits[3] = 1.0

        return logits

    err_str = "(oap::header_to_logits) invalid parameters: "
    err_str += "no configuration for these parameters possible"
    print >> sys.stderr, "\n" + err_str + "\n"
    raise ValueError(err_str)



def get_oap_data(files, pick, **kwargs):
    """
    For a given list of binary OAP images and a batch size "pick" this function
    returns a batch of OAP images as numpy arrays, their labels and a the list
    of the batch file names.
    Furthermore, this function returns a list of all unused given OAP images
    for following training or testing steps.
    """
    args = {'headersize': 1,
            'slicesize': 64,
            'imageheight': None,
            'dtype': "int64",
            'random': True,
            'delete': True,
            'batchfiles': True,
            'labels': True,
            'center': True,
            'mirror': False,
            'onecolor': False,
            'pick': 1,
            'classes': 4}

    verify = set(kwargs.keys()) - set(args.keys())
    if verify:
        err_str = "(oap::get_oap_data) invalid args: " + ", ".join(verify)
        print >> sys.stderr, "\n", err_str, "\n"
        raise KeyError(err_str)

    args.update(kwargs)


    x = []           # array of optical arrays
    y = []           # their labels
    batch_files = [] # list of oap file names


    # If the preferred batch size is bigger than the number
    # of files, the batch size will be smaller.
    # The list "batch" contains (randomly chosen) file indices.
    if args['random']:    batch = rnd.sample(xrange(0, len(files)),
                                             min(len(files), pick))
    else:                 batch = xrange(0, min(len(files), pick))


    for index in batch:
        optical_array, header = read_oap_file(files[index], "ARRAY",
                                              args['dtype'], args['headersize'],
                                              onecolor=args['onecolor'])

        if args['center']:
            xbary, _ = barycenter(optical_array, args['slicesize'])
            optical_array = center_particle_image(optical_array, xbary, args['imageheight'],
                                                  args['slicesize'], args['dtype'])
        elif args['imageheight']:
            optical_array = adjust_image_height(optical_array,
                                                args['imageheight'],
                                                args['slicesize'], args['dtype'])

        batch_files.append(files[index])
        x.append(optical_array)
        y.append(header_to_logits(header,
                                  headersize=args['headersize'],
                                  classes=args['classes']))

        if args['mirror']:
            flipped_array = xflip_array(optical_array, args['slicesize'], args['dtype'])

            if args['center']:
                xbary, _ = barycenter(flipped_array, args['slicesize'])
                flipped_array = center_particle_image(flipped_array, xbary, args['imageheight'],
                                                      args['slicesize'], args['dtype'])
            elif args['imageheight']:
                flipped_array = adjust_image_height(flipped_array,
                                                    args['imageheight'],
                                                    args['slicesize'], args['dtype'])

            x.append(flipped_array)
            y.append(header_to_logits(header,
                                      headersize=args['headersize'],
                                      classes=args['classes']))

    if args['delete']:
        for f in batch_files:
            files.remove(f)

    if args['batchfiles']:
        if args['labels']: return x, y, batch_files
        else: return x, batch_files
    else:
        if args['labels']: return x, y
        else: return x







def png_as_array(file, threshold):
    """
    Reads a black and white Blender Rendering as PNG image and translates
    it into an optical array. Uses thresholds to merge grayscales into
    4 greyscales -> Cel Shading
    """
    # Import PNG as numpy array -> also flattens RGB values.
    img = imread(file, flatten=True)
    img_height = len(img)
    slicesize = len(img[0])

    array = np.zeros(img_height * slicesize, dtype=int)

    for i in range(img_height):
        for j in range(slicesize):
            if img[i][j] >= threshold[0]:
                array[i*slicesize+j] = 0
            elif img[i][j] >= threshold[1]:
                array[i*slicesize+j] = 1
            elif img[i][j] >= threshold[2]:
                array[i*slicesize+j] = 2
            else:
                array[i*slicesize+j] = 3
    return array





# --- Modify Optical Array --------------------------------------------------------------




# --- Something is wrong with this function -> Some arrays seem to be empty after flipping --------------
def xflip_array(array, slicesize=64, dtype=int):
    """
    Flips optical array in x-direction. Returns a mirrored particle image as numpy array.
    """
    flipped = np.zeros(len(array), dtype)
    image_height = len(array) / slicesize

    for y in range(image_height):
        for x in range(slicesize):
            if array[y*slicesize+x] != 0:
                flipped[y*slicesize+(slicesize-x)] = array[y*slicesize+x]
    return flipped



def yflip_array(array, slicesize=64, dtype=int):
    """
    Flips optical array in x-direction. Returns a mirrored particle image as numpy array.
    """
    flipped = np.zeros(len(array), dtype)
    image_height = len(array) / slicesize

    for y in range(image_height):
        for x in range(slicesize):
            if array[y*slicesize+x] != 0:
                flipped[((image_height-1)-y)*slicesize+x] = array[y*slicesize+x]
    return flipped






# ---------------------------------------------------------------------- should clip and stuff --------------------------------------- This function is not perfect !!!
def unify_array(array,
                center=True,
                imageheight=125,
                monoscale=False,
                onecolor=False,
                color=MONOSC_SHADOWLEVEL,
                slicesize=64,
                dtype=int,
                warning=True):
    """
    Converts an optical array to a unified shape (image height, color, ...)
    for classifications.
    """
    if center:
        x_bary, _ = barycenter(array, coordinates=True, slicesize=slicesize)
        array = center_particle_image(array, x_bary, imageheight=imageheight, slicesize=slicesize, dtype=dtype, warning=warning)
    if monoscale:
        array = convert_to_monoscale(array, color=color, slicesize=slicesize, dtype=dtype)
    if onecolor:
        array = convert_to_onecolor(array, color=color, slicesize=slicesize, dtype=dtype)
    return array



def normalize(array, value=3.0):
    return array.astype(float) / value




# not used ----------------------------------------- maybe buggy or not necessary --------------------------------------------------------------------------
# --- Import / Export whole DataSets ----------------------------------------------------

def export_oap_dataset(path, name, X, Y):
    """
    Saves a given dataset (x, y) in a .txt-file.
    """
    file = open(os.path.join(path, name+".txt"), 'w')
    progress = 1
    for x, y in zip(X, Y):

        for i, elt in enumerate(x):
            file.write(str(elt))
            if i != len(x)-1:
                file.write(',')
        file.write("\n")

        for i, elt in enumerate(y):
            file.write(str(elt))
            if i != len(y)-1:
                file.write(',')
        file.write("\n")
        bnp.progress_bar(progress, len(X), prefix="Export Data:", suffix="Complete")
        progress += 1
    file.close()



def load_oap_dataset(path):
    """
    Reads a dataset as .txt-file and returns its values.
    """
    file = open(os.path.join(path), 'r')

    x = []
    y = []
    switch = True
    for line in file:
        if switch:
            x.append([float(elt) for elt in line.split(',')])
            switch = False
        else:
            y.append([float(elt) for elt in line.split(',')])
            switch = True
    file.close()

    return np.array(x), np.array(y)








# --- Particle Features -----------------------------------------------------------------






def particle_bounding_box(array, imageheight=125, slicesize=SLICE_SIZE):
    """
    Returns the bounding box of a cloud particle as a
    starting point, the width and the height.
    """
    min_x = slicesize-1
    max_x = 0
    min_y = imageheight-1
    max_y = 0

    for y in range(imageheight):
        for x in range(slicesize):
            if (array[y*slicesize+x] != 0 \
            and array[y*slicesize+x] != '0'):
                if x > max_x:
                    max_x = x
                if x < min_x:
                    min_x = x
                if y > max_y:
                    max_y = y
                if y < min_y:
                    min_y = y
    return (min_x, min_y), max_x-min_x, max_y-min_y




















# --- Graphical Representations ----------------------------------------------------------------------------

def particle_distribution(arrays):
    """
    Shows particle distribution for seconds of day
    """
    pass







# --- Experimental Functions - In Construction !!! --------------------------------------

def pearson_r(array, slicesize=64):
    """
    Computes the Pearson Correlation Coefficient of an optical array.
    """
    points = scatter_array(array, slicesize)
    return round(pearsonr(points[:,0], points[:,1])[0], 3)
