import factory
from factory import Faker, Factory


class Klasy:
    def __init__(self, Symbol, Profil):
        self.Symbol = Symbol
        self.Profil = Profil

        # TODO:
        # self.Wych = Wych

    @property
    def headers(self):
        return "Symbol;Profil" # add Wych

    def __str__(self):
        return f"{self.Symbol};{self.Profil}" # add ;{self.Wych}


class GeneratorKlas(Factory):
    class Meta:
        model = Klasy

    Symbol = Faker("word", ext_word_list=["Ia", "Ib", "IIa", "IIb", "IIIa", "IIIb"])
    Profil = Faker("word", ext_word_list=["matematyczny", "humanistyczny", "przyrodniczy", "techniczny"])



if __name__ == "__main__":
    print(GeneratorKlas().headers)
    print(GeneratorKlas())
