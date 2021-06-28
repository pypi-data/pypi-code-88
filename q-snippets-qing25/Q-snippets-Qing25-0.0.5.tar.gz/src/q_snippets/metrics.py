import os
import re
import collections
import string
import numpy as np

def compute_prediction_checklist(samples,
                                 features,
                                 predictions,
                                 version_2_with_negative: bool = False,
                                 n_best_size: int = 20,
                                 max_answer_length: int = 30,
                                 cls_threshold: float = 0.5):
    """
    Post-processes the predictions of a question-answering model to convert them to answers that are substrings of the
    original contexts. This is the base postprocessing functions for models that only return start and end logits.
    对于每条feature会有一个prediction， 先遍历features获得sample_id => [feature_idx,]的索引，可以对每个sample从多个feature
    获得多个结果，最后排序选择topn。
    version_2_with_negative: 结果中是否考虑无答案的情况。
    Args:
        samples: The non-preprocessed dataset (see the main script for more information).      
        features: The processed dataset (see the main script for more information).             
        predictions (:obj:`Tuple[np.ndarray, np.ndarray]`):
            The predictions of the model: two arrays containing the start logits and the end logits respectively. Its
            first dimension must match the number of elements of :obj:`features`.
        version_2_with_negative (:obj:`bool`, `optional`, defaults to :obj:`False`):
            Whether or not the underlying dataset contains samples with no answers.
        n_best_size (:obj:`int`, `optional`, defaults to 20):
            The total number of n-best predictions to generate when looking for an answer.
        max_answer_length (:obj:`int`, `optional`, defaults to 30):
            The maximum length of an answer that can be generated. This is needed because the start and end predictions
            are not conditioned on one another.
        cls_threshold (:obj:`float`, `optional`, defaults to 0):
            The threshold used to select the null answer: if the best answer has a score that is less than the score of
            the null answer minus this threshold, the null answer is selected for this sample (note that the score of
            the null answer for an sample giving several features is the maxnium of the scores for the null answer on
            each feature: all features must be aligned on the fact they `want` to predict a null answer).
            Only useful when :obj:`version_2_with_negative` is :obj:`True`.
    """
    assert len(predictions) == 3, "`predictions` should be a tuple with two elements (start_logits, end_logits, cls_logits)."
    all_start_logits, all_end_logits, all_cls_logits = predictions

    assert len(predictions[0]) == len(features), "Number of predictions should be equal to number of features."
    # if len(predictions[0]) != len(features):
        # features = features[:len(predictions[0])]

    # Build a map sample to its corresponding features.
    features_per_sample = collections.defaultdict(list)
    for i, feature in enumerate(features):
        features_per_sample[feature["sample_id"]].append(i)

    # The dictionaries we have to fill.
    all_predictions = collections.OrderedDict()
    all_nbest_json = collections.OrderedDict()
    all_cls_predictions = []

    # Let's loop over all the samples!
    for sample_index, sample in enumerate(samples):
        # Those are the indices of the features associated to the current sample.
        feature_indices = features_per_sample[sample['qid']]

        min_null_prediction = None
        prelim_predictions = []
        score_answerable = -1
        # Looping through all the features associated to the current sample.
        for feature_index in feature_indices:
            # We grab the predictions of the model for this feature.
            start_logits = all_start_logits[feature_index]
            end_logits = all_end_logits[feature_index]
            cls_logits = all_cls_logits[feature_index]
            # This is what will allow us to map some the positions in our logits to span of texts in the original
            # context.
            offset_mapping = features[feature_index]["offset_mapping"]
            # Optional `token_is_max_context`, if provided we will remove answers that do not have the maximum context
            # available in the current feature.
            token_is_max_context = features[feature_index].get("token_is_max_context", None)

            # Update minimum null prediction.
            feature_null_score = start_logits[0] + end_logits[0]
            exp_answerable_scores = np.exp(cls_logits - np.max(cls_logits))
            feature_answerable_score = exp_answerable_scores / exp_answerable_scores.sum()
            if feature_answerable_score[-1] > score_answerable:
                score_answerable = feature_answerable_score[-1]
                answerable_probs = feature_answerable_score
            if min_null_prediction is None or min_null_prediction["score"] > feature_null_score:
                min_null_prediction = {
                    "offsets": (0, 0),
                    "score": feature_null_score,
                    "start_logit": start_logits[0],
                    "end_logit": end_logits[0],
                }
            # Go through all possibilities for the `n_best_size` greater start and end logits.
            start_indexes = np.argsort(start_logits)[-1:-n_best_size - 1:-1].tolist()
            end_indexes = np.argsort(end_logits)[-1:-n_best_size - 1:-1].tolist()
            for start_index in start_indexes:
                for end_index in end_indexes:
                    # Don't consider out-of-scope answers, either because the indices are out of bounds or correspond
                    # to part of the input_ids that are not in the context.
                    if (start_index >= len(offset_mapping) or
                            end_index >= len(offset_mapping) or
                            offset_mapping[start_index] is None or
                            offset_mapping[end_index] is None or
                            offset_mapping[start_index] == (0, 0) or
                            offset_mapping[end_index] == (0, 0)):
                        continue
                    # Don't consider answers with a length that is either < 0 or > max_answer_length.
                    if end_index <= start_index or end_index - start_index + 1 > max_answer_length:
                        continue
                    # Don't consider answer that don't have the maximum context available (if such information is
                    # provided).
                    if token_is_max_context is not None and not token_is_max_context.get(
                            str(start_index), False):
                        continue
                    prelim_predictions.append({
                        "offsets": (offset_mapping[start_index][0],  offset_mapping[end_index][1]),
                        "score":start_logits[start_index] + end_logits[end_index],
                        "start_logit": start_logits[start_index],
                        "end_logit": end_logits[end_index],
                    })
        if version_2_with_negative:
            # Add the minimum null prediction
            prelim_predictions.append(min_null_prediction)
            pred_cls_label = True if np.argmax(np.array(answerable_probs)) == 0 else False
            all_cls_predictions.append([sample['qid'], pred_cls_label, answerable_probs[0], answerable_probs[1]])

        # Only keep the best `n_best_size` predictions.
        predictions = sorted(
            prelim_predictions, key=lambda x: x["score"],
            reverse=True)[:n_best_size]

        # Add back the minimum null prediction if it was removed because of its low score.
        if version_2_with_negative and not any(p["offsets"] == (0, 0) for p in predictions):
            predictions.append(min_null_prediction)

        # Use the offsets to gather the answer text in the original context.
        context = sample["context"]
        for pred in predictions:
            offsets = pred.pop("offsets")
            pred["text"] = context[offsets[0]:offsets[1]] if context[offsets[0]:offsets[1]] != "" else "no answer"

        # In the very rare edge case we have not a single non-null prediction, we create a fake prediction to avoid
        # failure.
        if len(predictions) == 0 or (len(predictions) == 1 and predictions[0]["text"] == "no answer"):
            predictions.insert(0, {
                "text": "no answer",
                "start_logit": 0.0,
                "end_logit": 0.0,
                "score": 0.0
            })

        # Compute the softmax of all scores (we do it with numpy to stay independent from torch/tf in this file, using
        # the LogSumExp trick).
        scores = np.array([pred.pop("score") for pred in predictions])
        exp_scores = np.exp(scores - np.max(scores))
        probs = exp_scores / exp_scores.sum()

        # Include the probabilities in our predictions.
        for prob, pred in zip(probs, predictions):
            pred["probability"] = prob

        # Pick the best prediction. If the null answer is not possible, this is easy.
        if not version_2_with_negative:
            all_predictions[sample["qid"]] = predictions[0]["text"]
        else:
            # Otherwise we first need to find the best non-empty prediction.
            i = 0
            while predictions[i]["text"] == "no answer" and i < len(predictions)-1:
                i += 1
            best_non_null_pred = predictions[i]

            if answerable_probs[1] < cls_threshold:
                all_predictions[sample['qid']] = "no answer"
            else:
                all_predictions[sample['qid']] = best_non_null_pred['text']

        # Make `predictions` JSON-serializable by casting np.float back to float.
        all_nbest_json[sample["qid"]] = [{
            k: (float(v)
                if isinstance(v, (np.float16, np.float32, np.float64)) else v)
            for k, v in pred.items()
        } for pred in predictions]
        all_cls_predictions = [
            [_[0], _[1], float(_[2]), float(_[3])]
            for _ in all_cls_predictions
        ]

    return all_predictions, all_nbest_json, all_cls_predictions



