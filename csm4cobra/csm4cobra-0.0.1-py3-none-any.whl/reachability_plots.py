import seaborn as sns

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from matplotlib.colors import ListedColormap
from matplotlib.gridspec import GridSpec

###################################################################################
# Function to plot the reachability matrix with omic data together with boxplots 
# for the distribution of the omic measurment associated to each gene
###################################################################################


def heatmap_boxplots(df_reach_sq, df_omics, omic_column, figsize=None,
                     ascending=False, highlight_uniqs=False, units="x",
                     zero_center=False, row_labels=None):



    ##############################################################
    # Creating figure and grid spec
    ##############################################################
    m, n = df_reach_sq.shape
    ratio = n / m
    if figsize is None:
        n *= 0.65 * (1 / ratio)
        m *= 0.45
        figsize = (m, n)

    fig = plt.figure(figsize=figsize, dpi=300)
    gs = GridSpec(2, 2, width_ratios=[3.5, 1], height_ratios=[3.5 * ratio, 1], figure=fig)

    ##############################################################

    # Dataframes used for creating the heatmap
    if row_labels is None:
        genes = df_reach_sq.columns
        genes = df_omics[genes].median().sort_values(ascending=ascending).index
    else:
        genes = row_labels

    df_reach_sq = df_reach_sq[genes]
    df_reach_sq_omic = (df_reach_sq * df_omics[genes].median()).T
    df_reach_sq = df_reach_sq.T
    
    # Dataframes used for creating the genes' boxplot
    df_genes_omic = df_omics[genes].T
    df_genes_omic['gene_id'] = df_genes_omic.index
    df_genes_omic = df_genes_omic.melt(id_vars=['gene_id'], value_name=omic_column, var_name='tissue')
    
    genes_medians = df_genes_omic.groupby('gene_id').median()
    genes_medians = genes_medians.sort_values(omic_column, ascending=ascending)
    genes_medians = genes_medians[omic_column]

    # Dataframes used to creating the products' boxplot
    df_prod_omic = df_reach_sq_omic.T.copy()
    df_prod_omic.index.name = 'product_id'
    df_prod_omic['product_id'] = df_prod_omic.index
    df_prod_omic = df_prod_omic.melt(id_vars=['product_id'], var_name='gene_id', 
                                     value_name=omic_column, value_vars=genes)
    
    df_prod_omic = df_prod_omic[~(df_prod_omic[omic_column] == 0)]
    products_medians = df_prod_omic[['product_id', omic_column]].groupby('product_id').aggregate('median')
    products = products_medians.sort_values(by=omic_column, ascending=ascending).index
    
    # Sort the rechability matrix using genes and producs order by median
    df_reach_sq_omic = df_reach_sq_omic.loc[genes, products]
    df_reach_sq = df_reach_sq.loc[genes, products]
    
    genes_counts = df_prod_omic.groupby('gene_id').count()
    genes_counts = genes_counts.product_id
    

    ##############################################################
    # Adding heatmap
    ##############################################################

    if genes_medians.min() < 0 < genes_medians.max() or zero_center:
        cmap = sns.diverging_palette(10, 220, as_cmap=True)
        center_zero = True
    else:
        pallette = sns.color_palette("Blues", n_colors=18)
        cmap = ListedColormap(pallette.as_hex())
        center_zero = False

    ax = plt.subplot(gs[0])

    if center_zero:
        sns.heatmap(df_reach_sq_omic, cmap=cmap, linewidths=0.05, ax=ax, center=0, cbar=False, linecolor='grey')
    else:
        sns.heatmap(df_reach_sq_omic, cmap=cmap, linewidths=0.05, ax=ax, cbar=False, linecolor='grey')

    ax.spines['right'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis='both', which='major', labelsize=11, bottom=True, right=True, 
                   labelright=True, left=False, labelleft=False, rotation=0)

    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="center", size=11)
    ax.zorder = 10
    ax.patch.set_linewidth(1)
    for i, xtl in enumerate(ax.get_xticklabels()):
        product_id = xtl.get_text()
        for j, ytl in enumerate(ax.get_yticklabels()):
            gene_id = ytl.get_text()
            lw = 1.
            if df_reach_sq.loc[gene_id, product_id] == 0:
                continue
            if genes_counts[gene_id] == 1 and highlight_uniqs:
                lw = 2.
            r = Rectangle((i, j), 1, 1, fill=False, edgecolor='#434343', lw=lw, zorder=1000)
            ax.add_patch(r)
    
    ##############################################################
    # Adding GENES' boxplots
    ##############################################################
    if center_zero:
        genes_medians = (genes_medians + genes_medians.abs().max() ) / (2 * genes_medians.abs().max())
    else:
        genes_medians = (genes_medians / genes_medians.max())
    colors = [cmap(genes_medians[i]) for i in genes]
    
    ax = plt.subplot(gs[1])
    sns.boxplot(data=df_genes_omic, y='gene_id', x=omic_column, 
                showfliers=False, order=genes, palette=colors, ax=ax)
    
    ax.set_ylabel("")
    ax.set_yticklabels([])
    ax.set_xlabel(units, size=11)
    ax.grid()
    
    ################################
    # Adding PRODUCTS' boxplots
    ################################
    if center_zero:
        products_medians = (products_medians + products_medians.abs().max() ) 
        products_medians /= (2 * products_medians.abs().max())
    else:
        products_medians =  (products_medians / products_medians.max())
    colors = [cmap(products_medians.loc[i, omic_column]) for i in products]
    
    ax = plt.subplot(gs[2])
    sns.boxplot(data=df_prod_omic, x='product_id', y=omic_column, order=products, showfliers=False, palette=colors, ax=ax)
    ax.set_xlabel("")
    ax.set_xticklabels([])
    ax.xaxis.tick_top()
    ax.set_ylabel(units, size=11)
    ax.grid()

    fig.tight_layout()

    return fig


