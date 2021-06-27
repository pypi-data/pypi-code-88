# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['text_embeddings',
 'text_embeddings.base',
 'text_embeddings.byte',
 'text_embeddings.hash',
 'text_embeddings.visual']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0',
 'coverage-badge>=1.0.1,<2.0.0',
 'coverage>=5.5,<6.0',
 'einops>=0.3.0,<0.4.0',
 'icecream>=2.1.0,<3.0.0',
 'interrogate>=1.3.2,<2.0.0',
 'loguru>=0.5.3,<0.6.0',
 'mmh3>=3.0.0,<4.0.0',
 'numpy>=1.20.2,<2.0.0',
 'pdoc3>=0.9.2,<0.10.0',
 'pytest>=6.2.3,<7.0.0',
 'torch>=1.8.1,<2.0.0',
 'transformers>=4.5.1,<5.0.0',
 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'text-embeddings',
    'version': '0.0.8',
    'description': 'Non-traditional/no-vocabulary text embeddings in one place.',
    'long_description': '![banner](./banner.png)\n[![PyPI version](https://badge.fury.io/py/text-embeddings.svg)](https://badge.fury.io/py/text-embeddings) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/112e50abd97444a4aca06f94fb7e8873)](https://www.codacy.com/gh/ChenghaoMou/embeddings/dashboard?utm_source=github.com&utm_medium=referral&utm_content=ChenghaoMou/embeddings&utm_campaign=Badge_Grade)[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/112e50abd97444a4aca06f94fb7e8873)](https://www.codacy.com/gh/ChenghaoMou/embeddings/dashboard?utm_source=github.com&utm_medium=referral&utm_content=ChenghaoMou/embeddings&utm_campaign=Badge_Coverage)\n\n## Features\n\n-   [x] Visual text embeddings ([Visual Text Representations](https://t.co/l9E6rL8O5p?amp=1))\n-   [x] Word-level hash embeddings ([PRADO/PQRNN](https://ai.googleblog.com/2020/09/advancing-nlp-with-efficient-projection.html))\n-   [x] Char-level hash embeddings ([CANINE](https://arxiv.org/abs/2103.06874))\n-   [x] Byte-level embeddings ([ByT5](https://arxiv.org/pdf/2105.13626.pdf))\n-   [x] Byte-level embedding module ([Charformer](https://arxiv.org/abs/2106.12672))\n\n## Examples\n\n-   [x] [Machine Translation](examples/translation/nmt_transformer.py)\n-   [x] [Text Classification](examples/classification/rnn.py)\n\n## Installation\n\n```bash\npip install text-embeddings --upgrade\n```\n\n## Documentation\n\n[Link](https://chenghaomou.github.io/embeddings/)\n\n## Example Usage\n\n```python\nfrom text_embeddings.visual import VTRTokenizer\nfrom transformers.tokenization_utils_base import PaddingStrategy, TruncationStrategy\n\ndata = [\n"Hello world!",\n"¡Hola Mundo!",\n"你好，世界！",\n]\n\ntokenizer = VTRTokenizer(\n    font_size=14,\n    window_size=10,\n    font="~/Library/Fonts/NotoSansDisplay-Regular.ttf",\n    max_length=36\n)\n\nresults = tokenizer(\n    text=data,\n    text_pair=data,\n    add_special_tokens=True,\n    padding=PaddingStrategy.LONGEST, \n    return_tensors=\'pt\',\n    truncation=TruncationStrategy.LONGEST_FIRST, \n    return_attention_mask=True, \n    return_special_tokens_mask=True,\n    return_length=True,\n    prepend_batch_axis=True,\n    return_overflowing_tokens=False,\n)\n\nassert results["input_ids"].shape == (3, results["input_ids"].shape[1], 14, 10) \nassert results["attention_mask"].shape == (3, results["input_ids"].shape[1])\nassert results["token_type_ids"].shape == (3, results["input_ids"].shape[1])\nassert results["length"].shape == (3, )\n```\n\n## Write Your Own Embedding Tokenizer\n\n```python\nimport numpy as np\nfrom typing import Optional, List, Dict\nfrom text_embeddings.base import EmbeddingTokenizer\n\n\nclass MyOwnTokenizer(EmbeddingTokenizer):\n\n    def __init__(\n        self,\n        model_input_names: Optional[List[str]] = None,\n        special_tokens: Optional[Dict[str, np.ndarray]] = None,\n        max_length: Optional[int] = 2048,\n    ):\n        super().__init__(model_input_names, special_tokens, max_length)\n\n    def text2embeddings(self, text: str) -> np.ndarray:\n        \n        sequence_length = 10\n        dimensions = (10, 10, 10) # each token is mapped to a 3-d array\n        return np.zeros((sequence_length, *dimensions))\n\n    def create_padding_token_embedding(self, input_embeddings=None) -> np.ndarray:\n\n        # let\'s create a consistent 3-d array\n        return np.zeros((10, 10, 10))\n\n```\n',
    'author': 'Chenghao Mou',
    'author_email': 'mouchenghao@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ChenghaoMou/embeddings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
