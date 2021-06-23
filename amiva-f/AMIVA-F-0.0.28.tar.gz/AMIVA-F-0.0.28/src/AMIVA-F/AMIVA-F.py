import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import freesasa
from Bio.PDB import PDBParser
from Bio.PDB import Selection
from Bio.PDB import NeighborSearch
from pymol import cmd
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
from weka.classifiers import Evaluation
from weka.core.classes import Random
from collections import defaultdict
import os
import sys


class GUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame()
        self.frame.grid()
        self.title = master.title("AMIVA-F analysis of mutations in variants of human Filamin C")


        #master.state = "500x1000"

        #master.state = "zoomed"
        """
        self.label1 = tk.Label(self.frame, text="Welcome to AMIVA-F, this script will aid you \n in preparing your"
                                                " test dataset for your mutational prediction")
        self.label1.grid(row=0, column=0, columnspan=2, sticky="nesw")

        self.button1 = tk.Button(self.frame, text="Detailled Manual / additional help", command=self.manual)
        self.button1.grid(row=1, column=0, sticky="nsew")

        self.buttonhelp = tk.Button(self.frame, text="Detailled Manual / additional help", command=self.manual)
        self.buttonhelp.grid(row=1, column=1, sticky="nsew")

        self.infoattribtn = tk.Button(self.frame, text="More information regarding calculations",
                                      command=None)
        self.infoattribtn.grid(row=1, column=2, sticky="e")
        """

    def manual(self):
        window = tk.Toplevel(root)
        window.title("Manual for AMIVA-F")
        s = tk.Scrollbar(window)
        exp = tk.Text(window, width=140, height=30)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        exp.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=exp.yview)
        exp.config(yscrollcommand=s.set)
        manualtext = \
        "Hello and welcome to AMIVA - F quick tutorial to help you prepare a testdataset for your mutations of choice. \
        \n\nFirst you should enter the mutation of interest in the style of wildtype 1-letter abbreviated amino acid \
        \nfollowed by position and 1-letter abbreviated amino acid code of the mutation e.g:  S162L \
        \n\nBefore clicking the green button, make sure to have 2 files ready on your computer: \
        \n1) wildtype.pdb (The file you can obtain from supplementary of our publication with the structure)\
        \n2) mutant.pdb (The mutant pdb is generated upon prediction of ΔΔG from DUET. After obtaining the ΔΔG 3 (which is the bottom one) \
        \nyou will see a button stating: download pdb mutant file. \
        \n\nAfterwards you click on the green button: Calculate SASA, changes in number of atoms \
        \nThis will prompt you in two separate windows to provide first the wildtype.pdb\
        \nand afterwards the mutant pdb.\nIf you provided both files, you should see 5 calculated values in the formsheet\
        \non the right side of the AMIVA-F prepare screen.\
        \n\nThe first entry should be filled with the ΔΔG(DUET) value you obtained before as you created the mutant.pdb  \
        \nand now you should open a graphical molecular viewing tool e.g Pymol for the following parameters: \n\
        \n*)Accessibility change is simply if there is a difference between entry 4 and 5\n\
        \n*)Clashes, phosphosites and others is a wildcard attribute. First you go to the wildtype.pdb and introduce\
        \nthe mutation via mutagenisis and check if there is a possible rotamere conformation that does not introduce clashes.\
        \nAdditionally this parameter takes into account phosphosites and binding partners, so feel free to click yes\
        \nIf you have additonal information about that mutation, e.g being the spot of other posttranslational modification\
        \nor anything related to RNA, DNA interaction.\n\
        \n*)The sidechain orientation is simply if the sidechain looks towards the other beta sheet/helix or if it\
        \nis looking towards the solvent.\n \
        \n*)The secondary structure parameter is either helix, beta, or loop, with the additional possibility of being\
        \nIR(Insertion region), which is the special part in Ig20 as specified in the original publication\n \
        \n*)For absolute accuracy the last parameter requires you to load a script into pymol and then follow \
        \nthe steps specified in this script. If this is too daunting or does not work properly, do not worry.\
        \nA quick and decent APPROXIMATION is computed by clicking the green button! If this is too unreliable for you \
        \n you can still put a ? in this spot and you are done with filling out all parameters.\n \
        \nAfter checking if everything is properly entered, click first Get list of mutations ids used (which will\
        \ngenerate a txt file containing the ids of the mutations e.g H123P, because the predictor does not store this information) \
        \nIf you want to predict multiple mutations you will get a result file with \
        \n1)yes 2)no 3)yes ... without any clue which prediction belongs to the corresponding mutations.\
        \nIf you are done with that, proceed by clicking the shiny blue button which will prepare your testfile and you are done.\
        \n\nIf you have any questions, feel free to write me an email:\nnagym72@univie.ac.at"

        exp.insert(tk.END, manualtext)
        window.mainloop()

