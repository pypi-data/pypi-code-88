"""
Library of SPAM functions for dealing with labelled images
Copyright (C) 2020 SPAM Contributors

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy

import sys
import os

from . import labelToolkit

import scipy.ndimage
import scipy.spatial
import matplotlib
import math
import progressbar
import spam.filters
import multiprocessing
import spam.DIC

# Define a random colourmap for showing labels
#   This is taken from https://gist.github.com/jgomezdans/402500
randomCmapVals = numpy.random.rand(256, 3)
randomCmapVals[0, :] = numpy.array([1.0, 1.0, 1.0])
randomCmapVals[-1, :] = numpy.array([0.0, 0.0, 0.0])
randomCmap = matplotlib.colors.ListedColormap(randomCmapVals)
del randomCmapVals


# If you change this, remember to change the typedef in tools/labelToolkit/labelToolkitC.hpp
labelType = '<u4'

# Global number of processes
nProcessesDefault = multiprocessing.cpu_count()

def boundingBoxes(lab):
    """
    Returns bounding boxes for labelled objects using fast C-code which runs a single time through lab

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

    Returns
    -------
        boundingBoxes : lab.max()x6 array of ints
            This array contains, for each label, 6 integers:

            - Zmin, Zmax
            - Ymin, Ymax
            - Xmin, Xmax

    Note
    ----
        Bounding boxes `are not slices` and so to extract the correct bounding box from a numpy array you should use:
            lab[ Zmin:Zmax+1, Ymin:Ymax+1, Xmin:Xmax+1 ]
        Otherwise said, the bounding box of a single-voxel object at 1,1,1 will be:
            1,1,1,1,1,1

        Also note: for labelled images where some labels are missing, the bounding box returned for this case will be obviously wrong: `e.g.`, Zmin = (z dimension-1) and Zmax = 0

    """
    lab = lab.astype(labelType)

    boundingBoxes = numpy.zeros((lab.max() + 1, 6), dtype='<u2')

    labelToolkit.boundingBoxes(lab, boundingBoxes)

    return boundingBoxes


def centresOfMass(lab, boundingBoxes=None, minVol=None):
    """
    Calculates (binary) centres of mass of each label in labelled image

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        minVol : int, optional
            The minimum volume in vx to be treated, any object below this threshold is returned as 0

    Returns
    -------
        centresOfMass : lab.max()x3 array of floats
            This array contains, for each label, 3 floats, describing the centre of mass of each label in Z, Y, X order
    """
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    if minVol is None:
        minVol = 0

    lab = lab.astype(labelType)

    centresOfMass = numpy.zeros((lab.max() + 1, 3), dtype='<f4')

    labelToolkit.centresOfMass(lab, boundingBoxes, centresOfMass, minVol)

    return centresOfMass


def volumes(lab, boundingBoxes=None):
    """
    Calculates (binary) volumes each label in labelled image, using potentially slow numpy.where

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

    Returns
    -------
        volumes : lab.max()x1 array of ints
            This array contains the volume in voxels of each label
    """
    # print "label.toolkit.volumes(): Warning this is a crappy python implementation"

    lab = lab.astype(labelType)

    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)

    volumes = numpy.zeros((lab.max() + 1), dtype='<u4')

    labelToolkit.volumes(lab, boundingBoxes, volumes)

    return volumes


def equivalentRadii(lab, boundingBoxes=None, volumes=None):
    """
    Calculates (binary) equivalent sphere radii of each label in labelled image

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        volumes : lab.max()x1 array of ints
            Vector contining volumes, if this is passed, the others are ignored

    Returns
    -------
        equivRadii : lab.max()x1 array of floats
            This array contains the equivalent sphere radius in pixels of each label
    """
    def vol2rad(volumes):
        return ((3.0 * volumes) / (4.0 * numpy.pi))**(1.0 / 3.0)

    # If we have volumes, just go for it
    if volumes is not None:
        return vol2rad(volumes)

    # If we don't have bounding boxes, recalculate them
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)

    return vol2rad(spam.label.volumes(lab, boundingBoxes=boundingBoxes))


def momentOfInertia(lab, boundingBoxes=None, minVol=None, centresOfMass=None):
    """
    Calculates (binary) moments of inertia of each label in labelled image

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

        minVol : int, optional
            The minimum volume in vx to be treated, any object below this threshold is returned as 0
            Default = default for spam.label.centresOfMass

    Returns
    -------
        eigenValues : lab.max()x3 array of floats
            The values of the three eigenValues of the moment of inertia of each labelled shape

        eigenVectors : lab.max()x9 array of floats
            3 x Z,Y,X components of the three eigenValues in the order of the eigenValues
    """
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    if centresOfMass is None:
        centresOfMass = spam.label.centresOfMass(lab, boundingBoxes=boundingBoxes, minVol=minVol)

    lab = lab.astype(labelType)

    eigenValues = numpy.zeros((lab.max() + 1, 3), dtype='<f4')
    eigenVectors = numpy.zeros((lab.max() + 1, 9), dtype='<f4')

    labelToolkit.momentOfInertia(lab, boundingBoxes, centresOfMass, eigenValues, eigenVectors)

    return [eigenValues, eigenVectors]


def ellipseAxes(lab, volumes=None, MOIeigenValues=None, enforceVolume=True, twoD=False):
    """
    Calculates length of half-axes a,b,c of the ellipitic fit of the particle.
    These are half-axes and so are comparable to the radius -- and not the diameter -- of the particle.

    See appendix of for inital work:
        "Three-dimensional study on the interconnection and shape of crystals in a graphic granite by X-ray CT and image analysis.", Ikeda, S., Nakano, T., & Nakashima, Y. (2000).

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels
            Note: This is not strictly necessary if volumes and MOI is given

        volumes : 1D array of particle volumes (optional, default = None)
            Volumes of particles (length of array = lab.max())

        MOIeigenValues : lab.max()x3 array of floats, (optional, default = None)
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        enforceVolume = bool (default = True)
            Should a, b and c be scaled to enforce the fitted ellipse volume to be
            the same as the particle?
            This causes eigenValues are no longer completely consistent with fitted ellipse

        twoD : bool (default = False)
            Are these in fact 2D ellipses?
            Not implemented!!

    Returns
    -------
        ABCaxes : lab.max()x3 array of floats
            a, b, c lengths of particle in pixels

    Note
    -----
        Our elliptic fit is not necessarily of the same volume as the original particle,
        although by default we scale all axes linearly with `enforceVolumes` to enforce this condition.

        Reminder: volume of an ellipse is (4/3)*pi*a*b*c

        Useful check from TM: Ia = (4/15)*pi*a*b*c*(b**2+c**2)

        Function contributed by Takashi Matsushima (University of Tsukuba)
    """
    # Full ref:
    # @misc{ikeda2000three,
    #         title={Three-dimensional study on the interconnection and shape of crystals in a graphic granite by X-ray CT and image analysis},
    #         author={Ikeda, S and Nakano, T and Nakashima, Y},
    #         year={2000},
    #         publisher={De Gruyter}
    #      }

    if volumes is None:
        volumes = spam.label.volumes(lab)
    if MOIeigenValues is None:
        MOIeigenValues = spam.label.momentOfInertia(lab)[0]

    ABCaxes = numpy.zeros((volumes.shape[0], 3))

    Ia = MOIeigenValues[:, 0]
    Ib = MOIeigenValues[:, 1]
    Ic = MOIeigenValues[:, 2]

    # Initial derivation -- has quite a different volume from the original particle
    # Use the particle's V. This is a source of inconsistency,
    # since the condition V = (4/3) * pi * a * b * c is not necessarily respected
    # ABCaxes[:,2] = numpy.sqrt( numpy.multiply((5.0/(2.0*volumes.ravel())),( Ib + Ia - Ic ) ) )
    # ABCaxes[:,1] = numpy.sqrt( numpy.multiply((5.0/(2.0*volumes.ravel())),( Ia + Ic - Ib ) ) )
    # ABCaxes[:,0] = numpy.sqrt( numpy.multiply((5.0/(2.0*volumes.ravel())),( Ic + Ib - Ia ) ) )

    mask = numpy.logical_and(Ia != 0, numpy.isfinite(Ia))
    # Calculate a, b and c: TM calculation 2018-03-30
    # 2018-04-30 EA and MW: swap A and C so that A is the biggest
    ABCaxes[mask, 2] = ((15.0 / (8.0 * numpy.pi)) * numpy.square((Ib[mask] + Ic[mask] - Ia[mask])) / numpy.sqrt(((Ia[mask] - Ib[mask] + Ic[mask]) * (Ia[mask] + Ib[mask] - Ic[mask])))) ** (1.0 / 5.0)
    ABCaxes[mask, 1] = ((15.0 / (8.0 * numpy.pi)) * numpy.square((Ic[mask] + Ia[mask] - Ib[mask])) / numpy.sqrt(((Ib[mask] - Ic[mask] + Ia[mask]) * (Ib[mask] + Ic[mask] - Ia[mask])))) ** (1.0 / 5.0)
    ABCaxes[mask, 0] = ((15.0 / (8.0 * numpy.pi)) * numpy.square((Ia[mask] + Ib[mask] - Ic[mask])) / numpy.sqrt(((Ic[mask] - Ia[mask] + Ib[mask]) * (Ic[mask] + Ia[mask] - Ib[mask])))) ** (1.0 / 5.0)

    if enforceVolume:
        # Compute volume of ellipse:
        ellipseVol = (4.0 / 3.0) * numpy.pi * ABCaxes[:, 0] * ABCaxes[:, 1] * ABCaxes[:, 2]
        # filter zeros and infs
        # print volumes.shape
        # print ellipseVol.shape
        volRatio = (volumes[mask] / ellipseVol[mask])**(1.0 / 3.0)
        # print volRatio
        ABCaxes[mask, 0] = ABCaxes[mask, 0] * volRatio
        ABCaxes[mask, 1] = ABCaxes[mask, 1] * volRatio
        ABCaxes[mask, 2] = ABCaxes[mask, 2] * volRatio

    return ABCaxes


def convertLabelToFloat(lab, vector):
    """
    Replaces all values of a labelled array with a given value.
    Useful for visualising properties attached to labels, `e.g.`, sand grain displacements.

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        vector : a lab.max()x1 vector with values to replace each label with

    Returns
    -------
        relabelled : 3D array of converted floats
    """
    lab = lab.astype(labelType)

    relabelled = numpy.zeros_like(lab, dtype='<f4')

    vector = vector.ravel().astype('<f4')

    labelToolkit.labelToFloat(lab, vector, relabelled)

    return relabelled


def makeLabelsSequential(lab):
    """
    This function fills gaps in labelled images,
    by relabelling them to be sequential integers.
    Don't forget to recompute all your grain properties since the label numbers will change

    Parameters
    -----------
        lab : 3D numpy array of ints ( of type spam.label.toolkit.labelType)
            An array of labels with 0 as the background

    Returns
    --------
        lab : 3D numpy array of ints ( of type spam.label.toolkit.labelType)
            An array of labels with 0 as the background
    """
    maxLabel = int(lab.max())
    lab = lab.astype(labelType)

    uniqueLabels = numpy.unique(lab)
    # print uniqueLabels

    relabelMap = numpy.zeros((maxLabel + 1), dtype=labelType)
    relabelMap[uniqueLabels] = range(len(uniqueLabels))

    labelToolkit.relabel(lab, relabelMap)

    return lab


def getLabel(labelledVolume, label, boundingBoxes=None, centresOfMass=None, margin=0, extractCube=False, extractCubeSize=None, maskOtherLabels=True, labelDilate=0, labelDilateMaskOtherLabels=False):
    """
    Helper function to extract labels from a labelled image/volume.
    A dictionary is returned with the a subvolume around the particle.
    Passing boundingBoxes and centresOfMass is highly recommended.

    Parameters
    ----------
        labelVolume : 3D array of ints
            3D Labelled volume

        label : int
            Label that we want information about

        boundingBoxes : nLabels*2 array of ints, optional
            Bounding boxes as returned by ``boundingBoxes``.
            Optional but highly recommended.
            If unset, bounding boxes are recalculated for every call.

        centresOfMass : nLabels*3 array of floats, optional
            Centres of mass as returned by ``centresOfMass``.
            Optional but highly recommended.
            If unset, centres of mass are recalculated for every call.

        extractCube : bool, optional
            Return label subvolume in the middle of a cube?
            Default = False

        extractCubeSize : int, optional
            half-size of cube to extract.
            Default = calculate minimum cube

        margin : int, optional
            Extract a ``margin`` pixel margin around bounding box or cube.
            Default = 0

        maskOtherLabels : bool, optional
            In the returned subvolume, should other labels be masked?
            If true, the mask is directly returned.
            Default = True

        labelDilate : int, optional
            Number of times label should be dilated before returning it?
            This can be useful for catching the outside/edge of an image.
            ``margin`` should at least be equal to this value.
            Requires ``maskOtherLabels``.
            Default = 0

        labelDilateMaskOtherLabels : bool, optional
            Strictly cut the other labels out of the dilated image of the requested label?
            Only pertinent for positive labelDilate values.
            Default = False


    Returns
    -------
        Dictionary containing:

            Keys:
                subvol : 3D array of bools or ints
                    subvolume from labelled image

                slice : tuple of 3*slices
                    Slice used to extract subvol for the bounding box mode

                sliceCube : tuple of 3*slices
                    Slice used to extract subvol for the cube mode, warning,
                    if the label is near the edge, this is the slice up to the edge,
                    and so it will be smaller than the returned cube

                boundingBox : 1D numpy array of 6 ints
                    Bounding box, including margin, in bounding box mode. Contains:
                    [Zmin, Zmax, Ymin, Ymax, Xmin, Xmax]
                    Note: uses the same convention as spam.label.boundingBoxes, so
                    if you want to use this to extract your subvolume, add +1 to max

                boundingBoxCube : 1D numpy array of 6 ints
                    Bounding box, including margin, in cube mode. Contains:
                    [Zmin, Zmax, Ymin, Ymax, Xmin, Xmax]
                    Note: uses the same convention as spam.label.boundingBoxes, so
                    if you want to use this to extract your subvolume, add +1 to max

                centreOfMassABS : 3*float
                    Centre of mass with respect to ``labelVolume``

                centreOfMassREL : 3*float
                    Centre of mass with respect to ``subvol``

                volumeInitial : int
                    Volume of label (before dilating)

                volumeDilated : int
                    Volume of label (after dilating, if requested)

    """
    import spam.mesh
    if boundingBoxes is None:
        print("\tlabel.toolkit.getLabel(): Bounding boxes not passed.")
        print("\tThey will be recalculated for each label, highly recommend calculating outside this function")
        boundingBoxes = spam.label.boundingBoxes(labelledVolume)

    if centresOfMass is None:
        print("\tlabel.toolkit.getLabel(): Centres of mass not passed.")
        print("\tThey will be recalculated for each label, highly recommend calculating outside this function")
        centresOfMass = spam.label.centresOfMass(labelledVolume)

    # Check if there is a bounding box for this label:
    if label >= boundingBoxes.shape[0]:
        return
        raise "No bounding boxes for this grain"

    bbo = boundingBoxes[label]
    com = centresOfMass[label]
    comRound = numpy.floor(centresOfMass[label])

    # 1. Check if boundingBoxes are correct:
    if (bbo[0] == labelledVolume.shape[0] - 1) and \
       (bbo[1] == 0) and \
       (bbo[2] == labelledVolume.shape[1] - 1) and \
       (bbo[3] == 0) and \
       (bbo[4] == labelledVolume.shape[2] - 1) and \
       (bbo[5] == 0):
        pass
        #print("\tlabel.toolkit.getLabel(): Label {} does not exist".format(label))

    else:
        # Define output dictionary since we'll add different things to it
        output = {}
        output['centreOfMassABS'] = com

        # We have a bounding box, let's extract it.
        if extractCube:
            # Calculate offsets between centre of mass and bounding box
            offsetTop = numpy.ceil(com - bbo[0::2])
            offsetBot = numpy.ceil(com - bbo[0::2])
            offset = numpy.max(numpy.hstack([offsetTop, offsetBot]))

            # If is none, assume closest fitting cube.
            if extractCubeSize is not None:
                if extractCubeSize < offset:
                    print("\tlabel.toolkit.getLabel(): size of desired cube is smaller than minimum to contain label. Continuing anyway.")
                offset = int(extractCubeSize)

            # if a margin is set, add it to offset
            #if margin is not None:
            offset += margin

            offset = int(offset)

            # we may go outside the volume. Let's check this
            labSubVol = numpy.zeros((3 * [2 * offset + 1]))

            topOfSlice = numpy.array([int(comRound[0] - offset),
                                      int(comRound[1] - offset),
                                      int(comRound[2] - offset)])
            botOfSlice = numpy.array([int(comRound[0] + offset + 1),
                                      int(comRound[1] + offset + 1),
                                      int(comRound[2] + offset + 1)])

            labSubVol = spam.helpers.slicePadded(labelledVolume, [topOfSlice[0], botOfSlice[0], topOfSlice[1], botOfSlice[1], topOfSlice[2], botOfSlice[2]])

            output['sliceCube'] = (slice(topOfSlice[0], botOfSlice[0]),
                                   slice(topOfSlice[1], botOfSlice[1]),
                                   slice(topOfSlice[2], botOfSlice[2]))

            output['boundingBoxCube'] = numpy.array([topOfSlice[0], botOfSlice[0]-1, topOfSlice[1], botOfSlice[1]-1, topOfSlice[2], botOfSlice[2]-1])

            output['centreOfMassREL'] = com - topOfSlice

        # We have a bounding box, let's extract it.
        else:
            topOfSlice = numpy.array([int(bbo[0] - margin),
                                      int(bbo[2] - margin),
                                      int(bbo[4] - margin)])
            botOfSlice = numpy.array([int(bbo[1] + margin + 1),
                                      int(bbo[3] + margin + 1),
                                      int(bbo[5] + margin + 1)])

            labSubVol = spam.helpers.slicePadded(labelledVolume, [topOfSlice[0], botOfSlice[0], topOfSlice[1], botOfSlice[1], topOfSlice[2], botOfSlice[2]])

            output['slice'] = (slice(topOfSlice[0], botOfSlice[0]),
                               slice(topOfSlice[1], botOfSlice[1]),
                               slice(topOfSlice[2], botOfSlice[2]))

            output['boundingBox'] = numpy.array([topOfSlice[0], botOfSlice[0]-1, topOfSlice[1], botOfSlice[1]-1, topOfSlice[2], botOfSlice[2]-1])

            output['centreOfMassREL'] = com - topOfSlice

        # Get mask for this label
        maskLab = labSubVol == label
        volume = numpy.sum(maskLab)
        output['volumeInitial'] = volume

        # if we should mask, just return the mask.
        if maskOtherLabels:
            # 2019-09-07 EA: changing dilation/erosion into a single pass by a spherical element, rather than repeated
            # iterations of the standard.
            if labelDilate > 0:
                if labelDilate >= margin:
                    print("\tlabel.toolkit.getLabel(): labelDilate requested with a margin smaller than or equal to the number of times to dilate. I hope you know what you're doing!")
                strucuringElement = spam.mesh.structuringElement(radius=labelDilate, order=2, dim=3)
                maskLab = scipy.ndimage.morphology.binary_dilation(maskLab, structure=strucuringElement, iterations=1)
                if labelDilateMaskOtherLabels:
                    # remove voxels that are neither our label nor pore
                    maskLab[numpy.logical_and(labSubVol!=label, labSubVol!=0)] = 0
            if labelDilate < 0:
                strucuringElement = spam.mesh.structuringElement(radius=-1*labelDilate, order=2, dim=3)
                maskLab = scipy.ndimage.morphology.binary_erosion(maskLab, structure=strucuringElement, iterations=1)

            # Just overwrite "labSubVol"
            labSubVol = maskLab
            # Update volume output
            output['volumeDilated'] = labSubVol.sum()

        output['subvol'] = labSubVol

        return output


def getImagettesLabelled(lab1, label, Phi, im1, im2, searchRange, boundingBoxes, centresOfMass, margin=0, labelDilate=0, maskOtherLabels=True, applyF='all', volumeThreshold=100):
    """
    This function is responsible for extracting correlation windows ("imagettes") from two larger images (im1 and im2) with the help of a labelled im1.
    This is generally to do image correlation, this function will be used for spam-ddic and pixelSearch modes.

    Parameters
    ----------
        lab1 : 3D numpy array of ints
            Labelled image containing nLabels

        label : int
            Label of interest

        Phi : 4x4 numpy array of floats
            Phi matrix representing the movement of imagette1,
            if not equal to `I`, imagette1 is deformed by the non-translation parts of Phi (F)
            and the displacement is added to the search range (see below)

        im1 : 3D numpy array
            This is the large input reference image of greyvalues

        im2 :  3D numpy array
            This is the large input deformed image of greyvalues

        searchRange : 6-component numpy array of ints
            This defines where imagette2 should be extracted with respect to imagette1's position in im1.
            The 6 components correspond to [ Zbot Ztop Ybot Ytop Xbot Xtop ].
            If Z, Y and X values are the same, then imagette2 will be displaced and the same size as imagette1.
            If 'bot' is lower than 'top', imagette2 will be larger in that dimension

        boundingBoxes : nLabels*2 array of ints
            Bounding boxes as returned by ``boundingBoxes``

        centresOfMass : nLabels*3 array of floats
            Centres of mass as returned by ``centresOfMass``

        margin : int, optional
            Margin around the grain to extract in pixels
            Default = 0

        labelDilate : int, optional
            How much to dilate the label before computing the mask?
            Default = 0

        maskOtherLabels : bool, optional
            In the returned subvolume, should other labels be masked?
            If true, the mask is directly returned.
            Default = True

        applyF : string, optional
            If a non-identity Phi is passed, should the F be applied to the returned imagette1?
            Options are: 'all', 'rigid', 'no'
            Default = 'all'
            Note: as of January 2021, it seems to make more sense to have this as 'all' for pixelSearch, and 'no' for local DIC

        volumeThreshold : int, optional
            Pixel volume of labels that are discarded
            Default = 100

    Returns
    -------
        Dictionary :

            'imagette1' :    3D numpy array,

            'imagette1mask': 3D numpy array of same size as imagette1 or None,

            'imagette2':     3D numpy array, bigger or equal size to imagette1

            'returnStatus':  int,
                Describes success in extracting imagette1 and imagette2.
                If == 1 success, otherwise negative means failure.

            'pixelSearchOffset': 3-component list of ints
                Coordinates of the top of the pixelSearch range in im1, i.e., the displacement that needs to be
                added to the raw pixelSearch output to make it a im1 -> im2 displacement
    """
    returnStatus  = 1
    imagette1     = None
    imagette1mask = None
    imagette2     = None

    intDisplacement = numpy.round(Phi[0:3, 3]).astype(int)
    PhiNoDisp = Phi.copy()
    #PhiNoDisp[0:3,-1] -= intDisplacement
    PhiNoDisp[0:3,-1] = numpy.zeros(3)
    if applyF == 'rigid':
        PhiNoDisp = spam.deformation.computeRigidPhi(PhiNoDisp)

    gottenLabel = getLabel(lab1, label,
                           extractCube=False,
                           boundingBoxes=boundingBoxes,
                           centresOfMass=centresOfMass,
                           margin=labelDilate + margin,
                           maskOtherLabels=True,
                           labelDilate=labelDilate,
                           labelDilateMaskOtherLabels=maskOtherLabels)

    # In case the label is missing or the Phi is duff
    if gottenLabel is None or not numpy.all(numpy.isfinite(Phi)):
        returnStatus = -7

    else:
        # Maskette 1 is either a boolean array if args.MASK
        #   otherwise it contains ints i.e., labels

        # Use new padded slicer, to remain aligned with getLabel['subvol']
        #  + add 1 on the "max" side for bounding box -> slice
        imagette1 = spam.helpers.slicePadded(im1, gottenLabel['boundingBox'] + numpy.array([0,1,0,1,0,1]))

        if applyF == "all" or applyF == "rigid":
            imagette1     = spam.DIC.applyPhi(imagette1,
                                              PhiNoDisp,
                                              PhiCentre=gottenLabel['centreOfMassREL'])
            imagette1mask = spam.DIC.applyPhi(gottenLabel['subvol'] > 0,
                                              PhiNoDisp,
                                              PhiCentre=gottenLabel['centreOfMassREL'],
                                              interpolationOrder=0) > 0
        elif applyF == "no":
            imagette1mask = gottenLabel['subvol']
        else:
            print("spam.label.getImagettesLabelled(): unknown option for applyF options are: ['all', 'rigid', 'no']")

        maskette1vol = numpy.sum(imagette1mask)

        if maskette1vol > volumeThreshold:
            # 2020-09-25 OS and EA: Prepare startStop array for imagette 2 to be extracted with new
            #   slicePadded, this should solved "Boss: failed imDiff" and RS=-5 forever
            startStopIm2 = [int(gottenLabel['boundingBox'][0] - margin - max(labelDilate, 0) + searchRange[0] + intDisplacement[0]    ),
                            int(gottenLabel['boundingBox'][1] + margin + max(labelDilate, 0) + searchRange[1] + intDisplacement[0] + 1),
                            int(gottenLabel['boundingBox'][2] - margin - max(labelDilate, 0) + searchRange[2] + intDisplacement[1]    ),
                            int(gottenLabel['boundingBox'][3] + margin + max(labelDilate, 0) + searchRange[3] + intDisplacement[1] + 1),
                            int(gottenLabel['boundingBox'][4] - margin - max(labelDilate, 0) + searchRange[4] + intDisplacement[2]    ),
                            int(gottenLabel['boundingBox'][5] + margin + max(labelDilate, 0) + searchRange[5] + intDisplacement[2] + 1)]

            imagette2 = spam.helpers.slicePadded(im2, startStopIm2)

            #imagette2imagette1sizeDiff = numpy.array(imagette2.shape) - numpy.array(imagette1.shape)

            # If all of imagette2 is nans it fell outside im2 (or in any case it's going to be difficult to correlate)
            if numpy.all(numpy.isnan(imagette2)):
                returnStatus = -5
        else:
            # Failed volume condition
            returnStatus = -5

    return {'imagette1':            imagette1,
            'imagette1mask':        imagette1mask,
            'imagette2':            imagette2,
            'returnStatus':         returnStatus,
            'pixelSearchOffset':    searchRange[0::2] - numpy.array([max(labelDilate, 0)]*3) - margin + intDisplacement
            }


def labelsOnEdges(lab):
    """
    Return labels on edges of volume

    Parameters
    ----------
        lab : 3D numpy array of ints
            Labelled volume

    Returns
    -------
        uniqueLabels : list of ints
            List of labels on edges
    """

    labelsVector = numpy.arange(lab.max() + 1)

    uniqueLabels = []

    uniqueLabels.append(numpy.unique(lab[:, :, 0]))
    uniqueLabels.append(numpy.unique(lab[:, :, -1]))
    uniqueLabels.append(numpy.unique(lab[:, 0, :]))
    uniqueLabels.append(numpy.unique(lab[:, -1, :]))
    uniqueLabels.append(numpy.unique(lab[0, :, :]))
    uniqueLabels.append(numpy.unique(lab[-1, :, :]))

    # Flatten list of lists:
    # https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    uniqueLabels = [item for sublist in uniqueLabels for item in sublist]

    # There might well be labels that appears on multiple faces of the cube, remove them
    uniqueLabels = numpy.unique(numpy.array(uniqueLabels))

    return uniqueLabels.astype(labelType)


def removeLabels(lab, listOfLabelsToRemove):
    """
    Resets a list of labels to zero in a labelled volume.

    Parameters
    ----------
        lab : 3D numpy array of ints
            Labelled volume

        listOfLabelsToRemove : list-like of ints
            Labels to remove

    Returns
    -------
        lab : 3D numpy array of ints
            Labelled volume with desired labels blanked

    Note
    ----
        You might want to use `makeLabelsSequential` after using this function,
        but don't forget to recompute all your grain properties since the label numbers will change
    """
    lab = lab.astype(labelType)

    # define a vector with sequential ints
    arrayOfLabels = numpy.arange(lab.max() + 1, dtype=labelType)

    # Remove the ones that have been asked for
    for l in listOfLabelsToRemove:
        arrayOfLabels[l] = 0

    labelToolkit.relabel(lab, arrayOfLabels)

    return lab


def setVoronoi(lab, poreEDT=None, maxPoreRadius=10):
    """
    This function computes an approximate set Voronoi for a given labelled image.
    This is a voronoi which does not have straight edges, and which necessarily
    passes through each contact point, so it is respectful of non-spherical grains.

    See:
    Schaller, F. M., Kapfer, S. C., Evans, M. E., Hoffmann, M. J., Aste, T., Saadatfar, M., ... & Schroder-Turk, G. E. (2013). Set Voronoi diagrams of 3D assemblies of aspherical particles. Philosophical Magazine, 93(31-33), 3993-4017.
    https://doi.org/10.1080/14786435.2013.834389

    and

    Weis, S., Schonhofer, P. W., Schaller, F. M., Schroter, M., & Schroder-Turk, G. E. (2017). Pomelo, a tool for computing Generic Set Voronoi Diagrams of Aspherical Particles of Arbitrary Shape. In EPJ Web of Conferences (Vol. 140, p. 06007). EDP Sciences.

    Parameters
    -----------
        lab: 3D numpy array of labelTypes
            Labelled image

        poreEDT: 3D numpy array of floats (optional, default = None)
            Euclidean distance map of the pores.
            If not given, it is computed by scipy.ndimage.morphology.distance_transform_edt

        maxPoreRadius: int (optional, default = 10)
            Maximum pore radius to be considered (this threshold is for speed optimisation)

    Returns
    --------
        lab: 3D numpy array of labelTypes
            Image labelled with set voronoi labels
    """
    if poreEDT is None:
        # print( "\tlabel.toolkit.setVoronoi(): Calculating the Euclidean Distance Transform of the pore with" )
        # print  "\t\tscipy.ndimage.morphology.distance_transform_edt, this takes a lot of memory"
        poreEDT = scipy.ndimage.morphology.distance_transform_edt(lab == 0).astype('<f4')

    lab = lab.astype(labelType)
    labOut = numpy.zeros_like(lab)
    maxPoreRadius = int(maxPoreRadius)

    # Prepare sorted distances in a cube to fit a maxPoreRadius.
    # This precomutation saves a lot of time
    # Local grid of values, centred at zero
    gridD = numpy.mgrid[-maxPoreRadius:maxPoreRadius + 1,
                        -maxPoreRadius:maxPoreRadius + 1,
                        -maxPoreRadius:maxPoreRadius + 1]

    # Compute distances from centre
    Rarray = numpy.sqrt(numpy.square(gridD[0]) + numpy.square(gridD[1]) + numpy.square(gridD[2])).ravel()
    sortedIndices = numpy.argsort(Rarray)

    # Array to hold sorted points
    coords = numpy.zeros((len(Rarray), 3), dtype='<i4')
    # Fill in with Z, Y, X points in order of distance to centre
    coords[:, 0] = gridD[0].ravel()[sortedIndices]
    coords[:, 1] = gridD[1].ravel()[sortedIndices]
    coords[:, 2] = gridD[2].ravel()[sortedIndices]
    del gridD

    # Now define a simple array (by building a list) that gives the linear
    #   entry point into coords at the nearest integer values
    sortedDistances = Rarray[sortedIndices]
    indices = []
    n = 0
    i = 0
    while i <= maxPoreRadius + 1:
        if sortedDistances[n] >= i:
            # indices.append( [ i, n ] )
            indices.append(n)
            i += 1
        n += 1
    indices = numpy.array(indices).astype('<i4')

    # Call C++ code
    labelToolkit.setVoronoi(lab, poreEDT.astype('<f4'), labOut, coords, indices)

    return labOut


def labelTetrahedra(dims, points, connectivity):
    """
    Labels voxels corresponding to tetrahedra according to a connectivity matrix and node points

    Parameters
    ----------
        dims: tuple representing z,y,x dimensions of the desired labelled output

        points: number of points x 3 array of floats
            List of points that define the vertices of the tetrahedra in Z,Y,X format.
            These points are referred to by line number in the connectivity array

        connectivity: number of tetrahedra x 4 array of integers
            Connectivity matrix between points that define tetrahedra.
            Each line defines a tetrahedron whose number is the line number + 1.
            Each line contains 4 integers that indicate the 4 points in the nodePos array.

    Returns
    -------
        3D array of ints, shape = dims
            Labelled 3D volume where voxels are numbered according to the tetrahedron number they fall inside of
    """
    assert(len(dims) == 3),                        "spam.label.labelTetrahedra(): dim is not length 3"
    assert(points.shape[1] == 3),                  "spam.label.labelTetrahedra(): points doesn't have 3 colums"
    assert(connectivity.shape[1] == 4),            "spam.label.labelTetrahedra(): connectivity doesn't have 4 colums"
    assert(points.shape[0] >= connectivity.max()), "spam.label.labelTetrahedra(): connectivity should not refer to points numbers biggest than the number of rows in points"

    dims = numpy.array(dims).astype('<u2')
    lab = numpy.ones(tuple(dims), dtype=labelType)*connectivity.shape[0]+1

    connectivity = connectivity.astype('<u4')
    points = points.astype('<f4')

    labelToolkit.tetPixelLabel(lab, connectivity, points)

    return lab


def labelTetrahedraForScipyDelaunay(dims, delaunay):
    """
    Labels voxels corresponding to tetrahedra coming from scipy.spatial.Delaunay
    Apparently the cells are not well-numbered, which causes a number of zeros
    when using `labelledTetrahedra`

    Parameters
    ----------
        dims: tuple
            represents z,y,x dimensions of the desired labelled output

        delaunay: "delaunay" object
            Object returned by scipy.spatial.Delaunay( centres )
            Hint: If using label.toolkit.centresOfMass( ), do centres[1:] to remove
            the position of zero.

    Returns
    -------
        lab: 3D array of ints, shape = dims
            Labelled 3D volume where voxels are numbered according to the tetrahedron number they fall inside of
    """

    # Big matrix of points poisitions
    points = numpy.zeros((dims[0] * dims[1] * dims[2], 3))

    mgrid = numpy.mgrid[0:dims[0], 0:dims[1], 0:dims[2]]
    for i in [0, 1, 2]:
        points[:, i] = mgrid[i].ravel()

    del mgrid

    lab = numpy.ones(tuple(dims), dtype=labelType)*delaunay.nsimplex+1
    lab = delaunay.find_simplex(points).reshape(dims)

    return lab


def fabricTensor(orientations):
    """
    Calculation of a second order fabric tensor from orientations

    Parameters
    ----------
        orientations: Nx3 array of floats
            Z, Y and X components of direction vectors
            Non-unit vectors are normalised.

    Returns
    -------
        N: 3x3 array of floats
            normalised second order fabric tensor
            with N[0,0] corresponding to z-z, N[1,1] to y-y and N[2,2] x-x

        F: 3x3 array of floats
            fabric tensor of the third kind (deviatoric part)
            with F[0,0] corresponding to z-z, F[1,1] to y-y and F[2,2] x-x

        a: float
            scalar anisotropy factor based on the deviatoric part F

    Note
    ----
        see [Kanatani, 1984] for more information on the fabric tensor
        and [Gu et al, 2017] for the scalar anisotropy factor

        Function contibuted by Max Wiebicke (Dresden University)
    """
    # from http://stackoverflow.com/questions/2850743/numpy-how-to-quickly-normalize-many-vectors
    norms = numpy.apply_along_axis(numpy.linalg.norm, 1, orientations)
    orientations = orientations / norms.reshape(-1, 1)

    # create an empty array
    N = numpy.zeros((3, 3))
    size = len(orientations)

    for i in range(size):
        orientation = orientations[i]
        tensProd = numpy.outer(orientation, orientation)
        N[:, :] = N[:, :] + tensProd

    # fabric tensor of the first kind
    N = N / size
    # fabric tensor of third kind
    F = (N - (numpy.trace(N) * (1. / 3.)) * numpy.eye(3, 3)) * (15. / 2.)

    # scalar anisotropy factor
    a = math.sqrt(3. / 2. * numpy.tensordot(F, F, axes=2))

    return N, F, a


def filterIsolatedCells(array, struct, size):
    """
    Return array with completely isolated single cells removed

    Parameters
    ----------
        array: 3-D (labelled or binary) array
            Array with completely isolated single cells

        struct: 3-D binary array
            Structure array for generating unique regions

        size: integer
            Size of the isolated cells to exclude
            (Number of Voxels)

    Returns
    -------
        filteredArray: 3-D (labelled or binary) array
            Array with minimum region size > size

    Notes
    -----
        function from: http://stackoverflow.com/questions/28274091/removing-completely-isolated-cells-from-python-array
    """

    filteredArray = ((array > 0) * 1).astype('uint8')
    idRegions, numIDs = scipy.ndimage.label(filteredArray, structure=struct)
    idSizes = numpy.array(scipy.ndimage.sum(filteredArray, idRegions, range(numIDs + 1)))
    areaMask = (idSizes <= size)
    filteredArray[areaMask[idRegions]] = 0

    filteredArray = ((filteredArray > 0) * 1).astype('uint8')
    array = filteredArray * array

    return array


def trueSphericity(lab, boundingBoxes=None, centresOfMass=None, gaussianFilterSigma=0.75, minVol=256):
    """
    Calculates the degree of True Sphericity (psi) for all labels, as per:
    "Sphericity measures of sand grains" Rorato et al., Engineering Geology, 2019
    and originlly proposed in: "Volume, shape, and roundness of rock particles", Waddell, The Journal of Geology, 1932.

    True Sphericity (psi) = Surface area of equivalent sphere / Actual surface area

    The actual surface area is computed by extracting each particle with getLabel, a Gaussian smooth of 0.75 is applied
    and the marching cubes algorithm from skimage is used to mesh the surface and compute the surface area.

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

        gaussianFilterSigma : float, optional
            Sigma of the Gaussian filter used to smooth the binarised shape
            Default = 0.75

        minVol : int, optional
            The minimum volume in vx to be treated, any object below this threshold is returned as 0
            Default = 256 voxels

    Returns
    -------
        trueSphericity : lab.max() array of floats
            The values of the degree of true sphericity for each particle

    Notes
    -----
        Function contributed by Riccardo Rorato (UPC Barcelona)

        Due to numerical errors, this value can be >1, it should be clipped at 1.0
    """
    import skimage.measure

    lab = lab.astype(labelType)

    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    if centresOfMass is None:
        centresOfMass = spam.label.centresOfMass(lab, boundingBoxes=boundingBoxes, minVol=minVol)


    trueSphericity = numpy.zeros((lab.max() + 1), dtype='<f4')

    sphereSurfaceArea = 4.0*numpy.pi*(equivalentRadii(lab, boundingBoxes=boundingBoxes)**2)

    for label in range(1, lab.max()+1):
        if not (centresOfMass[label]==numpy.array([0.0, 0.0, 0.0])).all():
            # Extract grain
            GL = getLabel(lab, label, boundingBoxes=boundingBoxes, centresOfMass=centresOfMass, extractCube=True, margin=2, maskOtherLabels=True)
            # Gaussian smooth
            grainCubeFiltered = scipy.ndimage.filters.gaussian_filter(GL['subvol'].astype('<f4'), sigma=gaussianFilterSigma)
            # mesh edge
            verts, faces, _, _ = skimage.measure.marching_cubes(grainCubeFiltered, level=0.5)
            # compute surface
            surfaceArea  = skimage.measure.mesh_surface_area(verts, faces)
            # compute psi
            trueSphericity[label] = sphereSurfaceArea[label]/surfaceArea
    return trueSphericity



def meanOrientation(orientations):
    """
    This function performs a Principal Component Analysis over a group of vectors in order to find the main direction of the set. Once the main direction is found, all the vectors are projected to the new basis.


    Parameters
    -----------

        orientations : Nx3 numpy array of floats
                        Z, Y and X components of direction vectors.
                        Non-unit vectors are normalised.

    Returns
    --------

        orientations_proj : Nx3 numpy array of floats with the [z,y,x] components of the projected vectors over the basis obtained in the Principal Component Analysis. All the projected vectors are normalized.

        main_axis : [z,y,x] components of the main axis of the data set.

        intermediate_axis : [z,y,x] components of the intermediate axis of the data set.

        minor_axis : [z,y,x] components of the minor axis of the data set.

    Notes
    -----
        PCA analysis taken from https://machinelearningmastery.com/calculate-principal-component-analysis-scratch-python/

    """

    # Read Number of Points
    numberOfPoints = orientations.shape[0]
    # Normalize all the vectors from http://stackoverflow.com/questions/2850743/numpy-how-to-quickly-normalize-many-vectors
    norms = numpy.apply_along_axis( numpy.linalg.norm, 1, orientations )
    orientations = orientations / norms.reshape( -1, 1 )
    # Flip if the z-component is located at z < 0
    for vector_i in range(numberOfPoints):
        z,y,x=orientations[vector_i]
        if z < 0: z = -z; y = -y; x = -x
        orientations[vector_i] = [z,y,x]
    # Run PCA
    orientationsPCA = numpy.concatenate((orientations, -1*orientations), axis=0) #COMENT
    # Compute mean of each column
    meanVal = numpy.mean(orientationsPCA, axis=0)
    # Center array
    orientationsPCA = orientationsPCA - meanVal
    # Compute covariance matrix of centered matrix
    covMat = numpy.cov(orientationsPCA.T)
    # Eigendecomposition of covariance matrix
    values, vectors = numpy.linalg.eig(covMat)
    # Decompose axis
    main_axis = vectors[:,numpy.argmax(values)]
    if main_axis[0]<0: main_axis[:]=-1*main_axis[:]
    intermediate_axis = vectors[:,3 - numpy.argmin(values) - numpy.argmax(values)]
    minor_axis = vectors[:,numpy.argmin(values)]

    # Project all vectors
    orientations_proj = numpy.zeros((numberOfPoints,3))
    for vector_i in range(numberOfPoints):
        orientations_proj[vector_i,0] = numpy.dot(orientations[vector_i,:],main_axis) / numpy.linalg.norm(main_axis)
        orientations_proj[vector_i,1] = numpy.dot(orientations[vector_i,:],intermediate_axis) / numpy.linalg.norm(intermediate_axis)
        orientations_proj[vector_i,2] = numpy.dot(orientations[vector_i,:],minor_axis) / numpy.linalg.norm(minor_axis)



    return orientations_proj, main_axis, intermediate_axis, minor_axis


#def _fixUndersegmentation(imLab, imGrey, listLabels, a, c, numVect=100, vect=None, boundingBoxes=None, centresOfMass=None, numberOfThreads=1, verbose=False):
    #"""
    #This function fix undersegmented particles using directional erosion over the particle
    #to get the seed for a new localized watershed.

    #Parameters
    #-----------
        #imLab : 3D numpy array
            #Labelled image

        #imGrey : 3D numpy array
            #Normalizaed greyscale of the labelled image, with a greyscale range between 0 and 1 and with peaks at 0.25 and 0.75. (You can use helpers.histogramTools.findHistogramPeaks and helpers.histogramTools.histogramNorm to obtain a normalized greyscale image)

        #listLabels : list of int
            #List of the labeles to work on

        #numVect : int
            #Number of vectors to run the directional erosion with
            #Default = 100

        #vect : list of n elements, each element correspond to a 1X3 array of floats
            #List of directional vectors for the directional erosion
            #Default None

        #a : int or float
            #Length of the secondary semi-axis of the structuring element

        #c : int or float
            #Lenght of the principal semi-axis of the structuring element

        #numberOfThreads : integer (optional, default = 1)
            #Number of Threads for multiprocessing of the directional erosion.
            #Default = 1

        #verbose : boolean (optional, default = False)
            #True for printing the evolution of the process
            #False for not printing the evolution of process

    #Returns
    #--------
        #imLab : 3D numpy array
            #New labelled image

    #Note
    #-----
        #Review spam.filters.morphologicalOperations.directionalErosion in order to
        #select properly the shape and size of the structuring element for the
        #directional erosion

    #"""
    #import spam.label

    #Check that a,c are valid inputs
    #if numpy.isnan(a) == True or numpy.isnan(c) == True:
        #print("\tlabel.fixUndersegmentation(): Parameters a or c are not valid. Some of them are NaN")
        #return
    #if a <= 0 or c <= 0:
        #print("\tlabel.fixUndersegmentation(): Parameters a or c are not valid. Some of them are negative or equal to zero")
        #return
    #Check that the greyscale image is normalized
    #if numpy.max(imGrey) > 1.0:
        #print("\tlabel.fixUndersegmentation(): The greyscale image is not normalized!")
        #return
    #Check that the list of vectors (if added) is a list
    #if vect is not None:
        #if isinstance(vect,list) == False:
            #print("\tlabel.fixUndersegmentation(): The directional vector must be a list")
            #return


    #Compute boundingBoxes if needed
    #if boundingBoxes is None:
        #boundingBoxes = spam.label.boundingBoxes(imLab)
    #if centresOfMass is None:
        #centresOfMass = spam.label.centresOfMass(imLab)
    #Compute the volume of the particles
    #volumes = spam.label.volumes(imLab)
    #Create the vectors for the directional erosion if needed
    #if vect is None:
        #import spam.plotting
        #vect = spam.plotting.orientationPlotter.SaffAndKuijlaarsSpiral(numVect)
        #vect = vect.tolist()
    #Initalize the variables
    #finishedCounter = 0
    #labelCounter = numpy.max(imLab)
    #labelDummy = numpy.zeros(imLab.shape)
    #successCounter = 0
    #pbar = progressbar.ProgressBar(maxval=len(listLabels)).start()
    #for i in range(len(listLabels)):
        #Continue = False
        #itCounter = 1
        #Get label
        #label_i = listLabels[i]
        #Get labelled subset data
        #labelData = spam.label.getLabel(imLab, label_i, boundingBoxes = boundingBoxes, centresOfMass = centresOfMass)
        #Check if label exists
        #if not labelData:
            #print("\tlabel.fixUndersegmentation(): This label does not exist: "+str(label_i))
            #Continue = True
        #else: # Labels exist!
            #bwIm = labelData['subvol']
        #while Continue == False:
            #Directional Erosion
            #imEroded = spam.filters.morphologicalOperations.directionalErosion(bwIm, vect,
                                                                               #a, c, numberOfThreads = numberOfThreads,
                                                                               #verbose = verbose)
            #Label the markers
            #markers, num_seeds = scipy.ndimage.label(imEroded)
            #New Segmentation
            #if verbose:
                #print('Processing label '+str(i)+' of '+str(len(listLabels))+'. Iteration #'+str(itCounter))
            #newSeg = spam.label.watershed(bwIm, markers=markers, verbose = verbose)
            #Check Number of Labels
            #if numpy.max(newSeg) > 1:
                #We have new labels! Lets check if they make sense
                #volNewSeg = spam.label.volumes(newSeg) / numpy.mean(volumes)
                #if any(volNewSeg > 0.3) == True:
                    #We have at least one new working particle
                    #Continue = True
                    #finishedCounter += 1
                    #pbar.update(finishedCounter)
                    #Assign the new labels to the grains
                    #for lab in numpy.unique(newSeg[newSeg != 0]):
                        #if volNewSeg[lab] < 0.3:
                            #Remove the labels that are too small
                            #newSeg = numpy.where(newSeg == lab, 0, newSeg)
                        #else:
                            #Assign new label to working particles
                            #newSeg = numpy.where( newSeg == lab, labelCounter + 1 , newSeg)
                            #labelCounter += 1
                    #Fill the holes inside the labels. (Usually needed when there are more markers than particles)
                    #fillNewSeg = numpy.zeros((newSeg.shape))
                    #for lab in numpy.unique(newSeg[newSeg != 0]):
                        #tempNewSeg = scipy.ndimage.morphology.binary_fill_holes(numpy.where(newSeg == lab, 1, 0))
                        #tempNewSeg = numpy.where(tempNewSeg == 1, lab, 0)
                        #fillNewSeg = fillNewSeg + tempNewSeg
                    #Create a disposable dummy sample to allocate the grains
                    #labelDummyUnit = numpy.zeros(labelDummy.shape)
                    #Alocate the grains
                    #labelDummyUnit[boundingBoxes[label_i][0] : boundingBoxes[label_i][1]+1,
                                   #boundingBoxes[label_i][2] : boundingBoxes[label_i][3]+1,
                                   #boundingBoxes[label_i][4] : boundingBoxes[label_i][5]+1] = fillNewSeg
                    #Add the grains
                    #labelDummy = labelDummy + labelDummyUnit
                    #Remove the label from the image
                    #imLab = spam.label.removeLabels(imLab, [label_i])
                    #Update the success counter
                    #successCounter += 1

                #else:
                    #We dont have any working new particles, lets modify the binarizing threshold to try to get it
                    #if itCounter != 4:
                        #We can modify the treshold
                        #itCounter += 1
                        #Grab the subset of the grain
                        #labelData = spam.label.getLabel(imLab, label_i,
                                                        #boundingBoxes = boundingBoxes,
                                                        #centresOfMass = centresOfMass)
                        #bwImOr = labelData['subvol']
                        #Get the same subset from the grey scale image
                        #greyIm_i = imGrey[boundingBoxes[label_i,0] : boundingBoxes[label_i,1]+1,
                                          #boundingBoxes[label_i,2] : boundingBoxes[label_i,3]+1,
                                          #boundingBoxes[label_i,4] : boundingBoxes[label_i,5]+1]
                        #Mask out the grey-level subset
                        #greyIm_i = greyIm_i * bwImOr
                        #Binarize the new image with a higher threshold
                        #bwIm = greyIm_i>= 0.5+itCounter*0.05
                    #else:
                        #We reached the maximum number of iterations, the grain can't be solved!
                        #Continue = True
                        #finishedCounter += 1
                        #pbar.update(finishedCounter)
            #else:
                #We dont have any new labels from the watershed, we should increase the binarizing threshold and do it again
                #if itCounter != 4:
                    #We can modify the treshold
                    #itCounter += 1
                    #Grab the subset of the grain
                    #labelData = spam.label.getLabel(imLab, label_i,
                                                    #boundingBoxes = boundingBoxes,
                                                    #centresOfMass = centresOfMass)
                    #bwImOr = labelData['subvol']
                    #Get the same subset from the grey scale image
                    #greyIm_i = imGrey[boundingBoxes[label_i,0] : boundingBoxes[label_i,1]+1,
                                      #boundingBoxes[label_i,2] : boundingBoxes[label_i,3]+1,
                                      #boundingBoxes[label_i,4] : boundingBoxes[label_i,5]+1]
                    #Mask out the grey-level subset
                    #greyIm_i = greyIm_i * bwImOr
                    #Binarize the new image with a higher threshold
                    #bwIm = greyIm_i>= 0.5+itCounter*0.05
                #else:
                    #We reached the maximum number of iterations, the grain can't be solved!
                    #Continue = True
                    #finishedCounter += 1
                    #pbar.update(finishedCounter)
    #We finish, lets add the new grains to the labelled image
    #imLab = imLab + labelDummy
    #Update the labels
    #imLab = spam.label.makeLabelsSequential(imLab)

    #pbar.finish()
    #print("\tlabel.fixUndersegmentation(): From "+str(len(listLabels))+" undersegmented labels, we successfully worked on "+str(successCounter))
    #return imLab


