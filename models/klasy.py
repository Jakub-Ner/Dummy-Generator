from factory import Faker, Factory

from . import Stringify
from .nauczyciele import TEACHERS_NUM

SYMBOLS = ["Ia", "Ib", "Ic", "IIa", "IIb", "IIIa", "IIIb", "IIIc", "IVa", "IVb"]
CLASSES_NUM = len(SYMBOLS)


class Klasy(Stringify):
    def __init__(self, Symbol, Profil, Wych):
        self.Symbol = Symbol
        self.Profil = Profil
        self.Wych = Wych

    @property
    def headers(self):
        return "Symbol;Profil;Wych"  # add Wych


class ClassGenerator(Factory):
    class Meta:
        model = Klasy

    Symbol = ""
    Profil = Faker("word", ext_word_list=["matematyczny", "humanistyczny", "przyrodniczy", "techniczny"])
    Wych = Faker("pyint", min_value=1, max_value=TEACHERS_NUM)


def generate_classes():
    for symbol in SYMBOLS:
        yield ClassGenerator(Symbol=symbol)


if __name__ == "__main__":
    print(ClassGenerator().headers)
    for row in generate_classes():
        print(row)
