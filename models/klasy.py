from factory import Faker, Factory

from datetime import date
import random

from . import Stringify
from .nauczyciele import TEACHERS_NUM

SYMBOLS = ["Ia", "Ib", "Ic", "IIa", "IIb", "IIIa", "IIIb", "IIIc", "IVa", "IVb"]
CLASSES_NUM = len(SYMBOLS)


def get_class_symbol(obj):
    age = (date.today() - obj.DUr).days // 365
    if age <= 16:
        return random.choice(SYMBOLS[:3])
    elif age == 17:
        return random.choice(SYMBOLS[3:5])
    elif age == 18:
        return random.choice(SYMBOLS[5:8])
    else:
        return random.choice(SYMBOLS[8:])


class Klasy(Stringify):
    def __init__(self, Symbol, Profil, Wych):
        self.Symbol = Symbol
        self.Profil = Profil
        self.Wych = Wych

    @property
    def headers(self):
        return "Symbol;Profil;Wych"


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
