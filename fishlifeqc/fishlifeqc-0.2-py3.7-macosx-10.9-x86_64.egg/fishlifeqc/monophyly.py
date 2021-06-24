#!/usr/bin/env python

import os
import re
import sys
import csv
import copy


import dendropy
import collections
from multiprocessing import Pool
# from fishlifeseq import headers

import pprint

from fishlifeqc.t_like import TreeExplore
from fishlifeqc.bl import BLCorrelations, RAXML
from fishlifeqc.utils import runshell



# import inspect
# import pprint
# def black_box(weird_obj):
#     pprint.pprint(
#         inspect.getmembers( weird_obj, lambda a:not(inspect.isroutine(a)) ),
#         indent= 4
#     )


class Consel:
    def __init__(self, 
                raxml_exe = RAXML,
                evomodel = 'GTRGAMMA',
                threads = 1):

        self.raxml_exe = raxml_exe
        self.threads   = threads
        self.evomodel  = evomodel

    def _site_likehood(self, seq_tree):

        seq,tree = seq_tree

        cmd = """
            {raxml}\
                -f g\
                -s {seq}\
                -m {model}\
                -z {constr}\
                -n {suffix}""".format(
                    raxml  = self.raxml_exe,
                    model  = self.evomodel,
                    seq    = seq,
                    constr = tree,
                    suffix = tree + "site_lnl").strip()

        runshell( 
            ( cmd.split(), tree + ".stdout" ),
            type = "stdout" 
        )

