import lib
from constants import *



class PasswordChecker:
    def __init__(self, default: bool = False):
        """Verifie si un mot de passe est correct en ajoutant des contraintes.

        Parameters:
        -----------
        default: boolean, optional, default=True
            Autoconfigure la verification. Voir la methode _default_setup

        See also:
        ---------
            default_setup: appelé quand default est vrai

        .. code-block:: python
        >>> checker = PasswordChecker().min(12)\
            .max(100)\
            .has().uppercase()\
            .has().lowercase()\
            .not_common()
        """

        self.properties: list = []
        self.positive: bool = True
        if default:
            self._default_setup()

    def _default_setup(self):
        """Methodes appelé quand le paramètre default de __init__ est vrai.

        Configure le verifcateur en suivant les recommandation du ministères
        de l'économie française.
        https://www.economie.gouv.fr/particuliers/creer-mot-passe-securise

        - Longueur minimale de 12 caractères.
        - Contient au moins une lettre majuscule
        - Contient au moins une lettre miniscule.
        - Contient au moins un nombre.
        - Contient au moins un caractère spécial.
        - Et le mot de passe n'est pas contenu dans la liste des 20 000 mot de
        passe les plus fréquents.
        """
        self.min(12) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits() \
            .has().symbols() \
            .not_common()

    def validate(self, pwd: str):
        """Valide le mot de passe passé en paramètre.

        .. code-block:: python
        >>> checker = PasswordChecker().min(12)

        Test avec un mot de passe ne respectant pas la longueur minimal de
        12 caractères.

        .. code-block:: python
        >>> checker.validate("short")
        False

        Test avec un mot de passe respectant la longueur minimal de 12
        caractères.

        .. python::
        >>> checker.validate("longlonglonglonglong")
        True

        Parameters:
        -----------
            pwd: string
            """
        return all(self.__is_password_valid_for(prop, pwd) for prop in
                   self.properties)

    def __register_property(self, func, *args) -> None:
        self.properties.append({
            'method': func,
            'positive': self.positive,
            'arguments': args,
        })

    @staticmethod
    def __is_password_valid_for(prop, password):
        return prop['method'](password, prop['positive'], *prop['arguments'])

    @staticmethod
    def __validate_num(num):
        assert (type(num) == 'int' or num > 0), error[
            'length']  # Pylint: disable=unidiomatic-typecheck

    def has(self, regexp: str = None):
        """Ajoute une propriété à la verification.

        See Also:
        ---------
            no: contraire de has"""
        self.positive: bool = True
        if regexp:
            self.__register_property(lib.apply_regexp, [re.compile(regexp)])
        return self

    def no(self, regexp: str = None):
        """Supprime une propriété à la verification

        Return False because `no().uppercase()` et dans le mot de passe, il  y
        a des majuscules.

        .. code-block:: python
        >>> PasswordChecker().no().uppercase().validate("AHHAHe")
        False

        .. code-block:: python
        >>> PasswordChecker().no().uppercase().validate("ahhaha")
        True

        See Also:
        ---------
            has: contraire de no
            """
        self.positive: bool = not self.positive
        if regexp:
            self.__register_property(lib.apply_regexp, [re.compile(regexp)])
        return self

    def uppercase(self):
        """Verifie si le mot de passe contient une majuscule.

        Renvoie True car il y a une majuscule dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().uppercase().validate("AHHAe")
        True

        Renvoie False car il n'y a pas de majuscule dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().uppercase().validate("ahhaa")
        False"""
        self.__register_property(lib.uppercase)
        return self

    def lowercase(self):
        """Verifie si le mot de passe contient une miniscule

        Renvoie True car il y a une miniscule dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().lowercase().validate("ahhha")
        True

        Renvoie False car il n'y a pas de miniscule dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().uppercase().validate("AHHAH")
        False
        """
        self.__register_property(lib.lowercase)
        return self

    def letters(self, min_: int = 0, max_: int = 0):
        """Verifie si le mot de passe contient des lettres.

        Si min_ et/ou max_ sont définis alors, vérifie aussi que le nombre de
        lettres respecte min_ et/ou max_

        Parameters:
        ----------
            min_: int, optional, default=0
            max_: int, optional, default=0

        Renvoie True car il y a une lettre dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().letters().validate("ahhha")
        True

        Renvoie False car il n'y a pas de lettres dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().letters().validate("1234")
        False

        Renvoie True car il y a entre 2 et 5 lettres dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().letters(2, 5).validate("aaa")
        True

        Renvoie False car il n'y a pas entre 2 et 5 lettres dans le mot de
        passe.

        .. code-block:: python
        >>> PasswordChecker().has().letters(2, 5).validate("123a")
        """
        self.__register_property(lib.letters, min_, max_)
        return self

    def not_common(self):
        """Verifie si le mot de passe est contenu dans une liste des 20000 mot
        de passe les plus courants.

        Renvoie True car H2TVZZH n'est pas contenu dans la liste

        .. code-block:: python
        >>> PasswordChecker().not_common().validate("H2TVZZH")
        True

        Renvoie False car azerty est présent dans la liste des 20000 mot de
        passe les plus courants.

        .. code-block:: python
        >>> PasswordChecker().not_common().validate("azerty")
        False
        """
        self.__register_property(lib.not_common)
        return self

    def digits(self, min_: int = 0, max_: int = 0):
        """Verifie si le mot de passe contient des chiffres.

        Si min_ et/ou max_ sont définis alors, vérifie aussi que le nombre de
        chffres respecte min_ et/ou max_

        Parameters:
        ----------
            min_: int, optional, default=0
            max_: int, optional, default=0

        Renvoie True car il y a un chiffre dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().digits().validate("222")
        True

        Renvoie False car il n'y a pas de chiffres dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().digits().validate("aaaac")
        False

        Renvoie True car il y a entre 2 et 5 chiffres dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().digits(2, 5).validate("2et5")
        True

        Renvoie False car il n'y a pas entre 2 et 5 chiffres dans le mot de
        passe.

        .. code-block:: python
        >>> PasswordChecker().has().digits(2, 5).validate("1seulchiffre")
        """
        self.__register_property(lib.digits, min_, max_)
        return self

    def min(self, min_: int = 10):
        """Verifie la longeur du mot de passe est supérieur à min_

        Parameters:
        -----------
            min_: int, optional, default=10

        .. code-block:: python
        >>> PasswordChecker().min(5).validate("longeur>5")
        True

        .. code-block:: python
        >>> PasswordChecker().min(10).validate("<10")
        False"""
        self.__register_property(lib.minimum, min_)
        return self

    def max(self, max_: int = 100):
        """Verifie la longeur du mot de passe est supérieur à min_

        Parameters:
        -----------
            min_: int, optional, default=100

        .. code-block:: python
        >>> PasswordChecker().max(20).validate("longeur<20")
        True

        .. code-block:: python
        >>> PasswordChecker().min(20).validate(
            "je suis plus long que vingt caractères ...")
        False"""
        self.__register_property(lib.maximum, max_)
        return self

    def spaces(self, min_: int = 0, max_: int = 0):
        """Verifie si le mot de passe contient des espaces.

        Si min_ et/ou max_ sont définis alors, vérifie aussi que le nombre d'
        espaces respecte min_ et/ou max_

        Parameters:
        ----------
            min_: int, optional, default=0
            max_: int, optional, default=0

        Renvoie True car il y a un espace dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().spaces().validate(" ehhe")
        True

        Renvoie False car il n'y a pas d'espaces dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().spaces().validate("nospace")
        False

        Renvoie True car il y a entre 2 et 5 espaces dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().spaces(2, 5).validate("  2 et 5espaces")
        True

        Renvoie False car il n'y a pas entre 2 et 5 espaces dans le mot de
        passe.

        .. code-block:: python
        >>> PasswordChecker().has().spaces(2, 5).validate(" seulespace")
        """
        self.__register_property(lib.spaces, min_, max_)
        return self

    def symbols(self, min_: int = 0, max_: int = 0):
        """Verifie si le mot de passe contient des symboles.

        Si min_ et/ou max_ sont définis alors, vérifie aussi que le nombre de
        symboles respecte min_ et/ou max_

        Parameters:
        ----------
            min_: int, optional, default=0
            max_: int, optional, default=0

        Renvoie True car il y a un symbole dans le mot de passe.

        .. code-block:: python
        >>> PasswordChecker().has().symbols().validate(":-)aa")
        True

        Renvoie False car il n'y a pas de symboles dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().symbols().validate("aaaac")
        False

        Renvoie True car il y a entre 2 et 5 symboles dans le mot de passe

        .. code-block:: python
        >>> PasswordChecker().has().symbols(2, 5).validate("troisymboles:-)")
        True

        Renvoie False car il n'y a pas entre 2 et 5 symboles dans le mot de
        passe.

        .. code-block:: python
        >>> PasswordChecker().has().symbols(2, 5).validate(".monosymbole")
        """
        self.__register_property(lib.symbols, min_, max_)
        return self


if __name__ == '__main__':
    pwd = PasswordChecker().has().lowercase() \
        .min(0).max(100) \
        .not_common().validate("hello")
    print(pwd)
