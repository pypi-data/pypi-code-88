import numpy as np
from PIL import Image as im
from tkinter.messagebox import *
import rawpy
#, imageio
import exifread
from scipy import ndimage, misc
import os.path

from dicalum.coeffs import *
from dicalum.DclExif import *

__all__ = ['rawread','darkread']

def rawread(rfile):
    kam=dclinst.camera
    len=dclinst.lens
    if (os.path.splitext(rfile)[1].lower() != CamList[kam].exte):
        showinfo(title='DiCaLum', message='File is not a RAW file compatible with the selected cameraa')
        return -1

    raw = rawpy.imread(rfile)
    try:
        dclex=read_exif_tags(rfile)
        En_iso.set(str(dclex.iso))
        En_ape.set(str(dclex.aperture))
        En_shu.set(str(dclex.shutter))
    except:
        dclex=DclExpo(0,0,0)
        En_iso.set('0')
        En_ape.set('0')
        En_shu.set('0')
        showinfo(title='DiCaLum', message='Exif data cannot be loaded! \ Set it manually')
    x = raw.raw_image.copy()
    B=x[1::2,1::2]
    if (float(En_ape.get())==0):
        apert = LensList[len].aper
        En_ape.set(str(apert))
    R=x[::2,::2]
    G1=x[1::2,::2]
    G2=x[::2,1::2]
    G=(G1+G2)*0.5
    s=G.shape
    ny=np.uint16(s[0])
    nx=np.uint16(s[1])
    if (nx!=CamList[kam].nx or ny!=CamList[kam].ny):
        showinfo(title='DiCaLum', message='Selected camera is not compatible with the RAW file')
        return -1
    nny=np.uint16(s[0]/2)
    nnx=np.uint16(s[1]/2)
    center= np.median(G[nny-100:nny+100,nnx-100:nnx+100])
    corner= np.median(G[0:100,0:100])
    #print(center)
    #print(corner)
    dark=CamList[kam].dark
    satu=CamList[kam].satu
    R=(R-dark)/(satu-dark)*CamList[kam].rdsu*LensList[len].corr
    G=(G-dark)/(satu-dark)*CamList[kam].gdsu*LensList[len].corr
    B=(B-dark)/(satu-dark)*CamList[kam].bdsu*LensList[len].corr
    R[R < 0.0] = 0.0
    G[G < 0.0] = 0.0
    B[B < 0.0] = 0.0
    V = dcldat.V
    R = R/V
    G = G/V
    B = B/V
    GG = ndimage.median_filter(G, size=5)
    RR = ndimage.median_filter(R, size=5)
    BB = ndimage.median_filter(B, size=5)
    center= np.mean(GG[nny-100:nny+100,nnx-100:nnx+100])
    #print(center)
    GG = ndimage.zoom(GG,0.25)
    RR = ndimage.zoom(RR,0.25)
    BB = ndimage.zoom(BB,0.25)
    D = ndimage.median_filter(GG, size=10)
    fcer =  2.39*RR  -0.65*GG  -1.15*BB;
    fceg = -1.02*RR  +2.66*GG  -0.73*BB;
    fceb = -0.37*RR  -1.01*GG  +2.89*BB;
    

    xss = 50/np.sqrt(np.median(G[nny-100:nny+100,nnx-100:nnx+100]))
    fRGB = np.dstack((R,G,B))
    fFCE = np.dstack((fcer,fceg,fceb))
    fRGB[fRGB < 0] = 0
    fFCE[fFCE < 0] = 0
    fRGB = np.sqrt(fRGB) * xss
    fFCE = np.sqrt(fFCE) * xss
    fRGB[fRGB > 255] = 255
    fFCE[fFCE > 255] = 255
    RGB =  np.uint8(fRGB)
    imRGB = im.fromarray(RGB)
    RGB =  np.uint8(fFCE)
    imFCE = im.fromarray(RGB)
    imRGB=imRGB.resize((300,200), im.BILINEAR)
    imFCE=imFCE.resize((300,200), im.BILINEAR)
    ddat=DclData(V,R,G,B,D,imRGB,imFCE,dclex,0)
    return ddat

def darkread(rfile):
    kam=dclinst.camera
    raw = rawpy.imread(rfile)
    try:
        dclex=read_exif_tags(rfile)
        Da_iso = dclex.iso
        Da_shu = dclex.shutter
    except:
        dclex=DclExpo(0,0,0)
        Da_iso = 0
        Da_shu = 0
    x = raw.raw_image.copy()
    #print(x.mean())
    dark=CamList[kam].dark
    satu=CamList[kam].satu
    x=(x-dark)/(satu-dark)*CamList[kam].gdsu
    dark=x.mean()
    #print(dark)
    return dark