class Monophyly(
        TreeExplore, 
        BLCorrelations,
        Consel):

    def __init__(self,
                 metadata = None,
                 recycle_monos = True,
                 force_all = False,
                 tgroup = None,
                 raxml_exe = RAXML,
                 evomodel = 'GTRGAMMA',
                 iterations = 10,
                 **kwargs):
        super().__init__(**kwargs)

        # user selected group 
        # for testing paraphyly
        self.tgroup = tgroup

        # selected groups
        self.s_groups = []

        # use already proposed monophyletic groups
        # found at input trees
        self.recycle_monos = recycle_monos

        # force monophyly on all
        # paraphyletic group regardless
        # of self.tgroup
        self.full_force= force_all

        self.metadata   = metadata

        # raxml vars
        self.raxml_exe  = raxml_exe
        self.evomodel   = evomodel
        self.iterations = iterations

        # internal variables
        self.seq_tree = []
        

    def _get_taxa(self, obj, is_nd = True):
        tmp_iter = obj.leaf_iter() if is_nd else obj.leaf_node_iter()
        return [i.taxon.label for i in tmp_iter]

    def _iter_taxa_file(self, mytaxa):
        #TODO: change index to zero after development
        index = 3
        mygroups = {}

        for mt in mytaxa:

            if not self._t_like_taxa.__contains__(mt):
                continue

            tmp_group = self._t_like_taxa[mt][index]
            if not mygroups.__contains__(tmp_group):
                mygroups[tmp_group] = [mt]
            else:
                mygroups[tmp_group] += [mt]    
        
        return mygroups
        
    def _get_groups(self, c_tree):
        mytaxa = self._get_taxa(c_tree, is_nd=False)
        return self._iter_taxa_file(mytaxa)

    def _get_status_groups(self, c_tree, mygroups):

        #TODO: change index to zero after development
        index = 3

        group_status = []

        for group,taxa in mygroups.items():

            nd      = c_tree.mrca(taxon_labels = taxa)
            nd_taxa = self._get_taxa(nd, is_nd=True)
            is_same = self._is_same_group(nd_taxa, group_indx = index)

            group_status.append( (group, is_same) )

        return group_status

    def deeper_relationships(self, tree, mono_taxa):
        """
        **Experimental**

        get deeper relationship
        between monophyletic groups
        """
        mono_nodes = {}
        for i in list(mono_taxa):
            tmp_node = tree.mrca( taxon_labels =  mono_taxa[i] )
            mono_nodes[i] = tmp_node

        taken = []
        while True:
            avai = set(list(mono_nodes)) - set(taken)

            if not avai:
                break

            a = list(avai)[0]
            g_nd =  mono_nodes[a]
            g_par = g_nd._parent_node

            if g_par is None:
                taken += [a]
                continue

            g_sister = set(g_par._child_nodes)-set([g_nd])

            match_group = []
            for k,v in mono_nodes.items():
                if k == a:
                    continue

                if not g_sister:
                    break

                if v in list(g_sister):
                    match_group.append(k)
                    g_sister -= set([v])

            if not g_sister:
                new_g = match_group + [a]
                for td in new_g:
                    del mono_nodes[td]

                f_m_g = "(%s)" % ",".join(new_g)
                mono_nodes[f_m_g] = g_par
                taken += new_g
            else:
                taken += [a]

        return mono_nodes

    def _force_mono(self, para_groups, target_group, mygroups, full = False):
        targettaxa = []
        monotaxa   = []
        no_parenth = []

        for k,v in mygroups.items():

            under_quote = ["'%s'" % i for i in v]

            if len(under_quote) <= 1:
                no_parenth += under_quote
                continue

            tmp_parenth = ["(%s)" % ",".join(under_quote)]

            if k in para_groups:
                # if full, `target_group`
                # is actually empty.
                # This takes all 
                # paraphyletic groups
                if full:
                    targettaxa += tmp_parenth
                    continue

                if k == target_group:
                    targettaxa +=  tmp_parenth
                    continue
            else:
                if self.recycle_monos:
                    monotaxa += tmp_parenth
                    continue

            no_parenth += under_quote
                
        all_sets = targettaxa + monotaxa + no_parenth

        return all_sets

    def _just_taxa(self, file_tree):

        bmfile = os.path.basename( file_tree )
        # sys.stdout.write("Processing: %s\n" % bmfile)
        # sys.stdout.flush()

        try:
            c_tree = dendropy.Tree.get(
                        path   = file_tree, 
                        schema = self.schema,
                        preserve_underscores = True
                    )
        except dendropy.dataio.newickreader.NewickReader.NewickReaderMalformedStatementError:
            sys.stderr.write("Error reading: %s\n" % bmfile)
            sys.stderr.flush()

        return self._get_taxa(c_tree, is_nd = False)
    
    def _check(self, seq_tree):
        # seq_tree  = self.seq_tree[0]
        seq,file_tree = seq_tree

        bmfile = os.path.basename( file_tree )
        sys.stdout.write("Processing: %s\n" % bmfile)
        sys.stdout.flush()

        try:
            c_tree = dendropy.Tree.get(
                        path   = file_tree, 
                        schema = self.schema,
                        preserve_underscores = True,
                        rooting='default-rooted'
                    )
        except dendropy.dataio.newickreader.NewickReader.NewickReaderMalformedStatementError:
            sys.stderr.write("Error reading: %s\n" % bmfile)
            sys.stderr.flush()
            return None
                    
        # c_tree = copy.deepcopy(tree)
        if self.collapsebylen or self.collpasebysupp:
            self.collapse(c_tree)

        self._rooting(c_tree)

        mygroups     = self._get_groups(c_tree)
        group_status = self._get_status_groups(c_tree, mygroups) 
        # True if monophyletic
        # [ (spp1 , True ),
        #   (spp2 , False),
        # ]

        para_groups = [i[0] for i in group_status  if i[1] is False]

        if not para_groups:
            return None
        # note: you can have only one 
        # paraphyletic group if this group
        # is being paraphyletic around
        # monophyletic groups
        target_group = ""
        if not self.full_force:
            # if not fully forced,
            # `target_group` must
            # contain a value.
            # Otherwise, `other_group`
            # are all paraphyletic groups
            for g in self.s_groups:
                if g in para_groups:
                    target_group += g
                    break

            if not target_group:
                sys.stderr.write("No groups to test at: %s\n" % bmfile)
                sys.stderr.flush()
                return None

        all_sets = self._force_mono(
            para_groups  = para_groups,
            target_group = target_group,
            mygroups     = mygroups,
            full         = self.full_force
        )

        c_newick = "(%s);" % ",".join(all_sets) 

        return (seq, c_newick, bmfile)

    def _taxa2groups(self, taxa):

        mytaxa =  set(taxa)
        c_taxa = [(k,len(v)) for k,v in self._iter_taxa_file(mytaxa).items()]
        sorted_taxa =  sorted(c_taxa, key = lambda kv: kv[1], reverse = True)
        return [g for g,_ in sorted_taxa]

    def _readmetadata(self):
        myrows = []
        with open(self.metadata, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                myrows.append(row)

        return myrows

    def _run_raxml(self, seq_constrStr_baseTree):
        # seq_constrStr_baseTree = out

        seq_pruned = []
        for seq,constr,treefile in seq_constrStr_baseTree:
            # seq,constr,treefile
            out_constr = treefile + "_para_forcedCons.tree"
            with open( out_constr,  'w'  ) as f:
                f.write(  constr + "\n"  )

            seq_pruned.append( (seq, out_constr) )

        return self.__iter_raxml__(seq_pruned=seq_pruned)

    def _run_consel(self,):
        pass

    def check(self):

        self.seq_tree = self._readmetadata()

        with Pool(processes = self.threads) as p:

            if self.full_force:
                self.s_groups = [] if not self.tgroup else [self.tgroup]

            else:
                sys.stderr.write("\nMapping taxa...\r")
                sys.stderr.flush()

                taxa = []
                for _,file_tree in self.seq_tree:
                    preout = p.map_async(self._just_taxa, (file_tree,)).get()[0]
                    # print(preout)
                    if preout:
                        taxa.extend(preout)

                self.s_groups = self._taxa2groups(taxa)
                sys.stderr.write("Mapping taxa...Ok\n\n")
                sys.stderr.flush()

            out = []
            for seq_tree in self.seq_tree:
                preout = p.map_async(self._check, (seq_tree,)).get()[0]
                if preout:
                    out.append(preout)

            # pprint.pprint(out, indent=4)
            failed, cons_trees = self._run_raxml(seq_constrStr_baseTree=out)
            # cons_trees
            # [ (seq1, raxml_tree1)
            #   (seq2, raxml_tree2)
            # ]
            # for seq_tree in cons_trees:
            #     self._site_likehood(seq_tree)  
            # print(failed)
            # print(cons_trees)
 
# import glob
# trees_glob = "/Users/ulises/Desktop/GOL/data/alldatasets/nt_aln/trimmed/renamed/no_Ts/all_gene_trees_TBL/*.treefile"
# genetrees = glob.glob(trees_glob)[:3]

genetrees = [
    # "/Users/ulises/Desktop/GOL/data/alldatasets/nt_aln/trimmed/renamed/no_Ts/all_gene_trees_TBL/E0670.listd_allsets_aln_trimmed_renamed_noT_aln_trimmed_TBL.NT_aligned.fasta_trimmed.nex.treefile",
    "/Users/ulises/Desktop/GOL/data/alldatasets/nt_aln/trimmed/renamed/no_Ts/all_gene_trees_TBL/E0470.listd_allsets_aln_trimmed_renamed_noT_aln_trimmed_TBL.NT_aligned.fasta_trimmed.nex.treefile",
    ]
outgroup = None
taxnomyfile = "/Users/ulises/Desktop/GOL/software/fishlifeqc/by_products/taxa_file.csv"
metadata = "/Users/ulises/Desktop/GOL/software/fishlifeqc/by_products/para_metadata.csv"

self = Monophyly(
        metadata = metadata,
        recycle_monos = True,
        force_all = False, # if True, it will force mono to ALL para
        tgroup = None,
        treefiles = genetrees, 
        schema = 'newick',
        collpasebylen = False,
        minlen = 0.000001,
        collpasebysupp = True,
        minsupp = 0,
        outfilename = 't_like.csv',
        taxnomyfile = taxnomyfile,
        outgroup = outgroup,
        suffix = '_fishlife',
        threads = 5,
        raxml_exe = RAXML,
        evomodel = 'GTRGAMMA',
        iterations = 1,
    )

self.check()
# print(self.__get_constr_tree__)
# print(self.evomodel)

