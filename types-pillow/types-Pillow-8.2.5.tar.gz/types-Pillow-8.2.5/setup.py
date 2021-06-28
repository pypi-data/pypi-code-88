from setuptools import setup

name = "types-Pillow"
description = "Typing stubs for Pillow"
long_description = '''
## Typing stubs for Pillow

This is an auto-generated PEP 561 type stub package for `Pillow` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Pillow`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/Pillow. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `2b64f54008f6dbaded7970336e26c4f02fa82fd9`.
'''.lstrip()

setup(name=name,
      version="8.2.5",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['PIL-stubs'],
      package_data={'PIL-stubs': ['_imaging.pyi', 'SpiderImagePlugin.pyi', 'WalImageFile.pyi', 'ImageCms.pyi', 'JpegPresets.pyi', 'PdfImagePlugin.pyi', 'FontFile.pyi', 'ImageFilter.pyi', 'FitsStubImagePlugin.pyi', 'MspImagePlugin.pyi', 'GribStubImagePlugin.pyi', 'ImageChops.pyi', 'GdImageFile.pyi', 'GifImagePlugin.pyi', 'ImageDraw.pyi', 'MicImagePlugin.pyi', 'BlpImagePlugin.pyi', 'BmpImagePlugin.pyi', 'PyAccess.pyi', 'Image.pyi', 'GbrImagePlugin.pyi', 'ImageTransform.pyi', 'FtexImagePlugin.pyi', 'CurImagePlugin.pyi', 'ImageShow.pyi', 'XbmImagePlugin.pyi', '_version.pyi', 'ImageOps.pyi', 'IptcImagePlugin.pyi', 'PaletteFile.pyi', '_binary.pyi', 'ImagePalette.pyi', 'WebPImagePlugin.pyi', 'ImageTk.pyi', 'ImImagePlugin.pyi', 'ImageStat.pyi', '__main__.pyi', 'ImageEnhance.pyi', 'IcnsImagePlugin.pyi', 'DdsImagePlugin.pyi', 'PcdImagePlugin.pyi', 'PngImagePlugin.pyi', 'PalmImagePlugin.pyi', 'DcxImagePlugin.pyi', 'ImageColor.pyi', 'SunImagePlugin.pyi', 'Hdf5StubImagePlugin.pyi', 'FpxImagePlugin.pyi', 'ImageFile.pyi', 'MpoImagePlugin.pyi', 'ImageGrab.pyi', 'ContainerIO.pyi', 'ImageMath.pyi', 'GimpGradientFile.pyi', 'TiffTags.pyi', 'ImageMorph.pyi', 'ImageFont.pyi', 'BdfFontFile.pyi', 'TgaImagePlugin.pyi', '_util.pyi', 'PsdImagePlugin.pyi', 'IcoImagePlugin.pyi', 'MpegImagePlugin.pyi', 'ImageQt.pyi', '_tkinter_finder.pyi', 'ImtImagePlugin.pyi', 'ExifTags.pyi', 'EpsImagePlugin.pyi', 'PSDraw.pyi', 'XVThumbImagePlugin.pyi', 'Jpeg2KImagePlugin.pyi', 'FliImagePlugin.pyi', 'PixarImagePlugin.pyi', 'PpmImagePlugin.pyi', 'ImageSequence.pyi', 'TarIO.pyi', 'BufrStubImagePlugin.pyi', 'McIdasImagePlugin.pyi', 'features.pyi', 'ImagePath.pyi', '__init__.pyi', 'ImageMode.pyi', 'PcfFontFile.pyi', 'XpmImagePlugin.pyi', 'JpegImagePlugin.pyi', 'SgiImagePlugin.pyi', 'ImageDraw2.pyi', 'WmfImagePlugin.pyi', 'ImageWin.pyi', 'PdfParser.pyi', 'TiffImagePlugin.pyi', 'PcxImagePlugin.pyi', 'GimpPaletteFile.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
