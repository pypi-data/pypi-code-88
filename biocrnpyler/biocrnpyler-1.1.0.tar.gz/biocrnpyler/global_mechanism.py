
#  Copyright (c) 2020, Build-A-Cell. All rights reserved.
#  See LICENSE file in the project root directory for details.

from typing import Dict, List
from warnings import warn

from .mechanism import Mechanism
from .mechanisms_enzyme import MichaelisMenten
from .reaction import Reaction
from .species import ComplexSpecies, OrderedPolymerSpecies, Species

"""
Global mechanisms are a lot like mechanisms. They are called only by mixtures
 on a list of all species have been generated by components. Global mechanisms are meant
 to work as universal mechanisms that function on each species or all species of some
 type or with some attribute. Global mechanisms may only act on one species at a time.

In order to decide which species a global mechanism acts upon, the filter_dict is used.
      filter_dict[species.material_type / specie.attributes / species.name / repr(species)] = True / False
 For each species, its material type, name, and attributes are sent through the filter_dict. If True
 is returned, the GlobalMechanism will act on the species. If False is returned, the
 the GlobalMechanism will not be called. If there are conflicts in the filter_dict, an error is raised.

If the species's name, material type, and attributes are all not in the filter_dict, the GlobalMechanism will
 be called if default_on == True and not called if default_on == False.
Note that the above filtering is done automatically. Any parameters needed by the global mechanism must be
 in the Mixture's parameter dictionary. These methods are assumed to take a single species
 as input.

An example of a global mechanism is degradation via dilution which is demonstrated in the Tests folder.

GlobalMechanisms should be used cautiously or avoided alltogether - the order in which they are called
may have to be carefully user defined in the subclasses of Mixture in order to ensure expected behavior.
"""


class GlobalMechanism(Mechanism):
    """Global mechanisms are a lot like mechanisms. They are called only by mixtures
    on a list of all species have been generated by components. Global mechanisms
    are meant to work as universal mechanisms that function on each species or
    all species of some material type or with some attribute. Global mechanisms
    may only act on one species at a time.

    In order to decide which species a global mechanism acts upon, the filter_dict
    is used.

    An example of a global mechanism is degradation via dilution which is
    demonstrated in the Tests folder.

    GlobalMechanisms should be used cautiously or avoided alltogether - the order
    in which they are called may have to be carefully user-defined in the
    subclasses of Mixture in order to ensure expected behavior.
    """
    def __init__(self, name: str, mechanism_type: str="", filter_dict: Dict=None,
                 default_on: bool=False, recursive_species_filtering: bool=False):
        """Creates a GlobalMechanisms instance.

        If the species's name, material type, and attributes are all not in the
        filter_dict, the GlobalMechanism will be called if default_on == True and
        not called if default_on == False.

        :param name: name of the GlobalMechanism
        :param mechanism_type:
        :param filter_dict: filter_dict[species.material_type / species.attributes] = True / False
         For each species, its material type or attributes are sent through the
        filter_dict. If True is returned, the GlobalMechanism will act on the
        species. If False is returned, the the GlobalMechanism will not be called.
        If filter_dict[attribute] is different from filter_dict[material_type],
        filter_dict[attribute] takes precedent. If multiple filter_dict[attribute]
        contradict for different attributes, an error is raised.
        Note that the above filtering is done automatically. Any parameters needed by
        the global mechanism must be in the Mixture's parameter dictionary. These
        methods are assumed to take a single species as input.
        :param default_on: what to do if a species doesn't come up in the filter dict. Also used for as the default if there is a filterdict conflict
        :param recursive_species_filtering:  keyword determines how the material_type and name of ComplexSpecies is defined.
        If True: the filter based upon all subspecies.type and name recursively going through
        all ComplexSpecies. If False: the filter dict will act only on the ComplexSpecies. By default, this is False.
        """
        if filter_dict is None:
            self.filter_dict = {}
        else:
            self.filter_dict = filter_dict

        self.default_on = default_on
        self.recursive_species_filtering = recursive_species_filtering
        Mechanism.__init__(self, name=name, mechanism_type=mechanism_type)

    def apply_filter(self, s: Species):
        """applies the filter dictionary to determine if a global mechanism acts on a species.

        :param s: Species
        :return:
        """
        fd = self.filter_dict
        use_mechanism = None
        species_list = s.get_species(recursive=self.recursive_species_filtering)
        for subs in species_list:
            for a in subs.attributes+[subs.material_type, subs.name]:
                if a in fd:
                    if use_mechanism is None:
                        use_mechanism = fd[a]
                    elif use_mechanism != fd[a]:
                        warn(f"species {repr(s)} has multiple attributes(or material type) which conflict with global mechanism filter {repr(self)}. Using default value {self.default_on}.")
                        use_mechanism = self.default_on

        if use_mechanism is None:
            use_mechanism = self.default_on
        return use_mechanism

    def update_species_global(self, species_list: List[Species], mixture):
        new_species = []
        for s in species_list:
            use_mechanism = self.apply_filter(s)
            if use_mechanism:
                new_species += self.update_species(s, mixture)
        return new_species

    def update_reactions_global(self, species_list: List[Species], mixture):
        fd = self.filter_dict
        new_reactions = []
        for s in species_list:
            use_mechanism = self.apply_filter(s)
            if use_mechanism:
                new_reactions += self.update_reactions(s, mixture)

        return new_reactions

    def get_parameter(self, species, param_name, mixture):
        param = mixture.get_parameter(mechanism = self, part_id = repr(species), param_name = param_name)
        if param is None:
            raise ValueError("No parameters can be found that match the "
                 "(mechanism, part_id, "
                f"param_name)=({repr(self)}, {repr(species)}, "
                f"{param_name}).")
        else:
            return param

    def update_species(self, s: Species, mixture):
        """All global mechanisms must use update_species functions with these inputs.

        :param s: Species instance
        :return:
        """
        return []

    def update_reactions(self, s, mixture):
        """All global mechanisms must use update_reactions functions with these inputs.

        :param s:
        :param mixture:
        :return:
        """
        return []


