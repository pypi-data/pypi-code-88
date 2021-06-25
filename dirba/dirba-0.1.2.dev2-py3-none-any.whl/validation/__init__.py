try:
    import sklearn
    import pandas
except ImportError as e:
    raise ImportError('You should install scikit-learn first. Try it with "pip install dirba[validation]"') from e

from dirba.validation import metrics
from dirba.validation import dataset
from dirba.validation.validation import Validator
