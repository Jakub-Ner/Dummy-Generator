import factory
from factory import Faker, Factory

from . import Stringify

from datetime import datetime
class Uczniowie(Stringify):
    def __init__(self, IdU, Nazwisko, Imie, DUr, Plec):
        self.IdU = IdU
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.DUr = DUr.strftime("%d-%m-%Y")
        self.Plec = Plec

        # self.KlasaU = KlasaU
        # self.Miasto = Miasto

    @property
    def headers(self):
        return "IdU;Nazwisko;Imie;DUr;Plec"  # ;KlasaU;Miasto


@factory.Faker.override_default_locale('pl_PL')
class StudentsFactory(Factory):
    class Meta:
        model = Uczniowie

    IdU = 0
    Nazwisko = Faker('last_name')
    Imie = Faker('first_name')
    DUr = Faker('date_of_birth', minimum_age=15, maximum_age=19)
    Plec = Faker('random_element', elements=('M', 'K'))

    # KlasaU = SubFactory(GeneratorKlas)
    # Miasto = Faker('city')


def generate_students(rows_num=60):
    for i in range(rows_num):
        yield StudentsFactory(IdU=i + 1)


if __name__ == "__main__":
    print(StudentsFactory().headers)
    for row in generate_students(10):
        print(row)