def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""

    def remove_articles(text):
        regex = re.compile(r"\b(a|an|the)\b", re.UNICODE)
        return re.sub(regex, " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    if s == '':
        return s
    return white_space_fix(remove_articles(remove_punc(lower(s))))


def get_tokens(s):
    if not s:
        return []
    return normalize_answer(s).split()


def compute_f1(a_gold, a_pred):
    gold_toks = get_tokens(a_gold)
    pred_toks = get_tokens(a_pred)
    common = collections.Counter(gold_toks) & collections.Counter(pred_toks)
    num_same = sum(common.values())
    if len(gold_toks) == 0 or len(pred_toks) == 0:
        # If either is no-answer, then F1 is 1 if they agree, 0 otherwise
        return int(gold_toks == pred_toks)
    if num_same == 0:
        return 0
    precision = 1.0 * num_same / len(pred_toks)
    recall = 1.0 * num_same / len(gold_toks)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1

from torchmetrics.functional import accuracy, precision_recall, precision



if __name__ == '__main__':
    # f1 = compute_f1("你好？hh", "NO go away 不好")
    # f1 = compute_f1("你好？", "你好")
    # print(f1)
    a = [1,1,1,0,0]
    b = [1,1,0,0,0]
    import torch
    print(accuracy(torch.tensor(a),torch.tensor(b)))
    print(precision_recall(torch.tensor(a),torch.tensor(b), 'macro', num_classes=2))
    print(precision(torch.tensor(a),torch.tensor(b)))