###################################################################################
# Function to plot the reachability matrix with omic data together with boxplots 
# for the distribution of the omic measurment associated to each gene
###################################################################################

def plot_clustermap(df_data, method='ward', vrange=(), linewidths=.01, figsize=(12, 18), cmap=None):

    if cmap is None:
        palette = sns.color_palette("Blues", n_colors=18)
        cmap = ListedColormap(palette.as_hex())

    if len(vrange) == 2:
        g = sns.clustermap(df_data, method=method, cmap=cmap, linewidths=linewidths, 
                           vmin=vrange[0], vmax=vrange[1], figsize=figsize)
    else:
        g = sns.clustermap(df_data, method=method, cmap=cmap, linewidths=linewidths, 
                           figsize=figsize)
    
    ax = g.ax_heatmap
    ax.set_xlabel("")
    ax.set_ylabel("")
    
    ax.tick_params(axis='both', which='major', labelsize=12, bottom=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax = g.ax_heatmap
    ax.patch.set_linewidth(0)
    ax.zorder = 10

    for i, xtl in enumerate(g.ax_heatmap.get_xticklabels()):
        compound_id = xtl.get_text()
        for j, ytl in enumerate(g.ax_heatmap.get_yticklabels()):
            gene_id = ytl.get_text()
            
            value = df_data.loc[gene_id, compound_id]
            
            if value == 0:
                continue
            r = Rectangle((i, j), 1, 1, fill=False, edgecolor='#434343', lw=1.5, zorder=10)
            r.zorder = 1000
            ax.add_patch(r)

    _ = ax.set_xticklabels(ax.get_xticklabels(), rotation=75, ha="right")

    fig = g.fig

    fig.subplots_adjust(top=0.98)
    fig.subplots_adjust(hspace=0.05)
    fig.subplots_adjust(left=0.02)
    fig.subplots_adjust(right=0.92)
    fig.subplots_adjust(bottom=0.16)

    return fig


def plot_boxplots(df_data, add_gene_counts=True, width=0.75):
    
    grpby = df_data[['precursor_id', 'dependency', 'ceres', 'tpm']].groupby('precursor_id')
    df_medians = grpby.aggregate('median')
    labels = df_medians.sort_values(by='ceres').index.tolist()
    
    fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 9), dpi=300)
    
    cmap = sns.diverging_palette(10, 220, as_cmap=True)
    ceres_medians = df_medians.ceres
    ceres_medians =  (ceres_medians + ceres_medians.abs().max() ) / (2 * ceres_medians.abs().max())
    colors = [cmap(ceres_medians[i]) for i in labels]
    g = sns.boxplot(x="precursor_id", y='ceres', order=labels, data=df_data, ax=axs[0], 
                    width=0.6, showfliers=False, palette=colors)
    
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    dep_medians = df_medians.dependency
    dep_medians =  (dep_medians + dep_medians.abs().max() ) / (2 * dep_medians.abs().max())
    colors = [cmap(dep_medians[i]) for i in labels]
    g = sns.boxplot(x="precursor_id", y='dependency', order=labels, data=df_data, ax=axs[1], 
                    width=0.6, showfliers=False, palette=colors)
    
    cmap = ListedColormap(sns.color_palette("Blues", n_colors=10).as_hex())
    tpm_medians =  df_medians.tpm / df_medians.tpm.max()
    colors = [cmap(tpm_medians[i]) for i in labels]
    g = sns.boxplot(x="precursor_id", y='tpm', order=labels, data=df_data, ax=axs[2],
                    width=width, showfliers=False, palette=colors)

    axs[0].tick_params(axis='both', which='major', labelsize=9, bottom=False)
    axs[0].set_xlabel("")
    axs[0].set_ylabel("CERES", fontsize=9)
    axs[0].yaxis.grid(True)
    axs[0].annotate("(A)", xy=(0.01, 0.93), xycoords="axes fraction", fontsize=11)

    axs[1].tick_params(axis='both', which='major', labelsize=9, bottom=False)
    axs[1].set_xlabel("")
    axs[1].set_ylabel("Dependency", fontsize=9)
    axs[1].yaxis.grid(True)
    axs[1].set_ylim(0, 1.15)
    axs[1].annotate("(B)", xy=(0.01, 0.93), xycoords="axes fraction", fontsize=11)
    
    axs[2].set_xlabel("")
    axs[2].tick_params(axis='both', which='major', labelsize=9, bottom=True)
    axs[2].set_ylabel("TPM(log2)", fontsize=9)
    axs[2].yaxis.grid(True)
    axs[2].annotate("(C)", xy=(0.01, 0.93), xycoords="axes fraction", fontsize=11)
    axs[2].set_xticklabels(axs[2].get_xticklabels(), position=(0,0.02), rotation=45, ha="right")
    
    if add_gene_counts:
        new_labels = []
        for l in labels:
            n = len(set(df_data.gene_id[df_data.precursor_id==l].values))
            strn = "%s (%i)" % (l,n)
            new_labels.append(strn)

        _ = axs[2].set_xticklabels(new_labels)

    fig.subplots_adjust(top=0.96)
    fig.subplots_adjust(hspace=0.05)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(bottom=0.22)
    
    sns.despine(fig, bottom=True)

    return fig
