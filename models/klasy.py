from factory import Faker, Factory

from . import Stringify

SYMBOLS = ["Ia", "Ib", "IIa", "IIb", "IIIa", "IIIb"]


class Klasy(Stringify):
    def __init__(self, Symbol, Profil):
        self.Symbol = Symbol
        self.Profil = Profil

        # TODO:
        # self.Wych = Wych

    @property
    def headers(self):
        return "Symbol;Profil"  # add Wych


class ClassGenerator(Factory):
    class Meta:
        model = Klasy

    Symbol = ""
    Profil = Faker("word", ext_word_list=["matematyczny", "humanistyczny", "przyrodniczy", "techniczny"])


def generate_classes(_):
    for symbol in SYMBOLS:
        yield ClassGenerator(Symbol=symbol)


if __name__ == "__main__":
    print(ClassGenerator().headers)
    for row in generate_classes(None):
        print(row)
