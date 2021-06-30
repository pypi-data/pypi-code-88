from enum import Enum


class DataTypesRoles(Enum):
    """ Enum of Roles"""

    ID = "id"
    TIMESTAMP = "time stamp"
    FEATURE = "feature"
    PREDICTION_PROBABILITY = "prediction probability"
    PREDICTION_VALUE = "prediction value"
    LABEL = "label"
    LABEL_TIMESTAMP = "label time stamp"
    LABEL_WEIGHT = "label weight"
    METADATA = "metadata"


class TaskTypes(Enum):
    """ Enum of DataTypes"""

    BINARY_CLASSIFICATION = "Binary Classification"
    BINARY_ESTIMATION = "Binary Estimation"
    REGRESSION = "Regression"
    MULTICLASS_CLASSIFICATION = "Multiclass Classification"


class FeatureType(Enum):
    """ Enum of FeatureType"""

    numeric = "Numeric"
    boolean = "Boolean"
    categorical = "Categorical"
    time_stamp = "Timestamp"
    unknown = "Unknown"


class CategoricalSecondaryType(Enum):
    constant = "Cat_constant"
    dense = "Cat_dense"
    sparse = "Cat_sparse"


class NumericSecondaryType(Enum):
    num_right_tail = "Num_right_tail"
    num_left_tail = "Num_left_tail"
    num_centered = "Num_centered"


class CategoricalSecondaryType(Enum):
    constant = "Cat_constant"
    dense = "Cat_dense"
    sparse = "Cat_sparse"


class BooleanSecondaryType(Enum):
    flag = "Boolean_flag"
    numeric = "Boolean_numeric"


class NumericSecondaryType(Enum):
    num_right_tail = "Num_right_tail"
    num_left_tail = "Num_left_tail"
    num_centered = "Num_centered"
