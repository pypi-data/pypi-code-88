# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gptsum']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.6,<0.9'],
 ':python_version < "3.8"': ['importlib-metadata>=3.7.3,<5.0.0']}

entry_points = \
{'console_scripts': ['gptsum = gptsum.cli:main']}

setup_kwargs = {
    'name': 'gptsum',
    'version': '0.0.10',
    'description': 'A tool to make disk images using GPT partitions self-verifiable',
    'long_description': 'gptsum\n======\nA tool to make disk images using GPT_ partitions self-verifiable, like\n`isomd5sum`_.\n\nNote this *only* works for read-only, immutable images!\n\n.. _GPT: https://en.wikipedia.org/wiki/GUID_Partition_Table\n.. _isomd5sum: https://github.com/rhinstaller/isomd5sum\n\nQuickstart\n**********\n.. When making changes to the quickstart code below,\n   make sure \'tests/test_readme.py\' is updated accordingly.\n\nFirst, create an empty disk image::\n\n    $ truncate -s64M image.raw\n\nThen, create a GPT partition table in it. Note, below we set an explicit\n`label-id`. In general, this should not be done and a random GUID will be\ngenerated. Simply remove the line.\n\n::\n\n    $ sfdisk image.raw << EOF\n    label: gpt\n    label-id: 132e3631-1ec9-4411-ab25-9b95b54b0903\n    first-lba: 2048\n    EOF\n\n    Checking that no-one is using this disk right now ... OK\n\n    Disk image.raw: 64 MiB, 67108864 bytes, 131072 sectors\n    Units: sectors of 1 * 512 = 512 bytes\n    Sector size (logical/physical): 512 bytes / 512 bytes\n    I/O size (minimum/optimal): 512 bytes / 512 bytes\n\n    >>> Script header accepted.\n    >>> Script header accepted.\n    >>> Script header accepted.\n    >>> Done.\n    Created a new GPT disklabel (GUID: 132E3631-1EC9-4411-AB25-9B95B54B0903).\n\n    New situation:\n    Disklabel type: gpt\n    Disk identifier: 132E3631-1EC9-4411-AB25-9B95B54B0903\n\n    The partition table has been altered.\n    Syncing disks.\n\nWe can retrieve the current disk GUID using ``gptsum``::\n\n    $ gptsum get-guid image.raw\n    132e3631-1ec9-4411-ab25-9b95b54b0903\n\nVerification should fail::\n\n    $ gptsum verify image.raw || echo "Verification failed!"\n    Disk GUID doesn\'t match expected checksum, got 132e3631-1ec9-4411-ab25-9b95b54b0903, expected 6190f5bb-1967-14ec-9fbd-a7d213a45461\n    Verification failed!\n\nEmbed the disk checksum as the label GUID::\n\n    $ gptsum embed image.raw\n\nVerification should now succeed::\n\n    $ gptsum verify image.raw && echo "Verification succeeded!"\n    Verification succeeded!\n\nIndeed, the GUID was changed::\n\n    $ gptsum get-guid image.raw\n    6190f5bb-1967-14ec-9fbd-a7d213a45461\n\n\nHow It Works\n************\nGenerally, when checksums are used to validate the integrity of a file, this\nchecksum needs to be provided out-of-band, e.g., in a separate file. This\ncomplicates the process a bit, since now multiple files need to be kept around\n(and potentially in sync).\n\nBeing able to verify a file\'s integrity without any external information would\nbe great. However, if we embed the checksum of a file in the file itself, we\nchange its checksum and verification would fail. So we need to apply some\ntricks.\n\nThe `isomd5sum`_ tool is often used to verify the integrity of ISO files, e.g.,\nLinux distribution releases. It uses an unused location in the ISO9660 file\nformat to embed an MD5 checksum of the actual data segments of said file. As\nsuch, this MD5 checksum does not represent the complete file contents but only\nthe pieces of data we\'re interested in.\n\nWe can translate this to GPT-partitioned disk images as well. In the GPT\nformat, there\'s no room to embed any arbitrary blobs (unless we\'d use the\nreserved or padding sections of the headers, which should be zeroed out so we\nshouldn\'t). However, GPT disks are identified by a GUID which is stored in the\ntwo metadata sections stored on the disk, at LBA 1 and as the last LBA on the\ndisk (the so-called primary and secondary GPT headers). This leaves room for 16\nbytes of semi-arbitrary data.\n\nFurthermore, the GPT headers themselves, including the GUID, are protected\nusing a CRC32 checksum.\n\nAs such, we can apply the following procedure:\n\n- Zero out the CRC32 and GUID fields in both GPT headers\n- Calculate a 16 byte checksum of the resulting image (covering all data,\n  except for the CRC32 and GUID fields)\n- Embed the checksum as the GUID field in both GPT headers (now becoming the\n  disk GUID)\n- Update the CRC32 fields in both GPT headers\n\nAt this point we have a fully valid GPT disk image with a GUID representing\nthe actual data contained in the image. One could argue this is no longer a\nvalid GUID (indeed it\'s not), but since it\'s generated using a secure hashing\nalgorithm over a (potentially large) file, we can assume the entropy is\nsufficient to avoid collisions. Essentially, if two disk images were to get the\nsame GUID, they\'re very likely the exact same disk image, content-wise.\n\nVerifying an image file is roughly the same procedure:\n\n- Zero out the CRC32 and GUID fields in both GPT headers (in-memory)\n- Calculate a 16 byte checksum of the resulting image\n- Verify this calculated checksum equals the actual GUID embedded in the image\n\nImplementation Details\n**********************\n`gptsum` is implemented in Python, and compatible with Python 3.6 and later.\nIt uses the `Blake2b`_ checksum algorithm to construct a 16 byte digest\nof the disk image.\n\nVarious subcommands are exposed by the CLI, refer to the `documentation`_\nfor more details.\n\n.. _Blake2b: https://en.wikipedia.org/wiki/BLAKE_(hash_function)#BLAKE2\n.. _documentation: https://nicolast.github.io/gptsum/\n',
    'author': 'Nicolas Trangez',
    'author_email': 'ikke@nicolast.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NicolasT/gptsum',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
