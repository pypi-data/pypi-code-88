from ..free_module import FreeModuleElement
from ..symmetric import SymmetricGroupElement
from ..symmetric import SymmetricRingElement, SymmetricRing

from ..simplicial import Simplex, SimplicialElement, Simplicial
from ..cubical import CubicalElement, Cubical
from ..utils import pairwise

from itertools import combinations, product, combinations_with_replacement
from operator import itemgetter
from functools import reduce
from math import floor, factorial


class SurjectionElement(FreeModuleElement):

    r"""Element in the surjection operad.

    For a positive integer :math:`r` let :math:`\mathcal X(r)_d` be the free
    :math:`R`-module generated by all functions
    :math:`s : \{1, \dots, d+r\} \to \{1, \dots, r\}` modulo the
    :math:`R`-submodule generated by degenerate functions, i.e., those which
    are either non-surjective or have a pair of equal consecutive values.
    There is a left action of :math:`\mathrm S_r` on :math:`\mathcal X(r)`
    which is up to signs defined on basis elements by
    :math:`\pi \cdot s = \pi \circ s`. We represent a surjection :math:`s` as
    the sequence of its values :math:`\big( s(1), \dots, s(n+r) \big)`. The
    boundary map in this complex is defined up to signs by

    .. math::
        \partial s =
        \sum_{i=1}^{r+d} \pm \big(s(1),\dots,\widehat{s(i)},\dots,s(n+r)\big).

    We refer to [McS] and [BF], where this operad was introduced, for their
    corresponding sign conventions, and to the corresponding methods below for
    the operadic composition and complexity filtration.

    REFERENCES
    ----------
    [McS]: J. McClure, and J. Smith. "Multivariable cochain operations and little
    n-cubes." Journal of the American Mathematical Society 16.3 (2003): 681-704.

    [BF]: C. Berger, and B. Fresse. "Combinatorial operad actions on cochains."
    Mathematical Proceedings of the Cambridge Philosophical Society. Vol. 137.
    No. 1. Cambridge University Press, 2004.

    ATTRIBUTES
    ----------
    convention : :class:`string` 'Berger-Fresse' or 'McClure-Smith'.
        The sign convention used.

    """

    default_convention = 'Berger-Fresse'
    """Class attribute: Used if :attr:`convention` is ``None`` during
        initialization."""

    def __init__(self, data=None, torsion=None, convention=None):
        """
        PARAMETERS
        ----------
        data : :class:`dict` or ``None``, default: ``None``
            Dictionary representing a linear combination of basis elements.
            Items in the dictionary correspond to `basis_element: coefficient`
            pairs. Each basis_element must create a :class:`tuple` of
            :class:`int` and `coefficient` must be an :class:`int`.
        torsion : :class:`int` or :class:`string` 'free', default 'free'
            The torsion of the underlying ring.

        EXAMPLES
        --------
        >>> s = SurjectionElement()
        >>> print(s)
        0
        >>> s = SurjectionElement({(1,2,1,3,1,3): 1})
        >>> print(s)
        (1,2,1,3,1,3)
        """
        if convention is None:
            convention = SurjectionElement.default_convention
        self.convention = convention
        super(SurjectionElement, self).__init__(data=data, torsion=torsion)

    def __str__(self):
        string = super().__str__()
        return string.replace(', ', ',')

    @property
    def arity(self):
        """Arity of *self*.

        Defined as ``None`` if *self* is not homogeneous. The arity of a basis
        surjection element agrees with the maximum value it attains.

        RETURNS
        _______
        :class:`int`
            The arity of *self*.

        EXAMPLE
        -------
        >>> SurjectionElement({(1,2,1,3,1): 1}).arity
        3

        """
        if not self:
            return None
        arities = set(max(surj) for surj in self.keys())
        if len(arities) == 1:
            return arities.pop()
        return None

    @property
    def degree(self):
        """Degree of *self*.

        Defined as ``None`` if *self* is not homogeneous. The degree of a basis
        surjection agrees with the cardinality of its domain minus its arity.

        RETURNS
        _______
        :class:`int`
            The degree of *self*.

        EXAMPLE
        -------
        >>> SurjectionElement({(1,2,1,3,1): 1}).arity
        3

        """
        if not self:
            return None
        degrees = set(len(surj) - max(surj) for surj in self.keys())
        if len(degrees) == 1:
            return degrees.pop()
        return None

    @property
    def complexity(self):
        r"""Complexity of *self*.

        Defined as ``None`` if *self* is not homogeneous. The complexity of a
        finite binary sequence (i.e. a sequence of two distinct values) is
        defined as the number of consecutive distinct elements in it. For
        example, (1,2,2,1) and (1,1,1,2) have complexities 2 and 1
        respectively. The complexity of a basis surjection element
        is defined as the maximum value of the complexities of its binary
        subsequences. Notice that for arity 2, the complexity of an element
        agrees with its degree. It is proven in [McCS] that the subcomplex
        generated by basis surjection elements of complexity at most :math:`n`
        define a suboperad of :math:`\mathcal X` modeling an
        :math:`E_{n+1}`-operad.

        RETURNS
        _______
        :class:`int`
            The complexity of *self*.

        EXAMPLE
        -------
        >>> SurjectionElement({(1,2,1,3,1): 1}).complexity
        1

        """
        complexity = 0
        for k in self.keys():
            for i, j in combinations(range(1, max(k) + 1), 2):
                seq = filter(lambda x: x == i or x == j, k)
                cpxty = len([p for p, q in pairwise(seq) if p != q]) - 1
                complexity = max(cpxty, complexity)
        return complexity

    @property
    def filtration(self):
        """Filtration by sum of all pairwise complexities.

        RETURNS
        _______
        :class:`int`
            The filtration level of *self*.

        EXAMPLE
        -------
        >>> SurjectionElement({(1,2,1,3,2): 1}).filtration
        3

        """
        filtration = 0
        for key in self.keys():
            binary_complexities = []
            for i, j in combinations(range(1, max(key) + 1), 2):
                r = tuple(k for k in key if k == i or k == j)
                cpxty = len([p for p, q in pairwise(r) if p != q]) - 1
                binary_complexities.append(cpxty)
            filtration = max(filtration, sum(binary_complexities))
        return filtration

    def boundary(self):
        r"""Boundary of *self*.

        Up to signs, it is defined by taking the sum of all elements
        obtained by removing one entry at the time. Explicitly, for
        basis surjection elements we have

        .. math::
           \partial s =
           \sum_{i=1}^{r+d} \pm s \circ \delta_i =
           \sum_{i=1}^{r+d} \pm \big(s(1),\dots,\widehat{s(i)},\dots,s(n+r)\big).

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The boundary of *self* with the corresponiding sign convention.

        EXAMPLE
        -------
        >>> s = SurjectionElement({(3,2,1,3,1,3): 1})
        >>> s.convention = 'Berger-Fresse'
        >>> print(s.boundary())
        (2,1,3,1,3) - (3,2,3,1,3) - (3,2,1,3,1)
        >>> s.convention = 'McClure-Smith'
        >>> print(s.boundary())
        (3,2,3,1,3) - (2,1,3,1,3) - (3,2,1,3,1)

        """

        answer = self.zero()
        if self.torsion == 2:
            for k in self.keys():
                for idx in range(0, len(k)):
                    bdry_summand = k[:idx] + k[idx + 1:]
                    if k[idx] in bdry_summand:
                        answer += self.create({bdry_summand: 1})
            return answer
        if self.convention == 'Berger-Fresse':
            for k, v in self.items():
                # determining the signs of the summands
                signs = {}
                alternating_sign = 1
                for idx, i in enumerate(k):
                    if i in k[idx + 1:]:
                        signs[idx] = alternating_sign
                        alternating_sign *= (-1)
                    elif i in k[:idx]:
                        occurs = (pos for pos, j in enumerate(k[:idx]) if i == j)
                        signs[idx] = signs[max(occurs)] * (-1)
                    else:
                        signs[idx] = 0
                # computing the summands
                for idx in range(0, len(k)):
                    bdry_summand = k[:idx] + k[idx + 1:]
                    if k[idx] in bdry_summand:
                        answer += self.create({bdry_summand: signs[idx] * v})
        if self.convention == 'McClure-Smith':
            for k, v in self.items():
                sign = 1
                for i in range(1, max(k) + 1):
                    for idx in (idx for idx, j in enumerate(k) if j == i):
                        new_k = k[:idx] + k[idx + 1:]
                        if k[idx] in new_k:
                            answer += answer.create({new_k: v * sign})
                        sign *= -1
                    sign *= -1
        return answer

    def __rmul__(self, other):
        """Left action: *other* ``*`` *self*

        Left multiplication by a symmetric group element or an integer.
        Defined up to signs on basis elements by applying the permutation
        to the values of the surjection.

        PARAMETERS
        ----------
        other : :class:`int` or :class:`comch.symmetric.SymmetricRingElement`.
            The element to left act on *self* with.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The product: *other* ``*`` *self*, with the given sign convention.

        EXAMPLE
        -------
        >>> surj = SurjectionElement({(1,2,3,1,2): 1})
        >>> print(- surj)
        - (1,2,3,1,2)
        >>> rho = SymmetricRingElement({(2,3,1): 1})
        >>> print(rho * surj)
        (2,3,1,2,3)
        """

        def check_input(self, other):
            if not isinstance(other, SymmetricRingElement):
                raise TypeError(
                    f'Type int or SymmetricRingElement not {type(other)}')
            if self.torsion != other.torsion:
                raise TypeError('only defined for equal attribute torsion')
            if self.arity != other.arity:
                raise TypeError('Unequal arity attribute')

        def sign(perm, surj, convention):
            if convention == 'Berger-Fresse':
                return 1
            assert convention == 'McClure-Smith'
            weights = [surj.count(i) - 1 for
                       i in range(1, max(surj) + 1)]
            sign_exp = 0
            for idx, i in enumerate(perm):
                right = [weights[perm.index(j)] for
                         j in perm[idx + 1:] if i > j]
                sign_exp += sum(right) * weights[idx]
            return (-1) ** (sign_exp % 2)

        if isinstance(other, int):
            return super().__rmul__(other)

        check_input(self, other)

        answer = self.zero()
        for (k1, v1), (k2, v2) in product(self.items(), other.items()):
            new_key = tuple(k2[i - 1] for i in k1)
            new_sign = sign(k2, k1, self.convention)
            answer += self.create({new_key: new_sign * v1 * v2})
        return answer

    def orbit(self, representation='trivial'):
        """The preferred representative of the symmetric orbit of *self*.

        The preferred representative in the orbit of basis surjections element
        is the one satisfying that the first occurence of each integer appear in
        increasing order.

        The representation used can be either 'trivial' or 'sign'.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The preferred element in the symmetric orbit of *self*.

        EXAMPLE
        -------
        >>> s = SurjectionElement({(1,3,2): 1})
        >>> print(s.orbit(representation='trivial'))
        (1,2,3)
        >>> print(s.orbit(representation='sign'))
        - (1,2,3)

        """

        def sign(permutation, representation):
            if representation == 'trivial':
                return 1
            if representation == 'sign':
                return permutation.sign

        answer = self.zero()
        for k, v in self.items():
            seen = []
            for i in k:
                if i not in seen:
                    seen.append(i)
            permutation = SymmetricGroupElement(seen).inverse()
            new_v = sign(permutation, representation) * v
            answer += permutation * self.create({k: new_v})

        return answer

    def __call__(self, other, coord=1):
        """The action: *self*(*other*).

        The action of *self* on the tensor factor specified by *coord* on an
        element in the tensor product of normalized chains of a standard simplex
        or of a standard cube.

        PARAMETERS
        ----------
        other : :class:`comch.simplicial.SimplicialElement` or\
        :class:`comch.cubical.CubicalElement`.
            The element to which apply *self* to
        coord : :class:`int`, default 1.
            The tensor factor of *other* to apply *self* to.

        RETURNS
        _______
        :class:`comch.simplicial.SimplicialElement` or\
        :class:`comch.cubical.CubicalElement`
            The action of *self* on *other* at *coord*.
        """

        def check_input(self, other, coord=1):
            if self.degree is None or self.arity is None:
                raise TypeError('defined for homogeneous surjections')
            if other.arity < coord:
                raise TypeError(f'arity = {other.arity} < coord = {coord}')
            if self.torsion != other.torsion:
                raise TypeError('only defined for equal attribute torsion')

        def compute_sign(k1, k2):
            """Returns the sign associated to a pair."""

            def ordering_sign(permu, weights):
                """Returns the exponent of the Koszul sign of the given
                permutation acting on the elements of degrees given by the
                list of weights

                """
                sign_exp = 0
                for idx, j in enumerate(permu):
                    to_add = [weights[permu.index(i)] for
                              i in permu[idx + 1:] if i < j]
                    sign_exp += weights[idx] * sum(to_add)
                return sign_exp % 2

            def action_sign(ordered_k1, ordered_weights):
                """Given a ordered tuple [1,..,1, 2,...,2, ..., r,...,r]
                and weights [w_1, w_2, ..., w_{r+d}] of the same length, gives
                the koszul sign obtained by inserting from the left a weight 1
                operator between equal consecutive elements.

                """
                sign_exp = 0
                for idx, (i, j) in enumerate(pairwise(ordered_k1)):
                    if i == j:
                        sign_exp += sum(ordered_weights[:idx + 1])
                return sign_exp % 2

            sign_exp = 0
            weights = [e.dimension % 2 for e in k2]
            inv_ordering_permu = [pair[0] for pair in
                                  sorted(enumerate(k1), key=itemgetter(1))]
            ordering_permu = tuple(inv_ordering_permu.index(i)
                                   for i in range(len(inv_ordering_permu)))
            sign_exp += ordering_sign(ordering_permu, weights)
            ordered_k1 = list(sorted(k1))
            ordered_weights = [weights[i] for i in inv_ordering_permu]
            sign_exp += action_sign(ordered_k1, ordered_weights)
            return (-1) ** sign_exp

        def simplicial(self, other, coord):
            """Action on Eilenberg-Zilber elements."""
            answer = other.zero()
            times = self.arity + self.degree - 1
            pre_join = other.iterated_diagonal(times, coord)
            for (k1, v1), (k2, v2) in product(self.items(), pre_join.items()):
                i, j = coord - 1, coord + len(k1) - 1
                left, k2, right = k2[:i], k2[i:j], k2[j:]
                new_k = []
                zero_summand = False
                for i in range(1, max(k1) + 1):
                    to_join = (spx for idx, spx in enumerate(k2)
                               if k1[idx] == i)
                    joined = Simplex(reduce(lambda x, y: x + y, to_join))
                    if joined.is_degenerate():
                        zero_summand = True
                        break
                    new_k.append(joined)
                if not zero_summand:
                    if self.torsion == 2:
                        sign = 1
                    else:
                        sign = compute_sign(k1, k2)
                        deg_left = sum(len(spx) - 1 for spx in left) % 2
                        sign *= (-1) ** (deg_left * self.degree)
                    new_k = left + tuple(new_k) + right
                    answer += answer.create({new_k: sign * v1 * v2})
            return answer

        def cubical(self, other):
            """Action on cubical Eilenberg-Zilber elements."""
            answer = other.zero()
            pre_join = other.iterated_diagonal(self.arity + self.degree - 1)
            for (k1, v1), (k2, v2) in product(self.items(), pre_join.items()):
                to_dist = []
                zero_summand = False
                for i in range(1, max(k1) + 1):
                    key_to_join = tuple(cube for idx, cube in enumerate(k2)
                                        if k1[idx] == i)
                    joined = other.create({key_to_join: 1}).join()
                    if not joined:
                        zero_summand = True
                        break
                    to_dist.append(joined)
                if not zero_summand:
                    if self.torsion == 2:
                        sign = 1
                    else:
                        sign = compute_sign(k1, k2)
                    items_to_dist = [summand.items() for summand in to_dist]
                    for pairs in product(*items_to_dist):
                        new_k = reduce(lambda x, y: x + y, (pair[0] for pair in pairs))
                        new_v = reduce(lambda x, y: x * y, (pair[1] for pair in pairs))
                        to_add = answer.create({tuple(new_k): sign * new_v * v1 * v2})
                        answer += to_add
            return answer

        if not self or not other:
            return other.zero()

        check_input(self, other, coord=1)

        if isinstance(other, SimplicialElement):
            if self.convention != 'McClure-Smith':
                raise NotImplementedError
            return simplicial(self, other, coord)
        elif isinstance(other, CubicalElement):
            return cubical(self, other)
        else:
            raise NotImplementedError

    def compose(self, other, position):
        r"""Operadic compositions: *self* :math:`\circ_{position}` *other*.

        The :math:`i`-th composition :math:`x \circ_i y` of
        :math:`x \in \mathcal X(r)` and :math:`y \in \mathcal X(s)` is defined
        by the following procedure: let :math:`w` be the cardinality of
        :math:`x^{-1}(i)`, for every collection of ordered indices

        .. math::
            1 = j_0 \leq j_1 \leq j_2 \leq \cdots \leq j_{w-1} \leq j_w = s

        we construct an associated splitting of :math:`y`

        .. math::
            (y(j_0), \dots, y(j_1));\ (y(j_1), \dots, y(j_2));\ \cdots \ ;\
            (y(j_{w-1}), \dots, y(j_w)).

        The element :math:`x \circ_i y \in \mathcal(r+s-1)` is represented, up
        to signs, as the sum over all possible collections of order indices of
        the sequence obtained in the following two steps: 1) replace each
        occurrence of :math:`i` in :math:`x` by the corresponding sequence in
        the associated splitting having its values shifted up by :math:`i-1`,
        and 2) shift up by :math:`s-1` the values of :math:`x` greater than
        :math:`i`.

        PARAMETERS
        ----------
        other : :class:`comch.surjection.SurjectionElement`
            The element to operad compose *self* with.
        position : :class:`int`
            The value at which the composition occurs.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The operadic composition of *self* and *other*.

        EXAMPLE
        -------
        >>> x = SurjectionElement({(1,2,1,3): 1}, convention='Berger-Fresse')
        >>> y = SurjectionElement({(1,2,1): 1}, convention='Berger-Fresse')
        >>> print(x.compose(y, 1))
        (1,3,1,2,1,4) - (1,2,3,2,1,4) - (1,2,1,3,1,4)

        """

        def bf_sign(p1, k1, p2, k2):
            """Sign associated to the Berger-Fresse composition."""

            def caesuras(k):
                """Returns the caesuras of a basis element."""
                caesuras = []
                for idx, i in enumerate(k):
                    if i in k[idx + 1:]:
                        caesuras.append(idx)
                return caesuras

            def weights(cae, p):
                """Returns the weights of the splitting knowing the caesuras."""
                weights = []
                for i, j in pairwise(p):
                    closed_open = len([e for e in cae if i <= e < j])
                    weights.append(closed_open)
                return [value % 2 for value in weights]

            p1 = [0] + p1 + [len(k1) - 1]
            cae1 = caesuras(k1)
            w1 = weights(cae1, p1)
            cae2 = caesuras(k2)
            w2 = weights(cae2, p2)
            sign_exp = 0
            for idx, w in enumerate(w2):
                if w:
                    sign_exp += sum(w1[idx + 1:]) % 2
            return (-1) ** sign_exp

        def ms_sign(positions, k1, p, k2):
            raise NotImplementedError

        answer = self.zero()
        for (k1, v1), (k2, v2) in product(self.items(), other.items()):
            positions = [idx for idx, j in enumerate(k1) if j == position]
            for p in combinations_with_replacement(
                    range(len(k2)), len(positions) - 1):
                p = (0,) + p + (len(k2) - 1,)
                split = []
                for a, b in pairwise(p):
                    split.append(tuple(k2[a:b + 1]))
                to_insert = (tuple(j + position - 1 for j in part) for part in split)
                new_k = list()
                for j in k1:
                    if j < position:
                        new_k.append(j)
                    elif j == position:
                        new_k += next(to_insert)
                    else:
                        new_k.append(j + other.arity - 1)
                if self.torsion == 2:
                    sign = 1
                elif self.convention == 'Berger-Fresse':
                    sign = bf_sign(positions, k1, p, k2)
                elif self.convention == 'McClure-Smith':
                    sign = ms_sign()
                answer += answer.create({tuple(new_k): v1 * v2 * sign})
        return answer

    def suspension(self):
        r"""Image of *self* in the suspension of the surjection operad.

        Given a basis element :math:`u` in arity :math:`r` and degree :math:`d`
        the suspension is in degree :math:`d-r+1` and is :math:`0` if
        :math:`(u(1),\dots,u(r))` is not a permutation and
        :math:`sgn(u(1),\dots,u(r)) (u(r),\dots,u(r+d))` otherwise.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The image of *self* in the suspension of the operad.

        EXAMPLE
        -------
        >>> x = SurjectionElement({(1,3,2,1,2):1}, convention='Berger-Fresse')
        >>> print(x.suspension())
        - (2,1,2)

        """
        if not self:
            return self
        if self.arity is None or self.degree is None:
            raise TypeError('defined for homogeneous elements only')
        if self.convention != 'Berger-Fresse':
            raise NotImplementedError
        answer = self.zero()
        for k, v in self.items():
            nonzero = False
            try:
                p = SymmetricGroupElement(k[:self.arity])
                sign = p.sign
                nonzero = True
            except TypeError:
                pass
            if nonzero:
                answer += self.create({k[self.arity - 1:]: v * sign})
        return answer

    def preferred_rep(self):
        """Preferred representative of *self*.

        Removes pairs `basis_element: coefficient` which satisfy either of:
        1) the basis element has equal consecutive values, 2) the basis
        element does not represent a surjection, or 3) the coefficient is 0.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The preferred representative of *self*.

        EXAMPLE
        -------
        >>> print(SurjectionElement({(1,1,2):1, (1,3):1, (1,2):0}))
        0

        """
        zeros = list()
        for k in self.keys():
            if set(k) != set(range(1, max(k) + 1)):
                zeros.append(k)
        for k in zeros:
            del self[k]
        for k, v in self.items():
            for i in range(len(k) - 1):
                if k[i] == k[i + 1]:
                    self[k] = 0
        super().preferred_rep()


