import numpy as np
import pandas as pd





def discretize_gene_expression(gene_expression, local_thresholds,
                               lb_global=0, ub_global=999999,
                               index_col='gene_id',
                               gene_list=None,
                               as_frame=True):

    confidences = [-1, 1, 2, 3]
    if gene_list is None:
        gene_list = list(gene_expression.keys())

    confidences_dict = {}
    for gene in gene_list:
        if gene not in local_thresholds.index:
            confidences_dict[gene] = 0
            continue

        gene_expression = gene_expression[gene]
        local_threshold = local_thresholds[gene]
        thresholds = sorted([local_threshold, lb_global, ub_global, np.inf])
        for th, conf in zip(thresholds, confidences):
            if gene_expression <= th:
                confidences_dict[gene] = conf
                break

    if as_frame:
        df_confidences = pd.DataFrame(data=list(confidences_dict.items()),
                                      columns=[index_col,  'confidence'])

        df_confidences = df_confidences.set_index(index_col)

        return df_confidences

    return confidences_dict