class Dilution(GlobalMechanism):
    """A global mechanism to represent dilution."""

    def __init__(self, name = "global_degredation_via_dilution",
                 mechanism_type = "dilution", filter_dict=None,
                 default_on = True, recursive_species_filtering = True):
        GlobalMechanism.__init__(self, name = name,
                                 mechanism_type = mechanism_type,
                                 default_on = default_on,
                                 filter_dict = filter_dict,
                                 recursive_species_filtering = recursive_species_filtering)

    def update_reactions(self, s: Species, mixture):
        k_dil = self.get_parameter(s, "kdil", mixture)
        rxn = Reaction.from_massaction(inputs=[s], outputs=[], k_forward=k_dil)
        return [rxn]


class AnitDilutionConstiutiveCreation(GlobalMechanism):
    """Global Mechanism to Constitutively Create Certain Species at the rate of dilution.

    Useful for keeping machinery species like ribosomes and polymerases at a constant concentration.
    """
    def __init__(self, name = "anti_dilution_constiuitive_creation",
                 material_type="dilution", filter_dict=None,
                 default_on = True,  recursive_species_filtering = True):
        GlobalMechanism.__init__(self, name = name,
                                 mechanism_type = material_type,
                                 default_on = default_on,
                                 filter_dict = filter_dict, 
                                 recursive_species_filtering = recursive_species_filtering)

    def update_reactions(self, s, mixture):
        k_dil = self.get_parameter(s, "kdil", mixture)
        rxn = Reaction.from_massaction(inputs=[], outputs=[s], k_forward=k_dil)
        return [rxn]