def convexVolume(lab, boundingBoxes=None, centresOfMass=None, volumes=None, nProcesses=nProcessesDefault, verbose=True):
    """
    This function compute the convex hull of each label of the labelled image and return a
    list with the convex volume of each particle.

    Parameters
    ----------
        lab : 3D array of integers
            Labelled volume, with lab.max() labels

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

        volumes : lab.max()x1 array of ints
            Volumes in format returned by ``volumes``
            If not defined (Default = None), it is recomputed by running ``volumes``

        nProcesses : integer (optional, default = nProcessesDefault)
            Number of processes for multiprocessing
            Default = number of CPUs in the system

        verbose : boolean (optional, default = False)
            True for printing the evolution of the process
            False for not printing the evolution of process

    Returns
    --------

        convexVolume : lab.max()x1 array of floats with the convex volume.

    Note
    ----
        convexVolume can only be computed for particles with volume greater than 3 voxels. If it is not the case, it will return 0.

    """
    lab = lab.astype(labelType)

    # Compute boundingBoxes if needed
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    # Compute centresOfMass if needed
    if centresOfMass is None:
        centresOfMass = spam.label.centresOfMass(lab)
    # Compute volumes if needed
    if volumes is None:
        volumes = spam.label.volumes(lab)
    # Compute number of labels
    nLabels = lab.max()

    # Result array
    convexVolume = numpy.zeros(nLabels+1, dtype='float')

    if verbose:
        widgets = [progressbar.FormatLabel(''), ' ', progressbar.Bar(), ' ', progressbar.AdaptiveETA()]
        pbar = progressbar.ProgressBar(widgets=widgets, maxval=nLabels)
        pbar.start()
        finishedNodes = 0

    # Function for convex volume
    global computeConvexVolume
    def computeConvexVolume(label):
        labelI = spam.label.getLabel(lab, label, boundingBoxes = boundingBoxes, centresOfMass = centresOfMass)
        subvol = labelI['subvol']
        points = numpy.transpose(numpy.where(subvol))
        try:
            hull = scipy.spatial.ConvexHull(points)
            deln = scipy.spatial.Delaunay(points[hull.vertices])
            idx = numpy.stack(numpy.indices(subvol.shape), axis = -1)
            out_idx = numpy.nonzero(deln.find_simplex(idx) + 1)
            hullIm = numpy.zeros(subvol.shape)
            hullIm[out_idx] = 1
            hullVol = spam.label.volumes(hullIm)
            return label, hullVol[-1]
        except:
            return label, 0

    # Run multiprocessing
    with multiprocessing.Pool(processes=nProcesses) as pool:
        for returns in pool.imap_unordered(computeConvexVolume, range(1, nLabels+1)):
            if verbose:
                finishedNodes += 1
                widgets[0] = progressbar.FormatLabel("  vol={:0>7.5f} ".format(returns[1]))
                pbar.update(finishedNodes)
            convexVolume[returns[0]] = returns[1]
        pool.close()
        pool.join()

    if verbose:
        pbar.finish()

    return convexVolume


