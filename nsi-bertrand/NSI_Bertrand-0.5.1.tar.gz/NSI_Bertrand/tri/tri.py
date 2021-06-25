__all__ = [
    "est_triee",
    "bulles",
    "insertion",
    "selection_min",
    "fusion",
    "pivot",
    "comptage",
]


def est_triee(l):
    """ Vérifie si un liste est triée

    :param l: une liste de nombre

    :return: True si la liste est triée, False sinon

    :example:
    >>> est_triee([1, 2, 5, 6])
    True
    >>> est_triee([1, 2, 6, 5])
    False
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def bulles(l):
    """ Trie la liste avec la méthode du tri à bulles

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> bulles([1, 2, 6, 5])
    [1, 2, 5, 6]

    """
    tab = l[:]
    n = len(tab)
    for i in range(n):
        for j in range(n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


def _insert(elem, tab):
    if len(tab) == 0:
        return [elem]
    if tab[0] > elem:
        return [elem] + tab
    return [tab[0]] + _insert(elem, tab[1:])


def insertion(tab):
    """ Trie la liste avec la méthode du tri par insertion

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> insertion([1, 2, 6, 5])
    [1, 2, 5, 6]
    """
    ordered_tab = []
    for i in tab:
        ordered_tab = _insert(i, ordered_tab)
    return ordered_tab


def _extract_min(tab):
    vmin = tab[0]
    head = []
    stack = []
    for e in tab[1:]:
        if e < vmin:
            head.append(vmin)
            head += stack
            stack = []
            vmin = e
        else:
            stack.append(e)

    return (vmin, head + stack)


def selection_min(tab):
    """ Trie la liste avec la méthode du tri selection du minimum

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> selection_min([1, 2, 6, 5])
    [1, 2, 5, 6]
    """
    ordered = []
    to_order = tab[:]
    while len(to_order):
        vmin, to_order = _extract_min(to_order)
        ordered.append(vmin)
    return ordered


def _fusion(tab1, tab2):
    """ Fusion de deux listes ordonnées


    >>> _fusion([1, 4], [2, 3, 6])
    [1, 2, 3, 4, 6]
    >>> _fusion([2, 3, 6], [1, 4])
    [1, 2, 3, 4, 6]
    >>> _fusion([1], [2])
    [1, 2]
    >>> _fusion([2], [1])
    [1, 2]
    """
    i = 0
    j = 0
    l_tab1 = len(tab1)
    l_tab2 = len(tab2)
    fusionned = []

    while i < l_tab1 and j < l_tab2:
        if tab1[i] < tab2[j]:
            fusionned.append(tab1[i])
            i += 1
        else:
            fusionned.append(tab2[j])
            j += 1

    if i == len(tab1):
        fusionned += tab2[j:]
    if j == len(tab2):
        fusionned += tab1[i:]
    return fusionned


def fusion(tab):
    """ Trie la liste avec la méthode du tri par fusion

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> fusion([1, 2, 6, 5])
    [1, 2, 5, 6]
    """
    if len(tab) == 1:
        return tab
    middle = len(tab) // 2
    ans = _fusion(fusion(tab[middle:]), fusion(tab[:middle]))
    return ans


def pivot(tab):
    """ Trie la liste avec la méthode du tri par pivot

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> pivot([1, 2, 6, 5])
    [1, 2, 5, 6]
    """
    if len(tab) <= 1:
        return tab
    _pivot = tab[-1]
    bigger = []
    smaller = []
    for i in tab[:-1]:
        if i > _pivot:
            bigger.append(i)
        else:
            smaller.append(i)
    return pivot(smaller) + [_pivot] + pivot(bigger)


def comptage(L):
    """ Trie la liste avec la méthode du tri par comptage

    :param l: Un tableau de nombre
    :return: une copie de la liste triée

    >>> comptage([1, 2, 6, 5])
    [1, 2, 5, 6]
    """
    vmin = min(L)
    vmax = max(L)
    hist = [0 for _ in range(vmin, vmax + 1)]
    for l in L:
        hist[l - vmin] += 1

    ans = []
    for i, v in enumerate(hist):
        ans += [i+vmin] * v
    return ans
