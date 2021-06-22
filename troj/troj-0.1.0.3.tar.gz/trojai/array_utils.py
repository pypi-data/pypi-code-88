import numpy as np
import copy


def AdvLossSort(adv_examples, adv_losses, preds, k=5):
    '''

    :param adv_examples: Adversarial perturbations
    :param adv_losses: The losses for the perturbations
    :param preds: Adversarial predictions
    :param k:number of examples to return
    :return: top k loss examples, their losses, and the predictions.
    '''
    index_order = np.argsort(adv_losses, axis=1)
    sorted_preds = preds.copy()
    resorted_losses = adv_losses.copy()
    outs_array = adv_examples.copy()
    for i in range(index_order.shape[0]):
        outs_array[i] = adv_examples[i, index_order[i]]
        resorted_losses[i] = adv_losses[i, index_order[i]]
        sorted_preds[i] = preds[i, index_order[i]]
    return outs_array[:, :k], resorted_losses[:, :k], sorted_preds[:, :k]

def get_flipped(labels, adv_preds, original_ims, outs_array, losses):
    pass



def get_min_pert(original_ims, outs_array, losses, preds, norm=np.inf):
    '''

    :param original_ims:
    :param outs_array:
    :param losses:
    :param preds:
    :param norm:
    :return:
    '''
    # original_ims is the original images, and the outs_array are the adversarial examples, sorted by highest loss
    # make a copy of the original images the same shape as the output, copying the images along the second axis
    tile_list = [original_ims for i in range(outs_array.shape[1])]
    tiled = np.stack(tile_list)
    # swap the first and second axis
    tiled = np.swapaxes(tiled, 0, 1)
    assert tiled[0, 0, 0, 0, 0] == tiled[0, 1, 0, 0, 0]

    # reshape outputs and original images to collection of vectors
    flattened_shape = (
        outs_array.shape[0],
        outs_array.shape[1],
        outs_array.shape[2] * outs_array.shape[3] * outs_array.shape[4],
    )
    flattened_outs = np.reshape(outs_array, flattened_shape)
    flattened_original = np.reshape(tiled, flattened_shape)

    # subtract the original from the perturbed to get the perturbation vector
    perturbations = flattened_outs - flattened_original
    perturbation_norms = np.linalg.norm(perturbations, norm, axis=2)
    min_per_sample_idx = np.argmin(perturbation_norms, axis=1)

    min_pert_losses = []
    min_pert_preds = []
    min_pert_outs = []
    for idx in range(len(min_per_sample_idx)):
        min_pert_outs.append(outs_array[idx, min_per_sample_idx[idx]])
        min_pert_losses.append(losses[idx, min_per_sample_idx[idx]])
        min_pert_preds.append(preds[idx, min_per_sample_idx[idx]])

    min_pert_outs = np.asarray(min_pert_outs)
    min_pert_preds = np.asarray(min_pert_preds)
    min_pert_losses = np.asarray(min_pert_losses)
    return min_pert_outs, min_pert_preds, min_pert_losses


def true_min_pert(labels, preds, original, perturbation, losses, norm=np.inf):
    tile_list = [original for i in range(perturbation.shape[1])]
    tiled = np.stack(tile_list)
    # swap the first and second axis
    tiled = np.swapaxes(tiled, 0, 1)
    assert tiled[0, 0, 0, 0, 0] == tiled[0, 1, 0, 0, 0]

    # reshape outputs and original images to collection of vectors
    flattened_shape = (
        perturbation.shape[0],
        perturbation.shape[1],
        perturbation.shape[2] * perturbation.shape[3] * perturbation.shape[4],
    )
    flattened_outs = np.reshape(perturbation, flattened_shape)
    flattened_original = np.reshape(tiled, flattened_shape)

    # subtract the original from the perturbed to get the perturbation vector
    perturbations = flattened_outs - flattened_original
    perturbation_norms = np.linalg.norm(perturbations, norm, axis=2)

    tiled_labels = [labels for i in range(preds.shape[1])]
    tiled_labels = np.stack(tiled_labels)
    # swap the first and second axis
    tiled_labels = np.swapaxes(tiled_labels, 0, 1)
    #If the label isn't flipped, set min pert to 1.
    perturbation_norms[tiled_labels==preds] = 1.0
    min_per_sample_idx = np.argmin(perturbation_norms, axis=1)

    min_pert_losses = []
    min_pert_preds = []
    min_pert_outs = []
    for idx in range(len(min_per_sample_idx)):
        min_pert_outs.append(perturbation[idx, min_per_sample_idx[idx]])
        min_pert_losses.append(losses[idx, min_per_sample_idx[idx]])
        min_pert_preds.append(preds[idx, min_per_sample_idx[idx]])

    min_pert_outs = np.asarray(min_pert_outs)
    min_pert_preds = np.asarray(min_pert_preds)
    min_pert_losses = np.asarray(min_pert_losses)
    return min_pert_outs, min_pert_preds, min_pert_losses


def compute_Lp_distance(x1, x2, p=np.inf):
    '''

    :param x1:
    :param x2:
    :param p:
    :return:
    '''
    x1 = np.reshape(x1, (x1.shape[0], -1))
    x2 = np.reshape(x2, (x2.shape[0], -1))
    difference_vect = x1 - x2
    lp_distance = np.linalg.norm(difference_vect, p, axis=1)
    return lp_distance
