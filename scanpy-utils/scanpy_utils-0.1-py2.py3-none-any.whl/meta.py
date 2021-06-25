import anndata as ad
import pandas as pd


def _select_first(df: pd.DataFrame, col_pattern: str) -> pd.Series:
    """\
    Selects first non-empty value from columns matching ``col_pattern``

    Parameters
    ----------
    df
        Pandas data frame
    col_pattern
        Pattern to match columns

    Returns
    -------
    Pandas series with first non-empty value among the matching columns
    selected for each index of the dataframe
    """
    x = df.loc[:, df.columns[df.columns.str.match(col_pattern)]]
    cols = x.T.notna().idxmax()
    x = x.reset_index().melt("index")
    x = x.set_index(
        ["index", "variable"]
    ).loc[zip(cols.index, cols.values), :].droplevel("variable")
    return x


def merge_gene_info(adata: ad.AnnData):
    """\
    Merges gene information from different batches

    After concatenating several datasets, the gene information dataframe
    ``adata.var`` can have a lot of duplicate columns from all the batches.

    This function merges ``gene_ids``, ``feature_types`` and ``genome``
    information from batches, inserts them in the table and removes the
    batch-associated columns.

    Parameters
    ----------
    adata
        Annotated data matrix.

    Example
    -------
    >>> datasets = [sc.read_h5ad(path) for path in paths]
    >>> adata = datasets[0].concatenate(datasets[1:], join="outer")
    >>> sc_utils.merge_gene_info(adata)
    """
    for i, column in enumerate(["gene_ids", "feature_types", "genome"]):
        adata.var.insert(
            i,
            column,
            _select_first(adata.var, rf"{column}-\d+")
        )
        adata.var.drop(
            adata.var.columns[adata.var.columns.str.match(r"{column}-\d+")],
            inplace=True,
            axis=1
        )