def moveLabels(lab, PhiField, returnStatus = None, boundingBoxes=None, centresOfMass=None, margin=3, PhiCOM=True, threshold=0.5, labelDilate=0, nProcesses=nProcessesDefault):
    """
    This function applies a discrete Phi field (from DDIC?) over a labelled image.

    Parameters
    -----------
        lab : 3D numpy array
            Labelled image

        PhiField : (multidimensional x 4 x 4 numpy array of floats)
            Spatial field of Phis

        returnStatus : lab.max()x1 array of ints, optional
            Array with the return status for each label (usually returned by ``spam-ddic``)
            If not defined (Default = None), all the labels will be moved
            If returnStatus[i] == 2, the label will be moved, otherwise is omitted and erased from the final image

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

        margin : int, optional
            Margin, in pixels, to take in each label.
            Default = 3

        PhiCOM : bool, optional
            Apply Phi to centre of mass of particle?, otherwise it will be applied in the middle of the particle\'s bounding box.
            Default = True

        threshold : float, optional
             Threshold to keep interpolated voxels in the binary image.
             Default = 0.5

        labelDilate : int, optional
            Number of times label should be dilated/eroded before returning it.
            If ``labelDilate > 0`` a dilated label is returned, while ``labelDilate < 0`` returns an eroded label.
            Default = 0

        nProcesses : integer (optional, default = nProcessesDefault)
            Number of processes for multiprocessing
            Default = number of CPUs in the system

    Returns
    --------
        labOut : 3D numpy array
            New labelled image with the labels moved by the deformations established by the PhiField.

    """

    # Check for boundingBoxes
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    # Check for centresOfMass
    if centresOfMass is None:
        centresOfMass = spam.label.centresOfMass(lab)
    # Create output label image
    labOut = numpy.zeros_like(lab, dtype=spam.label.labelType)
    # Get number of labels
    numberOfLabels = min(lab.max(), PhiField.shape[0]-1)
    numberOfLabelsToMove = 0
    labelsToMove = []
    # Add the labels to move
    for label in range(1, numberOfLabels+1):
        # Skip the particles if the returnStatus == 2 and returnStatus != None
        if type(returnStatus) == numpy.ndarray and returnStatus[label] != 2:
            pass
        else: # Add the particles
            labelsToMove.append(label)
            numberOfLabelsToMove += 1

    # Function for moving labels
    global funMoveLabels
    def funMoveLabels(label):
        getLabelReturn = spam.label.getLabel(lab,
                                             label,
                                             labelDilate=labelDilate,
                                             margin=margin,
                                             boundingBoxes=boundingBoxes,
                                             centresOfMass=centresOfMass,
                                             extractCube=True)
        # Check that the label exist
        if getLabelReturn is not None:
            # Get Phi field
            Phi = PhiField[label].copy()
            # Phi will be split into a local part and a part of floored displacements
            disp = numpy.floor(Phi[0:3,-1]).astype(int)
            Phi[0:3,-1] -= disp
            # Check that the displacement exist
            if numpy.isfinite(disp).sum() == 3:
                # Just move binary label
                # Need to do backtracking here to avoid holes in the NN interpolation
                #   Here we will cheat and do order 1 and re-threshold full pixels
                if PhiCOM:
                    labSubvolDefInterp = spam.DIC.applyPhi(getLabelReturn['subvol'],
                                                           Phi=Phi,
                                                           interpolationOrder=1,
                                                           PhiCentre=getLabelReturn['centreOfMassREL'])
                else:
                    labSubvolDefInterp = spam.DIC.applyPhi(getLabelReturn['subvol'],
                                                           Phi=Phi,
                                                           interpolationOrder=1,
                                                           PhiCentre=(numpy.array(getLabelReturn['subvol'].shape)-1)/2.0)

                # "death mask"
                labSubvolDefMask = labSubvolDefInterp >= threshold

                del labSubvolDefInterp
                # Get the boundary of the cube
                topOfSlice = numpy.array([getLabelReturn['boundingBoxCube'][0] + disp[0],
                                          getLabelReturn['boundingBoxCube'][2] + disp[1],
                                          getLabelReturn['boundingBoxCube'][4] + disp[2]])

                botOfSlice = numpy.array([getLabelReturn['boundingBoxCube'][1] + disp[0],
                                          getLabelReturn['boundingBoxCube'][3] + disp[1],
                                          getLabelReturn['boundingBoxCube'][5] + disp[2]])

                topOfSliceCrop = numpy.array([max(topOfSlice[0], 0),
                                            max(topOfSlice[1], 0),
                                            max(topOfSlice[2], 0)])
                botOfSliceCrop = numpy.array([min(botOfSlice[0], lab.shape[0]),
                                            min(botOfSlice[1], lab.shape[1]),
                                            min(botOfSlice[2], lab.shape[2])])
                # Update grainSlice with disp
                grainSlice = (slice(topOfSliceCrop[0], botOfSliceCrop[0]),
                            slice(topOfSliceCrop[1], botOfSliceCrop[1]),
                            slice(topOfSliceCrop[2], botOfSliceCrop[2]))

                # Update labSubvolDefMask
                labSubvolDefMaskCrop = labSubvolDefMask[topOfSliceCrop[0]-topOfSlice[0] : labSubvolDefMask.shape[0]-1 + (botOfSliceCrop[0]-botOfSlice[0]),
                                                        topOfSliceCrop[1]-topOfSlice[1] : labSubvolDefMask.shape[1]-1 + (botOfSliceCrop[1]-botOfSlice[1]),
                                                        topOfSliceCrop[2]-topOfSlice[2] : labSubvolDefMask.shape[2]-1 + (botOfSliceCrop[2]-botOfSlice[2])]
                return label, grainSlice, labSubvolDefMaskCrop

            # Nan displacement, run away
            else:
                return label, 0, 0, -1
        # Got None from getLabel()
        else:
            return label, 0,0,-1

    # Create progressbar
    widgets = [progressbar.FormatLabel(''), ' ', progressbar.Bar(), ' ', progressbar.AdaptiveETA()]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=numberOfLabels)
    pbar.start()
    finishedNodes = 0
    # Run multiprocessing
    with multiprocessing.Pool(processes=nProcesses) as pool:
        for returns in pool.imap_unordered(funMoveLabels, labelsToMove):
            finishedNodes += 1
            #widgets[0] = progressbar.FormatLabel("{}/{} ".format(finishedNodes, numberOfLabels))
            pbar.update(finishedNodes)
            # Set voxels in slice to the value of the label if not in greyscale mode
            if returns[0] > 0:
                labOut[returns[1]][returns[2]] = returns[0]
        pool.close()
        pool.join()

    # End progressbar
    pbar.finish()


    return labOut


