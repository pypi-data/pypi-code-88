import numpy as np
from numpy.linalg import inv
from itertools import product, chain

def get_all_snap_rotations(snap):
    cloned_snaps = []
    for theta in [0, np.pi / 2, np.pi, 3 * np.pi / 2]:
        # Rotate around the y axis
        # From https://en.wikipedia.org/wiki/Rotation_matrix
        rotation = np.array([
            [np.cos(theta), 0, np.sin(theta), 0],
            [0, 1, 0, 0],
            [-np.sin(theta), 0, np.cos(theta), 0],
            [0, 0, 0, 1],
        ])
        transform = snap.transform @ rotation @ inv(snap.transform)
        cloned_snaps.append(snap.transformed_copy(transform))
    return cloned_snaps


def get_all_transformed_snaps(snaps):
    """
    Returns a list of all male snaps with quarter rotations about y
    and return a list of female snaps (no rotations applied) because
    only one piece needs to rotate
    """
    male = [s for s in snaps if s.polarity == '+']
    all_male = []
    for snap in male:
        all_male.extend(get_all_snap_rotations(snap))
    female = [s for s in snaps if s.polarity == '-']
    return {
        'male': all_male,
        'female': female,
    }


def get_all_transformed_snap_pairs(instance1_snaps, instance2_snaps):
    snaps1 = get_all_transformed_snaps(instance1_snaps)
    snaps2 = get_all_transformed_snaps(instance2_snaps)
    return chain(
        product(snaps1['male'], snaps2['female']),
        product(snaps1['female'], snaps2['male']),
    )


def closest_transform(snap_cands1, snap_cands2):
    min_dist = None
    snap_pair = None
    snap_cands1f = [snap for snap in snap_cands1
            if snap.polarity == '-']
    snap_cands1m = [snap for snap in snap_cands1
            if snap.polarity == '+']
    snap_cands2f = [snap for snap in snap_cands2
            if snap.polarity == '-']
    snap_cands2m = [snap for snap in snap_cands2
            if snap.polarity == '+']
    for snap1, snap2 in product(snap_cands1f, snap_cands2m):
        v = snap1.transform[:3, -1] - snap2.transform[:3, -1]
        dist = np.linalg.norm(v)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            snap_pair = snap1, snap2
    for snap1, snap2 in product(snap_cands1m, snap_cands2f):
        v = snap1.transform[:3, -1] - snap2.transform[:3, -1]
        dist = np.linalg.norm(v)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            snap_pair = snap1, snap2

    # http://www.boris-belousov.net/2016/12/01/quat-dist/
    Q = snap2.transform[:3, :3]
    min_rot_dist = None
    best_P = None
    best_rotation = None
    for phi in [0, np.pi / 2, np.pi, 3 * np.pi / 2]:
        # Rotate around the y axis
        # From https://en.wikipedia.org/wiki/Rotation_matrix
        rotation = np.array([
            [np.cos(phi), 0, np.sin(phi), 0],
            [0, 1, 0, 0],
            [-np.sin(phi), 0, np.cos(phi), 0],
            [0, 0, 0, 1],
        ])
        
        transform = snap1.transform @ rotation @ inv(snap2.transform)
        P = transform[:3, :3]
        R = P @ Q.T
        
        # Could use theta instead of val, but using val
        # to avoid the extra computation
        # theta = np.arccos((np.trace(R) - 1) / 2)
        val = -np.trace(R)
        if min_rot_dist is None or val < min_rot_dist:
            min_rot_dist = val
            best_P = P
            best_rotation = rotation

    snap1, snap2 = snap_pair
    #transform = snap1.transform
    #transform[:3, :3] = best_P
    #return transform @ np.linalg.inv(snap2.transform), snap1, snap2
    final_transform = snap1.transform @ best_rotation @ inv(snap2.transform)
    return final_transform, snap1, snap2
