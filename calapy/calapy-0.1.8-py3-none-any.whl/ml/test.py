# websites:
# https://pytorch.org/docs/stable/torchvision/transforms.html
# https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py
# https://pytorch.org/hub/pytorch_vision_resnet/
# https://discuss.pytorch.org/t/normalize-each-input-image-in-a-batch-independently-and-inverse-normalize-the-output/23739
# https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

from . import torch
import numpy as np
from .. import clock as cp_clock
from ..strings import format_float_to_str as cp_strings_format_float_to_str


def classifier(model, loader, criterion):
    cp_timer = cp_clock.Timer()

    headers_stats = ['N_samples', *['C_' + str(v) for v in range(loader.V)], 'Loss', 'Accuracy']

    n_columns_stats = len(headers_stats)
    line_stats = [loader.n_samples, *loader.n_conditions_directories, None, None]  # type: list

    stats = {
        'headers': {headers_stats[i]: i for i in range(n_columns_stats)},
        'lines': [line_stats]}

    headers_trials = [
        'ID_Trial',
        *['Condition_' + str(v) for v in range(loader.V)],
        'Label',
        *['Probability_' + str(k) for k in range(loader.K)],
        'Classification',
        'Correct_Classification'
    ]

    n_columns_trials = len(headers_trials)

    trials = {
        'headers': {headers_trials[i]: i for i in range(n_columns_trials)},
        'lines': None}

    n_decimals_for_printing = 6

    if model.training:
        model.eval()  # Set model to evaluate mode

    if criterion.training:
        criterion.eval()

    softmax = torch.nn.Softmax(dim=1)
    if softmax.training:
        softmax.eval()

    # Now set requires_grad to false
    for param_model in model.parameters():
        param_model.requires_grad = False

    for param_criterion in criterion.parameters():
        param_criterion.requires_grad = False

    for param_softmax in softmax.parameters():
        param_softmax.requires_grad = False

    torch.set_grad_enabled(False)

    running_loss_e = 0.0
    running_corrects_e = 0

    start_index_samples = 0
    stop_index_samples = 0

    index_combinations_e = np.empty(2, dtype=object)
    index_combinations_e[1] = slice(0, loader.V, 1)
    combinations_e = np.empty([loader.n_samples, loader.V], dtype=object)

    index_outputs_e = np.empty(2, dtype=object)
    index_outputs_e[1] = slice(0, loader.K, 1)
    outputs_e = np.empty([loader.n_samples, loader.K], dtype=object)

    index_labels_e = np.empty(2, dtype=object)
    index_labels_e[1] = 0
    labels_e = np.empty([loader.n_samples, 1], dtype=object)

    classifications_e = labels_e.copy()

    correct_classifications_e = labels_e.copy()

    id_trials = np.arange(loader.n_samples, dtype=object)[:, None]

    # b = 0
    # Iterate over data.
    for data_eb in loader:
        samples_eb, labels_eb, combinations_eb = data_eb

        # forward
        outputs_eb = model(samples_eb)
        probabilities_eb = softmax(outputs_eb)
        _, classifications_eb = torch.max(outputs_eb, 1)
        correct_classifications_eb = (classifications_eb == labels_eb).long()
        loss_eb = criterion(outputs_eb, labels_eb)

        # todo: get probabilities
        # todo: fill trials['lines']

        stop_index_samples += samples_eb.shape[0]
        index_samples = slice(start_index_samples, stop_index_samples, 1)

        index_combinations_e[0] = index_samples
        combinations_e[tuple(index_combinations_e)] = combinations_eb.tolist()

        index_outputs_e[0] = index_samples
        outputs_e[tuple(index_outputs_e)] = probabilities_eb.tolist()

        index_labels_e[0] = index_samples
        labels_e[tuple(index_labels_e)] = labels_eb.tolist()

        classifications_e[tuple(index_labels_e)] = classifications_eb.tolist()

        correct_classifications_e[tuple(index_labels_e)] = correct_classifications_eb.tolist()

        start_index_samples = stop_index_samples

        running_loss_e += loss_eb.item() * samples_eb.shape[0]
        # noinspection PyTypeChecker
        running_corrects_e += torch.sum(correct_classifications_eb).item()

        # b += 1

    loss_e = running_loss_e / loader.n_samples
    accuracy_e = running_corrects_e / loader.n_samples

    stats['lines'][0][stats['headers']['Loss']] = loss_e
    stats['lines'][0][stats['headers']['Accuracy']] = accuracy_e

    trials['lines'] = np.concatenate(
        (id_trials, combinations_e, labels_e, outputs_e, classifications_e, correct_classifications_e),
        axis=1)

    loss_str_e = cp_strings_format_float_to_str(loss_e, n_decimals=n_decimals_for_printing)
    accuracy_str_e = cp_strings_format_float_to_str(accuracy_e, n_decimals=n_decimals_for_printing)

    print('Test. Loss: {:s}. Accuracy: {:s}.'.format(loss_str_e, accuracy_str_e))
    print()

    time_test = cp_timer.get_delta_time()

    print('Test completed in {d} days {h} hours {m} minutes {s} seconds'.format(
        d=time_test.days, h=time_test.hours,
        m=time_test.minutes, s=time_test.seconds))

    return stats, trials
