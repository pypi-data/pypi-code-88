# =================================================
# * Licensed under The MIT License
# * Written by KAI-ZHAO and Shanghua-Gao
# =================================================
import numpy as np
from . import nms_ext
from scipy.ndimage.filters import convolve
from ..image import norm01

def nms(E):
  assert isinstance(E, np.ndarray)
  E = E.astype(np.float32)
  E = norm01(E)
  t = theta(E.astype(np.float32))
  nmsed = np.zeros_like(E, dtype=np.float32)
  nms_ext.nms_func(E.astype(np.float32), t.astype(np.float32), nmsed)
  return nmsed

def theta(E):
  assert isinstance(E, np.ndarray)
  E = E.astype(np.float32)
  convx = convTri(E, 4)
  [Oy, Ox] = np.gradient(convx)
  [Oxy, Oxx] = np.gradient(Ox)
  [Oyy, Oyx] = np.gradient(Oy)
  tmp1 = np.multiply(Oyy, np.sign(-Oxy))
  tmp2 = np.divide(tmp1, Oxx + 1e-5)
  theta = np.mod(np.arctan(tmp2), np.pi)
  return theta

def convTri(x, r):
  x=np.squeeze(x)
  assert x.ndim == 2
  assert isinstance(r, int)
  assert r > 1
  flt_head = np.arange(1, r+2, 1)
  flt_tail = np.arange(r, 0, -1)
  flt = np.concatenate((flt_head, flt_tail)).astype(np.float32)
  flt = flt / ((r+1)**2)
  flt = flt[np.newaxis, :]
  conv = convolve(convolve(x, flt), flt.transpose())
  return conv

