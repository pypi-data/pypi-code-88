# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchmetal',
 'torchmetal.datasets',
 'torchmetal.datasets.cifar100',
 'torchmetal.modules',
 'torchmetal.toy',
 'torchmetal.transforms',
 'torchmetal.utils',
 'torchmetal.utils.data']

package_data = \
{'': ['*'],
 'torchmetal.datasets': ['assets/cifar100/cifar-fs/*',
                         'assets/cifar100/fc100/*',
                         'assets/cub/*',
                         'assets/doublemnist/*',
                         'assets/omniglot/*',
                         'assets/tcga/*',
                         'assets/triplemnist/*']}

install_requires = \
['h5py',
 'numpy>=1.14.0',
 'ordered-set',
 'pillow>=7.0.0',
 'requests',
 'torch>=1.4.0,<1.9.0',
 'torchvision>=0.5.0,<0.10.0',
 'tqdm>=4.0.0']

extras_require = \
{'tcga': ['academictorrents>=2.1.0,<2.2.0',
          'pandas>=0.24.0,<0.25.0',
          'six>=1.11.0,<1.12.0']}

setup_kwargs = {
    'name': 'torchmetal',
    'version': '0.1.0',
    'description': 'A library for Meta-Learning and Few-Shot Learning with PyTorch',
    'long_description': '# torchmetal\n[![PyPI](https://img.shields.io/pypi/v/torchmetal)](https://pypi.org/project/torchmetal/) <!--[![Build Status](https://travis-ci.com/tristandeleu/pytorch-meta.svg?branch=master)](https://travis-ci.com/tristandeleu/pytorch-meta) [![Documentation](https://img.shields.io/badge/docs-torchmetal-blue)](https://tristandeleu.github.io/pytorch-meta/)-->\n\nA library for few-shot learning & meta-learning in [PyTorch][pytorch].\ntorchmetal contains popular meta-learning benchmarks, fully compatible with\nboth [`torchvision`][torchvision] and PyTorch\'s [`DataLoader`][pt-dataloader].\n\n#### Features\n  - A unified interface for both few-shot classification and regression problems, to allow easy benchmarking on multiple problems and reproducibility.\n  - Helper functions for some popular problems, with default arguments from the literature.\n  - An thin extension of PyTorch\'s [`Module`][pt-module], called `MetaModule`, that simplifies the creation of certain meta-learning models (e.g. gradient based meta-learning methods). See the [MAML example](examples/maml) for an example using `MetaModule`.\n\n#### Datasets available\n  - **Few-shot regression** (toy problems):\n    - Sine waves ([Finn et al., 2017](https://arxiv.org/abs/1703.03400))\n    - Harmonic functions ([Lacoste et al., 2018](https://arxiv.org/abs/1806.07528))\n    - Sinusoid & lines ([Finn et al., 2018](https://arxiv.org/abs/1806.02817))\n  - **Few-shot classification** (image classification):\n    - Omniglot ([Lake et al., 2015](http://www.sciencemag.org/content/350/6266/1332.short)[, 2019](https://arxiv.org/abs/1902.03477))\n    - Mini-ImageNet ([Vinyals et al., 2016](https://arxiv.org/abs/1606.04080), [Ravi et al., 2017](https://openreview.net/forum?id=rJY0-Kcll))\n    - Tiered-ImageNet ([Ren et al., 2018](https://arxiv.org/abs/1803.00676))\n    - CIFAR-FS ([Bertinetto et al., 2018](https://arxiv.org/abs/1805.08136))\n    - Fewshot-CIFAR100 ([Oreshkin et al., 2018](https://arxiv.org/abs/1805.10123))\n    - Caltech-UCSD Birds ([Hilliard et al., 2019](https://arxiv.org/abs/1802.04376), [Wah et al., 2019](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html))\n    - Double MNIST ([Sun, 2019](https://github.com/shaohua0116/MultiDigitMNIST))\n    - Triple MNIST ([Sun, 2019](https://github.com/shaohua0116/MultiDigitMNIST))\n  - **Few-shot segmentation** (semantic segmentation):\n    - Pascal5i 1-way Setup\n\n## Installation\nYou can install torchmetal either using Python\'s package manager pip, or from source. To avoid any conflict with your existing Python setup, it is suggested to work in a virtual environment with [`virtualenv`](https://docs.python-guide.org/dev/virtualenvs/). To install `virtualenv`:\n```bash\npip install --upgrade virtualenv\nvirtualenv venv\nsource venv/bin/activate\n```\n\n#### Using pip\nThis is the recommended way to install torchmetal:\n```bash\npip install torchmetal\n```\n\n#### From source\nYou can also install torchmetal from source. This is recommended if you want to contribute to torchmetal.\n```bash\ngit clone https://github.com/tristandeleu/pytorch-meta.git\ncd pytorch-meta\npython setup.py install\n```\n\n## Example\n\n#### Minimal example\nThis minimal example below shows how to create a dataloader for the 5-shot 5-way Omniglot dataset with torchmetal. The dataloader loads a batch of randomly generated tasks, and all the samples are concatenated into a single tensor. For more examples, check the [examples](examples/) folder.\n```python\nfrom torchmetal.datasets.helpers import omniglot\nfrom torchmetal.utils.data import BatchMetaDataLoader\n\ndataset = omniglot("data", ways=5, shots=5, test_shots=15, meta_train=True, download=True)\ndataloader = BatchMetaDataLoader(dataset, batch_size=16, num_workers=4)\n\nfor batch in dataloader:\n    train_inputs, train_targets = batch["train"]\n    print(\'Train inputs shape: {0}\'.format(train_inputs.shape))    # (16, 25, 1, 28, 28)\n    print(\'Train targets shape: {0}\'.format(train_targets.shape))  # (16, 25)\n\n    test_inputs, test_targets = batch["test"]\n    print(\'Test inputs shape: {0}\'.format(test_inputs.shape))      # (16, 75, 1, 28, 28)\n    print(\'Test targets shape: {0}\'.format(test_targets.shape))    # (16, 75)\n```\n\n#### Advanced example\nHelper functions are only available for some of the datasets available. However, all of them are available through the unified interface provided by torchmetal. The variable `dataset` defined above is equivalent to the following\n```python\nfrom torchmetal.datasets import Omniglot\nfrom torchmetal.transforms import Categorical, ClassSplitter, Rotation\nfrom torchvision.transforms import Compose, Resize, ToTensor\nfrom torchmetal.utils.data import BatchMetaDataLoader\n\ndataset = Omniglot("data",\n                   # Number of ways\n                   num_classes_per_task=5,\n                   # Resize the images to 28x28 and converts them to PyTorch tensors (from Torchvision)\n                   transform=Compose([Resize(28), ToTensor()]),\n                   # Transform the labels to integers (e.g. ("Glagolitic/character01", "Sanskrit/character14", ...) to (0, 1, ...))\n                   target_transform=Categorical(num_classes=5),\n                   # Creates new virtual classes with rotated versions of the images (from Santoro et al., 2016)\n                   class_augmentations=[Rotation([90, 180, 270])],\n                   meta_train=True,\n                   download=True)\ndataset = ClassSplitter(dataset, shuffle=True, num_train_per_class=5, num_test_per_class=15)\ndataloader = BatchMetaDataLoader(dataset, batch_size=16, num_workers=4)\n```\nNote that the dataloader, receiving the dataset, remains the same.\n\n\n[pytorch]: https://pytorch.org/\n[torchvision]: https://pytorch.org/docs/stable/torchvision/index.html\n[pt-dataloader]: https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader\n[pt-module]: https://pytorch.org/docs/stable/nn.html#torch.nn.Module\n',
    'author': 'Tristan Deleu',
    'author_email': 'tristan.deleu@gmail.com',
    'maintainer': 'Derek Goddeau',
    'maintainer_email': 'derek.j.goddeau@pm.me',
    'url': 'https://github.com/sevro/torchmetal',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
