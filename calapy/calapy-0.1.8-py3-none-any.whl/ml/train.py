# websites:
# https://pytorch.org/docs/stable/torchvision/transforms.html
# https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py
# https://pytorch.org/hub/pytorch_vision_resnet/
# https://discuss.pytorch.org/t/normalize-each-input-image-in-a-batch-independently-and-inverse-normalize-the-output/23739
# https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

from . import torch
import math
import os
import copy
from .. import txt as cp_txt
from .. import clock as cp_clock
from ..strings import format_float_to_str as cp_strings_format_float_to_str


def classifier_with_early_stop(
        model, loader, criterion, optimizer, scheduler, I=10, E=None, directory_outputs=None):

    cp_timer = cp_clock.Timer()

    for key_loader_k in loader.keys():
        if key_loader_k == 'training' or key_loader_k == 'validation':
            pass
        else:
            raise ValueError('Unknown keys in loader')

    headers = [
        'Epoch', 'Unsuccessful Epochs', 'Training Loss', 'Training Accuracy',
        'Validation Loss', 'Lowest Validation Loss', 'Is Lower Loss',
        'Validation Accuracy', 'Highest Validation Accuracy', 'Is Higher Accuracy']

    n_columns = len(headers)
    new_line_stats = [None] * n_columns  # type: list

    stats = {
        'headers': {headers[k]: k for k in range(n_columns)},
        'n_columns': n_columns,
        'lines': []}

    if directory_outputs is None:
        directory_outputs = 'outputs'

    os.makedirs(directory_outputs, exist_ok=True)

    directory_best_model_state = os.path.join(directory_outputs, 'best_model_state.pth')
    directory_last_model_state = os.path.join(directory_outputs, 'last_model_state.pth')

    directory_best_model = os.path.join(directory_outputs, 'best_model.pth')
    directory_last_model = os.path.join(directory_outputs, 'last_model.pth')

    directory_stats = os.path.join(directory_outputs, 'stats.csv')

    n_decimals_for_printing = 6

    best_model_wts = copy.deepcopy(model.state_dict())

    lowest_loss = math.inf
    lowest_loss_str = str(lowest_loss)
    highest_accuracy = -math.inf
    highest_accuracy_str = str(highest_accuracy)

    if E is None:
        E = math.inf

    if I is None:
        I = math.inf

    i = 0
    e = 0

    n_dashes = 110
    dashes = '-' * n_dashes
    print(dashes)

    while (e < E) and (i < I):

        print('Epoch {e} ...'.format(e=e))

        stats['lines'].append(new_line_stats.copy())
        stats['lines'][e][stats['headers']['Epoch']] = e

        # Each epoch has a training and a validation phase
        # training phase
        model.train()  # Set model to training mode
        criterion.train()

        running_loss_e = 0.0
        running_corrects_e = 0
        n_samples_e = 0

        b = 0
        # Iterate over data.
        for batch_eb, labels_eb in loader['training']:
            # zero the parameter gradients
            optimizer.zero_grad()

            # forward
            # track history
            torch.set_grad_enabled(True)
            outputs = model(batch_eb)
            _, preds = torch.max(outputs, 1)
            loss_eb = criterion(outputs, labels_eb)

            # backward + optimize
            loss_eb.backward()
            optimizer.step()

            torch.set_grad_enabled(False)

            running_loss_e += loss_eb.item() * batch_eb.shape[loader['training'].batch_axis_inputs]
            # noinspection PyTypeChecker
            running_corrects_e += torch.sum(preds == labels_eb).item()
            
            n_samples_e += batch_eb.shape[loader['training'].batch_axis_inputs]

            b += 1

        # scheduler.step()

        loss_e = running_loss_e / n_samples_e
        accuracy_e = running_corrects_e / n_samples_e

        loss_str_e = cp_strings_format_float_to_str(loss_e, n_decimals=n_decimals_for_printing)
        accuracy_str_e = cp_strings_format_float_to_str(accuracy_e, n_decimals=n_decimals_for_printing)

        print('Epoch: {:d}. Training.   Loss: {:s}. Accuracy: {:s}.'.format(e, loss_str_e, accuracy_str_e))

        stats['lines'][e][stats['headers']['Training Loss']] = loss_e
        stats['lines'][e][stats['headers']['Training Accuracy']] = accuracy_e

        # validation phase
        model.eval()  # Set model to evaluate mode

        criterion.eval()

        # zero the parameter gradients
        optimizer.zero_grad()

        torch.set_grad_enabled(False)

        running_loss_e = 0.0
        running_corrects_e = 0

        n_samples_e = 0

        b = 0
        # Iterate over data.
        for batch_eb, labels_eb in loader['validation']:

            # forward
            outputs = model(batch_eb)
            _, preds = torch.max(outputs, 1)
            loss_eb = criterion(outputs, labels_eb)

            running_loss_e += loss_eb.item() * batch_eb.shape[loader['validation'].batch_axis_inputs]
            # noinspection PyTypeChecker
            running_corrects_e += torch.sum(preds == labels_eb).item()

            n_samples_e += batch_eb.shape[loader['validation'].batch_axis_inputs]

            b += 1

        loss_e = running_loss_e / n_samples_e
        accuracy_e = running_corrects_e / n_samples_e

        loss_str_e = cp_strings_format_float_to_str(loss_e, n_decimals=n_decimals_for_printing)
        accuracy_str_e = cp_strings_format_float_to_str(accuracy_e, n_decimals=n_decimals_for_printing)

        stats['lines'][e][stats['headers']['Validation Loss']] = loss_e
        stats['lines'][e][stats['headers']['Validation Accuracy']] = accuracy_e

        if accuracy_e > highest_accuracy:
            highest_accuracy = accuracy_e
            highest_accuracy_str = cp_strings_format_float_to_str(highest_accuracy, n_decimals=n_decimals_for_printing)

            stats['lines'][e][stats['headers']['Is Higher Accuracy']] = 1
            stats['lines'][e][stats['headers']['Highest Validation Accuracy']] = highest_accuracy
        else:
            stats['lines'][e][stats['headers']['Is Higher Accuracy']] = 0
            stats['lines'][e][stats['headers']['Highest Validation Accuracy']] = highest_accuracy

        if loss_e < lowest_loss:

            lowest_loss = loss_e
            lowest_loss_str = cp_strings_format_float_to_str(lowest_loss, n_decimals=n_decimals_for_printing)
            i = 0
            stats['lines'][e][stats['headers']['Is Lower Loss']] = 1
            stats['lines'][e][stats['headers']['Unsuccessful Epochs']] = i
            stats['lines'][e][stats['headers']['Lowest Validation Loss']] = lowest_loss

            best_model_wts = copy.deepcopy(model.state_dict())  # deep copy the model
            for directory_i in [directory_best_model, directory_best_model_state]:
                if os.path.isfile(directory_i):
                    os.remove(directory_i)

            torch.save(model, directory_best_model)
            torch.save(best_model_wts, directory_best_model_state)

        else:
            i += 1
            stats['lines'][e][stats['headers']['Is Lower Loss']] = 0
            stats['lines'][e][stats['headers']['Unsuccessful Epochs']] = i
            stats['lines'][e][stats['headers']['Lowest Validation Loss']] = lowest_loss

        last_model_wts = copy.deepcopy(model.state_dict())  # deep copy the model
        for directory_i in [directory_last_model, directory_last_model_state, directory_stats]:
            if os.path.isfile(directory_i):
                os.remove(directory_i)

        torch.save(model, directory_last_model)
        torch.save(last_model_wts, directory_last_model_state)

        cp_txt.lines_to_csv_file(stats['lines'], directory_stats, stats['headers'])

        print('Epoch: {:d}. Validation. Loss: {:s}. Lowest Loss: {:s}. Accuracy: {:s}. Highest Accuracy: {:s}.'.format(
            e, loss_str_e, lowest_loss_str, accuracy_str_e, highest_accuracy_str))

        print('Epoch {e} - Unsuccessful Epochs {i}.'.format(e=e, i=i))

        e += 1
        print(dashes)

    print()
    E = e

    time_training = cp_timer.get_delta_time()

    print('Training completed in {d} days {h} hours {m} minutes {s} seconds'.format(
        d=time_training.days, h=time_training.hours,
        m=time_training.minutes, s=time_training.seconds))
    print('Number of Epochs: {E:d}'.format(E=E))
    print('Lowest Validation Loss: {:s}'.format(lowest_loss_str))
    print('Highest Validation Accuracy: {:s}'.format(highest_accuracy_str))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model, stats
