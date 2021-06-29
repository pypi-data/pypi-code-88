import os, sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def str_liste(liste, sep1 = ", ", sep2 = " et ", begin = "", end = ""):
    str_ = sep1.join([str(e) for e in liste[:-1]])
    if len(liste)>1:
        str_ = sep2.join([str_, str(liste[-1])])
    else:
        str_ = str(liste[0])
    return "".join([begin, str_, end])

def str_liste_de_listes(liste_de_listes, 
    sep11 = ", ", sep12 = " et ", begin1 = "", end1 = "", 
    sep21 = ", ", sep22 = " et ", begin2 = "(", end2 = ")"
    ):
        liste_str = []
        for liste in liste_de_listes:
            liste_str.append(str_liste(liste, sep21, sep22, begin2, end2))
        return str_liste(liste_str, sep11, sep12, begin1, end1)
                
def print_liste(liste, sep1 = ", ", sep2 = " et ", begin = "", end = ""):
    print(str_liste(liste, sep1, sep2, begin, end))

def print_liste_de_listes(liste_de_listes, 
    sep11 = ", ", sep12 = " et ", begin1 = "", end1 = "", 
    sep21 = ", ", sep22 = " et ", begin2 = "(", end2 = ")"
    ):
    print(str_liste_de_listes(liste_de_listes, sep11, sep12, begin1, end1, sep21, sep22, begin2, end2))

def lister_test(liste, fonction_test, cle_de_tri):
    liste_test = []
    for e in liste:
        if fonction_test(e):
            if e not in liste_test:
                liste_test.append(e)
    liste_test.sort(key = cle_de_tri)
    return liste_test

def lister_paires_test(liste, fonction_test, cle_de_tri_1, cle_de_tri_2):
    liste_paires_test = []
    for e1 in liste:
        for e2 in liste:
            if e1 != e2:
                if fonction_test(e1, e2):
                    if [e1, e2] not in liste_paires_test and [e2, e1] not in liste_paires_test:
                        p = [e1, e2]
                        p.sort(key = cle_de_tri_2)
                        liste_paires_test.append(p)
    liste_paires_test.sort(key = cle_de_tri_1)
    return liste_paires_test

def periodiser(N, vecteur_y_periode):
    Nperiode = len(vecteur_y_periode)
    Pperiodes = int(np.ceil(N/Nperiode))
    return np.concatenate([vecteur_y_periode]*Pperiodes)[0:N]

def analyser_kwargs(kwargs, nom_variable, fonction_test, valeur_par_defaut):
    valeur = kwargs.get(nom_variable, None)
    if nom_variable in kwargs:
        valeur = kwargs.get(nom_variable)
        del kwargs[nom_variable]
        test = True
    else:
        valeur = valeur_par_defaut
        test = False

    if not fonction_test(valeur):
        print("Erreur dans l'analyse de arguments {0} = {1} est impossible".format(nom_variable, valeur))
        sys.exit()
    return valeur, test

def analyser_args(args, nom_variable, fonction_test, valeur_par_defaut):
    if len(args) > 0:
        valeur = args.pop(0)
        test = True
    else:
        valeur = valeur_par_defaut
        test = False

    if not fonction_test(valeur):
        print("Erreur dans l'analyse de arguments {0} = {1} est impossible".format(nom_variable, valeur))
        sys.exit()
    return valeur, test

def analyser_args_kwargs(args, kwargs, nom_variable, fonction_test, valeur_par_defaut):
    valeur_args, test_args = analyser_args(args, nom_variable, fonction_test, valeur_par_defaut)
    valeur_kwargs, test_kwargs = analyser_kwargs(kwargs, nom_variable, fonction_test, valeur_par_defaut)
    if test_args == test_kwargs == True:
        print("Erreur dans l'analyse de arguments {0} est défini deux fois".format(nom_variable))
        sys.exit()
    elif test_kwargs:
        return valeur_kwargs
    else:
        return valeur_args

def tester_ux(ux):
    axe = plt.gca()
    try:
        if ux != axe.ux:
            return False
    except:
        axe.ux = ux
    return True

def tester_uy(uy):
    axe = plt.gca()
    try:
        if uy != axe.uy:
            return False
    except:
        axe.uy = uy
    return True


def tester_unite_axe(unite = "", axe = "x"):
    axe_ref = plt.gca()
    try:
        liste_unites = axe_ref.liste_unites
    except:
        liste_unites = axe_ref.liste_unites = [None, None]
    indice_unite_a_tester = 0 if axe == "x" else 1
    
    test = liste_unites[indice_unite_a_tester] == None or liste_unites[indice_unite_a_tester] == unite
    if not test:
        return False
    liste_unites[indice_unite_a_tester] = unite
    return True

def calculer_vecteur_dB(vecteur_entree, dBmin = -100):
    vecteur_sortie = np.abs(vecteur_entree)
    minus = 10**(dBmin/20)
    vecteur_sortie = np.clip(vecteur_sortie, minus, max(np.max(vecteur_sortie), minus))
    return 20*np.log10(vecteur_sortie)


if __name__ == "__main__":
    v = np.linspace(0,10, 100)
    print(calculer_vecteur_dB(v, dBmin = -100))
    
    # bdt = AxeXBase([0,1], 1e-3)

    # N = 4
    # liste = []
    # for i in range(N):
    #     liste.append(SignalBase(bdt))

    # print(str_liste(liste, begin = "(", end = ")"))
    # N1, N2 = 3, 2
    # liste_de_listes = []
    # for i in range(N1):
    #     liste = []
    #     for i in range(N2):
    #         liste.append(SignalBase(bdt))
    #     liste_de_listes.append(liste)

    # print(str_liste_de_listes(liste_de_listes))

    # args = []#["zorro", 2, AxeXBase([0,1], 1e-3)]
    # kwargs = {}
    # kwargs["arg1"] = "bidon"

    # print(analyser_args_kwargs(args, kwargs, "arg1", lambda x: isinstance(x, str), "superman"))