import datetime as dt
from typing import Any, Dict, List, Optional, Tuple

import importlib_resources
import numpy as np
import spiceypy as spice
from scipy.interpolate import interp1d
from scipy.io import readsav


class CalibrationException(Exception):
    def __init__(self, msg: Optional[str] = None):
        super(CalibrationException, self).__init__(msg)


class UVISCalibrator(object):
    """
    Class for handling UVIS data calibration.
    """

    def __init__(self, channel: str = "FUV"):
        """
        Constructor method.

        :param channel: UVIS data channel (`FUV` is the default and only accepted value, `EUV` not implemented).
        """
        self.uvis_channel = channel
        self.calib_dir = importlib_resources.files("uvisaurorae.resources").joinpath(
            "calibration_files"
        )  # type: ignore

        self.wcal, self.ucal, self.ucalerr = self.get_lab_sensitivity()
        self.wavelength = self.get_wavelength()

        self.spica_times_et, self.spica_data = self.prep_cal_modifiers()

        self.spica_ff_data_preburn = self.read_spica_ff_file(
            self.calib_dir / "FLATFIELD_FUV_PREBURN.txt"
        )
        self.spica_ff_data_postburn = self.read_spica_ff_file(
            self.calib_dir / "FLATFIELD_FUV_POSTBURN.txt"
        )

    def get_lab_sensitivity(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Load laboratory-measured instrument sensitivities.

        :return: Arrays containing wavelengths, sensitivities and sensitivity measurement errors.
        """
        if self.uvis_channel != "FUV":
            raise CalibrationException(
                f"Calibrations for channel {self.uvis_channel} not available."
            )
        lsdata = np.genfromtxt(self.calib_dir / "FUV_1999_Lab_Cal.dat", skip_header=1)
        wcal = np.append(lsdata[:, 0], lsdata[:, 3])
        ucal = np.append(lsdata[:, 1], lsdata[:, 4])
        ucalerr = np.append(lsdata[:, 2], lsdata[:, 5])
        return wcal, ucal, ucalerr

    def get_wavelength(self, bbin: int = 1) -> np.ndarray:
        """
        Determine wavelengths for a given wavelength binning.

        :param bbin: Wavelength binning.
        :return: Array containing each bin's central wavelength.
        """
        if self.uvis_channel != "FUV":
            raise CalibrationException(
                f"Wavelength scales for channel {self.uvis_channel} not available."
            )
        d = 1e7 / 1066
        alpha = np.radians(9.22 + 0.032) + 3.46465e-5
        beta = (np.arange(1024) - 511.5) * 0.025 * 0.99815 / 300
        beta = np.arctan(beta) + np.radians(0.032) + 3.46465e-5
        lam = d * (np.sin(alpha) + np.sin(beta))
        if bbin == 1:
            return np.array(lam)
        e_wavelength = np.full((int(1024 / bbin)), np.nan)
        for iii in range(len(e_wavelength)):
            e_wavelength[iii] = np.mean(lam[iii * bbin : (iii + 1) * bbin])
        return e_wavelength

    def prep_cal_modifiers(self) -> Tuple[np.ndarray, Dict[str, Any]]:
        """
        Prepare calibration modifiers. These encode the temporal degradation of the sensor which was determined by
        measuring the intensity of the star Spica every now and then.

        :return: Array of timestamps at which modifiers were determined, dict containing the modifiers themselves.
        """
        # Load file
        spica_file = self.calib_dir / "spica_variability4_data.sav"
        spica_data = readsav(spica_file)
        nitems = len(spica_data["arr"])
        # Get time parameters
        year = [spica_data["arr"].desc[iii].year_start.item() for iii in range(nitems)]
        doy = [spica_data["arr"].desc[iii].doy_start.item() for iii in range(nitems)]
        hour = [spica_data["arr"].desc[iii].hour_start.item() for iii in range(nitems)]
        minute = [spica_data["arr"].desc[iii].min_start.item() for iii in range(nitems)]
        second = [spica_data["arr"].desc[iii].sec_start.item() for iii in range(nitems)]
        # Convert to datetime
        spica_times = np.array(
            [
                dt.datetime(
                    year=year[iii],
                    month=1,
                    day=1,
                    hour=hour[iii],
                    minute=minute[iii],
                    second=int(np.floor(second[iii])),
                )
                + dt.timedelta(days=int(doy[iii] - 1))
                for iii in range(nitems)
            ]
        )
        return spice.datetime2et(spica_times), spica_data

    def get_uvis_cal_modifier(self, et_time: float) -> np.ndarray:
        """
        Get Spica-calibrated sensitivity modifiers for a certain timestamp.

        :param et_time: Ephemeris time for which a modifier is to be retrieved.
        :return: Modifier array.
        """
        # If observation was before the first file, return array of 1s
        if et_time < self.spica_times_et[0]:
            return np.ones(1024)
        # If observation was after the last file, return last array
        elif et_time > self.spica_times_et[-1]:
            return np.array(self.spica_data["arr"].ratio[-1])
        # If observation was in between two files, do linear interpolation
        arg1 = np.where(self.spica_times_et <= et_time)[0][-1]
        arg2 = np.where(self.spica_times_et >= et_time)[0][0]
        specmod1 = self.spica_data["arr"].ratio[arg1]
        specmod2 = self.spica_data["arr"].ratio[arg2]
        m = (specmod2 - specmod1) / (
            self.spica_times_et[arg2] - self.spica_times_et[arg1]
        )
        return np.array(specmod1 + m * (et_time - self.spica_times_et[arg1]))

    @staticmethod
    def read_spica_ff_file(file: str) -> np.ndarray:
        """
        Read a flat field modifier file.

        :param file: Filename.
        :return: Flat field modifier array.
        """
        ff = np.zeros((64, 1024))
        skip_header_zero = 3
        for iii in range(64):
            thisskip = skip_header_zero + iii * 173
            tmp1 = np.genfromtxt(file, skip_header=thisskip, max_rows=170)
            tmp2 = np.genfromtxt(file, skip_header=thisskip + 170, max_rows=1)
            tmp = np.append(np.ravel(tmp1), tmp2)
            ff[iii, :] = tmp
        return ff

    def get_uvis_ff_modifier(self, et_time: float) -> np.ndarray:
        """
        Determine flat field modifiers for a certain timestamp.

        :param et_time: Ephemeris time for which flat field modifiers are to be loaded.
        :return: Flat field modifier array.
        """
        # Get times of flat field modifier files
        ff_path = self.calib_dir / "UVIS_flat-field_modifiers_2016-01-13"
        ff_files = sorted(ff_path.glob(f"{self.uvis_channel}*.dat"))
        ff_times_str = [
            str(ff_files[iii]).split("_UVIS")[0].split(self.uvis_channel)[-1]
            for iii in range(len(ff_files))
        ]
        ff_times = np.array(
            [
                spice.datetime2et(
                    dt.datetime.strptime(ff_times_str[iii], "%Y_%j_%H_%M_%S")
                )
                for iii in range(len(ff_times_str))
            ]
        )
        # If observation was before the first flat field modifier file, return array of 1s
        if et_time < ff_times[0]:
            return np.ones((64, 1024))
        # If observation was after the last flat field modifier file, return last array
        elif et_time > ff_times[-1]:
            ff_array = np.squeeze(
                np.fromfile(ff_files[-1], dtype="<(64,1024)f4", count=-1)
            )
            ff_array[61, :] = 1  # Why?
            return np.array(ff_array)
        # If observation was in between two ff modifier files, do linear interpolation
        arg1 = np.where(ff_times < et_time)[0][-1]
        arg2 = np.where(ff_times > et_time)[0][0]
        ffarray1 = np.squeeze(
            np.fromfile(ff_files[arg1], dtype="<(64,1024)f4", count=-1)
        )
        ffarray2 = np.squeeze(
            np.fromfile(ff_files[arg2], dtype="<(64,1024)f4", count=-1)
        )
        m = (ffarray2 - ffarray1) / (ff_times[arg2] - ff_times[arg1])
        ffarray = ffarray1 + m * (et_time - ff_times[arg1])
        ffarray[61, :] = 1  # Why?
        return np.array(ffarray)

    # Interpolate each spectrum. Input in shape [line,band].
    @staticmethod
    def interpolate_nans(wave: np.ndarray, arr_in: np.ndarray) -> np.ndarray:
        """
        Interpolate missing values in a spectral UVIS calibration array.

        :param wave: Wavelengths of each spectral bin.
        :param arr_in: Original array.
        :return: Interpolated array.
        """
        arr_out = np.zeros(np.shape(arr_in))
        for iii in range(np.shape(arr_in)[0]):
            spec = np.copy(arr_in[iii, :])
            if not np.any(np.isnan(spec)):
                arr_out[iii, :] = spec
            elif len(spec) - np.sum(np.isnan(spec)) <= 1:
                print("Warning: only nan values, spectrum could not be interpolated.")
                arr_out[iii, :] = spec
            else:
                ndxfin = np.where(np.isfinite(spec))
                ndxnan = np.where(np.isnan(spec))
                f = interp1d(wave[ndxfin], spec[ndxfin], fill_value="extrapolate")
                spec[ndxnan] = f(wave[ndxnan])
                arr_out[iii, :] = spec
        return arr_out

    # window_def = [UL_BAND, UL_LINE, LR_BAND, LR_LINE]
    # bin_def = [BAND_BIN, LINE_BIN]
    def get_interpolated_calibration(
        self, et_time: float, slit_width: int, window_def: List[int], bin_def: List[int]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get interpolated calibration array which is to be multiplied with a raw UVIS data cube to obtain a calibrated
        image.

        :param et_time: Ephemeris time of the observation for which a calibration array is needed.
        :param slit_width: Slit width of the observation.
        :param window_def: Window definition, containing spectral and spatial (pixel) ranges. Format is
            `[UL_BAND, UL_LINE, LR_BAND, LR_LINE]`.
        :param bin_def: Spectral and spatial binnings, of format `[BAND_BIN, LINE_BIN]`.
        :return: Full spectral calibration array.
        """
        # Check slit width validity
        if slit_width < 1 or slit_width > 2:
            raise CalibrationException("Invalid slit width.")

        # Apply slit width correction
        ucal = self.ucal / slit_width
        ucalerr = self.ucalerr / slit_width

        # Interpolate the discrete-wavelength sensitivity to the full spectral range of the detector
        tmp = interp1d(self.wcal, ucal, fill_value="extrapolate")
        ucal = tmp(self.wavelength) / 60
        tmp = interp1d(self.wcal, ucalerr, fill_value="extrapolate")
        ucalerr = tmp(self.wavelength) / 60

        # Define the average pixel bandpass in [A] (dispersion x pixel width)
        pixel_bandpass = 0.78

        # Apply factor for continuous input spectrum (sensitivity units now counts/s/kR/A)
        ucal *= pixel_bandpass
        ucalerr *= pixel_bandpass

        # Apply a time-dependent adjustment to the lab-measured sensitivity based on repeated observations of Spica
        specmod = self.get_uvis_cal_modifier(et_time)
        ucal *= specmod
        ucalerr *= specmod  # not in the original code but should be?

        # Construct a 2D array and fill with the 1D sensitivity
        u_cal = np.zeros((64, 1024))
        u_cal_err = np.zeros_like(u_cal)
        for kkk in range(2, 62):
            u_cal[kkk, :] = ucal
            u_cal_err[kkk, :] = ucalerr

        # Apply flat field correction, adjust sensitivity to account for elimination of evil pixels in
        # original calibration
        ucal /= 0.91
        ucalerr /= 0.91
        if et_time >= spice.datetime2et(dt.datetime(year=2002, month=6, day=6)):
            ff = self.spica_ff_data_postburn.copy()
        else:
            ff = self.spica_ff_data_preburn.copy()
        ndxnan = np.where(np.isnan(ff))
        # Adjust flat field normalization to account for asymmetry in histogram distribution
        ff *= 1.05
        # Row 2 and row 61 in the FUV flat-field correction appear erroneous, eliminate by setting to 1
        ff[2, :] = 1
        ff[61, :] = 1
        # Apply the flat field corrector (the flat field must be multiplied with the data, or equivalently
        # divided by the sensitivity where calibration=1/sensitivity)
        u_cal /= ff
        u_cal_err /= ff
        # Apply the flat field modifier
        arrmod = self.get_uvis_ff_modifier(et_time)
        arrmod[ndxnan] = 1
        u_cal *= arrmod
        u_cal_err *= arrmod

        # Interpolate the correction before collapsing
        u_cal = self.interpolate_nans(self.wavelength, u_cal)
        u_cal_err = self.interpolate_nans(self.wavelength, u_cal_err)

        # Get sizing and binning
        ul_band, ul_line, lr_band, lr_line = [int(i) for i in window_def]
        band_bin, line_bin = [int(i) for i in bin_def]
        # Size of unbinned window
        band_size = lr_band - ul_band + 1
        line_size = lr_line - ul_line + 1
        # Pad to integral multiples of the binning parameters
        band_size_pad = int(band_bin * np.ceil(band_size / band_bin))
        line_size_pad = int(line_bin * np.ceil(line_size / line_bin))
        # Size of final returned array (partial bins at the end included)
        band_size_final = int(np.ceil(band_size / band_bin))
        line_size_final = int(np.ceil(line_size / line_bin))

        # Make binned and padded versions of wavelength vector, sensitivity and sensitivity uncertainty
        wave_temp = np.zeros(band_size_pad)
        u_cal_temp = np.zeros((line_size_pad, band_size_pad))
        u_cal_err_temp = np.zeros((line_size_pad, band_size_pad))
        wave_temp[:band_size] = self.wavelength[ul_band : (lr_band + 1)]
        u_cal_temp[:line_size, :band_size] = u_cal[
            ul_line : (lr_line + 1), ul_band : (lr_band + 1)
        ]
        u_cal_err_temp[:line_size, :band_size] = u_cal_err[
            ul_line : (lr_line + 1), ul_band : (lr_band + 1)
        ]

        # Make final versions
        u_wavelength = np.zeros(band_size_final)
        cal_temp = np.zeros((line_size_final, band_size_final))
        err_temp = np.zeros((line_size_final, band_size_final))
        # Average wavelength values within each bin
        for bbb in range(band_size_final):
            u_wavelength[bbb] = np.nanmean(
                wave_temp[bbb * band_bin : (bbb + 1) * band_bin]
            )

        for lll in range(line_size_final):
            for bbb in range(band_size_final):
                # Sum the sensitivity
                cal_temp[lll, bbb] = np.sum(
                    u_cal_temp[
                        lll * line_bin : (lll + 1) * line_bin,
                        bbb * band_bin : (bbb + 1) * band_bin,
                    ]
                )
                # Sum the sensitivity uncertainty in quadrature
                err_temp[lll, bbb] = np.sum(
                    u_cal_err_temp[
                        lll * line_bin : (lll + 1) * line_bin,
                        bbb * band_bin : (bbb + 1) * band_bin,
                    ]
                )
                err_temp[lll, bbb] /= np.sqrt(band_bin * line_bin)

        cal_temp[np.where(cal_temp == 0)] = 1e10
        err_temp[np.where(err_temp == 0)] = 1e10

        # Invert the sensitivity to obtain the calibration factor
        # units will be in (kR/A) / (counts/sec)
        u_calibration = 1 / cal_temp
        u_calibration_error = err_temp / cal_temp ** 2
        u_calibration[np.where(u_calibration < 1e-9)] = 0
        u_calibration_error[np.where(u_calibration_error < 1e-9)] = 0

        return u_wavelength, u_calibration, u_calibration_error