def erodeLabels(lab, erosion=1, boundingBoxes=None, centresOfMass=None, nProcesses=nProcessesDefault):
    """
    This function erodes a labelled image.

    Parameters
    -----------
        lab : 3D numpy array
            Labelled image

        erosion : int, optional
            Erosion level

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

        nProcesses : integer (optional, default = nProcessesDefault)
            Number of processes for multiprocessing
            Default = number of CPUs in the system

    Returns
    --------
        erodeImage : 3D numpy array
            New labelled image with the eroded labels.

    Note
    ----
        The function makes use of spam.label.moveLabels() to generate the eroded image.

    """
    # Get number of labels
    numberOfLabels = lab.max()
    # Create the Empty Phi field
    PhiField = numpy.zeros((numberOfLabels+1, 4, 4))
    # Setup Phi as the identity
    for i in range(0, numberOfLabels+1, 1):
        PhiField[i] = numpy.eye(4)
    # Use moveLabels
    erodeImage = spam.label.moveLabels(lab, 
                                       PhiField, 
                                       boundingBoxes=boundingBoxes, 
                                       centresOfMass=centresOfMass, 
                                       margin=1, 
                                       PhiCOM=True, 
                                       threshold=0.5, 
                                       labelDilate=-erosion, 
                                       nProcesses=nProcesses)
    return erodeImage


