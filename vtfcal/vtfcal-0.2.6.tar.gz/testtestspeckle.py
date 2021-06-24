import subprocess as subp

import numpy as np

from astropy.io import fits


def run_testSpeckle(
    width=2048,
    height=2048,
    tile_size=128,
    burst_directory="/home/dkistdev/data",
    burst_prefix="bbso",
    burst_suffix=".pnm",
    burst_size=80,
    fixed_width=0,
    gpus=0,
    master_gpu=0,
    L1=0.949999988,
    L2=0.0900000036,
    iterations=10,
    out_prefix="byproducts",
    fried_parameter=0.100000001,
    wavelength=656.281982,
    pixel_scale=0.0170000009,
    diameter=4,
    dark=None,
    gain=None,
    npsd=None,
    init_with_mean=False,
    floats=False,
):

    # Define bispectrum indices?
    # call spectral ratio library?
    # construct speckle class
    # read darks
    # read flats
    # read 'burst' image files
    # correct for darks and flats
    # sum images?
    # call reconstruction

    if not isinstance(gpus, int):
        gpus = {gpus}

    print(f"{gpus}")

    speckle_command = [
        "./testSpeckle",
        "-w",
        f"{width}",
        "-h",
        f"{height}",
        "-t", f"{tile_size}",
        "-d",
        f"{burst_directory}",
        "-p",
        f"{burst_prefix}",
        "-s",
        f"{burst_suffix}",
        "-n",
        f"{burst_size}",
        f"--fixed-width={fixed_width}",
        f"--gpus={gpus}",
        f"--master-gpu={master_gpu}",
        f"--L1={L1}",
        f"--L2={L2}",
        f"--iterations={iterations}",
        f"--fried-parameter={fried_parameter}",
        f"--wavelength={wavelength}",
        f"--pixel-scale={pixel_scale}",
        f"--diameter={diameter}",
    ]
    if dark:
        speckle_command.append(f"--dark={dark}")
    if gain:
        speckle_command.append(f"--gain={gain}")
    if npsd:
        speckle_command.append(f"--npsd={npsd}")
    if init_with_mean:
        speckle_command.append(f"--init-with-mean={init_with_mean}")
    if floats:
        speckle_command.append(f"--floats={floats}")

    subp.run(speckle_command)

    recon = np.fromfile("byproducts-reconstruction.raw", dtype="float32").reshape(
        (1024, 1024)
    )
    fits.writeto("speckle-output.FITS", recon, overwrite=True)


if __name__ == "__main__":
    run_testSpeckle(
        width=1024,
        height=1024,
        burst_directory="vtfTestImages",
        burst_prefix="cssSim_1024x1024",
        burst_suffix=".raw",
        burst_size=99,
        fixed_width=3,
        gpus=0,
    )
