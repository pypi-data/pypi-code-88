import os
import sys
import shutil

import runshell
import fishlifeseq
from fishlifeqc.concatenate import Concatenate

myos = sys.platform

if myos == 'darwin':
    RAXML = 'raxmlHPC-PTHREADS-SSE3_Darwin_64bit'

elif myos == 'linux' or  myos == 'linux2':
    RAXML = 'raxmlHPC-PTHREADS-SSE3_Linux_64bit'

elif myos == 'win32':
    RAXML = 'raxmlHPC-PTHREADS-SSE3.exe'

class Raxml:

    def __init__(self, 
                 alignments   = None,
                 concatenate  = False,
                 name_concate = "mysupermatrix.txt",
                 raxml_exe  = RAXML,
                 evomodel   = "GTRGAMMA",
                 bootstrap  = 10,
                 raxml_failures = "raxml_failures.txt",
                 threads    = 1):

        self.alignments   = alignments
        self.concatenate  = concatenate
        self.name_concate = name_concate
        self.raxml_exe  = RAXML
        self.evomodel   = evomodel
        self.bootstrap  = bootstrap
        self.threads    = threads
        self.RAXML_FAIL = raxml_failures

        self.parsimonyseed = 12345
        self.bootstrapseed = 12345

    def __get_bootstrap__(self, myaln):
        # myaln = '../data/E0537.NT_aligned.fasta_trimmed_rblastd'

        alname    = os.path.basename(myaln)
        currentwd = os.path.abspath(os.path.dirname(myaln))
        newwd     = os.path.join(currentwd, "raxml_" + alname)

        try:
            os.mkdir(newwd)
        except FileExistsError:
            pass
        
        cmd = """
        {raxml} -m {model}  \
                -p {pseed}  \
                -b {bseed}  \
                -s {aln}    \
                -N {boot}   \
                -n {suffix} \
                -T {threads}\
                -w {abspath}""".format(
                    raxml   = self.raxml_exe,
                    model   = self.evomodel,
                    pseed   = self.parsimonyseed,
                    bseed   = self.bootstrapseed,
                    aln     = myaln,
                    boot    = self.bootstrap,
                    suffix  = 'bootstrap',
                    threads = self.threads,
                    abspath = newwd
                ).strip()

        status = runshell.get(cmd)

        if status:

            shutil.rmtree(newwd)
            return None
        else:
            try:
                os.remove( myaln + ".reduced" )
            except FileNotFoundError:
                pass

            return newwd

    def __get_ML_tree__(self, myaln, newwd):

        cmd = """
        {raxml} -m {model}  \
                -p {pseed}  \
                -s {aln}    \
                -N {runs}   \
                -n {suffix} \
                -T {threads}\
                -w {abspath}""".format(
                    raxml   = self.raxml_exe,
                    model   = self.evomodel,
                    pseed   = self.parsimonyseed,
                    aln     = myaln,
                    runs    = self.bootstrap,
                    suffix  = "ML",
                    threads = self.threads,
                    abspath = newwd
                ).strip()

        status = runshell.get(cmd)

        if status:

            shutil.rmtree(newwd)
            return False
        else:
            try:
                os.remove( myaln + ".reduced" )
            except FileNotFoundError:
                pass
            return True

    def __get_genetree__(self, myaln, newwd):

        oldwd      = os.path.dirname(myaln)
        if not oldwd:
            oldwd = "."
        mltree     = os.path.join(newwd, "RAxML_bestTree.ML")
        bootstraps = os.path.join(newwd, "RAxML_bootstrap.bootstrap")

        cmd = """
        {raxml} -f b           \
                -m {model}     \
                -t {mltree}    \
                -z {bootstraps}\
                -n {suffix}    \
                -T {threads}   \
                -w {abspath}""".format(
                    raxml      = self.raxml_exe,
                    model      = self.evomodel,
                    mltree     = mltree,
                    bootstraps = bootstraps,
                    suffix     = 'final',
                    threads    = self.threads,
                    abspath    = newwd
                ).strip()

        status = runshell.get(cmd)

        if status:
            shutil.rmtree(newwd)
            return False

        defaultree  = os.path.join(newwd, "RAxML_bipartitions.final")

        mytreebname = os.path.basename(myaln) + "_raxmltree"
        mytree      = os.path.join(newwd, mytreebname)

        os.rename(defaultree, mytree)
        filedest = os.path.join(oldwd, mytreebname)

        if os.path.exists(filedest):
            os.remove(filedest)

        shutil.move(mytree, oldwd)
        shutil.rmtree(newwd)
        return True

    def __get_constr_tree__(self, seq):

        suffix = "$exonname'_raxml_constr'"
        pruned = seq + "_constr.tree"

        cmd = """
        {raxml} -p 12345\
                -g {pruned}\
                -m {model}\
                -s {seq}\
                -n {suffix}\
                -T {threads}\
                --silent\
                -N {runs}
                """.format(
                    raxml  = self.raxml_exe,
                    pruned = pruned,
                    model  = self.evomodel,
                    seq    = seq,
                    suffix = suffix,
                    runs   = self.bootstrap
                ).strip()

        print(cmd)

    def run(self):
        # RAXML_FAIL = "raxml_failures.txt"

        f_boot = []
        f_ml   = []
        f_join = []

        if self.concatenate:

            concaclass = Concatenate(
                            alignments      = self.alignments,
                            supermatrixname = self.name_concate,
                            partitionsname  = self.name_concate + "_partitions",
                            threads         = self.threads
                        )

            concaclass.run()

            self.alignments = [self.name_concate]

        for aln in self.alignments:

            newwd = self.__get_bootstrap__(aln)

            if not newwd:
                f_boot.append(aln)
                continue

            worked = self.__get_ML_tree__(aln, newwd)

            if not worked:
                f_ml.append(aln)
                continue

            worked = self.__get_genetree__(aln, newwd)

            if not worked:
                f_join.append(aln)
                continue

        if f_boot or f_ml or f_join:

            with open(self.RAXML_FAIL, "w") as f:

                f.write("file,what_process\n")

                if f_join:
                    for i in f_join:
                        f.write("%s,bipartition\n" % i)

                if f_boot:
                    for i in f_boot:
                        f.write("%s,boostrap\n" % i)

                if f_ml:
                    for i in f_ml:
                        f.write("%s,ml\n" % i)