class Entry_formular:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame()
        self.frame.grid()

        # label for entry button amino acid substitution

        self.header = tk.Label(self.frame, text="AMIVA-F analysis of mutations in variants of human Filamin C", font="Helvetica 16 bold", fg="black")
        self.header.grid(row=0, column=0, sticky="nswe", ipady=5)
        self.label1 = tk.Label(self.frame, text="Please enter your mutation of interest into the entry field below.")
        self.label1.grid(row=1, column=0, columnspan=1, sticky="news")
        self.label2 = tk.Label(self.frame, text="Accepted format: e.g M82K", font="Helvetica 10 bold")
        self.label2.grid(row=2, column=0, ipadx=10, sticky="news")
        self.label3 = tk.Label(self.frame, text="for Methionine (M) being mutated to Lysine (K) ")
        self.label3.grid(row=3, column=0, ipadx=10, sticky="news")
        self.label4 = tk.Label(self.frame, text="Allowed range:\n35 - 2725", font="helvetica 10 italic")
        self.label4.grid(row=4, column=0, ipadx=10, columnspan=1, sticky="news")

        # entry + button for amino acid substitution
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=5, column=0)
        self.lblexplain = tk.Label(self.frame, text="After entering your desired mutation"
                                                    ", the blue button will give you a prediction after a couple of seconds")
        self.lblexplain.grid(row=6, column=0)
        self.button = tk.Button(self.frame, text="Predict mutation!"
                                , relief="ridge", borderwidth=4, bg="blue", fg="white",height=2, width=15,
                                command=lambda:[self.hydrophobicity_atomnumb(), entry_form.outfile_handler_weka()])
        self.button.config(font="helvetica 10 bold")
        self.button.grid(row=7, column=0, pady=(10,10))

        self.phosphohits = []

        self.pb = ttk.Progressbar(self.frame, orient="horizontal", mode="determinate", length=300)
        self.pb.grid(column=0, row=8, pady=(20, 0))

    def step(self):
        self.pb["value"] += 20

    def hydrophobicity_atomnumb(self):
        """dictionaries containing hydrophobicity values as determined by Kyte and Doolittle and number of atoms"""

        hydrophobchange = {"G": -0.4, "A": 1.8, "V": 4.2, "I": 4.5, "L": 3.8, "M": 1.9, "F": 2.8,
                           "Y": -1.3,
                           "W": -0.9, "P": -1.6, "C": 2.5, "Q": -3.5, "N": -3.5, "T": -0.7, "S": -0.8,
                           "E": -3.5, "D": -3.5, "K": -3.9, "H": -3.2, "R": -4.5}

        atomchangelib = {"G": 5, "A": 6, "V": 8, "I": 9, "L": 9, "M": 9, "F": 12, "Y": 13, "W": 15,
                         "P": 8,
                         "C": 7, "Q": 10, "N": 9, "T": 8, "S": 7, "E": 10, "D": 9, "K": 10, "H": 11,
                         "R": 12}

        "unelegant solution to retrieve IDS e.g I1928P, K82R ... from user after preparation because WEKAs outfile " \
        "will not contain information about the mutation names... it will just be ->  1: yes   2:no   3:no " \
        "in order to prevent information loss if one user wants multiple mutations to be classified this info will be " \
        "saved"

        """Clear all entries before run/ so that prior runs don't get overwritten"""

        self.pb["value"] += 20
        self.pb.update_idletasks()
        for entries in entryids:
            entries.delete(0,"end")
        entry_form.var.set(1)
        entry_form.var1.set(1)
        entry_form.var2.set(1)
        entry_form.var3.set(1)
        entry_form.phosphosites_entry.delete(0,"end")
        del intro_form.phosphohits       #removal of hits and opening of empty list
        intro_form.phosphohits = []      #new empty list for next round of mutations
        entry_form.addinfoentry.delete(0,"end")

        global mutation_ids
        mutation_ids = []
        #retrieve information from user and calculate SASA, dAtom, dHydrophobicity
        global entry_start
        entry_start = self.entry1.get()
        mutation_ids.append(entry_start)
        aa_wt = entry_start[0:1]
        aa_mut = entry_start[-1:]
        global pos
        pos = entry_start[1:-1]


        entry_list = []   #we check the user input in case he puts random stuff like M8H2K instead of M82K
        for entries in pos:
            entry_list.append(entries)

        for elements in entry_list:
            if elements in atomchangelib:
                messagebox.showerror("Invalid Input","Please enter a valid input")

        if entry_start == "":
            messagebox.showerror("Invalid Input", "Please enter a valid input")

        if entry_start[-1] not in atomchangelib:  # if someone enters a non canonical aa we forbid that.
            messagebox.showerror("Invalid Input", "Please enter a valid input")
        elif entry_start[0] not in atomchangelib:
            messagebox.showerror("Invalid Input", "Please enter a valid input")





        # SASA calculations
        #self.msg1 = tk.messagebox.showinfo("Wildtype.pdb", "In order to generate your parameters"
        #                                                   " you will now need to provide the wildtype .pdb file"
        #                                                   " after clicking Ok")
        #pdbfile1 = tk.filedialog.askopenfilename()
        parser = PDBParser(QUIET=True)
        """Automatically get file that corresponds to the entered mutation"""
        global domaininfo
        if int(pos) > 35 and int(pos) < 263:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_ABD.pdb"
            domaininfo = "ABD"
        elif int(pos) >= 270 and int(pos) <= 368:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_1.pdb"
            domaininfo = "Ig1"
        elif int(pos) >= 370 and int(pos) <= 468:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_2.pdb"
            domaininfo = "Ig2"
        elif int(pos) >= 469 and int(pos) <= 565:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_3.pdb"
            domaininfo = "Ig3"
        elif int(pos) >= 568 and int(pos) <= 658:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_4.pdb"
            domaininfo = "Ig4"
        elif int(pos) >= 659 and int(pos) <= 760:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_5.pdb"
            domaininfo = "Ig5"
        elif int(pos) >= 761 and int(pos) <= 861:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_6.pdb"
            domaininfo = "Ig6"
        elif int(pos) >= 862 and int(pos) <= 960:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_7.pdb"
            domaininfo = "Ig7"
        elif int(pos) >= 961 and int(pos) <= 1056:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_8.pdb"
            domaininfo = "Ig8"
        elif int(pos) >= 1057 and int(pos) <= 1149:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_9.pdb"
            domaininfo = "Ig9"
        elif int(pos) >= 1150 and int(pos) <= 1244:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_10.pdb"
            domaininfo = "Ig10"
        elif int(pos) >= 1245 and int(pos) <= 1344:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_11.pdb"
            domaininfo = "Ig11"
        elif int(pos) >= 1345 and int(pos) <= 1437:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_12.pdb"
            domaininfo = "Ig12"
        elif int(pos) >= 1438 and int(pos) <= 1533:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_13.pdb"
            domaininfo = "Ig13"
        elif int(pos) >= 1535 and int(pos) <= 1630:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_14.pdb"
            domaininfo = "Ig14"
        elif int(pos) >= 1631 and int(pos) <= 1734:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_15.pdb"
            domaininfo = "Ig15"
        elif int(pos) >= 1759 and int(pos) <= 1853:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_16.pdb"
            domaininfo = "Ig16"
        elif int(pos) >= 1854 and int(pos) <= 1946:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_17.pdb"
            domaininfo = "Ig17"
        elif int(pos) >= 1947 and int(pos) <= 2033:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_18.pdb"
            domaininfo = "Ig18"
        elif int(pos) >= 2036 and int(pos) <= 2128:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_19.pdb"
            domaininfo = "Ig19"
        elif int(pos) >= 2129 and int(pos) <= 2315:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_20.pdb"
            domaininfo = "Ig20"
        elif int(pos) >= 2316 and int(pos) <= 2401:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_21.pdb"
            domaininfo = "Ig21"
        elif int(pos) >= 2402 and int(pos) <= 2509:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_22.pdb"
            domaininfo = "Ig22"
        elif int(pos) >= 2510 and int(pos) <= 2598:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_23.pdb"
            domaininfo = "Ig23"
        elif int(pos) >= 2633 and int(pos) <= 2725:
            pdbfile1 = "./FLNc_structures_pdb/FLNc_domain_24.pdb"
            domaininfo = "Ig24"
        else:
            msgerr = messagebox.showerror("Outside of FLNc position boundaries", "FlnC is only covered between 35 and 2725.\n"
                                                                                 "Please enter a position that lies between these boundaries!")

        trans_aa_code_dict ={"A": "ALA", "G": "GLY", "S":"SER", "T":"THR", "C":"CYS", "M":"MET", "V":"VAL", "I":"ILE",
                             "L":"LEU", "F":"PHE", "Y": "TYR", "W": "TRP", "H": "HIS", "Q": "GLN", "E": "GLU", "N": "ASN",
                             "D": "ASP", "P": "PRO", "K": "LYS", "R": "ARG"}

        reverse_trans_aa_dict = {"ALA": "A","GLY":"G" ,"SER":"S","THR":"T", "CYS":"C", "MET":"M", "VAL":"V", "ILE":"I",
                             "LEU":"L", "PHE":"F", "TYR": "Y", "TRP": "W", "HIS": "H", "GLN": "Q", "GLU": "E", "ASN": "N",
                             "ASP": "D", "PRO": "P", "LYS": "K", "ARG": "R"}


        with open(pdbfile1, "r") as pdbfile1_0:
            structure = parser.get_structure("FLNc", pdbfile1_0)
            correct_atom_question = structure[0]["A"][int(pos)]
            resnamecheck = correct_atom_question.get_resname()

            """check if amino acid  entered is really amino acid at the correct position in the structure"""

            if resnamecheck == trans_aa_code_dict[aa_wt]:
                pass
            else:
                msg = messagebox.askquestion("Upps, wrong amino acid!", ("The specified amino acid at position " + str(pos) + " is " + resnamecheck + " instead of " + trans_aa_code_dict[aa_wt]
                                                                   + "\nShall we proceed with " + resnamecheck + "?"))
                if msg == "yes":
                    aa_wt = reverse_trans_aa_dict[resnamecheck]
                    self.entry1.delete(0)
                    self.entry1.insert(0, aa_wt)           #we correct the first position with the correct amino acid in the entry field
                    entry_start = self.entry1.get()        #also grab the correct amino acid for further downstream calculation (not only in the entry formular)

                else:
                    messagebox.showerror("Wrong amino acid!","Cant proceed with wrong amino acid! \nLeaving the application now")
                    root.after(2000, root.destroy())


            #structure = freesasa.Structure(pdbfile1_0, {"hetatm": False, "hydrogen": False})
            #print(structure[0]["A"][int(pos)])
            result, residue_areas = freesasa.calcBioPDB(structure)
            res2 = freesasa.Result.residueAreas(result)
            dumpres = self.dump((res2["A"][str(pos)]))
            #print(((dumpres[-4], dumpres[-3], round(dumpres[-1], 2), round(dumpres[-5], 3))))
            # conversion into relative SASA for wt
            entryids[1].insert(0, round(dumpres[-1], 2))
            if round(dumpres[-5], 2) > 0.43:
                entryids[2].insert(0, "accessible")
            elif round(dumpres[-5], 2) < 0.43 and (round(dumpres[-5], 2) > 0.17):
                entryids[2].insert(0, "partially")            #changed from partially accessible to partially
            else:
                entryids[2].insert(0, "inaccessible")
            # entrylst[5].insert(0, round(dumpres[-5],2))

            dhydrophob = round(hydrophobchange[aa_mut] - hydrophobchange[aa_wt], 2)
            datom = atomchangelib[aa_mut] - atomchangelib[aa_wt]
            entryids[4].insert(0, datom)
            entryids[5].insert(0, dhydrophob)
        # pymol part begins here

        entry_form.r2clash.select()  #we start with assumption that there is no clash!
        """Works but needs overhaul and better except part"""
        cmd.reinitialize("everything")
        object_pymol = pdbfile1.split("/")
        correct_modelname = object_pymol[-1][0:-4]
        cmd.load(pdbfile1)
        cmd.wizard("mutagenesis")
        cmd.do("refresh_wizard")
        idx = pos
        mutation_trgt = trans_aa_code_dict[aa_mut]  # HERE INSERT THE CORRECT AMINO ACID
        cmd.get_wizard().set_mode(mutation_trgt)
        cmd.get_wizard().do_select(idx + "/")
        trgt = cmd.get_wizard().bump_scores

        #print(dir(cmd.get_wizard()))
        #cmd.get_wizard().apply()
        #print(trgt_check)
        rot = 0
        rot_ex = 0
        rot_super_strict = 0
        sum_strain = 0
        for strain in trgt:
            sum_strain += strain
            if strain < 44:
                rot += 1
                # print("found at least one suitable rotamere at cutoff 44 strain!")
            if strain < 30:
                rot_ex += 1
            if strain < 23:  # makes most sense and is strict enough
                rot_super_strict += 1
        #print("Total amount of rotameres found below cutoff of 44 strain:", rot)
        #print("Total amount of rotameres found below cutoff of 30 strain:", rot_ex)
        #print("Total amount of rotameres found below cutoff of 25 strain:", rot_super_strict)

        #if sum_strain != 0:
        #    print(sum_strain / len(trgt))
        #else:
        #    print("no rotameres")
        #    trgt.append("0")  #list with entry 0 to prevent error from index(which requires a list



        """Better selector for clashes of sidechain atoms"""



        #to be done

        """selection if sidechain clashes or not:
            Arbitraryly found thresholds selected for now, might improve later.
            Additionally the average of all rotameres might be added to improve quality of selection.
            Now just implemented as basic version to get a fully automated experience
            """

        #entry_form.r1clash.select()
        try:
            index_hit = trgt.index(min(trgt))  # fish out the best hit
        except:
            index_hit = 0

        cmd.frame(index_hit)
        #print(index_hit)
        cmd.get_wizard().apply()
        cmd.set_wizard()
        mut_pdb_save = "./FLNc_mutant_structures_pdb/FLNc_" + entry_start + ".pdb"  # We generate a mutant pdb file for the user #not correct
        #print(correct_modelname)
        cmd.save(mut_pdb_save, correct_modelname)  # saved into the correct directory.
        cmd.reinitialize("everything")
        #clashscore implementation



        """
        #clashscore end


        #checking phosphosites and posttranslational modifications

        posttranslational_list = []
        with open("./Posttranslational_modifications_and_binding_partners/Posttranslational_modification_list.txt", "r") as post_fh:
            lines = post_fh.readlines()
            for entries in lines:
                stripped = entries.replace("\n","")
                sitenumber = stripped.split(",") #list containing 2 entries -> 1) position of modification 2) type of modification
                positions_of_modifications = sitenumber[0]   #we grab the positions
                posttranslational_list.append(int(positions_of_modifications))  #convert to int from string to be used for check


        with open(pdbfile1, "r") as pdbfile1_0:
            parser = PDBParser(QUIET=True)
            structurephosphosites = parser.get_structure("FLNc", pdbfile1_0)
            target_residue = int(pos)    #we search around the submitted position by the user in the entryfield
            residue_of_int = list(structurephosphosites[0]["A"][target_residue])  #making a list containing all atoms of specified residue
            target_atoms = [atom.get_coord() for atom in
                            residue_of_int]  # all atoms of residue that gets modified posttranslationally
            search_atoms = Selection.unfold_entities(structurephosphosites, "A")    #we search through all available atoms in the structure

            ns = NeighborSearch(search_atoms)

            hits = []
            for check_atoms in target_atoms:         #only those atoms that are within 8 A radius of a sphere are selected and added to our hitlist
                proximal_atoms = ns.search(check_atoms, 8, "R")
                for matches in proximal_atoms:
                    hits.append(matches)

            unique_hits = list(set(hits))  # sorting duplicates

            phosphocheck = False    #we set this for later to retrieve into about phosphosites


            for check in unique_hits:  # we search through all unique hits within 8 A radius of a sphere
                if check.get_id()[1] in posttranslational_list:  # if the atom id found in this sphere matches our known phosphosites we respond
                    entry_form.r1clash.select()           #if it appears to be within 8 A cutoff radius we select clashes or phosphosites in the entrypanel
                    if entryids[2].get() == "inaccessible":      #if the wildtype residue is 
                        entry_form.r2clash.select()
                    phosphocheck = True     #if we find a site we prompt this later in the user output
                    #print(("next to phosphosite", check.get_id()[1]))
                    spotted_site = check.get_id()[1]
                    self.phosphohits.append(spotted_site)


        for hits in self.phosphohits:
            entry_form.phosphosites_entry.insert(0, (str(hits) + " (P) "))

        if len(self.phosphohits) == 0:
            entry_form.phosphosites_entry.insert(0, "None")

        """
                                                 #print(len(self.phosphohits))  here it works
        #selectionprocess end
        """ 
        index_hit = trgt.index(min(trgt))       #fish out the best hit
        cmd.frame(index_hit)
        print(index_hit)
        cmd.get_wizard().apply()
        cmd.set_wizard()
        mut_pdb_save = "./FLNc_mutant_structures_pdb/FLNc_" + entry_start + ".pdb"  # We generate a mutant pdb file for the user #not correct
        print(correct_modelname)
        cmd.save(mut_pdb_save, correct_modelname)  # saved into the correct directory.
        #cmd.quit()
        """
        #secondary struc part comes here

        self.pb["value"] += 20
        self.pb.update_idletasks()

        cmd.load(pdbfile1)
        ids = []
        resis = []
        resnames = []
        secstruc = []
        idx = pos  # user entry submitted position
        cmd.iterate_state(1, "i. " + idx + " and name ca",
                          "ids.append(ID), resis.append(resi), resnames.append(resn), secstruc.append(ss)",
                          space={'ids': ids, 'resis': resis, 'resnames': resnames, "secstruc": secstruc})

        #print((ids, resis, resnames, secstruc))


        #block to get secondary structure selected
        for secstruc in secstruc:
            if secstruc == "L":
                #print("Loop residue!")
                entry_form.r3secstr.select()
            elif secstruc == "S":
                #print("Sheet residue!")
                entry_form.r2secstr.select()
            elif secstruc == "H":
                #print("Helix residue!")
                entry_form.r1secstr.select()
            elif secstruc == "":
                entry_form.r3secstr.select()
        if int(pos) <= 2243 and int(pos) >= 2162:                   #this will mark the members of the IR region accordingly
            entry_form.r4secstr.select()
        else:
            entry_form.r4secstr.configure(state="disabled")


        # mutant SASA

        try:
            mutname = "./FLNc_mutant_structures_pdb/FLNc_" + entry_start +".pdb"
        except:
            self.msg = tk.messagebox.showinfo("Mutant.pdb", "Continue now by providing the mutant .pdb file")
            mutname = tk.filedialog.askopenfilename()


        with open(mutname, "r") as pdbfile2:
            structure1 = parser.get_structure("FLNc", pdbfile2)
            result_mut, residue_areas = freesasa.calcBioPDB(structure1)
            res2 = freesasa.Result.residueAreas(result_mut)
            dumpres = self.dump((res2["A"][str(pos)]))
            #print(((dumpres[-4], dumpres[-3], round(dumpres[-1], 2), round(dumpres[-5], 3))))

            entryids[0].insert(0, round(dumpres[-1], 2))
            if round(dumpres[-5], 2) > 0.43:
                entryids[3].insert(0, "accessible")
            elif round(dumpres[-5], 2) < 0.43 and (round(dumpres[-5], 2) > 0.17):
                entryids[3].insert(0, "partially")  #changed from partially accessible to partially
            else:
                entryids[3].insert(0, "inaccessible")

            #sidechainorientation selector part

            if round(dumpres[-2],2) > 20:
                entry_form.r1sidechain.select()
            elif dumpres[-3] == "PRO" or dumpres[-3] == "GLY":
                entry_form.r3sidechain.select()
            elif round(dumpres[-2],2) < 20:
                entry_form.r2sidechain.select()

            if dumpres[-3] != "PRO" and dumpres[-3] != "GLY":       #we dont allow this to be selected if mutated aa is not gly or pro
                entry_form.r3sidechain.configure(state="disabled")

            #sidechainorientation selector part stops

            #entering sap:

        """block to get accessibility change upon mutation"""


        if entryids[2].get() == entryids[3].get():            #if they are the same there is no difference
            entry_form.r3.select()
        elif entryids[2].get() != entryids[3].get():          #if they are different then the following might occur
            if entryids[3].get() == "accessible":             #mutant == accessible and different than wt means it got better
                entry_form.r1.select()
            elif entryids[3].get() == "partially": #mutant == partially and different from wt means it could be either way
                if entryids[2].get() == "inaccessible":       #mutant == partially and wt == inaccessible means it got better
                    entry_form.r1.select()
                if entryids[2].get() == "accessible":         #mutant == partially and wt == accessible means it got worse
                    entry_form.r2.select()
            if entryids[2].get() == "accessible":             #mutant != wt and wt is accessible means it can only be worse in mutant
                entry_form.r2.select()
            if entryids[2].get() == "partially":   #mutant != wt and wt is more accessible than mutant
                entry_form.r2.select()


        #pdbfile2.close()


        def sap_score(pdbfile_id):
            """atomnumberslib is required to deal with the case that the inspected residue is the last residue in the pdb file"""
            atomnumberslib = {"G": 5, "A": 6, "V": 8, "I": 9, "L": 9, "M": 9, "F": 12, "Y": 13, "W": 15,
                             "P": 8,
                             "C": 7, "Q": 10, "N": 9, "T": 8, "S": 7, "E": 10, "D": 9, "K": 10, "H": 11,
                             "R": 12}


            sapscoredict = {"CYS": [0.179, 95.2439], "GLN": [-0.25, 147.855], "ILE": [0.442, 151.242],
                        "SER": [-0.142, 81.2159], "VAL": [0.324, 124.237], "GLY": [0.0, 23.1338],
                        "PRO": [0.21, 111.533], "LYS": [-0.218, 177.366], "ASP": [-0.473, 110.209],
                        "THR": [-0.051, 111.597], "PHE": [0.499, 186.7], "ALA": [0.115, 64.7809],
                        "MET": [0.237, 164.674], "HIS": [-0.336, 147.95], "GLU": [-0.458, 143.924],
                        "LEU": [0.442, 139.524], "ARG": [-0.501, 210.02], "TRP": [0.377, 229.619],
                        "ASN": [-0.265, 113.187], "TYR": [0.379, 200.306]}

            global atom_ids
            global parsed_pdb_sasa


            atom_ids = []
            parsed_pdb_sasa = defaultdict(list)

            radius = float(10)
            probe_radius_val = 1.4
            resolution_val = 20

            trgt_file_to_parse = pdbfile_id
            cmd.load(trgt_file_to_parse)
            if len(cmd.get_names('selections')) == 0:
                cmd.select('all')
            with open(mutname, "r") as sap_pdb:
                biopdb_parser = PDBParser(QUIET=True)
                biopdb_structure = biopdb_parser.get_structure('bio', sap_pdb)

                model_name = "FLNc_" + self.entry1.get()
                #print(model_name)
                freesasa_struct = freesasa.structureFromBioPDB(biopdb_structure,
                                                       freesasa.Classifier.getStandardClassifier('naccess'))

                result = freesasa.calc(freesasa_struct, freesasa.Parameters(
                    {'algorithm': freesasa.ShrakeRupley, 'probe-radius': float(probe_radius_val),
                    'n-points': float(resolution_val)}))

            # print(result.nAtoms())         #1853 atoms in ABD -> true

                for i in range(result.nAtoms()):
                    cmd.alter('id %s and %s' % (i, model_name), 'b = %s' % (str(result.atomArea(i))))

                cmd.iterate_state(1, model_name, "parsed_pdb_sasa[ID] = b",
                          space={'parsed_pdb_sasa': parsed_pdb_sasa, 'sap_model_name': model_name})

                cmd.iterate_state(1, model_name, 'atom_ids.append(ID)',
                          space={'atom_ids': atom_ids, 'sap_model_name': model_name})

                residue_of_interest = biopdb_structure[0]["A"][int(pos)][
                    "N"]  # we fish for the N because each residue starts with atom index N
                try:
                    next_residue = biopdb_structure[0]["A"][int(int(pos)+1)]["N"]
                    stopping_atom = next_residue.get_serial_number()
                except:
                    stopping_atom = residue_of_interest.get_serial_number() + atomnumberslib[entry_start[-1:]]

                starting_atom = residue_of_interest.get_serial_number()  # all relevant atoms are inbetween N from residue of interest (including N) and N-1 index from the next residue


                short_atom_search = []  # instead of iterating through the whole molecule we collect only info about the relevant part

                for i in range(starting_atom, stopping_atom):
                    short_atom_search.append(i)

                sap_atom_dictionary = defaultdict()

                for i in short_atom_search:

                    global surrounding_atoms
                    surrounding_atoms = defaultdict(list)

                    cmd.select('index %s around %s and %s' % (i, radius, model_name))
                    cmd.iterate_state(1, 'sele', 'surrounding_atoms[resn].append(ID)',
                              space={'surrounding_atoms': surrounding_atoms})

                    for j in surrounding_atoms:

                        idxlist = surrounding_atoms[j]

                        tmp = []

                        for idx in idxlist:
                            tmp.append(parsed_pdb_sasa[idx])

                        surrounding_atoms[j] = sum(tmp)

                    surrounding_score_list = []

                    for surrounding_residue in surrounding_atoms:
                        normalized_hydrophobicity = sapscoredict[surrounding_residue.upper()][0]
                        fully_exposed_saa = sapscoredict[surrounding_residue.upper()][1]

                        surrounding_score_list.append(
                            surrounding_atoms[surrounding_residue] / fully_exposed_saa * normalized_hydrophobicity)

                    sap_score_i = sum(surrounding_score_list)
                    sap_atom_dictionary[i] = sap_score_i

                    cmd.alter('ID %s and %s' % (i, model_name), 'b = %s' % sap_score_i)
                    cmd.sort()
                    cmd.delete('sele')

                total_sap_residue = 0
                for i in range(starting_atom, stopping_atom):
                    total_sap_residue += sap_atom_dictionary[i]

                #print(total_sap_residue / (stopping_atom - starting_atom))  # this works perfect!
                normalized_sap_per_residue = total_sap_residue / (stopping_atom - starting_atom)

                return normalized_sap_per_residue

        sap_score_residue_interest = sap_score(mutname)
        self.pb["value"] += 20
        self.pb.update_idletasks()

        #print(sap_score_residue_interest)
        entryids[6].insert(0, round(sap_score_residue_interest, 2))        #sap score calculated according to dominics method but shortcut, same accuracy as his method
        #8 digits after comma similar.



        #clashcheck new

        contact_count, clash_count = self.clashcheck(mutname)      #reads in the mutant pdb , retrieves contact and clashcount
        #print((str(contact_count), str(clash_count)))
        if clash_count > 0:
            entry_form.r1clash.select()
        #clashcheck ends

        #binding partner check

        self.binding_partners(mutname)
        self.posttranslational_sites(mutname)


    def posttranslational_sites(self,pdbfile):
        posttranslational_list = []
        with open("./Posttranslational_modifications_and_binding_partners/Posttranslational_modification_list.txt", "r") as post_fh:
            lines = post_fh.readlines()
            for entries in lines:
                stripped = entries.replace("\n","")
                sitenumber = stripped.split(",") #list containing 2 entries -> 1) position of modification 2) type of modification
                positions_of_modifications = sitenumber[0]   #we grab the positions
                posttranslational_list.append(int(positions_of_modifications))  #convert to int from string to be used for check


        with open(pdbfile, "r") as pdbfile1_0:
            parser = PDBParser(QUIET=True)
            structurephosphosites = parser.get_structure("FLNc", pdbfile1_0)
            target_residue = int(pos)    #we search around the submitted position by the user in the entryfield
            residue_of_int = list(structurephosphosites[0]["A"][target_residue])  #making a list containing all atoms of specified residue
            target_atoms = [atom.get_coord() for atom in
                            residue_of_int]  # all atoms of residue that gets modified posttranslationally
            search_atoms = Selection.unfold_entities(structurephosphosites, "A")    #we search through all available atoms in the structure

            ns = NeighborSearch(search_atoms)

            hits = []
            for check_atoms in target_atoms:         #only those atoms that are within 8 A radius of a sphere are selected and added to our hitlist
                proximal_atoms = ns.search(check_atoms, 8, "R")
                for matches in proximal_atoms:
                    hits.append(matches)

            unique_hits = list(set(hits))  # sorting duplicates

            phosphocheck = False    #we set this for later to retrieve into about phosphosites


            for check in unique_hits:  # we search through all unique hits within 8 A radius of a sphere
                if check.get_id()[1] in posttranslational_list:  # if the atom id found in this sphere matches our known phosphosites we respond
                    entry_form.r1clash.select()           #if it appears to be within 8 A cutoff radius we select clashes or phosphosites in the entrypanel
                    phosphocheck = True     #if we find a site we prompt this later in the user output
                    #print(("next to phosphosite", check.get_id()[1]))
                    spotted_site = check.get_id()[1]
                    self.phosphohits.append(spotted_site)


        for hits in self.phosphohits:
            entry_form.phosphosites_entry.insert(0, (str(hits) + " (P) "))

        if len(self.phosphohits) == 0:
            entry_form.phosphosites_entry.insert(0, "None")           #if there is a hit in the phosphohits list then we select clash
        else:
            entry_form.r1clash.select()


    def dump(self, obj):
        reslist = []
        for attr in dir(obj):
            reslist.append(getattr(obj, attr))
        return reslist

    def clashcheck(self,pdbfile):
        pdbfile2 = pdbfile
        parser = PDBParser(QUIET=True)
        structureclash = parser.get_structure("FLNc", pdbfile2)

        target_residue = int(pos)
        atoms_of_interest = list(structureclash[0]["A"][target_residue])
        atoms_interest_without_mainchain = []
        #print(len(atoms_of_interest))
        for atom in atoms_of_interest:
            if atom.get_name() != "N" and atom.get_name() != "O" and atom.get_name() != "C" and atom.get_name() != "CA":
                atoms_interest_without_mainchain.append(atom)

        target_atoms = [atom.get_coord() for atom in
                        atoms_interest_without_mainchain]  # all atoms of residue that gets modified posttranslationally

        #print(len(target_atoms))
        search_atoms = Selection.unfold_entities(structureclash, "A")  # load in all atoms of structure

        ns = NeighborSearch(search_atoms)

        hits_contacts = []
        hits_clashes = []
        for check_atoms in target_atoms:
            proximal_atoms = ns.search(check_atoms, 4, "A")        #we define contacts as below 4 Angström radius cutoff
            for matches in proximal_atoms:
                hits_contacts.append(matches)

        for check_atoms in target_atoms:
            clash_atoms = ns.search(check_atoms, 2, "A")         #we define clashes as below 2.5 Angström radius cutoff
            for matches in clash_atoms:
                hits_clashes.append(matches)

        # print((len(hits_clashes),len(hits_contacts)))
        clashset = set(hits_clashes)
        contactset = set(hits_contacts)
        clashresidues = []
        contactresidues = []
        clashcounter = 0
        contactcounter = 0

        for a in clashset:
            #print((a.get_parent().get_resname(), a.get_parent().get_id()[1], a.get_name()))
            clashresidues.append(a.get_parent().get_id()[1])

        for a in contactset:
            # print((a.get_parent().get_resname(), a.get_parent().get_id()[1], a.get_name()))
            contactresidues.append(a.get_parent().get_id()[1])

        while target_residue in clashresidues:  # removal of hits that are the target atom itself
            clashresidues.remove(int(target_residue))

        while target_residue in contactresidues:
            contactresidues.remove(int(target_residue))

        # print(len(clashresidues))
        # for hits in clashresidues:
        #    print(hits)
        for hits in contactresidues:
            # print(hits)
            contactcounter += 1
        for hits in clashresidues:
            #print(hits)
            contactcounter += 1
            clashcounter += 1

        # print((len(clashset),len(contactset)))
        #print(str(contactcounter) + " contacts", str(clashcounter) + " clashes")
        return (contactcounter,clashcounter)

    def binding_partners(self,pdbfile):
        """This segment will be utilized to grab known binding partner positions and accordingly take those into account for predictions"""

        binding_partner_dict = {}
        binding_partner_list = []
        with open("./Posttranslational_modifications_and_binding_partners/Binding_partners_list.txt", "r") as post_fh:
            lines = post_fh.readlines()
            for entries in lines:
                stripped = entries.replace("\n", "")
                sitenumber = stripped.split(",")  # list containing 2 entries -> 1) position of modification 2) type of modification
                positions_of_bindingsite = sitenumber[0]  # we grab the positions
                info_about_binding_partner = sitenumber[1]
                binding_partner_dict[str(sitenumber[0])] = info_about_binding_partner        #to retrieve information later on about the type of binding partner
                binding_partner_list.append(int(positions_of_bindingsite))  # convert to int from string to be used for check

        with open(pdbfile, "r") as pdbfile1_0:
            parser = PDBParser(QUIET=True)
            structurebindingsites = parser.get_structure("FLNc", pdbfile1_0)
            target_residue = int(pos)    #we search around the submitted position by the user in the entryfield
            residue_of_int = list(structurebindingsites[0]["A"][target_residue])  #making a list containing all atoms of specified residue
            target_atoms = [atom.get_coord() for atom in residue_of_int]  # all atoms of residue that are relevant in binding to another moiety
            search_atoms = Selection.unfold_entities(structurebindingsites, "A")    #we search through all available atoms in the structure

            ns = NeighborSearch(search_atoms)

            hits = []
            for check_atoms in target_atoms:         #only those atoms that are within 8 A radius of a sphere are selected and added to our hitlist
                proximal_atoms = ns.search(check_atoms, 8, "R")
                for matches in proximal_atoms:
                    hits.append(matches)

            unique_hits = list(set(hits))  # sorting duplicates

            bindingpartnercheck = False  # we set this for later to retrieve into about phosphosites

            binding_sites_spotted = []
            for check in unique_hits:  # we search through all unique hits within 8 A radius of a sphere
                if check.get_id()[1] in binding_partner_list:  # if the atom id found in this sphere matches our known relevant binding partner sides we select accordingly
                    entry_form.r1clash.select()  # if it appears to be within 8 A cutoff radius we select clashesl
                    if entryids[2].get() == "inaccessible" and entryids[3].get() == "inaccessible" and entry_form.phosphosites_entry.get() == "None":      #if the wildtype residue and the mutant are buried-> we dont care about effect
                        entry_form.r2clash.select()
                    if pos in binding_partner_list:          #if the residue is the exact one in the list specified we still take it as a hit.
                        entry_form.r1clash.select()
                    bindingpartnercheck = True  # if we find a site we prompt this later in the user output
                    #print(("next to bindingsite", check.get_id()[1]))
                    spotted_site = check.get_id()[1]
                    binding_sites_spotted.append(spotted_site)

            #print(len(binding_sites_spotted))
            for entries in binding_sites_spotted:
                if str(entries) in binding_partner_dict:
                    entry_form.addinfoentry.insert(0, (str(entries) + " " + binding_partner_dict[str(entries)] +" "))

            if len(binding_sites_spotted) == 0:
                #print("yes")
                entry_form.addinfoentry.insert(0, "None")



