import matplotlib.pyplot as plt
import seaborn as sns


def essential_vs_non_essential(df_deletions, df_gene_omic, ax=None):

    if ax is None:
       fig, ax = plt.subplots()

    thr = df_deletions.growth.max() * 0.01
    essential = set(df_deletions.index[df_deletions.growth < thr]) & set(df_gene_omic.index)
    non_essential = set(df_deletions.index[df_deletions.growth >= thr]) & set(df_gene_omic.index)

    ax.set_xlim([-1.57, 0.57])
    ax.set_xlabel("CERES Score x")
    if i == 0:
        ax.set_ylabel("P(x)")

    x = df_gene_omic.loc[essential]
    y = df_gene_omic.loc[non_essential]

    nx = str(len(x))
    ny = str(len(y))
    sns.distplot(y, ax=ax, kde=True, label='$In$-$silico$ NE (' + ny + ')')
    sns.distplot(x, ax=ax, kde=True, rug=True, label='$In$-$silico$ E (' + nx + ')')

    ax.legend(facecolor='w')