# Raxml(
#     alignments = ['data/E0537.NT_aligned.fasta_trimmed_rblastd', 
#                   'data/mock1.txt' ],
#     concatenate= True,
#     name_concate= "mysupermatrix.txt",
#     raxml_exe  = RAXML,
#     evomodel   = "GTRGAMMA",
#     bootstrap  = 5,
#     threads    = 2
# ).run()

import csv
out_tlike = "/Users/ulises/Desktop/GOL/data/alldatasets/nt_aln/gene_trees/no_rblasted_shr_alrt/backup/t_like_complete.csv"
table = []
with open(out_tlike, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        table.append(row)

import re

selected_rows = []
for i in table[1::]:
    # i
    ori      = set(i[1].split(","))
    del_in   = set(i[3].split(","))
    leftover = ori - del_in
    reason   = i[5]
    # if re.findall('3 group', reason):
    #     selected_rows.append(i)

    if len(ori) > 1 and len(del_in) > 1:
        if  re.findall("3 group", reason):
            selected_rows.append(i)
['E0713.listd_allsets.NT_aligned.fasta_trimmed.nex.treefile_renamed',
  'Clupeiformes_Clupeidae_Alosa_alosa_53,Esociformes_Esocidae_Esox_lucius_29',
  'Clupeiformes_Clupeidae_Alosa_alosa_53',
  'Esociformes_Esocidae_Esox_lucius_29,Clupeiformes_Clupeidae_Alosa_alosa_53',
  '',
  'T clade has only S taxa with outside sister nodes at 3 group']
myfunc = lambda x: x
gene_trees = [1]

from multiprocessing import Pool

threads = 2
with Pool(processes = threads) as p:
    out = [*p.map(myfunc, gene_trees)]

with Pool(processes = threads ) as p:
    preout = []
    for gene_tree in gene_trees:
        result = p.apply_async(myfunc, (gene_tree,))
        preout.append(result)