def convexFillHoles(lab, boundingBoxes=None, centresOfMass=None):
    """
    This function fills the holes computing the convex volume around each label.

    Parameters
    -----------
        lab : 3D numpy array
            Labelled image

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

    Returns
    --------
        labOut : 3D numpy array
            New labelled image.

    Note
    ----
        The function works nicely for convex particles. For non-convex particles, it will alter the shape.

    """

    # Check for boundingBoxes
    if boundingBoxes is None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    # Check for centresOfMass
    if centresOfMass is None:
        centresOfMass = spam.label.centresOfMass(lab)
    # Create output label image
    labOut = numpy.zeros_like(lab, dtype=spam.label.labelType)
    # Get number of labels
    numberOfLabels = lab.max()
    # Create progressbar
    widgets = [progressbar.FormatLabel(''), ' ', progressbar.Bar(), ' ', progressbar.AdaptiveETA()]
    pbar = progressbar.ProgressBar(widgets=widgets, maxval=numberOfLabels)
    pbar.start()
    for i in range(1,numberOfLabels+1,1):
        # Get label
        getLabelReturn = spam.label.getLabel(lab,
                                             i,
                                             labelDilate=0,
                                             margin=3,
                                             boundingBoxes=boundingBoxes,
                                             centresOfMass=centresOfMass,
                                             maskOtherLabels=False)
        # Get subvolume
        subVol = getLabelReturn['subvol']
        # Transform to binary
        subVolBinMask = (subVol > 0).astype(int)
        # Mask out all the other labels
        subVolBinMaskLabel = numpy.where(subVol == i, 1, 0).astype(int)
        # Mask only the current label - save all the other labels
        subVolMaskOtherLabel = subVolBinMask - subVolBinMaskLabel
        # Fill holes with convex volume
        points = numpy.transpose(numpy.where(subVolBinMaskLabel))
        hull = scipy.spatial.ConvexHull(points)
        deln = scipy.spatial.Delaunay(points[hull.vertices])
        idx = numpy.stack(numpy.indices(subVol.shape), axis = -1)
        out_idx = numpy.nonzero(deln.find_simplex(idx) + 1)
        hullIm = numpy.zeros(subVol.shape)
        hullIm[out_idx] = 1
        hullIm = hullIm > 0
        # Identify added voxels
        subVolAdded = hullIm - subVolBinMaskLabel
        # Identify the wrong voxels - they are inside other labels
        subVolWrongAdded = subVolAdded * subVolMaskOtherLabel
        # Remove wrong filling areas
        subVolCorrect = (hullIm - subVolWrongAdded) > 0
        # Get slice
        grainSlice = (slice(getLabelReturn['slice'][0].start, getLabelReturn['slice'][0].stop),
                        slice(getLabelReturn['slice'][1].start, getLabelReturn['slice'][1].stop),
                        slice(getLabelReturn['slice'][2].start, getLabelReturn['slice'][2].stop))
        # Add it to the output file
        labOut[grainSlice][subVolCorrect] = i
        # Update the progressbar
        widgets[0] = progressbar.FormatLabel("{}/{} ".format(i, numberOfLabels))
        pbar.update(i)

    return labOut