class Entryfield:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame()
        self.frame.grid()

        """This will be written into the outfile! Same names used to train the multilayer perceptron"""
        attributelst = ["Absolute_SASA_mutant(A**2)",
                        "Absolute_SASA_wt(A**2)",
                        "relative_SASA_wt", "relative_SASA_mutant", "'delta_number_of_atoms(mutant- wt)'",
                        "'dhydrophobicity(mutant - wt)'",
                        "change accessibility(upon mutation)",
                        "clashes AND/OR binding partner interference AND/OR phosphosite",
                        "sidechain_orientation", "secondary_structure", "SAP_score_average_per_residue", "malign"
                        ]

        """This will be depicted next to the entryfields to avoid confusion"""
        global attributeshown
        attributeshown = ["Absolute SASA mutant",
                        "Absolute SASA wildtype",
                        "Relative SASA wildtype", "Relative SASA mutant", "Δ Number of atoms",
                        "Δ Hydrophobicity",
                        "Δ Accessibility (upon mutation)",
                        "Clashes AND/OR binding partner interference AND/OR phosphosite",
                        "Sidechain_orientation", "Secondary structure", "SAP score per residue"]

        global entryids
        entryids = []  # this will contain all the specific positions from where to retrieve the inserted information
        # that will be written into an outfile.

        attribute_explainer = [
                               "Calculated with Shrake-Rupley algorithm, Freesasa",
                               "Calculated with Shrake-Rupley algorithm, Freesasa",
                               "Calculated with Shrake-Rupley algorithm, Freesasa",
                               "Calculated with Shrake-Rupley algorithm, Freesasa",
                               "Change in number of atoms, ignoring Hydrogen atoms",
                               "Calculated in hydrophobicity upon mutation, Kyte-Doolittle table values used",
                               "Does the accessibility change upon mutation (compare entry 4 and 5)",
                               "Does the inserted mutation generates clashes in the structure?\n"
                               "Are you aware of any potential phosphosites (8 Angström cutoff)\n "
                               "or binding partners in close vicinity (see original paper)",
                               "Does the side chain of the residue look towards the solvent or the other beta sheet/helix?",
                               "What type of secondary structure does the effected residue belong to?",
                               "SAP-score, a propensity to be calculated via external sources,\n"
                               "takes into account accessibility and change in hydrophobicity together\n"
                               "calculate SAP on the *mutant.pdb*\n If you click on the green button, you will get\n"
                               "a very close approximation, sufficient in most cases!\n"
                                ]
        # generates all entry explaining comments left from the entry labels
        #for idx, entries in enumerate(attribute_explainer[7:]):
        #    self.label = tk.Label(self.frame, text=entries)
        #    self.label.grid(column=0, row=idx, sticky="w")

        # generates all attribute labels and their respective entry fields right to them
        for idx, entries in enumerate(attributeshown[:6]):
            self.label = tk.Label(self.frame, text=entries)
            self.entry = tk.Entry(self.frame, width=50)
            entryids.append(self.entry)
            self.label.grid(column=0, row=idx+1, sticky="e")
            self.entry.grid(column=1, row=idx+1, sticky="w")

        for idx, entries in enumerate(attributeshown[6:]):
            self.label=tk.Label(self.frame, text=entries)
            self.label.grid(column=0, row=idx+7, sticky="e")

        # radiobuttons for pymol visual observations
        # change accessibility
        self.var = tk.StringVar()
        self.var.set(1)
        self.frame0 = tk.Frame(self.frame, width=10)
        self.frame0.grid(row=7, column=1, sticky="w")
        self.r1 = tk.Radiobutton(self.frame0, text="more accessible", variable=self.var, value="better", command=None)
        self.r1.grid(row=0, column=0)
        self.r2 = tk.Radiobutton(self.frame0, text="less accessible", variable=self.var, value="worse", command=None)
        self.r2.grid(row=0, column=1)
        self.r3 = tk.Radiobutton(self.frame0, text="no difference", variable=self.var, value="no", command=None)
        self.r3.grid(row=0, column=2)

        # clashes, phosphosites, methylations, binding partners buttons:
        self.var1 = tk.StringVar()
        self.var1.set(1)
        self.frame1 = tk.Frame(self.frame, width=10)
        self.frame1.grid(row=8, column=1, sticky="w")
        self.r1clash = tk.Radiobutton(self.frame1, text="yes", variable=self.var1, value="yes", command=None)
        self.r1clash.grid(row=0, column=0)
        self.r2clash = tk.Radiobutton(self.frame1, text="no", variable=self.var1, value="no", command=None)
        self.r2clash.grid(row=0, column=1)

        # sidechain orientation, radiobuttons

        self.var2 = tk.StringVar()
        self.var2.set(1)
        self.frame2 = tk.Frame(self.frame, width=10)
        self.frame2.grid(row=9, column=1, sticky="w")
        self.r1sidechain = tk.Radiobutton(self.frame2, text="solvent", variable=self.var2, value="solvent",
                                          command=None)
        self.r1sidechain.grid(row=0, column=0)
        self.r2sidechain = tk.Radiobutton(self.frame2, text="helix/beta", variable=self.var2, value="beta",
                                          command=None)
        self.r2sidechain.grid(row=0, column=1)
        self.r3sidechain = tk.Radiobutton(self.frame2, text="Gly/Pro residue", variable=self.var2, value="?",
                                          command=None)
        self.r3sidechain.grid(row=0, column=2)

        # secondary structure, radiobuttons

        self.var3 = tk.StringVar()
        self.var3.set(1)
        self.frame3 = tk.Frame(self.frame, width=10)
        self.frame3.grid(row=10, column=1, sticky="w")
        self.r1secstr = tk.Radiobutton(self.frame3, text="helix", variable=self.var3, value="helix", command=None)
        self.r1secstr.grid(row=0, column=0)
        self.r2secstr = tk.Radiobutton(self.frame3, text="beta", variable=self.var3, value="beta", command=None)
        self.r2secstr.grid(row=0, column=1)
        self.r3secstr = tk.Radiobutton(self.frame3, text="loop", variable=self.var3, value="loop", command=None)
        self.r3secstr.grid(row=0, column=2)
        self.r4secstr = tk.Radiobutton(self.frame3, text="IR (Ig20)", variable=self.var3, value="ID", command=None)
        self.r4secstr.grid(row=0, column=3)

        # SAP and malign prediction entry fields
        self.SAPlabel = tk.Label(self.frame, text="Spatial-aggregation-Propensity score, SAP")
        self.SAPlabel.grid(row=11, column=0, sticky="e")
        self.SAPentry = tk.Entry(self.frame)
        entryids.append(self.SAPentry)
        self.SAPentry.grid(row=11, column=1, sticky="w")

        #posttranslationalmodification entry field

        self.Phosphositeinfo = tk.Label(self.frame, text="Found posttranslational modification sites")
        self.Phosphositeinfo.grid(row=12, column=0, sticky="e")
        self.phosphosites_entry = tk.Entry(self.frame, width=50)
        self.phosphosites_entry.grid(row=12, column=1, sticky="w")

        #additional info about binding partners etc
        """This block should contain information about known binding partners or other relevant information"""

        self.additionalinfo = tk.Label(self.frame, text="Additional information")
        self.additionalinfo.grid(row=13, column=0, sticky="e")
        self.addinfoentry = tk.Entry(self.frame, width=50)
        self.addinfoentry.grid(row=13, column=1, sticky="w")


        #for hits in intro_form.phosphohits:
        #    print(hits)


        # buttons for submission
        self.frame5 = tk.Frame(self.frame)
        self.frame5.grid(row=14, column=0,columnspan=3, pady= 10)

        #self.clearbtn = tk.Button(self.frame5, text="Clear", command=self.clear_bn, borderwidth=4, width=10)
        #self.clearbtn.grid(row=1, column=5, sticky="we")

        #self.subbutnlbl = tk.Label(self.frame5, text="")
        #self.subbutnlbl.grid(row=1, column=0, ipadx=10)

        #self.subbtn = tk.Button(self.frame5, text="Generate \n template file", relief="ridge",
        #                        borderwidth=4, command=self.outfile_handler_weka, bg="blue", fg="white")
        #self.subbtn.grid(row=1, column=2, sticky="wnse")
        #self.addmut = tk.Button(self.frame5, text="Add mutations",
        #                        command=self.add_mutants, borderwidth=4)
        #self.addmut.grid(row=1, column=5)

        #self.mut_info = tk.Button(self.frame5, text="Get mutations ids",
        #                        command=lambda: self.mut_ids(mutation_ids), borderwidth=4)
        #self.mut_info.grid(row=1, column=6, pady=10)
        self.tutbutton = tk.Button(self.frame5, text="Read Tutorial", command=self.manual, borderwidth=4, width=15)
        self.tutbutton.grid(row=1,column=0, sticky="we")

        self.phosphoinfoadd = tk.Button(self.frame5, text="Inspect Phospholibrary", command=self.phosphoinfoadder, borderwidth=4)
        self.phosphoinfoadd.grid(row=1,column=1, sticky="we")

        self.bindinginfoadd = tk.Button(self.frame5, text="Inspect Bindinglibrary", command=self.bindinginfoadder, borderwidth=4)
        self.bindinginfoadd.grid(row=1, column=2, sticky="nwes")

        """Start WEKA related stuff"""

        #self.infoline = tk.Label(self.frame5, text="--------------------------------------------------  WEKA-Prediction  "
        #                                           "-----------------------------------------------------",font="Arial 12 bold")
        #self.infoline.grid(row=2, column=0, columnspan=7, pady=(20,0))

        self.extndinfo = tk.Label(self.frame5, text="Eibe Frank, Mark A. Hall, and Ian H. Witten (2016).\n The WEKA Workbench. "
                                                    "Online Appendix for 'Data Mining: Practical Machine Learning Tools and Techniques',\n Morgan Kaufmann, Fourth Edition, 2016.")
        self.extndinfo.config(font="Helvetica 8")
        self.extndinfo.grid(row=3, column=0, columnspan=7)


        #buttons to make weka predictions

        self.frame6 = tk.Frame(self.frame)
        self.frame6.grid(row = 0, column=0, pady=(20,50), columnspan=4)

        #self.frame6_1 = tk.Frame(self.frame)
        #self.frame6_1.grid(row=15, column=0, pady=(10,60), columnspan=5)

        #self.wekalbl = tk.Label(self.frame6, text="Here will be the weka stuff / placeholder")
        #self.wekalbl.grid(row=1, column=1, pady=20, sticky="w")

        #self.wekabtn = tk.Button(self.frame5, text="Prediction on\n pathogenicity", borderwidth=4, bg="red", fg="white",
        #                         relief="ridge", command=self.wekaprediction)
        #self.wekabtn.grid(row=3, column=0, columnspan=1, ipady=1, sticky="we")
        #self.wekabtntrainset = tk.Button(self.frame6_1, text="Trainingset info", borderwidth=4, command=self.trainingsetdetails)
        #self.wekabtntrainset.grid(row=3, column=1, sticky="we")
        self.wekabtnmutantpdb = tk.Button(self.frame5, text="Clear", borderwidth=4, command=self.fullclear)
        self.wekabtnmutantpdb.grid(row=1, column=5, sticky="we")
        self.wekabtnoutputfile = tk.Button(self.frame5, text="Save mutation prediction", borderwidth=4, command=self.outputfilemutant)
        self.wekabtnoutputfile.grid(row=1, column=4, sticky="we")
        self.exitamiva = tk.Button(self.frame5, text="Exit AMIVA-F", command=self.exiting_amiva, borderwidth=4)
        self.exitamiva.grid(row=1, column=6, sticky="we")


        #self.wekaentrytag = tk.Label(self.frame6, text="WEKA-Output", font="Helvetica 13")
        #self.wekaentrytag.grid(row=5, column=0)
        self.wekaentryid = tk.Entry(self.frame6, width=10)
        self.wekaentryid.grid(row=1, column=1, sticky="nsew", ipady=6)
        self.wekaentrydomaininfo = tk.Entry(self.frame6, width=10)
        self.wekaentrydomaininfo.grid(row=1, column=2, sticky="nsew")
        self.wekaentrydis = tk.Entry(self.frame6, width=15)
        self.wekaentrydis.grid(row=1, column=3, sticky="nswe")
        #self.wekaentryconf = tk.Entry(self.frame6, width=5)
        #self.wekaentryconf.grid(row=5, column=4, sticky="nsew")

        self.wekaentryidlbl = tk.Label(self.frame6, text="mutation", font="Helvetica 16")
        self.wekaentryidlbl.grid(row=0, column=1, pady=(0,0))
        self.wekaentrydomainlbl = tk.Label(self.frame6, text="domain", font="Helvetica 16")
        self.wekaentrydomainlbl.grid(row=0, column=2, pady=(0, 0))
        self.wekaentrydiseaselbl = tk.Label(self.frame6, text="pathogenicity", font="Helvetica 16")
        self.wekaentrydiseaselbl.grid(row=0, column=3, pady=(0, 0))
        #self.wekaentryconflbl = tk.Label(self.frame6, text="confidence", font="Helvetica 13")
        #self.wekaentryconflbl.grid(row=4, column=4, pady=(20, 0))


        #self.wekaexplainlbl = tk.Label(self.frame6, text="The predicted outcome and its associated confidence\n of your submitted mutation are:")
        #self.wekaexplainlbl.grid(row=4, column=0, sticky="w")

    def phosphoinfoadder(self):
        window = tk.Toplevel(root)
        window.title("Annotated Phosphosites")
        s = tk.Scrollbar(window)
        exp = tk.Text(window, width=100, height=30)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        exp.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=exp.yview)
        exp.config(yscrollcommand=s.set)
        with open("./Posttranslational_modifications_and_binding_partners/Posttranslational_modification_list.txt") as fh_phos:
            phosphoinfo = fh_phos.readlines()
            for lines in phosphoinfo:
                exp.insert(tk.END, lines)

    def bindinginfoadder(self):
        window = tk.Toplevel(root)
        window.title("Annotated Bindingpartners")
        s = tk.Scrollbar(window)
        exp = tk.Text(window, width=100, height=30)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        exp.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=exp.yview)
        exp.config(yscrollcommand=s.set)
        with open(
                "./Posttranslational_modifications_and_binding_partners/Binding_partners_list.txt") as fh_binders:
            bindinginfo = fh_binders.readlines()
            for lines in bindinginfo:
                exp.insert(tk.END, lines)

    def manual(self):
        window = tk.Toplevel(root)
        window.title("Manual for AMIVA-F")
        s = tk.Scrollbar(window)
        exp = tk.Text(window, width=150, height=100)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        exp.pack(side=tk.LEFT, fill=tk.Y)
        s.config(command=exp.yview)
        exp.config(yscrollcommand=s.set)
        with open("./WEKA_associated_files/AMIVA-F_tutorial.txt") as fhtut:
            texttutorial = fhtut.readlines()
            for lines in texttutorial:
                exp.insert(tk.END, lines)

    def clearweka(self):
        self.wekaentryid.delete(0, tk.END)
        self.wekaentrydomaininfo.delete(0, tk.END)
        self.wekaentrydis.delete(0, tk.END)
        #entry_form.clear_btn()
        #self.wekaentryconf.delete(0, tk.END)


    def fullclear(self):
        self.wekaentryid.delete(0, tk.END)
        self.wekaentrydomaininfo.delete(0, tk.END)
        self.wekaentrydis.delete(0, tk.END)
        entry_form.clear_btn()
        intro_form.button.config(bg="blue")
        intro_form.pb["value"] = 0

    def wekaprediction(self):
        """Here we will do the wekabridging and the prediction for the mutations"""
        jvm.start()
        intro_form.pb["value"] += 20
        intro_form.pb.update_idletasks()

        self.clearweka()   #remove old stuff before new entries
        falsepredict = False    #if everything is fine this will stay false and we make a normal prediction

        selfchecker = intro_form.entry1.get()  #if the first aa is the exact same as the last its obviously not pathogenic. we need to specify this case because we dont cover this case in our training set

        try:
            if intro_form.entry1.get() == "":
                messagebox.showerror("No mutation specified above",
                                 "You first need to fill out the form above!\nPlease specify the mutation of choice above the green button")
                falsepredict = True   #if the entryfield is empty we dont show a prediction
        except:
            print(intro_form.entry1.get())


        data_dir = r"./WEKA_associated_files"
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file(data_dir + "/AMIVA_trainingset.arff")
        data.class_is_last()          #what we want to predict is last column
        testmutant = loader.load_file(data_dir + "/mutation_to_be_predicted.arff")
        testmutant.class_is_last()

        cls = Classifier(classname="weka.classifiers.functions.MultilayerPerceptron", options=["-L", "0.78", "-M", "0.2", "-N", "517", "-V", "0", "-S", "0", "-E", "20", "-H",
                                  "a,2,3", "-resume"])
    # print(cls.to_commandline())              # looks good
        cls.build_classifier(data)                 #training dataset used here (n=173)
    # print(cls)    #looks good as well. shows weights for each node
        evl = Evaluation(data)
        evl.crossvalidate_model(cls, data, 10, Random(1))
        #print(evl.percent_correct)          #we can show this for interested users in a separate window?
        global evl_summary
        evl_summary = evl.summary()
        global evl_class_details
        evl_class_details = evl.class_details()
        prediction_disease_dict = {}
        for index, inst in enumerate(testmutant):
            pred = cls.classify_instance(inst)
            dist = cls.distribution_for_instance(inst)
            resultconf =dist.tolist()
            prediction_disease_dict[inst.class_attribute.value(int(pred))] = resultconf[1]

        intro_form.pb["value"] += 20
        intro_form.pb.update_idletasks()

        #self.clear_btn()     #if something old is still there, remove it now
        #print("The prediction for your submitted mutation and its associated confidence are:")

        # collecting variables for later output file
        global parameterlist
        parameterlist = []  # we fill this list with the precalculated parameters
        parameterlist.append(intro_form.entry1.get())
        for userinput in entryids[0:-1]:
            if userinput.get() == "":
                parameterlist.append("?")
            else:
                parameterlist.append(userinput.get())

        parameterlist.append(self.var.get())
        parameterlist.append(self.var1.get())
        parameterlist.append(self.var2.get())
        parameterlist.append(self.var3.get())
        if self.SAPentry.get() == "":
            parameterlist.append("?")
        else:
            parameterlist.append(self.SAPentry.get())
        parameterlist.append(self.phosphosites_entry.get())
        parameterlist.append(self.addinfoentry.get())

        for keys, values in prediction_disease_dict.items():
            if keys == "yes":
                self.wekaentrydis.insert(0, "disease related")
                #self.wekaentryconf.insert(0, round(values,2))
                self.wekaentrydis.config(foreground="red", font="Helvetica 18 bold")
                #self.wekaentryconf.config(font="Helvetica 18")
                self.wekaentryid.insert(0, parameterlist[0])
                self.wekaentryid.config(font="Helvetica 18")
                self.wekaentrydomaininfo.insert(0, domaininfo)
                self.wekaentrydomaininfo.config(font="Helvetica 18")
                intro_form.button.config(bg="red")
            else:
                self.wekaentrydis.insert(0, "neutral/benign")
                #self.wekaentryconf.insert(0, round(values,2))
                #self.wekaentryconf.config(font="Helvetica 18 bold")
                self.wekaentrydis.config(foreground="green", font="Helvetica 18 bold")
                self.wekaentryid.insert(0, parameterlist[0])
                self.wekaentryid.config(font="Helvetica 18")
                self.wekaentrydomaininfo.insert(0,domaininfo)
                self.wekaentrydomaininfo.config(font="Helvetica 18")
                intro_form.button.config(bg="green")

        if falsepredict == True:     #with wrong inputs we just clear random stuff that make no sense.
            self.clearweka()

        if selfchecker[0] == selfchecker[-1]:      #if wildtype aa is mutated aa they are obviously non pathogenic... this case is although not covered in our trainingset.. we thereby specify it here.
            self.clearweka()
            messagebox.showinfo("No mutation inserted", "The specified mutation is the same as wildtype.")
            self.wekaentrydis.insert(0, "benign")
            # self.wekaentryconf.insert(0, round(values,2))
            # self.wekaentryconf.config(font="Helvetica 18 bold")
            self.wekaentrydis.config(foreground="green", font="Helvetica 18 bold")
            self.wekaentryid.insert(0, parameterlist[0])
            self.wekaentryid.config(font="Helvetica 18")
            self.wekaentrydomaininfo.insert(0, domaininfo)
            self.wekaentrydomaininfo.config(font="Helvetica 18")

        intro_form.pb["value"] = 0
        intro_form.pb.update_idletasks()

        #intro_form.pb.grid_forget()
        #self.wekatxt = tk.Label(self.frame6, text=intro_form.entry1.get())
        #self.wekatxt.grid(row=1, column=2, sticky="w")

        #jvm.stop()

    def outputfilemutant(self):
        """Write an outfile that contains the calculated values and their associated predictions together with the
        corresponding labels that identify the calculated values"""

        attributeshown = ["Mutation of interest" ,"Absolute SASA mutant",
                          "Absolute SASA wildtype",
                          "Relative SASA wildtype", "Relative SASA mutant", "Δ Number of atoms",
                          "Δ Hydrophobicity",
                          "Δ Accessibility (upon mutation)",
                          "Clashes AND/OR binding partner interference AND/OR phosphosite",
                          "Sidechain_orientation", "Secondary structure", "SAP score per residue", "posttranslational modifciation sites (8A cutoff)",
                          "binding partners (8A cutoff)"]
        lstmerge = []

        mutfilename = self.wekaentryid.get()
        savedir = filedialog.askdirectory()
        dirtarget = savedir + "/" + mutfilename + ".txt"
        with open(dirtarget, "w", encoding="utf-8") as mutfh:
            for parameters in parameterlist:          #we will fill the parameters obtained to this new list (redundant work)
                lstmerge.append(parameters)
            #lstmerge.append(self.phosphosites_entry.get())

            mutfh.write("AMIVA-F analysis of mutations in variants of human Filamin C\n\n")
            mutfh.write("The following attributes and associated values were used to obtain the prediction:\n\n")
            mergedlists = zip(lstmerge, attributeshown)
            for a, b in mergedlists:                #attributelabel and associated values
                mutfh.write(str(b))
                mutfh.write("\t")
                mutfh.write(str(a))
                mutfh.write("\n")



            mutfh.write("\nThe mutation of interest and its prediction:\n\n")
            mutfh.write("----------------------------------------------------------\n")
            mutfh.write((str(self.wekaentryid.get()) + "\t" + self.wekaentrydomaininfo.get() + "\t"  + self.wekaentrydis.get() ))
            mutfh.write(
                "\n----------------------------------------------------------")
            mutfh.write("\n\n")


            mutfh.write("\nInformation about the data used to train the algorithm:\n\n")
            data_dir = r"./WEKA_associated_files"
            loader = Loader(classname="weka.core.converters.ArffLoader")
            data = loader.load_file(data_dir + "/AMIVA_trainingset.arff")
            data.class_is_last()
            cls = Classifier(classname="weka.classifiers.functions.MultilayerPerceptron",
                             options=["-L", "0.78", "-M", "0.2", "-N", "517", "-V", "0", "-S", "0", "-E", "20", "-H",
                                      "a,2,3", "-resume"])
            # print(cls.to_commandline())              # looks good
            cls.build_classifier(data)  # training dataset used here (n=173)
            evl = Evaluation(data)
            evl.crossvalidate_model(cls, data, 10, Random(3))
            evl_summary = evl.summary()
            evl_class_details = evl.class_details()
            conf_matrix = evl.confusion_matrix

            mutfh.write("\n")
            mutfh.write(str(evl_summary))
            mutfh.write("\n")
            mutfh.write(str(evl_class_details))

    def exiting_amiva(self):
        result = messagebox.askquestion("Exit", "Do you really want to quit AMIVA-?")
        if result == "yes":
            root.destroy()
            jvm.stop()



    def trainingsetdetails(self):#
        window2 = tk.Toplevel(root)
        window2.title("Infos about the unterlying trainingdataset")
        scrollbar1 = tk.Scrollbar(window2)
        exp1 = tk.Text(window2, width=100, height=30)
        scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
        exp1.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar1.config(command=exp1.yview)
        exp1.config(yscrollcommand=scrollbar1.set)

        jvm.start()
        data_dir = r"./WEKA_associated_files"
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file(data_dir + "/AMIVA_trainingset.arff")
        data.class_is_last()
        cls = Classifier(classname="weka.classifiers.functions.MultilayerPerceptron",
                         options=["-L", "0.78", "-M", "0.2", "-N", "517", "-V", "0", "-S", "0", "-E", "20", "-H",
                                  "a,2,3", "-resume"])
        # print(cls.to_commandline())              # looks good
        cls.build_classifier(data)  # training dataset used here (n=173)
        evl = Evaluation(data)
        evl.crossvalidate_model(cls, data, 10, Random(0))
        evl_summary = evl.summary()
        evl_class_details = evl.class_details()


        exp1.insert(tk.END, (evl_summary + "\n" + evl_class_details))
        window2.mainloop()


    def retriever(self, entryids):
        for entries in entryids:
            print(entries.get())

    def mut_ids(self, mutation_ids):
        """print input of calculated stuff , id of mutation"""
        with open("mutations_ordered_list.txt","a") as outfileids:
            for entries in mutation_ids:
                outfileids.write((entries + "\n"))



    def clear_btn(self):
        for entries in entryids:
            entries.delete(0,"end")
        entry_form.var.set(1)
        entry_form.var1.set(1)
        entry_form.var2.set(1)
        entry_form.var3.set(1)
        self.phosphosites_entry.delete(0,"end")
        del intro_form.phosphohits       #removal of hits and opening of empty list
        intro_form.phosphohits = []      #new empty list for next round of mutations
        self.addinfoentry.delete(0,"end")
        intro_form.entry1.delete(0,"end")
        entry_form.r3sidechain.configure(state="normal")
        entry_form.r4secstr.configure(state="normal")

    def outfile_handler_weka(self):
        """direct prep for weka utilization"""

        attributelst = ["Absolute_SASA_mutant(A**2)",
                        "Absolute_SASA_wt(A**2)",
                        "relative_SASA_wt", "relative_SASA_mutant", "'delta_number_of_atoms(mutant- wt)'",
                        "'dhydrophobicity(mutant - wt)'",
                        "'change accessibility(upon mutation)'",
                        "'clashes AND/OR binding partner interference AND/OR phosphosite'",
                        "sidechain_orientation", "secondary_structure", "SAP_score_average_per_residue", "malign"]

        typelst = ["numeric", "numeric", "{accessible,partially,inaccessible}",
                   "{accessible,inaccessible,partially}", "numeric", "numeric", "{no,better,worse}", "{no,yes}",
                   "{solvent,beta}", "{beta,loop,helix,ID}", "numeric", "{no,yes}"]

        with open("./WEKA_associated_files/mutation_to_be_predicted.arff", "w") as outfile1:
            outfile1.write(("@relation" + " mutation_to_be_predicted\n\n"))
            i = 0
            for entries in attributelst:
                outfile1.write("@attribute " + entries + " " + typelst[i] + "\n")
                i += 1
            outfile1.write("\n")
            outfile1.write("@data\n")
            for userinput in entryids[0:-1]:  #exclude SAP
                if userinput.get() == "":
                    outfile1.write("?" + ",")
                    continue
                outfile1.write((str(userinput.get()) + ","))
            outfile1.write(self.var.get())
            outfile1.write(",")
            outfile1.write(self.var1.get())
            outfile1.write(",")
            outfile1.write(self.var2.get())
            outfile1.write(",")
            outfile1.write(self.var3.get())
            outfile1.write(",")
            if self.SAPentry.get() == "":
                outfile1.write("?" + "," + "?")
            else:
                outfile1.write(self.SAPentry.get())
                outfile1.write(",")
                outfile1.write("?")

        self.wekaprediction()


    def add_mutants(self):
        """This function will add additional mutations to the file of to be predicted mutants"""
        with open("./mutation_to_be_predicted.arff", "a") as outfile1:
            outfile1.write("\n")
            for userinput in entryids[0:-1]:
                print(userinput.get())
                if userinput.get() == "":
                    outfile1.write("?" + ",")
                    continue
                outfile1.write((str(userinput.get()) + ","))
            outfile1.write(self.var.get())
            outfile1.write(",")
            outfile1.write(self.var1.get())
            outfile1.write(",")
            outfile1.write(self.var2.get())
            outfile1.write(",")
            outfile1.write(self.var3.get())
            outfile1.write(",")
            if self.SAPentry.get() == "":
                outfile1.write("?" + "," + "?")
            else:
                outfile1.write(self.SAPentry.get())
                outfile1.write(",")
                outfile1.write("?")


root = tk.Tk()
#root.geometry("700x900")
trial = GUI(root)
intro_form = Entry_formular(root)
entry_form = Entryfield(root)

root.mainloop()
