# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cclm', 'cclm.augmentation', 'cclm.pretrainers', 'cclm.shelf']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=1.1.3,<2.0.0',
 'mlflow>=1.16.0,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'tensorflow>=2.0.0,<3.0.0',
 'tokenizers>=0.10.0,<0.11.0',
 'tqdm>=4.0.0,<5.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.6.0,<2.0.0']}

setup_kwargs = {
    'name': 'cclm',
    'version': '0.1.2',
    'description': 'NLP framework for composing together models modularly',
    'long_description': '## CCLM\n\n### Composable, Character-Level Models\n\n#### Why `cclm`?\n\n\nThe goal of `cclm` is to make the deep learning model development process modular by providing abstractions for structuring a computational graph.\n\nIf we think of the ML lifecycle as producing a usable class `Model` that consumers can call on `input` to get `output`, then comparing the model training process to human-led software development highlights some big differences. For instance often when we retrain models, we usually change the whole model at once - imagine a developer telling you every commit they made touched every line of code in the package. Similarly, using a pretrained model is like using a \'batteries included\' framework: you likely end up inheriting a good deal of functionality you don\'t require, and it may be hard to customize. These differences suggest that there may be changes that could make it easier to manage deep learning model development, particularly as models continue to explode in size.\n\n#### How does it work?\n\nThe way `cclm` aims to achieve the above is by making the model building process composable. There are many ways to pretrain a model on text, and infinite corpora on which to train, and each application has different needs.\n\n`cclm` makes it possible to define a `base` input on which to build many different computational graphs, then combine them. For instance, if there is a standard, published `cclm` model trained with masked language modeling (MLM) on (`wikitext` + `bookcorpus`), you might start with that, but add a second component to that model that uses the same `base`, but is pretrained to extract entities from `wiki-ner`. By combining the two pretrained components with a `ComposedModel`, you get a model with information from both tasks that you can then use as a starting point for your downstream task.\n\nCommon model components will be published onto the `cclm-shelf` to make it simple to mix and match capabilities.\n\nThe choice to emphasize character-level rather than arbitrary tokenization schemes is to make the input as generically useful across tasks as possible. Character-level input also makes it simpler to add realistic typos/noise to make models more robust to imperfect inputs.\n\n\n#### Basic concepts\n\nThe main output of a training job with `cclm` is a `ComposedModel`, which consists of a `Preprocessor` that turns text into a vector[int], a base model that embeds that vector input, and one or more model components that accept the output of the embedder. The `ComposedModel` concatenates the output from those models together to produce its final output.\n\nThe package uses `datasets` and `tokenizers` from `huggingface` for a standard interface and to benefit from their great framework. To fit models and preprocessors, you can also pass a `List[str]` directly.\n\nTo start, you need a `Preprocessor`.\n\n```python\nfrom cclm.preprocessing import Preprocessor\n\nprep = Preprocessor()  # set max_example_len to specify a maximum input length\nprep.fit(dataset) # defines the model\'s vocabulary (character-level)\n```\n\nOnce you have that, you can create an `Embedder`, which is the common base on which all the separate models will sit. This is a flexible class primarily responsible for holding a model that embeds a sequence of integers (representing characters) into a space the components expect. For more complicated setups, the `Embedder` could have a `ComposedModel` as its `model`\n\n```python\nfrom cclm.models import Embedder\n\nembedder = Embedder(prep.max_example_len, prep.n_chars)\n```\n\nThe embedder doesn\'t necessarily need to be fit by itself, as you can fit it while you do your first pretraining task.\n\nNow you\'re ready to build your first model using a pretraining task (here masked language modeling)\n\n```python\nfrom cclm.pretraining import MaskedLanguagePretrainer\n\npretrainer = MaskedLanguagePretrainer(embedder=embedder)\npretrainer.fit(dataset, epochs=10)\n```\n\nThe `MaskedLanguagePretrainer` defines a transformer-based model to do masked language modeling. Calling `.fit()` will use the `Preprocessor` to produce masked inputs and try to identify the missing input token(s) using `sampled_softmax` loss or negative sampling. This is just one example of a pretraining task, but others can be found in `cclm.pretrainers`.\n\nOnce you\'ve trained one or more models using `Pretrainer` objects, you can compose them together into one model.\n\n```python\ncomposed = ComposedModel(embedder, [pretrainer_a.model, pretrainer_b.model])\n```\n\nYou can then use `composed.model(x)` to embed input\n\n```python\nx = prep.string_to_array("cclm is neat", prep.max_example_len)\nemb = composed.model(x)   # has shape (1, prep.max_example_len, pretrainer_a_model_shape[-1]+pretrainer_b_model_shape[-1])\n```\n\n... or create a new model with something like\n\n```python\n# pool the output across the character dimension\ngmp = tf.keras.layers.GlobalMaxPool1D()\n# add a classification head on top\nd = tf.keras.layers.Dense(1, activation="sigmoid")\nkeras_model = tf.keras.Model(composed.model.input, d(gmp(composed.model.output)))\n```\n\n### Shelf\n\nThe `Shelf` class is used to load off-the-shelf components. These are published to a separate repo using git lfs, and are loaded with a specific tag.\n\n```python\nfrom cclm.shelf import Shelf\n\nshelf = Shelf()\nidentifier = "en_wiki_clm_1"\nitem_type = "preprocessor"\nshelf.fetch(identifier, item_type, tag="v0.2.1", cache_dir=".cclm")\nprep = Preprocessor(\n    load_from=os.path.join(cache_dir, identifier, item_type, "cclm_config.json")\n)\n```',
    'author': 'jamesmf',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesmf/cclm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
