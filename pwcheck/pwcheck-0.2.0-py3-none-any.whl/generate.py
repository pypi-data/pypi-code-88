from string import ascii_lowercase, ascii_uppercase, \
    digits as _digits
from secrets import choice, token_hex


class Generator:
    def __init__(self, *, upper: bool = True, lower: bool = True,
                 special_cars: bool = False, digits: bool = True,
                 similar_car: bool = True, ambiguous: bool = False,
                 space: bool = False, minus: bool = True,
                 bracket: bool = True, underscore: bool = True,
                 all_: bool = False):
        if all_:
            upper = True
            lower = True
            special_cars = True
            digits = True
            similar_car = True
            ambiguous = True
            space = True
            minus = True
            bracket = True
            underscore = True

        self.alpha = ""
        if upper:
            self.alpha += ascii_uppercase
        if lower:
            self.alpha += ascii_lowercase
        if special_cars:
            self.alpha += "!#$%&'*+,./:;<=>?@\\^`|\"~"
        if space:
            self.alpha += " "
        if minus:
            self.alpha += "-"
        if underscore:
            self.alpha += "_"
        if bracket:
            self.alpha += "[]{}()<>"
        if digits:
            self.alpha += _digits
        if similar_car:
            for car in "il1Lo0O":
                self.alpha = self.alpha.replace(car, "")
        if ambiguous:
            for car in "{}[]()/\\'\"`~,;:.<>":
                self.alpha = self.alpha.replace(car, "")

    def generate(self, len_: int = None, char: str = ""):
        if len_ is None: len_ = 12
        for c in char:
            if c not in self.alpha: self.alpha += c
        return "".join([choice(self.alpha) for _ in range(len_)])


if __name__ == '__main__':
    gen = Generator()
    print(gen.generate())
    print(len(gen.generate()))
