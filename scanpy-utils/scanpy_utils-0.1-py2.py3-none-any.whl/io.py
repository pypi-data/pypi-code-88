import gzip
import os

import pandas as pd
import scipy.io


def write_mtx(adata, output_dir):
    """\
    Save scanpy object in mtx cellranger v3 format.

    Saves basic information from adata object as cellranger v3 mtx folder.
    Saves only ``adata.var_names``, ``adata.obs_names``
    and ``adata.X`` fields.
    Creates directory ``output_dir`` if it does not exist.
    Creates 3 files: ``features.tsv.gz``, ``barcodes.tsv.gz`` and ``matrix.mtz.gz``.
    Will overwrite files in the output directory.

    Parameters
    ----------
    adata
        Annotated data matrix.
    output_dir
        Directory where to save results
    """
    pd.DataFrame({
        0: adata.var_names,
        1: adata.var_names,
        2: "Gene Expression"
    }).to_csv(
        os.path.join(output_dir, "features.tsv.gz"),
        sep="\t",
        index=False,
        header=False
    )
    pd.DataFrame(adata.obs_names).to_csv(
        os.path.join(output_dir, "barcodes.tsv.gz"),
        sep="\t",
        index=False,
        header=False
    )
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with gzip.open(os.path.join(output_dir, "matrix.mtx.gz"), "wb") as f:
        scipy.io.mmwrite(f, adata.X.T)