class Degredation_mRNA_MM(GlobalMechanism, MichaelisMenten):
    """Michaelis Menten mRNA Degredation by Endonucleases
       mRNA + Endo <--> mRNA:Endo --> Endo
       All species of type "rna" are degraded by this mechanisms, including those inside of a ComplexSpecies.
       ComplexSpecies are seperated by this process, including embedded ComplexSpecies. 
       OrderedPolymerSpecies are ignored.
    """
    def __init__(self, nuclease, name="rna_degredation_mm", mechanism_type = "rna_degredation", 
        default_on = False, recursive_species_filtering = True, filter_dict = None, **keywords):

        if isinstance(nuclease, Species):
            self.nuclease = nuclease
        else:
            raise ValueError("'nuclease' must be a Species.")
        MichaelisMenten.__init__(self=self, name=name, mechanism_type = mechanism_type)

        if filter_dict is None:
            filter_dict = {"rna":True, "notdegradable":False}

        GlobalMechanism.__init__(self, name = name, mechanism_type = mechanism_type, default_on = default_on,
                                 filter_dict = filter_dict, recursive_species_filtering = recursive_species_filtering)

    def update_species(self, s, mixture):
        species = []

        #Check if rna species are inside a ComplexSpecies. 
        #If so, break up the ComplexSpecies and degrade the RNA
        if isinstance(s, ComplexSpecies) and s.material_type != "rna" and not isinstance(s, OrderedPolymerSpecies):
            internal_species = s.get_species(recursive = True)
            non_rna_species = [sp for sp in internal_species if sp.material_type != "rna" and sp != s]
            if len(non_rna_species)>0:
                prod = non_rna_species
            else:
                prod = None
            species += MichaelisMenten.update_species(self, Enzyme = self.nuclease, Sub = s, Prod = prod)

        #If the material type is simply RNA, break it up.
        elif s.material_type == "rna":
            species += MichaelisMenten.update_species(self, Enzyme = self.nuclease, Sub = s, Prod = None)
        else:
            #This case includes OrderedPolymerSpecies with RNA inside them and species with RNA in their name (but not mateiral type)
            species = []

        return species

    def update_reactions(self, s, mixture):
        reactions = []

        #Check if rna species are inside a ComplexSpecies. 
        #If so, break up the ComplexSpecies and degrade the RNA

        

        if isinstance(s, ComplexSpecies) and s.material_type != "rna" and not isinstance(s, OrderedPolymerSpecies):
            kdeg = self.get_parameter(s, "kdeg", mixture)
            kb = self.get_parameter(s, "kb", mixture)
            ku = self.get_parameter(s, "ku", mixture)

            internal_species = s.get_species(recursive = True)
            non_rna_species = [sp for sp in internal_species if sp.material_type != "rna" and sp != s]
            if len(non_rna_species)>0:
                prod = non_rna_species
            else:
                prod = None
            reactions += MichaelisMenten.update_reactions(self, Enzyme = self.nuclease, Sub = s, Prod = prod, kb=kb, ku=ku, kcat=kdeg)

        #If the material type is simply RNA, break it up.
        elif s.material_type == "rna":
            kdeg = self.get_parameter(s, "kdeg", mixture)
            kb = self.get_parameter(s, "kb", mixture)
            ku = self.get_parameter(s, "ku", mixture)
            
            reactions += MichaelisMenten.update_reactions(self, Enzyme = self.nuclease, Sub = s, Prod = None, kb=kb, ku=ku, kcat=kdeg)
        else:
            #This case includes OrderedPolymerSpecies with RNA inside them and species with RNA in their name (but not mateiral type)
            reactions = []

        return reactions


class Deg_Tagged_Degredation(GlobalMechanism, MichaelisMenten):
    """Michaelis Menten Degredation of deg-tagged proteins by degredase (such as proteases)
       Species_degtagged + degredase <--> Species_degtagged:degredase --> degredase
       All species with the attribute degtagged and material_type protein are degraded. The method is not recursive.
    """
    def __init__(self, degredase, deg_tag = "degtagged", name="deg_tagged_degredation", mechanism_type="degredation", 
        filter_dict= None, recursive_species_filtering = False, default_on = False, **keywords):
        if isinstance(degredase, Species):
            self.degredase = degredase
        else:
            raise ValueError("'degredase' must be a Species.")
        MichaelisMenten.__init__(self=self, name=name, mechanism_type=mechanism_type)

        if filter_dict is None:
            filter_dict = {deg_tag:True}
            
        GlobalMechanism.__init__(self, name = name, mechanism_type = mechanism_type, default_on = default_on,
                                 filter_dict = filter_dict, recursive_species_filtering = recursive_species_filtering)

    def update_species(self, s, mixture):
        species = []
        species += MichaelisMenten.update_species(self, Enzyme = self.degredase, Sub = s, Prod = None)
        return species

    def update_reactions(self, s, mixture):

        kdeg = self.get_parameter(s, "kdeg", mixture)
        kb = self.get_parameter(s, "kb", mixture)
        ku = self.get_parameter(s, "ku", mixture)

        rxns = []
        rxns += MichaelisMenten.update_reactions(self, Enzyme = self.degredase, Sub = s, Prod = None, kb=kb, ku=ku, kcat=kdeg)
        return rxns
