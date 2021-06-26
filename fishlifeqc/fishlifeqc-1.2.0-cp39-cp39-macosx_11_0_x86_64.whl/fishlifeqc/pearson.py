import copy
import re
import dendropy



tns = dendropy.TaxonNamespace()


spps_tree = dendropy.Tree.get(
    path = "./test_tree/prota.1132.MSCtree",
    schema = 'newick'
)

spps_tree_tips = [i.label for i in spps_tree.taxon_set ]
len(spps_tree_tips)

gene_tree = dendropy.Tree.get(
    path = "./test_tree/E0158.listd_allsets.NT_aligned.fasta_trimmed_rblastd.nex.treefile",
    schema = 'newick',
    taxon_namespace = tns
)

gene_tree_tips = [i.label for i in gene_tree.taxon_set]
len(gene_tree_tips)

new_str_tree = (spps_tree
                    .extract_tree_with_taxa_labels(labels = gene_tree_tips)
                    .as_string(schema = 'newick'))



new_str_tree.strip()



newtree = dendropy.Tree.get_from_string(new_str_tree, 'newick', taxon_namespace = tns)
# edge_lengths = [nd.edge.length for nd in newtree]


gene_tree.encode_bipartitions()
newtree.encode_bipartitions()

from dendropy.calculate import treecompare

treecompare.symmetric_difference(gene_tree, newtree)

# from dendropy.simulate import treesim
# import pprint

# tree = treesim.birth_death_tree(birth_rate=1.0, death_rate=0.5, ntax=10)
# pdm = tree.phylogenetic_distance_matrix()

# pp = pprint.PrettyPrinter(depth=2)
# pp.pprint(pdm.as_data_table()._data)


newtree_tips = [i.label for i in newtree.taxon_set]
len(newtree_tips)


for i in range(len(newtree.taxon_set)):
    if newtree_tips[i] == gene_tree_tips[i]:
        print(newtree_tips[i], 'coincides')
    else:
        print('keep dreaming')


from Bio import Phylo

spps_tree = Phylo.read("./test_tree/prota.1132.MSCtree", 'newick')
gene_tree = Phylo.read("./test_tree/E0151.listd_allsets.NT_aligned.fasta_trimmed_rblastd.nex.treefile", 'newick')
# tree.ladderize()
# Phylo.draw(tree)

gene_tree.prune(target=spps_tree)
spps_tree.total_branch_length()

import numpy

def to_adjacency_matrix(tree):
    """Create an adjacency matrix (NumPy array) from clades/branches in tree.

    Also returns a list of all clades in tree ("allclades"), where the position
    of each clade in the list corresponds to a row and column of the numpy
    array: a cell (i,j) in the array is 1 if there is a branch from allclades[i]
    to allclades[j], otherwise 0.

    Returns a tuple of (allclades, adjacency_matrix) where allclades is a list
    of clades and adjacency_matrix is a NumPy 2D array.
    """
    allclades = list(tree.find_clades(order="level"))
    lookup = {}
    for i, elem in enumerate(allclades):
        lookup[elem] = i
    adjmat = numpy.zeros((len(allclades), len(allclades)))
    for parent in tree.find_clades(terminal=False, order="level"):
        for child in parent.clades:
            adjmat[lookup[parent], lookup[child]] = 1
    if not tree.rooted:
        # Branches can go from "child" to "parent" in unrooted trees
        adjmat = adjmat + adjmat.transpose()
    return (allclades, numpy.matrix(adjmat))

to_adjacency_matrix(gene_tree)