import numpy as np

from .. import entities
from . import BaseModelAdapter, metrics

# Utility functions to use in the model adapters
#   these wrapper function should ease to make sure all predictions are built with proper metadata structure


def create_collection():
    collection = entities.AnnotationCollection(item=None)
    return collection


def model_info_name(model: entities.Model, snapshot: entities.Snapshot):
    return "{}-{}".format(model.name, snapshot.name)


def add_box_prediction(left, top, right, bottom, label, score,
                       adapter: BaseModelAdapter = None,
                       model: entities.Model = None, snapshot: entities.Snapshot = None,
                       collection: entities.AnnotationCollection = None):

    if collection is None:
        collection = create_collection()

    if adapter is not None:
        model = adapter.model_entity
        snapshot = adapter.snapshot

    model_snap_name = model_info_name(model=model, snapshot=snapshot)
    collection.add(
        annotation_definition=entities.Box(
            left=float(left),
            top=float(top),
            right=float(right),
            bottom=float(bottom),
            label=str(label)
        ),
        model_info={
            'name': model_snap_name,
            'confidence': float(score),
            'model_id': model.id,
            'snapshot_id': snapshot.id
        }
    )
    return collection


def add_classification(label, score,
                       adapter: BaseModelAdapter = None,
                       model: entities.Model = None, snapshot: entities.Snapshot = None,
                       collection: entities.AnnotationCollection = None):
    if collection is None:
        collection = create_collection()

    if adapter is not None:
        model = adapter.model_entity
        snapshot = adapter.snapshot

    model_snap_name = model_info_name(model=model, snapshot=snapshot)
    collection.add(annotation_definition=entities.Classification(label=label),
                   model_info={
                       'name': model_snap_name,
                       'confidence': float(score),
                       'model_id': model.id,
                       'snapshot_id': snapshot.id
                   })
    return collection


def is_ann_pred(ann: entities.Annotation, model: entities.Model = None, snapshot: entities.Snapshot = None, verbose=False):
    is_pred = 'user' in ann.metadata and 'model_info' in ann.metadata['user']

    if is_pred and model is not None:
        is_pred = is_pred and model.id == ann.metadata['user']['model_info']['model_id']
        verbose and print("Annotation {!r} prediction with model mismatch".format(ann.id))

    if is_pred and snapshot is not None:
        is_pred = is_pred and snapshot.id == ann.metadata['user']['model_info']['snapshot_id']
        verbose and print("Annotation {!r} prediction with snapshot mismatch".format(ann.id))

    return is_pred


def measure_item_box_predictions(item: entities.Item, model: entities.Model = None, snapshot: entities.Snapshot = None):
    annotations = item.annotations.list(filters=entities.Filters(field='type', values='box', resource=entities.FiltersResource.ANNOTATION))
    actuals = [ann for ann in annotations if 'model_info' not in ann.metadata['user']]
    predictions = [ann for ann in annotations if is_ann_pred(ann, model=model, snapshot=snapshot)]

    r_boxes, t_boxes = actuals, predictions  # TODO: test if we need to change the order of ref /test

    box_scores = metrics.match_box(ref_annotations=r_boxes,
                                   test_annotations=t_boxes,
                                   geometry_only=True)
    # Create the symmetric IoU metric
    test_iou_scores = [match.annotation_score for match in box_scores.values() if match.annotation_score > 0]
    matched_box = int(np.sum([1 for score in test_iou_scores if score > 0]))  # len(test_iou_scores)
    total_box = len(r_boxes) + len(t_boxes)
    extra_box = len(t_boxes) - matched_box
    missing_box = len(r_boxes) - matched_box
    assert total_box == extra_box + 2 * matched_box + missing_box
    # add missing to score
    test_iou_scores += [0 for i in range(missing_box)]
    test_iou_scores += [0 for i in range(extra_box)]

    boxes_report = {'box_ious': box_scores,
                    'box_annotations': r_boxes,
                    'box_mean_iou': np.mean(test_iou_scores),
                    'box_attributes_scores': np.mean([match.attributes_score for match in box_scores.values()]),
                    'box_ref_number': len(r_boxes),
                    'box_test_number': len(t_boxes),
                    'box_missing': missing_box,
                    'box_total': total_box,
                    'box_matched': matched_box,
                    'box_extra': extra_box,
                    }

    return boxes_report