class Surjection:
    """Produces surjection elements of interest."""

    @staticmethod
    def may_steenrod_structure(arity, degree, torsion=None, convention=None):
        r"""Representative of the requested Steenrod product.

        Let :math:`\mathrm{C}_n` be the cyclic group of order :math:`n` thought
        of as the subgroup of :math:`\mathrm{S}_n` generated by an element
        :math:`\rho`. We denote this inclusion by
        :math:`\iota : \mathrm C_r \to \mathrm S_r`. The elements

        .. math:: T = \rho-1 \quad \text{ and } \quad N = 1+\rho+\cdots+\rho^{r-1}

        in :math:`R[C_r]` define a minimal resolution :math:`W(r)`

        .. math::
            R[C_r] \stackrel{T}{\longleftarrow}
            R[C_r] \stackrel{N}{\longleftarrow}
            R[C_r] \stackrel{T}{\longleftarrow} \cdots

        of :math:`R` by a free differential graded :math:`R[C_r]`-module. We denote
        a preferred basis element of :math:`W(r)_i` by :math:`e_i`.

        A May-Steenrod structure on an operad :math:`\mathcal O` is a
        morphism of :math:`\mathrm{C}`-modules
        :math:`\mathcal W \stackrel{\psi}{\longrightarrow} \mathcal O` for which
        there exists a factorization through an :math:`E_\infty`-operad

        .. math::
            \mathcal W \stackrel{\iota}{\longrightarrow}
            \mathcal R \stackrel{\phi}{\longrightarrow} \mathcal O

        such that :math:`\iota` is a weak equivalence and :math:`\phi` a
        morphism of operads.

        This method returns the image under the May-Steenrod structure
        constructed in [KMM] of the preferred basis element of :math:`W(r)_i`.

        PARAMETERS
        ----------
        arity : :class:`int`
            The arity considered.
        degree : :class:`int`
            The degree considered.
        torsion : :class:`int` or ``None``, default ``None``
            The torsion of the underlying ring.
        convention : :class:`string` or ``None``, default ``None``
            The sign convention of the surjection operad.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The image of the basis element under the May-Steenrod structure.

        REFERENCES
        ----------
        [KMM]: Kaufmann, R. M., & Medina-Mardones, A. M. (2020). Chain level
        Steenrod operations. arXiv preprint arXiv:2010.02571.
        """

        def i(surj, iterate=1):
            """Inclusion of Surj(r) into Surj(r+1)

            Defined by appending 1 at the start of basis elements and
            raising the value of all other entries by 1."""

            if iterate == 1:
                answer = surj.zero()
                for k, v in surj.items():
                    answer += answer.create(
                        {(1,) + tuple(j + 1 for j in k): v})
                return answer
            if iterate > 1:
                return i(i(surj, iterate=iterate - 1))

        def p(surj, iterate=1):
            """Projection of Surj(r) to Surj(r-1)

            Defined by removing 1 from a basis element with only one
            occurrences of value 1 and subtracting 1 from all other entries.

            """
            if iterate == 1:
                answer = surj.zero()
                for k, v in surj.items():
                    if k.count(1) == 1:
                        idx = k.index(1)
                        new_k = (tuple(j - 1 for j in k[:idx]) +
                                 tuple(j - 1 for j in k[idx + 1:]))
                        answer += answer.create({new_k: v})
                return answer
            if iterate > 1:
                return p(p(surj, iterate=iterate - 1))

        def s(surj):
            """Chain homotopy from the identity to the composition pi.
            Explicitly, id - ip = ds + sd."""
            answer = surj.zero()
            for k, v in surj.items():
                answer += answer.create({(1,) + tuple(j for j in k): v})
            return answer

        def h(surj):
            """Chain homotopy from the identity to i...i p..p.
            In Surj(r), realizing its contractibility to Surj(1)."""
            answer = s(surj)
            for r in range(1, arity - 1):
                answer += i(s(p(surj, r)), r)
            return answer

        operators = {
            0: SymmetricRing.norm_element(arity),
            1: SymmetricRing.transposition_element(arity)
        }

        def psi(arity, degree, convention=convention):
            """Recursive definition of steenrod product over the integers."""
            if degree == 0:
                return SurjectionElement({tuple(range(1, arity + 1)): 1},
                                         convention=convention)
            else:
                previous = psi(arity, degree - 1, convention=convention)
                acted_on = operators[degree % 2] * previous
                answer = h(acted_on)
                return answer

        if convention is None:
            convention = SurjectionElement.default_convention
        integral_answer = psi(arity, degree, convention=convention)
        if torsion:
            integral_answer.set_torsion(torsion)
        return integral_answer

    @staticmethod
    def steenrod_operation(p, s, q, bockstein=False, convention='McClure-Smith'):
        r"""Chain level representative of :math:`P_s` or :math:`\beta P_s`.

        Let :math:`A` be such that :math:`\mathrm{End}_A` is equipped with a
        May-Steenrod structure

        .. math:: \psi : W \to \mathrm{End}_A.

        For any prime :math:`p`, define the linear map
        :math:`D_d : A \otimes \mathbb F_p \to A \otimes \mathbb F_p`
        by

        .. math::
           D_d(a) = \begin{cases}
           \psi(e_d)(a^{\otimes p})& d \geq 0 \\
           0 & d < 0.
           \end{cases}

        For any integer :math:`s`, the Steenrod operations

        .. math::
            P_s : H_\bullet(A; \mathbb F_2)
            \to
            H_{\bullet + s}(A; \mathbb F_2)

        and, for :math:`p > 2`,

        .. math::
           P_s : H_\bullet(A; \mathbb F_p)
           \to
           H_{\bullet + 2s(p-1)}(A; \mathbb F_p)
           \qquad
           \beta P_s : H_\bullet(A; \mathbb F_p)
           \to
           H_{\bullet+2s(p-1)-1}(A; \mathbb F_p)

        are defined for a class :math:`[a]` of degree
        :math:`q` respectively by

        .. math:: P_s\big([a]\big) = \big[D_{s-q}(a)\big] \qquad

        and

        .. math::
           P_s\big([a]\big) = \big[(-1)^s \nu(q) D_{(2s-q)(p-1)}(a)\big]
           \qquad
           \beta P_s\big([a]\big) = \big[(-1)^s \nu(q)D_{(2s-q)(p-1)-1}(a)\big]

        where :math:`\nu(q) = (-1)^{q(q-1)m/2}(m!)^q` and :math:`m = (p-1)/2`.

        PARAMETERS
        ----------
        p : :class:`int`
            The prime considered.
        s : :class:`int`
            The subscript of the Steenrod operation.
        q : :class:`int`
            The degree of the class acted on.
        bockstein : :class:`bool`, default ``False``
            Determines the use of the Bockstein homomorphism.
        convention : :class:`string` default 'McClure-Smith'
            The sign convention used.

        RETURNS
        _______
        :class:`comch.surjection.SurjectionElement`
            The surjection element representing the given Steenrod operation.

        REFERENCES
        ----------
        [May]: May, J. Peter. "A general algebraic approach to Steenrod
        operations." The Steenrod Algebra and its Applications: a conference
        to celebrate NE Steenrod's sixtieth birthday. Springer, Berlin,
        Heidelberg, 1970.

        """

        # input check
        if not all(isinstance(i, int) for i in {p, s, q}):
            raise TypeError('initialize with three int p,s,n')
        if not isinstance(bockstein, bool):
            raise TypeError('bockstein must be a boolean')
        if p == 2 and bockstein:
            raise TypeError('bP only defined for odd primes')

        if p == 2:
            coeff = 1
            d = s - q
            if d < 0:
                return SurjectionElement(torsion=2)
        else:
            b = int(bockstein)
            # Serre convention: v(2j)=(-1)^j & v(2j+1)=v(2j)*m! w/ m=(p-1)/2
            coeff = (-1) ** (floor(q / 2) + s)
            if q / 2 - floor(q / 2):
                coeff *= factorial((p - 1) / 2)
            # degree of the element: (2s-q)(p-1)-b
            d = (2 * s - q) * (p - 1) - b
            if d < 0:
                return SurjectionElement(torsion=p)

        return int(coeff) * Surjection.may_steenrod_structure(
            p, d, torsion=p, convention=convention)

    @staticmethod
    def steenrod_chain(p, s, q, bockstein=False, shape='simplex'):
        """Chain representative of a Steenrod operation.

        Given the parameters of a Steenrod operation: prime p, subindex s, and
        cochain degree q, and bockstein, it returns the chain in the tensor
        product of a standard simplex on which the iterated tensor product of
        the cochain acts defining a cochain representative of its image under
        the operation.

        PARAMETERS
        ----------
        p : :class:`int`
            The prime considered.
        s : :class:`int`
            The subscript of the Steenrod operation.
        q : :class:`int`
            The degree of the class acted on.
        bockstein : :class:`bool`, default ``False``
            Determines the use of the bockstein homomorphism.
        shape: :class:`string`, 'simplex' or 'cube'
            Action on the standard simplex or cube

        RETURNS
        _______
        :class:`comch.simplicial.SimplicialElement`\
        or :class:`comch.cubical.CubicalElement`
            The tensor product elment obtained by applying the representative
            of the specified Steenrod operation.

        EXAMPLES
        --------
        >>> print(Surjection.steenrod_chain(2, -1, -2))
        ((0,2,3),(0,1,2)) + ((0,1,3),(1,2,3))

        """

        def filter_homogeneous(element):
            homogeneous = {}
            for k, v in element.items():
                if len(set(elmt.dimension for elmt in k)) == 1:
                    homogeneous[k] = v
            return element.create(homogeneous)

        surj = Surjection.steenrod_operation(p, s, q, bockstein=bockstein)
        b = int(bockstein)

        if p == 2:
            d = q + s
        else:
            d = q + 2 * s * (p - 1) - b

        if shape == 'simplex':
            element = Simplicial.standard_element(-d, torsion=p)
        elif shape == 'cube':
            element = Cubical.standard_element(-d, torsion=p)

        return filter_homogeneous(surj(element))

    @staticmethod
    def basis(arity, degree, complexity=None):
        r"""Basis of the chain complex.

        Basis of :math:`\mathcal X` In the given arity, degree and complexity.

        PARAMETERS
        ----------
        arity : :class:`int`
            The arity considered.
        degree : :class:`int`
            The degree considered.
        complexity : :class:`int`, default ``None``
            The complexity considered.

        RETURNS
        _______
        :class:`list` of :class:`tuple` of :class:`int`
            The basis for the complex of surjection in the given arity, degree
            and complexity.

        EXAMPLES
        --------
        >>> Surjection.basis(2,1)
        [(1, 2, 1), (2, 1, 2)]

        """
        if complexity is None:
            complexity = degree
        a, d, c = arity, degree, complexity
        basis = []
        for s in product(range(1, a + 1), repeat=a + d):
            surj = SurjectionElement({s: 1})
            if surj and surj.complexity <= c and surj.arity == a:
                basis.append(s)
        return basis