def getNeighbours(lab, listOfLabels, method='getLabel', parameter=None, centresOfMass=None, boundingBoxes=None):
    """
    This function computes the neighbours for a list of labels.

    Parameters
    -----------
        lab : 3D numpy array
            Labelled image

        listOfLabels : list of ints
            List of labels to which the neighbours will be computed

        method : string
            Method to compute the neighbours.
            'getLabel' : The neighbours are the labels inside the subset obtained through spam.getLabel()
            'mesh' : The neighbours are computed using a tetrahedral connectivity matrix
            Default = 'getLabel'

        parameter : int
            Parameter controlling each method.
            For 'getLabel', it correspond to the size of the subset. Default = 3
            For 'mesh', it correspond to the size of the alpha shape used for carving the mesh. Default = 5*meanDiameter.

        boundingBoxes : lab.max()x6 array of ints, optional
            Bounding boxes in format returned by ``boundingBoxes``.
            If not defined (Default = None), it is recomputed by running ``boundingBoxes``

        centresOfMass : lab.max()x3 array of floats, optional
            Centres of mass in format returned by ``centresOfMass``.
            If not defined (Default = None), it is recomputed by running ``centresOfMass``

    Returns
    --------
        neighbours : list
            List with the neighbours for each label in listOfLabels.

    """
    # Create result list
    neighbours = []
    # Compute centreOfMass if needed
    if centresOfMass == None:
        centresOfMass = spam.label.centresOfMass(lab)
    # Compute boundingBoxes if needed
    if boundingBoxes == None:
        boundingBoxes = spam.label.boundingBoxes(lab)
    # Compute Radii
        radii = spam.label.equivalentRadii(lab)
    if method == 'getLabel':
        # Compute for each label in the list of labels
        for label in listOfLabels:
            # Compute parameter if needed
            if parameter == None:
                parameter = radii[label]
            getLabelReturn = spam.label.getLabel(lab,
                                                 label,
                                                 labelDilate=parameter,
                                                 margin=parameter,
                                                 boundingBoxes=boundingBoxes,
                                                 centresOfMass=centresOfMass,
                                                 maskOtherLabels=False)
            # Get subvolume
            subVol = getLabelReturn['subvol']
            # Get neighbours
            neighboursLabel = numpy.unique(subVol)
            # Remove label and 0 from the list of neighbours
            neighboursLabel = neighboursLabel[~numpy.in1d(neighboursLabel, label)]
            neighboursLabel = neighboursLabel[~numpy.in1d(neighboursLabel, 0)]
            # Add the neighbours to the list
            neighbours.append(neighboursLabel)

    elif method == 'mesh':
        # Compute parameter if needed
        if parameter == None:
            parameter = 5*2*numpy.mean(radii)
        # Get connectivity matrix
        conn = spam.mesh.triangulate(centresOfMass, weights=radii**2, alpha=parameter)
        # Compute for each label in the list of labels
        for label in listOfLabels:
            neighboursLabel = numpy.unique(conn[numpy.where(numpy.sum(conn == label, axis=1))])
            # Remove label from the list of neighbours
            neighboursLabel = neighboursLabel[~numpy.in1d(neighboursLabel, label)]
            # Add the neighbours to the list
            neighbours.append(neighboursLabel)
    else:
        print('spam.label.getNeighbours(): Wrong method, aborting')

    return neighbours
