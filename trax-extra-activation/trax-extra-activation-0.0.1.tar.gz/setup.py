# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['trax_extra_activation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'trax-extra-activation',
    'version': '0.0.1',
    'description': 'Extra activation functions for Trax',
    'long_description': '# Trax Extra Activation Functions\nExtra activation functions for [Trax](https://github.com/google/trax)\n\n<code>pip install trax-extra-activation</code>\n\n## How to use\nYou can use activation functions in the same way as that ones implemented in Trax.\n\n```python\nfrom trax_extra_activation import TanhExp\nmodel = tl.Serial(\n    tl.Embedding(vocab_size=8192, d_feature=256),\n    tl.Mean(axis=1),\n    tl.Dense(2),\n    TanhExp()\n)\n```\n\n## Activations\n- HardShrink\n  ```python\n  HardShrink(lmbda: float = 0.5) -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Hardshrink.html#torch.nn.Hardshrink)\n- HardSwish\n  ```python\n  HardSwish() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Hardswish.html#torch.nn.Hardswish)\n- LogSigmoid\n  ```python\n  LogSigmoid() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.LogSigmoid.html#torch.nn.LogSigmoid)\n- Relu6\n  ```python\n  Relu6() -> PureLayer\n  ```\n  - [PyTorch Doument](https://pytorch.org/docs/stable/generated/torch.nn.ReLU6.html#torch.nn.ReLU6)\n- Celu\n  ```python\n  Celu(a: float = 1.0) -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.CELU.html#torch.nn.CELU)\n- Silu\n  ```python\n  Silu() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.SiLU.html#torch.nn.SiLU)\n- Mish\n  ```python\n  Mish() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Mish.html#torch.nn.Mish)\n- SoftShrink\n  ```python\n  SoftShrink(lmbda: float = 0.5) -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Softshrink.html#torch.nn.Softshrink)\n- SoftSign\n  ```python\n  SoftSign() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Softsign.html#torch.nn.Softsign)\n- TanhShrink\n  ```python\n  TanhShrink() -> PureLayer\n  ```\n  - [PyTorch Document](https://pytorch.org/docs/stable/generated/torch.nn.Tanhshrink.html#torch.nn.Tanhshrink)\n- TanhExp\n  ```python\n  TanhExp() -> PureLayer\n  ```\n  - [Paper](https://arxiv.org/abs/2003.09855)\n',
    'author': 'Catminusminus',
    'author_email': 'getomya@svk.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Catminusminus/trax-extra-activation',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
