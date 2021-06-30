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
This package was generated from typeshed commit `f260ea238308fe9ad1b9bd57ed6b573e6b653c97`.
'''.lstrip()

setup(name=name,
      version="8.2.6",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['PIL-stubs'],
      package_data={'PIL-stubs': ['WmfImagePlugin.pyi', 'GribStubImagePlugin.pyi', 'SunImagePlugin.pyi', 'ImageMath.pyi', 'PixarImagePlugin.pyi', 'WebPImagePlugin.pyi', 'ImageMorph.pyi', 'DdsImagePlugin.pyi', 'DcxImagePlugin.pyi', 'PcdImagePlugin.pyi', 'ContainerIO.pyi', 'XbmImagePlugin.pyi', 'PdfImagePlugin.pyi', 'TiffTags.pyi', 'ImageFile.pyi', 'Image.pyi', 'JpegPresets.pyi', 'ImageFont.pyi', '_util.pyi', 'FtexImagePlugin.pyi', 'ImageWin.pyi', 'MpoImagePlugin.pyi', 'ImageChops.pyi', 'ExifTags.pyi', 'ImtImagePlugin.pyi', 'PdfParser.pyi', 'GimpPaletteFile.pyi', 'XpmImagePlugin.pyi', 'McIdasImagePlugin.pyi', 'ImageStat.pyi', 'PngImagePlugin.pyi', 'TiffImagePlugin.pyi', '_imaging.pyi', 'SpiderImagePlugin.pyi', 'PaletteFile.pyi', 'PyAccess.pyi', 'Hdf5StubImagePlugin.pyi', 'ImImagePlugin.pyi', 'Jpeg2KImagePlugin.pyi', 'ImageColor.pyi', 'PpmImagePlugin.pyi', 'EpsImagePlugin.pyi', 'BlpImagePlugin.pyi', 'ImageTransform.pyi', '_version.pyi', 'WalImageFile.pyi', 'ImageDraw.pyi', '__main__.pyi', 'FontFile.pyi', 'IptcImagePlugin.pyi', 'GdImageFile.pyi', 'ImageOps.pyi', 'ImageCms.pyi', 'features.pyi', 'PcfFontFile.pyi', 'FliImagePlugin.pyi', 'BdfFontFile.pyi', 'BmpImagePlugin.pyi', '_tkinter_finder.pyi', 'ImageTk.pyi', 'GbrImagePlugin.pyi', 'PsdImagePlugin.pyi', 'FpxImagePlugin.pyi', 'IcnsImagePlugin.pyi', 'ImageGrab.pyi', 'PcxImagePlugin.pyi', 'PalmImagePlugin.pyi', 'MpegImagePlugin.pyi', 'GimpGradientFile.pyi', 'JpegImagePlugin.pyi', 'SgiImagePlugin.pyi', 'BufrStubImagePlugin.pyi', 'ImageMode.pyi', '_binary.pyi', 'PSDraw.pyi', 'ImageEnhance.pyi', 'TarIO.pyi', 'MicImagePlugin.pyi', 'MspImagePlugin.pyi', 'ImageFilter.pyi', 'TgaImagePlugin.pyi', 'ImagePalette.pyi', 'ImageSequence.pyi', 'ImageQt.pyi', '__init__.pyi', 'IcoImagePlugin.pyi', 'ImageShow.pyi', 'CurImagePlugin.pyi', 'GifImagePlugin.pyi', 'XVThumbImagePlugin.pyi', 'FitsStubImagePlugin.pyi', 'ImageDraw2.pyi', 'ImagePath.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
