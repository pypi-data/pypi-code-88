import logging
import time
import warnings
from itertools import product, repeat
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import List, Optional, Tuple

import importlib_resources
import numpy as np
import spiceypy as spice
from shapely.geometry import Point, Polygon, box
from tqdm import tqdm

from uvisaurorae.data_retrieval import make_metakernel

logger = logging.getLogger(__name__)


class UVISAuroralProjector(object):
    """
    Class for managing auroral projections.
    """

    def __init__(
        self,
        nbins_lon: int,
        nbins_lat: int,
        spice_dir: Path,
        raise_spice_insufficient: bool = True,
    ):
        """
        Constructor method.

        :param nbins_lon: Number of projection bins in longitude (0...360 deg).
        :param nbins_lat: Number of projection bins in latitude (-90...90 deg).
        :param spice_dir: Root directory of SPICE kernels.
        :param raise_spice_insufficient: Whether the projector should raise an exception if a record is not covered by
            SPICE kernels. If `false`, will silently skip records which cannot be projected.
        """
        # Set up binning
        self.lon_bins = np.linspace(0, 360, num=nbins_lon + 1)
        self.lat_bins = np.linspace(-90, 90, num=nbins_lat + 1)
        self.lon_centers = self.lon_bins[:-1] + np.diff(self.lon_bins) / 2
        self.lat_centers = self.lat_bins[:-1] + np.diff(self.lat_bins) / 2

        # Determine bin-binning for polar pixels (combine bins near the pole for projection speed)
        self.bin_map = np.full((len(self.lon_centers), len(self.lat_centers)), np.nan)
        self.is_master_bin = np.zeros(self.bin_map.shape, dtype=bool)
        bin_colat_start = 85
        for lat_idx in np.where(np.abs(self.lat_centers) > bin_colat_start)[0]:
            n_bins = (
                (90 - np.abs(self.lat_centers[lat_idx])) / (90 - bin_colat_start)
            ) ** 2 * len(self.lon_centers)
            self.bin_map[:, lat_idx] = (
                np.digitize(self.lon_centers, np.linspace(0, 360, int(n_bins) + 1)) - 1
            )
            for i in np.unique(self.bin_map[:, lat_idx]):
                tmp = np.where(self.bin_map[:, lat_idx] == i)[0]
                self.is_master_bin[int(np.mean(tmp)), lat_idx] = True

        self.spice_dir = spice_dir
        self.metakernels: List[Path] = []
        self.raise_spice_insufficient = raise_spice_insufficient
        self.reset_spice()

    def reset_spice(self) -> None:
        """
        Clear SPICE kernel cache and reload all necessary kernels, needed for loading updated metakernels. Will create
        a new unique metakernel and add its path to ``self.metakernels`` to make sure it can be deleted later.

        :return: None
        """
        # Clear SPICE kernels
        spice.kclear()

        # Load SPICE kernels
        metakernel = make_metakernel(self.spice_dir)
        time.sleep(0.5)  # Need to wait for a bit here to avoid file reading errors
        spice.furnsh(str(metakernel))
        self.metakernels.append(metakernel)

        # Load some additional SPICE kernels if not loaded already
        # Note that "saturn1100.tpc" redefines the size of Saturn (may be needed to refresh the kernel pool before other
        # calculations using this parameter are performed)
        for kernel in ["naif0012.tls", "saturn1100.tpc", "frame_ksmag.tf"]:
            k = importlib_resources.files("uvisaurorae.resources").joinpath(kernel)  # type: ignore
            try:
                spice.kinfo(str(k))
            except spice.stypes.SpiceyError:
                spice.furnsh(str(k))

    def remove_metakernels(self) -> None:
        """
        Delete all metakernels which are listed in ``self.metakernels``.

        :return: None
        """
        for mk in self.metakernels:
            if mk.exists():
                mk.unlink()
        self.metakernels = []

    @staticmethod
    def get_fov_vectors(
        line_bin: int, ul_corner_line: int, lr_corner_line: int
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Return field of view vectors of a pixel binning in the SPICE UVIS frame.

        :param line_bin: Number of neighboring pixels binned together.
        :param ul_corner_line: First used pixel.
        :param lr_corner_line: Last used pixel.
        :return: Array with pixel center vectors of shape (# pixels, 3), array with pixel edge/corner vectors of shape
            (# pixels, # edge/corner vectors / hardcoded 12, 3).
        """
        # Calculate number of pixels along the sensor
        npx = int(np.ceil((lr_corner_line + 1 - ul_corner_line) / line_bin))

        # Get UVIS_FUV FOV (NAIF ID of UVIS_FUV -82840, max number of vectors returned)
        _, _, boresight, _, boundvec = spice.getfov(-82840, 100)

        # Get all angles between corner points of the field of view
        all_angles = []
        for iii in range(len(boundvec)):
            for jjj in range(iii + 1, len(boundvec)):
                all_angles.append(np.arccos(np.dot(boundvec[iii], boundvec[jjj])))
        sorted_angles = np.sort(np.unique(np.array(all_angles)))
        width_rad = sorted_angles[0]  # short side
        length_rad = sorted_angles[1]  # long side

        # Get all corner points between detector pixels
        all_corners = np.full((npx + 1, 2, 3), np.nan)
        corner_bins = np.arange(ul_corner_line - 32, lr_corner_line + 2 - 32, line_bin)
        for iii in range(len(corner_bins)):
            all_corners[iii, 0, :] = spice.rotvec(
                spice.rotvec(boresight, width_rad / 2, 2),
                length_rad / 64 * corner_bins[iii],
                1,
            )
            all_corners[iii, 1, :] = spice.rotvec(
                spice.rotvec(boresight, -width_rad / 2, 2),
                length_rad / 64 * corner_bins[iii],
                1,
            )

        # Determine the 1 center and 4 corner viewing directions of each pixel in the UVIS_FUV frame
        fov_centers = np.full((npx, 3), np.nan)
        fov_corners = np.full((npx, 4, 3), np.nan)
        center_bins = corner_bins[:-1] + np.diff(corner_bins) / 2
        for iii in range(npx):
            fov_corners[iii, :2, :] = all_corners[iii, :, :]
            fov_corners[iii, 2:, :] = all_corners[iii + 1, ::-1, :]
            fov_centers[iii, :] = spice.rotvec(
                boresight, length_rad / 64 * center_bins[iii], 1
            )

        # Get some support vectors along the pixel corners
        n_supp = 2
        fov_corners_supp = np.full((npx, 4 * (n_supp + 1), 3), np.nan)
        for iii in range(npx):
            cnt = 0
            for ccc in range(4):
                start_vec = fov_corners[iii, ccc, :]
                end_vec = fov_corners[iii, (ccc + 1) % 4, :]
                for sss in range(n_supp + 1):
                    fov_corners_supp[iii, cnt, :] = (
                        start_vec * (n_supp + 1 - sss) + end_vec * sss
                    ) / (n_supp + 1)
                    cnt += 1

        return fov_centers, fov_corners_supp

    def proj_point(
        self, view_dir: np.ndarray, et_time: float
    ) -> Tuple[np.ndarray, float]:
        """
        Calculate the intersection of a viewing vector in the SPICE UVIS frame with Saturn's auroral layer.

        :param view_dir: Viewing vector in the SPICE UVIS frame.
        :param et_time: Ephemeris time.
        :return: (longitude, latitude), elevation angle (all in deg)
        """
        try:
            with spice.no_found_check():
                center_proj_cart, _, _, found = spice.sincpt(
                    "ELLIPSOID",
                    "SATURN",
                    et_time,
                    "CASSINI_KSMAG",
                    "LT+S",
                    "CASSINI",
                    "CASSINI_UVIS_FUV",
                    view_dir,
                )
            if not found:
                return np.array([np.nan, np.nan]), np.nan
        except (
            spice.utils.exceptions.SpiceSPKINSUFFDATA,
            spice.utils.exceptions.SpiceCKINSUFFDATA,
        ) as e:
            if self.raise_spice_insufficient:
                raise e
            else:
                logger.warning(
                    "Insufficient SPICE data to calculate surface intercept, ignored"
                )
                return np.array([np.nan, np.nan]), np.nan

        center_proj_sph = np.array(spice.reclat(center_proj_cart))
        center_proj_sph[1:] *= 180 / np.pi
        # 0 LT/lon starts at -X axis
        center_proj_sph[1] = (center_proj_sph[1] + 180) % 360
        # Calculate viewing angle
        radii = spice.bodvrd("SATURN", "RADII", 3)[1]
        sfnm = spice.surfnm(*radii, center_proj_cart)
        viewdir_ksm = spice.mxv(
            spice.pxform("CASSINI_UVIS_FUV", "CASSINI_KSMAG", et_time), view_dir
        )
        rad_angle = spice.vsep(viewdir_ksm, sfnm) - np.pi / 2
        return center_proj_sph[1:], rad_angle / np.pi * 180


def project_data_parallel(
    projector: UVISAuroralProjector,
    integrated_data: np.ndarray,
    et_times: np.ndarray,
    line_bin: int,
    ul_corner_line: int,
    lr_corner_line: int,
    records: Optional[List[int]] = None,
    n_workers: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Project UVIS data in parallel mode; maps ``project_data`` to several parallel workers.

    :param projector: Projector handling the projection.
    :param integrated_data: Integrated UVIS intensity data in shape (# records, # pixels).
    :param et_times: 1D array of shape (# records) holding the start of each record.
    :param line_bin: LINE BIN metadata item.
    :param ul_corner_line: UL CORNER LINE metadata item.
    :param lr_corner_line: LR CORNER LINE metadata item.
    :param records: List of record numbers to project, zero-indexed.
    :param n_workers: Number of workers to perform the projection with.
    :return: Projection grids with intensity sum, number of UVIS pixels in the bin, minimum spacecraft elevation angle.
    """
    tstart = time.time()
    logger.info("Starting projection in parallel mode")
    if n_workers is None:
        n_workers = cpu_count()
        logger.info(f"Auto setting to use {n_workers} workers")
    else:
        logger.info(f"Using {n_workers} workers")
    n_workers = min(n_workers, cpu_count())

    if records is None:
        records = np.arange(integrated_data.shape[0] - 1).astype(int)
    record_lists = np.array_split(records, n_workers)
    record_lists = [r for r in record_lists if len(r)]

    with Pool(n_workers) as p:
        output = p.starmap(
            project_data,
            zip(
                repeat(projector),
                repeat(integrated_data),
                repeat(et_times),
                repeat(line_bin),
                repeat(ul_corner_line),
                repeat(lr_corner_line),
                record_lists,
                repeat(True),
            ),
        )

    proj_sum = np.sum(np.array(output)[:, 0], axis=0)
    proj_num = np.sum(np.array(output)[:, 1], axis=0)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        proj_min_angle = np.nanmin(np.array(output)[:, 2], axis=0)
    proj_min_angle[proj_num == 0] = np.nan

    tstop = time.time()
    logger.info("Projection successful, took {:0.1f} seconds".format(tstop - tstart))

    return proj_sum, proj_num, proj_min_angle


def project_data(
    projector: UVISAuroralProjector,
    integrated_data: np.ndarray,
    et_times: List[float],
    line_bin: int,
    ul_corner_line: int,
    lr_corner_line: int,
    records: Optional[List[int]] = None,
    disable_progress: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Project UVIS data with a single worker.

    :param projector: Projector handling the projection.
    :param integrated_data: Integrated UVIS intensity data in shape (# records, # pixels).
    :param et_times: 1D array of shape (# records) holding the start of each record.
    :param line_bin: LINE BIN metadata item.
    :param ul_corner_line: UL CORNER LINE metadata item.
    :param lr_corner_line: LR CORNER LINE metadata item.
    :param records: List of record numbers to project, zero-indexed.
    :param disable_progress: Whether to disable the progress bar.
    :return: Projection grids with intensity sum, number of UVIS pixels in the bin, minimum spacecraft elevation angle.
    """
    tstart = time.time()
    if not disable_progress:
        logger.info("Starting projection")

    # Set up output arrays
    nbins_lon = len(projector.lon_centers)
    nbins_lat = len(projector.lat_centers)
    proj_sum = np.zeros((nbins_lon, nbins_lat))
    proj_num = np.zeros((nbins_lon, nbins_lat))
    proj_min_angle = np.full((nbins_lon, nbins_lat), np.nan)

    projector.reset_spice()

    # Make list of records if needed
    if records is None:
        records = np.arange(integrated_data.shape[0] - 1).astype(int)

    fov_centers, fov_corners = projector.get_fov_vectors(
        line_bin, ul_corner_line, lr_corner_line
    )

    for record in tqdm(records, disable=disable_progress):
        for pixel in range(integrated_data.shape[1] - 1):
            if np.isnan(integrated_data[record, pixel]):
                continue

            # Get surface intercept point and incidence angle for pixel boresight
            inters_center, angle_center = projector.proj_point(
                fov_centers[pixel, :], et_times[record]
            )
            if np.any(np.isnan(inters_center)):
                continue

            # Get surface intercept for pixel corners
            inters_corners = np.array(
                [
                    projector.proj_point(fov_corners[pixel, iii, :], et_times[record])[
                        0
                    ]
                    for iii in range(fov_corners.shape[1])
                ]
            )
            if np.any(np.isnan(inters_corners)):
                continue

            # Create projected pixel polygon in polar view and check whether it intersects the pole
            inters_lon = inters_corners[:, 0] * np.pi / 180
            inters_lat = 90 - np.abs(inters_corners[:, 1])
            is_polar = False
            if np.any(inters_lat < 1):
                polar_corners = [
                    [
                        inters_lat[iii] * np.cos(inters_lon[iii]),
                        inters_lat[iii] * np.sin(inters_lon[iii]),
                    ]
                    for iii in range(len(inters_lon))
                ]
                pixel_polar_view = Polygon(np.array(polar_corners))
                is_polar = pixel_polar_view.contains(Point(0, 0))

            # Check for non-polar bins crossing the 360-0 longitude boundary
            # Rotate them by lon=180deg, perform calculations and rotate back
            is_boundary_pixel = (
                np.max(inters_corners[:, 0]) - np.min(inters_corners[:, 0]) > 270
            ) & ~is_polar
            if is_boundary_pixel:
                inters_corners[:, 0] = (inters_corners[:, 0] + 180) % 360

            # Create projected pixel polygon in lon-lat view from corners
            pixel_lon_lat_view = Polygon(inters_corners)
            # Find bins which might intersect
            if is_polar:
                lon_min = 0
                lon_max = 360
                if inters_center[1] > 0:
                    lat_min = np.min(inters_corners[:, 1])
                    lat_max = 90
                else:
                    lat_min = -90
                    lat_max = np.max(inters_corners[:, 1])
            else:
                lon_min, lat_min, lon_max, lat_max = pixel_lon_lat_view.bounds

            arg_lon_bins = np.where(
                (projector.lon_bins[1:] >= lon_min)
                & (projector.lon_bins[:-1] <= lon_max)
            )[0]
            arg_lat_bins = np.where(
                (projector.lat_bins[1:] >= lat_min)
                & (projector.lat_bins[:-1] <= lat_max)
            )[0]

            # Iterate through all lon-lat bin candidates, check exact shapes
            for arg_lon, arg_lat in product(arg_lon_bins, arg_lat_bins):
                # Continue if bin is part of a combined bin and not the master
                if (
                    np.isfinite(projector.bin_map[arg_lon, arg_lat])
                    and not projector.is_master_bin[arg_lon, arg_lat]
                ):
                    continue
                # Get bin corners
                min_lon, max_lon = projector.lon_bins[arg_lon : arg_lon + 2]
                min_lat, max_lat = projector.lat_bins[arg_lat : arg_lat + 2]
                # For pole pixels, perform intersection checking in flat polar view
                if is_polar:
                    bin_corners = np.array(
                        [
                            [min_lon, min_lat],
                            [min_lon, max_lat],
                            [max_lon, max_lat],
                            [max_lon, min_lat],
                        ]
                    )
                    tmp_theta = bin_corners[:, 0] * np.pi / 180
                    tmp_r = 90 - np.abs(bin_corners[:, 1])
                    bin_polar_view = Polygon(
                        np.array(
                            [
                                [
                                    tmp_r[iii] * np.cos(tmp_theta[iii]),
                                    tmp_r[iii] * np.sin(tmp_theta[iii]),
                                ]
                                for iii in range(len(tmp_r))
                            ]
                        )
                    )
                    valid = bin_polar_view.intersects(pixel_polar_view)
                # For other pixels, check intersection in lon-lat view
                else:
                    bin_lon_lat_view = box(
                        min_lon,
                        min_lat,
                        max_lon,
                        max_lat,
                    )
                    valid = bin_lon_lat_view.intersects(pixel_lon_lat_view)
                if not valid:
                    continue

                # Add pixel to projection
                if is_boundary_pixel:
                    arg_lon = int(
                        (arg_lon + (len(projector.lon_bins) - 1) / 2)
                        % (len(projector.lon_bins) - 1)
                    )
                if projector.is_master_bin[arg_lon, arg_lat]:
                    fill_lons = np.where(
                        projector.bin_map[:, arg_lat]
                        == projector.bin_map[arg_lon, arg_lat]
                    )[0]
                else:
                    fill_lons = arg_lon
                proj_sum[fill_lons, arg_lat] += integrated_data[record, pixel]
                proj_num[fill_lons, arg_lat] += 1
                if (
                    np.isnan(proj_min_angle[fill_lons, arg_lat]).any()
                    or (angle_center < proj_min_angle[fill_lons, arg_lat]).any()
                ):
                    proj_min_angle[fill_lons, arg_lat] = angle_center

    if not disable_progress:
        tstop = time.time()
        logger.info(
            "Projection successful, took {:0.1f} seconds".format(tstop - tstart)
        )

    projector.remove_metakernels()

    return proj_sum, proj_num, proj_min_angle
