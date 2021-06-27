import sfu_ml_lib.metrics.aggregation.metric_functions as metric_functions
from sfu_ml_lib.base.metrics import Metric
from sfu_ml_lib.metrics.aggregation.aggregator import Statistic, Aggregation


MEAN_ABSOLUTE_ERROR = Aggregation(
    metric=Metric.MEAN_ABSOLUTE_ERROR,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=metric_functions.mean_absolute_error,
)

MEAN_SQUARE_ERROR = Aggregation(
    metric=Metric.MEAN_SQUARE_ERROR,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=metric_functions.mean_squared_error,
)

PEARSON_CORRELATION = Aggregation(
    metric=Metric.PEARSON_CORRELATION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=metric_functions.pearson_correlation,
)

ACCURACY_MULTICLASS = Aggregation(
    metric=Metric.ACCURACY,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.accuracy(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
    ),
)

ACCURACY_MULTILABEL = Aggregation(
    metric=Metric.ACCURACY,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.accuracy(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
    ),
)

JACCARD_SCORE_MULTILABEL = Aggregation(
    metric=Metric.JACCARD_SCORE,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.jaccard_score_multilabel(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
    ),
)

CROSS_ENTROPY_MULTICLASS = Aggregation(
    metric=Metric.CROSS_ENTROPY,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=metric_functions.cross_entropy_multiclass,
)

CROSS_ENTROPY_MULTILABEL = Aggregation(
    metric=Metric.CROSS_ENTROPY,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=metric_functions.cross_entropy_multilabel,
)

WEIGHTED_F1_MULTICLASS = Aggregation(
    metric=Metric.WEIGHTED_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='weighted',
    ),
)

WEIGHTED_F1_MULTILABEL = Aggregation(
    metric=Metric.WEIGHTED_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='weighted',
    ),
)

WEIGHTED_PRECISION_MULTICLASS = Aggregation(
    metric=Metric.WEIGHTED_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='weighted',
    ),
)

WEIGHTED_PRECISION_MULTILABEL = Aggregation(
    metric=Metric.WEIGHTED_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='weighted',
    ),
)

WEIGHTED_RECALL_MULTICLASS = Aggregation(
    metric=Metric.WEIGHTED_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='weighted',
    ),
)

WEIGHTED_RECALL_MULTILABEL = Aggregation(
    metric=Metric.WEIGHTED_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='weighted',
    ),
)

MICRO_F1_MULTICLASS = Aggregation(
    metric=Metric.MICRO_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='micro',
    ),
)

MICRO_F1_MULTILABEL = Aggregation(
    metric=Metric.MICRO_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='micro',
    ),
)

MICRO_PRECISION_MULTICLASS = Aggregation(
    metric=Metric.MICRO_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='micro',
    ),
)

MICRO_PRECISION_MULTILABEL = Aggregation(
    metric=Metric.MICRO_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='micro',
    ),
)

MICRO_RECALL_MULTICLASS = Aggregation(
    metric=Metric.MICRO_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='micro',
    ),
)

MICRO_RECALL_MULTILABEL = Aggregation(
    metric=Metric.MICRO_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='micro',
    ),
)

MACRO_F1_MULTICLASS = Aggregation(
    metric=Metric.MACRO_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='macro',
    ),
)

MACRO_F1_MULTILABEL = Aggregation(
    metric=Metric.MACRO_F1,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.f1_score(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='macro',
    ),
)

MACRO_PRECISION_MULTICLASS = Aggregation(
    metric=Metric.MACRO_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='macro',
    ),
)

MACRO_PRECISION_MULTILABEL = Aggregation(
    metric=Metric.MACRO_PRECISION,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.precision(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='macro',
    ),
)

MACRO_RECALL_MULTICLASS = Aggregation(
    metric=Metric.MACRO_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multiclass(logits),
        average='macro',
    ),
)

MACRO_RECALL_MULTILABEL = Aggregation(
    metric=Metric.MACRO_RECALL,
    statistics=[Statistic.TARGET, Statistic.LOGITS],
    function=lambda targets, logits: metric_functions.recall(
        targets=targets,
        predictions=metric_functions.logits_to_predictions_multilabel(logits),
        average='macro',
    ),
)
