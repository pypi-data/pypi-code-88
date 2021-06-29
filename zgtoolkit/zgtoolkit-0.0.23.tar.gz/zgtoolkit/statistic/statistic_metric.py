import numpy as np
from multiprocessing import Pool
from .iou import iou
from terminaltables import AsciiTable
from copy import deepcopy


def tpfp(cls_pred, cls_label, iou_thre):

    num_preds = cls_pred.shape[0]
    num_labels = cls_label.shape[0]
    tp = np.zeros(num_preds, dtype=np.float32)
    fp = np.zeros(num_preds, dtype=np.float32)

    if num_labels == 0:
        fp[...] = 1
        return tp, fp

    ious = iou(cls_pred[:, 0:4], cls_label[:, 0:4], iou_thre)
    ious_max = ious.max(axis=1)
    ious_argmax = ious.argmax(axis=1)

    sort_inds = np.argsort(-cls_pred[:, -2])
    gt_covered = np.zeros(num_labels, dtype=bool)
    for i in sort_inds:
        if ious_max[i] > iou_thre:
            matched_gt = ious_argmax[i]
            if not gt_covered[matched_gt]:
                gt_covered[matched_gt] = True
                tp[i] = 1
            else:
                fp[i] = 1
        else:
            fp[i] = 1

    return tp, fp


def get_cls_result(preds: list, labels: list, cls_id: int, score_thre):
    cls_preds = []
    cls_labels = []

    for pred, label in zip(preds, labels):
        cls_inds = np.logical_and(pred[:, -1] == cls_id, pred[:, -2] >= score_thre)
        cls_preds.append(pred[cls_inds])

        cls_inds = label[:, -1] == cls_id
        cls_labels.append(label[cls_inds])
    return cls_preds, cls_labels


def statistic_bbox_recall(preds: list, labels: list, score_thre, iou_thre, ignore_cls, classes, nproc=12):
    """
    :param preds: [[N, 6], ...]
    :param labels: [[M, 5], ...]
    :param score_thre:
    :param iou_thre:
    :param ignore_cls:
    :param classes:
    :return:
    """
    assert len(preds) == len(labels)
    img_nums = len(preds)
    if ignore_cls is not None:
        ignore_cls = [ignore_cls] if not isinstance(ignore_cls, list) else ignore_cls

    tables = [['class', 'gts', 'dets', 'tps', 'fps', 'precious', 'recall']]
    total_dets = []
    total_tps = []
    total_gts = []
    pool = Pool(nproc)
    for i, cls in enumerate(classes):
        if ignore_cls is not None and cls in ignore_cls:
            continue

        cls_preds, cls_labels = get_cls_result(preds, labels, i, score_thre)

        tpfps = pool.starmap(tpfp,
                             zip(cls_preds, cls_labels,
                                 [iou_thre for _ in range(img_nums)]))
        tps, fps = tuple(zip(*tpfps))
        gts = np.vstack(cls_labels).shape[0]
        dets = np.vstack(cls_preds).shape[0]

        tps = np.hstack(tps)
        fps = np.hstack(fps)
        tps = tps.sum()
        fps = fps.sum()
        assert dets == tps + fps

        precious = tps / dets * 100
        recall = tps / gts * 100
        total_gts.append(gts)
        total_tps.append(tps)
        total_dets.append(dets)
        tables.append([cls, f'{gts}', f'{dets}', f'{tps}', f'{fps}', f'{precious:.2f}', f'{recall:.2f}'])
    pool.close()
    total_gts = sum(total_gts)
    total_dets = sum(total_dets)
    total_tps = sum(total_tps)
    total_fps = total_dets - total_tps

    total_precious = total_tps / total_dets * 100
    total_recall = total_tps / total_gts * 100

    tables.append(['total', f'{total_gts}', f'{total_dets}', f'{total_tps}', f'{total_fps}',
                   f'{total_precious:.2f}', f'{total_recall:.2f}'])
    tables = AsciiTable(tables)
    tables.inner_footing_row_border = True

    print(tables.table)
